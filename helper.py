__author__ = 'peto'
from collections import deque


class Buff_avg():
    def __init__(self, size, precision=0):
        self.buff = []
        self.buff = deque((), size)
        self.size = size
        self.prec = precision

    def add_value(self, v):
        # if len(self.buff) >= self.size:
        # self.buff.remove()
        self.buff.append(v)
        c = 0
        for a in self.buff:
            c += a
        if self.prec <= 0:
            return c / len(self.buff)
        return round(c / len(self.buff), self.prec)

    def get_value(self):
        c = 0
        for a in self.buff:
            c += a
        if self.prec <= 0:
            return c / len(self.buff)
        return round(c / len(self.buff), self.prec)

        # buff=Buff_avg(5)
        # print buff.add_value(0.1531)

        #print buff.add_value(5.0)


def time_from_ms(num):
    ms = str(num % 1000)
    if len(ms) == 1:
        ms = "00" + ms
    if len(ms) == 2:
        ms = "0" + ms
    num = num / 1000
    sec = str(num % 60)
    if len(sec) == 1:
        sec = "0" + sec
    num = num / 60
    min = str(num % 60)

    num = num / 60
    strng = min + ":" + sec + ":" + ms
    return strng


    # print time_from_ms(750050)


def scale_image(img, height, width):
    pass