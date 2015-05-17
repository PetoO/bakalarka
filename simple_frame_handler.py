__author__ = 'peto'

import helper
import google_map as mapp
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import time
import cv2


class Simple_frame_handler:
    def __init__(self, vr=None, dc=None):
        self.digits = []
        self.kmh = None
        self.digit_size_w = 0
        self.digit_size_h = 0
        self.path = "simple_frame_handler"
        self.frame_size_w = 0
        self.frame_size_h = 0
        self.video_reader = vr
        self.digit_ratio = 0.100
        if self.video_reader is not None:
            self.frame_size_w = int(self.video_reader.get_frame_width())
            self.frame_size_h = int(self.video_reader.get_frame_height())
        self.heart = Image.open(self.path + "/images/" + "heart.png")
        self.no_map = Image.open(self.path + "/images/" + "no_map.png")
        # axes are different
        self.pic_pos_y = int(self.video_reader.get_frame_width()) - 1870
        self.pic_pos_x = int(self.video_reader.get_frame_height()) - 250
        # print self.pic_pos_x
        # print self.pic_pos_y
        self.last_beat_time = 0
        self.map = mapp.Google_map(dc)
        self.show_map = True
        self.show_hr = True
        self.show_speed = True
        self.show_alt = True
        print "loadign digits"
        self.load_digits()
        print "digits loaded"

    def create_frame(self, frame, data):
        if data is None:
            return frame
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = Image.fromarray(frame)

        if self.show_speed:
            frame = self.create_speed(int(data["Speed"]), frame)

        if self.show_map:
            frame = self.add_map(frame, data)

        if self.show_hr:
            frame = self.add_hrm(frame, data)

        if self.show_alt:
            frame = self.add_alt(frame, data)
        frame = np.array(frame)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        return np.array(frame)

    def add_alt(self, frame, data):
        draw = ImageDraw.Draw(frame)
        font = ImageFont.truetype("arial.ttf", 35)
        draw.text(((self.frame_size_w - 175, self.frame_size_h - 305)), str(int(data["AltitudeMeters"])) + " alt",
                  font=font,
                  fill=(255, 255, 255, 255))
        return frame

    def add_hrm(self, frame, data):
        frame.paste(self.heart, (55, self.frame_size_h - self.digit_size_h - 25 - self.heart.size[0]), self.heart)
        draw = ImageDraw.Draw(frame)
        font = ImageFont.truetype("arial.ttf", 35)
        draw.text((60 + self.heart.size[1], self.frame_size_h - self.digit_size_h - 25 - (self.heart.size[0] / 2)),
                  str(data["HeartRateBpm"]) + " bpm", font=font, fill=(255, 0, 0, 255))
        return frame

    def add_map(self, frame, data):
        mapimg = self.map.get_image(data["LatitudeDegrees"], data["LongitudeDegrees"])
        mapimg = Image.fromarray(mapimg)
        w, h = mapimg.size
        bigsize = (w * 3, h * 3)
        mask = Image.new('L', bigsize, 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0) + bigsize, fill=255)
        mask = mask.resize(mapimg.size, Image.ANTIALIAS)
        mapimg.putalpha(mask)

        frame.paste(mapimg, (self.frame_size_w - w, self.frame_size_h - h), mapimg)
        return frame

    def load_digits(self):
        self.kmh = Image.open(self.path + "/images/" + "kmh.png")
        self.digit_size_w, self.digit_size_h = self.kmh.size
        size = int(self.frame_size_w * self.digit_ratio)
        maxsize = (size, size)
        print size
        self.kmh.thumbnail(maxsize, Image.ANTIALIAS)
        self.digit_size_w, self.digit_size_h = self.kmh.size

        for i in range(0, 10):
            self.digits.append(Image.open(self.path + "/images/" + str(i) + ".png"))
            self.digits[i].thumbnail(maxsize, Image.ANTIALIAS)

    def create_speed(self, speed, frame, posw=0, posh=0):
        if posw == 0 and posh == 0:
            posw = 10
            posh = int(self.frame_size_h - 10 - self.digit_size_h)
        d1 = None
        d2 = None
        d3 = None
        if speed < 100:
            d1 = 0
            if speed < 10:
                d2 = 0
                if speed == 0:
                    d3 = 0
                else:
                    d3 = speed % 1
            else:
                d3 = speed % 10
                speed /= 10
                d2 = speed % 10
        else:
            d3 = speed % 10
            speed /= 10
            d2 = speed % 10
            speed /= 10
            d1 = speed % 10
        # (width, height)
        # blank_image = Image.new("RGB", (int(self.digit_size_w*4), int(self.digit_size_h)))
        frame.paste(self.digits[d1], (posw, posh), self.digits[d1])
        frame.paste(self.digits[d2], (int(posw + self.digit_size_w * 1), posh), self.digits[d2])
        frame.paste(self.digits[d3], (int(posw + self.digit_size_w * 2), posh), self.digits[d3])
        frame.paste(self.kmh, (int(posw + self.digit_size_w * 3), posh), self.kmh)
        return frame

