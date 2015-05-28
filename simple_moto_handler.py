__author__ = 'peto'

from PIL import Image, ImageDraw, ImageOps
import numpy as np
import cv2


class Simple_moto_handler:
    def __init__(self, vr=None, dc=None):
        self.path = "simple_moto_handler"
        self.frame_size_w = 0
        self.frame_size_h = 0
        self.video_reader = vr
        self.data_collection = dc
        if self.video_reader is not None:
            self.frame_size_w = int(self.video_reader.get_frame_width())
            self.frame_size_h = int(self.video_reader.get_frame_height())
        self.speedometer = Image.open(self.path + "/images/" + "speedometer.png")
        self.arrow = Image.open(self.path + "/images/" + "arrow.png")
        # axes are different
        self.last_beat_time = 0
        self.show_map = True
        self.show_speed = True
        self.lx = 0
        self.ly = 0
        self.mratio = 0
        self.mapp = None
        self.create_map()


    def create_frame(self, frame, data):
        if data is None:
            return frame
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = Image.fromarray(frame)

        if self.show_speed:
            frame = self.create_speed(int(data["Speed"]), frame)

        if self.show_map:
            frame = self.add_map(frame, data)

        frame = np.array(frame)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        return np.array(frame)

    def create_map(self):
        def f((xx, yy)):
            return (((xx - lx) * mratio + 50), ((yy - ly) * mratio) + 50)

        mapp = Image.new("RGBA", (1100, 1100), (255, 255, 255, 0))
        draw = ImageDraw.Draw(mapp)
        gx = 0.0
        gy = 0.0
        lx = 1000.0
        ly = 1000.0
        points = []
        trackpoints = self.data_collection.trackpoints
        for x in trackpoints:
            if x["LatitudeDegrees"] > gy:
                gy = x["LatitudeDegrees"]
            if x["LatitudeDegrees"] < ly:
                ly = x["LatitudeDegrees"]
            if x["LongitudeDegrees"] > gx:
                gx = x["LongitudeDegrees"]
            if x["LongitudeDegrees"] < lx:
                lx = x["LongitudeDegrees"]
            points.append((x["LongitudeDegrees"], x["LatitudeDegrees"]))
        rx = 1000.0 // (gx - lx)
        ry = 1000.0 // (gy - ly)
        mratio = 0
        if rx > ry:
            mratio = ry
        else:
            mratio = rx
        pp = []
        for x in points:
            pp.append(f(x))

        self.lx = lx
        self.ly = ly
        self.mratio = mratio
        self.mapp = mapp

        draw.line(pp, fill=(255, 0, 0, 255), width=15)

        # mapp.save("asd.jpg", "JPEG")

    def add_map(self, frame, data):
        y = data["LatitudeDegrees"]
        x = data["LongitudeDegrees"]

        def f((xx, yy)):
            return (((xx - self.lx) * self.mratio) + 50, ((yy - self.ly) * self.mratio) + 50)

        mapp = self.mapp.copy()
        draw = ImageDraw.Draw(mapp)
        xx, yy = f((x, y))
        draw.ellipse([(int(xx) - 40), (int(yy) - 40), (int(xx) + 40), (int(yy) + 40)], fill=(255, 255, 255))
        mapp = mapp.rotate(270)
        x = int(self.frame_size_w / 3.84)
        mapp = mapp.resize((x, x), Image.BICUBIC)
        mapp = ImageOps.mirror(mapp)
        frame.paste(mapp, (self.frame_size_w - x - 5, self.frame_size_h - x - 5), mapp)
        return frame

    def create_speed(self, speed, frame, posw=0, posh=0):
        speedometer = self.speedometer.copy()
        angle = 45 - (speed * 1.5)
        size = 512, 512
        arr = self.arrow.rotate(angle, expand=1)
        x, y = arr.size
        speedometer.paste(arr, ((512 - x) / 2, (512 - y) / 2), arr)
        sz = int(self.frame_size_h / 4)
        speedometer = speedometer.resize((sz, sz), Image.BICUBIC)

        if posw == 0 and posh == 0:
            posw = 10
            posh = int(self.frame_size_h - 10 - sz)
        frame.paste(speedometer, (posw, posh), speedometer)
        return frame

