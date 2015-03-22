__author__ = 'peto'
from cv2 import imread, resize, FONT_HERSHEY_SIMPLEX, \
    putText, LINE_AA, COLOR_BGR2GRAY, cvtColor, threshold, bitwise_not, THRESH_BINARY, addWeighted, bitwise_and, add
import google_map as mapp


class Simple_frame_handler:
    # gets video reader instance on the input, possibly data collection in future
    def __init__(self, vr=None, dc=None):
        self.video_reader = vr
        self.img = imread("hr.png")
        self.img = resize(self.img, (0, 0), fx=0.26, fy=0.26)
        self.img1 = imread("hr1.png")
        self.img1 = resize(self.img1, (0, 0), fx=0.26, fy=0.26)
        # axes are different
        self.pic_pos_y = int(self.video_reader.get_frame_width()) - 1870
        self.pic_pos_x = int(self.video_reader.get_frame_height()) - 250
        # print self.pic_pos_x
        #print self.pic_pos_y
        self.last_beat_time = 0
        self.map = mapp.Google_map(dc)
        return

    def create_frame(self, frame, data):
        font = FONT_HERSHEY_SIMPLEX
        if data != None:
            # print data
            putText(frame, str(int(data["Speed"])) + " km/h", (50, int(self.video_reader.get_frame_height() - 40)),
                    font, 2, (255, 255, 255), 2, LINE_AA)
            putText(frame, str(int(data["AltitudeMeters"])) + " mnm", (
                int(self.video_reader.get_frame_width()) - 600, int(self.video_reader.get_frame_height()) - 40), font,
                    2,
                    (255, 255, 255), 2,
                    LINE_AA)
            # I want to put logo on top-left corner, So I create a ROI

            # heart rate
            if data["HeartRateBpm"] <= 0 or self.last_beat_time == 0:
                a1 = 0.0
                a2 = 1.0
                self.last_beat_time = self.video_reader.get_position_in_ms()
            else:
                beat_time = 60000 / data["HeartRateBpm"]
                curr_time = self.video_reader.get_position_in_ms() - self.last_beat_time
                if curr_time >= beat_time:
                    a1 = 0.0
                    a2 = 1.0
                    self.last_beat_time = self.video_reader.get_position_in_ms()
                else:
                    d = (((beat_time / curr_time)) % 10) / 10
                    d = round(d, 2)
                    #a1 = 0.3+d
                    #a2 = 0.7-d
                    a1 = d
                    a2 = 1.0 - d
                    #print a1
                    #print a2
                    #print "---"
                    #a1 = 0.3
                    # a2 = 0.7

            #self.pic_pos_x:(self.pic_pos_x+rows), self.pic_pos_y:(self.pic_pos_y+cols)
            #0:rows, 0:cols
            rows, cols, channels = self.img.shape
            roi = frame[self.pic_pos_x:(self.pic_pos_x + rows), self.pic_pos_y:(self.pic_pos_y + cols)]
            # Now create a mask of logo and create its inverse mask also
            imggray = cvtColor(self.img, COLOR_BGR2GRAY)
            ret, mask = threshold(imggray, 10, 255, THRESH_BINARY)
            mask_inv = bitwise_not(mask)

            # Now black-out the area of logo in ROI
            frame_bg = bitwise_and(roi, roi, mask=mask_inv)

            # Take only region of logo from logo image.
            img_fg = bitwise_and(self.img, self.img, mask=mask)

            # Put logo in ROI and modify the main image
            dst = add(frame_bg, img_fg)
            frame[self.pic_pos_x:(self.pic_pos_x + rows), self.pic_pos_y:(self.pic_pos_y + cols)] = addWeighted(
                frame[self.pic_pos_x:(self.pic_pos_x + rows), self.pic_pos_y:(self.pic_pos_y + cols)], a1, dst, a2, 0)
            if data["HeartRateBpm"] != 0:
                putText(frame, str(int(data["HeartRateBpm"])),
                        (self.pic_pos_y + cols / 2 - 30, self.pic_pos_x + rows / 2 ), font, 1, (255, 255, 255), 2,
                        LINE_AA)

            mapimg = self.map.get_image(data["LatitudeDegrees"], data["LongitudeDegrees"])
            rows, cols, channels = mapimg.shape
            roi = frame[100:350, 100:350]
            # TODO if no pic was returned due the network problem or smth, its problem BIG
            # frame[0:250, 100:350] = addWeighted(frame[0:250, 100:350], 0.5, mapimg, 0.5, 0)
            #self.video_reader.get_frame_width()
            #self.video_reader.get_frame_height()
            frame[(self.video_reader.get_frame_height() - 250):self.video_reader.get_frame_height(),
            (self.video_reader.get_frame_width() - 250):self.video_reader.get_frame_width()] = addWeighted(
                frame[(self.video_reader.get_frame_height() - 250):self.video_reader.get_frame_height(),
                (self.video_reader.get_frame_width() - 250):self.video_reader.get_frame_width()], 0.5, mapimg, 0.5, 0)
        else:
            putText(frame, str(0) + " km/h", (50, int(self.video_reader.get_frame_height() - 40)), font, 2,
                    (255, 255, 255), 2, LINE_AA)
            putText(frame, str(0) + " mnm", (
                int(self.video_reader.get_frame_width()) - 380, int(self.video_reader.get_frame_height()) - 40), font,
                    2,
                    (255, 255, 255), 2, LINE_AA)
        return frame