# encoding: utf-8
import epd7in5b
from PIL import Image, ImageDraw, ImageFont
import pytz
import datetime

EPD_WIDTH = 640
EPD_HEIGHT = 384

def main():
    epd = epd7in5b.EPD()
    epd.init()

    # For simplicity, the arguments are explicit numerical coordinates
    image_red = Image.new('1', (EPD_WIDTH, EPD_HEIGHT), 255)    # 255: clear the frame
    draw_red = ImageDraw.Draw(image_red)
    image_black = Image.new('1', (EPD_WIDTH, EPD_HEIGHT), 255)    # 255: clear the frame
    draw_black = ImageDraw.Draw(image_black)
    # font = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMonoBold.ttf', 24)
    # font = ImageFont.truetype('/usr/share/fonts/truetype/takao-gothic/TakaoPGothic.ttf', 50)
    font = ImageFont.truetype('/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc', 45)
    # draw_red.rectangle((0, 6, 640, 40), fill = 0)
    # draw_red.text((200, 10), 'e-Paper demo', font = font, fill = 255)
    draw_black.text((15, 10), "Hello, world. " + u"こんにちは。", font = font, fill = 0)
    draw_red.rectangle((200, 80, 600, 280), fill = 0)
    draw_red.chord((240, 120, 580, 220), 0, 360, fill = 255)
    draw_black.rectangle((20, 80, 160, 280), fill = 0)
    draw_red.chord((40, 80, 180, 220), 0, 360, fill = 0)
    jp_now = datetime.datetime.now(pytz.timezone('Asia/Tokyo'))
    draw_black.text((15, 300), jp_now.strftime('%m/%d %H:%M ') + u"表示", font = font, fill = 0)
    epd.display_frame(epd.get_frame_buffer(image_black),epd.get_frame_buffer(image_red))

if __name__ == '__main__':
    main()
