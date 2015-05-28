__author__ = 'peto'
from cv2 import VideoCapture


class Video_reader:
    def __init__(self, filename):
        self.curr_frame = 0  # BE careful !!! IT IS NOT ALWAYS UPDATED !!!!
        self.frames_count = 0
        print("Initializing video reader.")
        self.filename = filename
        print("Opening video file.")
        self.video = None
        try:
            self.video = VideoCapture(filename)
        except:
            print("Videofile failed to load.")
        if self.is_open():
            self.frames_count = self.video.get(7)
            print("Video " + filename + " is opened.")

    def read_frame(self, frame=-1):
        if frame is None:
            return None
        if frame <= -1:
            ret, frame = self.video.read()
            self.curr_frame += 1
            if ret:
                return frame
        try:
            self.video.set(1, int(frame))
        except:
            return None
        self.curr_frame = frame
        ret, frame = self.video.read()
        if ret:
            return frame

    def read_frame_at_time(self, time):
        self.video.set(0, time)
        ret, frame = self.video.read()
        if ret:
            return frame

    def set_position_in_ms(self, time):
        if self.video is not None:
            self.video.set(0, time)

    def set_position_frame(self, frame):
        if self.video is not None:
            if frame < 0:
                self.video.set(1, 0)
            elif frame > self.frames_count:
                self.video.set(1, self.frames_count - 1)
            else:
                self.video.set(1, frame)
                # self.curr_frame = frame

    def get_position_in_ms(self):
        if self.video is not None:
            return self.video.get(0)

    def get_position_frames(self):
        # self.curr_frame = self.video.get(1)
        if self.video is not None:
            return self.video.get(1)

    def get_position_ratio(self):
        if self.video is not None:
            return self.video.get(2)

    def get_frame_width(self):
        if self.video is not None:
            return self.video.get(3)

    def get_frame_height(self):
        if self.video is not None:
            return self.video.get(4)

    def get_fps(self):
        if self.video is not None:
            return self.video.get(5)

    def get_fourcc(self):
        if self.video is not None:
            return self.video.get(6)

    def get_frames_count(self):
        return self.frames_count

    def get_filename(self):
        return self.filename

    def is_open(self):
        if self.video is not None:
            return self.video.isOpened()
        else:
            return False

# ####debug code######

# v = Video_reader("test2.mp4")
# i = 0
# print v.get_frames_count()
# while(v.is_open()):
# print "i = " + str(i) + ", frame : "+ str(v.get_position_frames()) + ", time : " + str(v.get_position_in_ms())
#    v.read_frame()
#    i+=1
