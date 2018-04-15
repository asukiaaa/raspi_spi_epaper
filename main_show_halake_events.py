# encoding: utf-8
debug_mode=False
if (not debug_mode):
    import epd7in5b
from connpass import Connpass
from PIL import Image, ImageDraw, ImageFont
import pytz
from datetime import datetime
from dateutil import parser

EPD_WIDTH = 640
EPD_HEIGHT = 384
CONNPASS_GROUP_ID = 1382
#CONNPASS_GROUP_ID = 1
JP_WEEK_DAYS = [u'日', u'月', u'火', u'水', u'木', u'金', u'土']

def get_events(group_id):
    utc = pytz.UTC
    global events
    events = []
    date_now = utc.localize(datetime.utcnow())
    for event in Connpass().search(series_id=[group_id])['events']:
        started_at = parser.parse(event['started_at'])
        if started_at > date_now:
            events.append(event)
    return sorted(events, key=lambda event: event['started_at'])

def get_datetime_str(target_datetime):
    date_str = target_datetime.strftime('%m/%d')
    week_day_str = JP_WEEK_DAYS[int(target_datetime.strftime('%w'))]
    week_day_str = '(' + week_day_str + ')'
    time_str = target_datetime.strftime('%H:%M')
    return date_str + week_day_str + time_str

def draw_events(draw_black, font, events, line_x, line_y, first_line_step, second_line_step, max_event_count):
    for idx, event in enumerate(events):
        if (idx == max_event_count):
            break
        draw_black.text((line_x, line_y), event['title'], font = font, fill = 0)
        line_y += first_line_step
        started_at = parser.parse(event['started_at'])
        datetime_str = get_datetime_str(started_at)
        accepted_str = str(event['accepted']) + u'人参加予定'
        draw_black.text((line_x, line_y), datetime_str + u'  ' + accepted_str, font = font, fill = 0)
        line_y += second_line_step
    if (len(events) == 0):
        draw_black.text((line_x, line_y), u"予定している", font = font, fill = 0)
        line_y += first_line_step
        draw_black.text((line_x, line_y), u"イベントはありません。", font = font, fill = 0)
        line_y += second_line_step
    return line_y

def draw_last_line(draw_black, font, event_count, line_x, time_line_x, line_y, max_event_count):
    if (event_count > max_event_count):
        draw_black.text((line_x, line_y), u"他" + str(event_count - max_event_count) + u"件", font = font, fill = 0)
    x = line_x
    if event_count > max_event_count:
        x = time_line_x
    jp_now = datetime.now(pytz.timezone('Asia/Tokyo'))
    draw_black.text((x, line_y), get_datetime_str(jp_now) + u" 表示", font = font, fill = 0)

def main():
    if (not debug_mode):
        epd = epd7in5b.EPD()
        epd.init()

    events = get_events(CONNPASS_GROUP_ID)

    image_red = Image.new('1', (EPD_WIDTH, EPD_HEIGHT), 255) # 255: clear the frame
    draw_red = ImageDraw.Draw(image_red)
    image_black = Image.new('1', (EPD_WIDTH, EPD_HEIGHT), 255) # 255: clear the frame
    draw_black = ImageDraw.Draw(image_black)
    line_y = 0
    line_x = 10
    time_line_x = 200
    first_line_step = 53
    second_line_step = 100
    font_size = 45
    font = ImageFont.truetype('/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc', font_size)
    max_event_count = 2
    line_y = draw_events(draw_black, font, events, line_x, line_y, first_line_step, second_line_step, max_event_count)
    draw_last_line(draw_black, font, len(events), line_x, time_line_x, line_y, max_event_count)
    if (not debug_mode):
        epd.display_frame(epd.get_frame_buffer(image_black),epd.get_frame_buffer(image_red))
    else:
        image_black.save('debug.jpg')

if __name__ == '__main__':
    main()
