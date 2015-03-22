__author__ = 'peto'
from cv2 import VideoCapture


class Video_reader:
    def __init__(self, filename):
        print
        "Initializing video reader."
        self.filename = filename
        print
        "Opening video file."
        self.video = VideoCapture(filename)
        if self.is_open():
            print
            "Video " + filename + " is opened."

    def read_frame(self, frame=-1):
        if frame == -1:
            ret, frame = self.video.read()
            if ret:
                return frame
        self.video.set(1, int(frame))
        ret, frame = self.video.read()
        if ret:
            return frame

    def read_frame_at_time(self, time):
        self.video.set(0, time)
        ret, frame = self.video.read()
        if ret:
            return frame

    def set_position_in_ms(self, time):
        self.video.set(0, time)

    def set_position_frame(self, frame):
        self.video.set(1, frame)

    def get_position_in_ms(self):
        return self.video.get(0)

    def get_position_frames(self):
        return self.video.get(1)

    def get_position_ratio(self):
        return self.video.get(2)

    def get_frame_width(self):
        return self.video.get(3)

    def get_frame_height(self):
        return self.video.get(4)

    def get_fps(self):
        return self.video.get(5)

    def get_fourcc(self):
        return self.video.get(6)

    def get_frames_count(self):
        return self.video.get(7)

    def get_filename(self):
        return self.filename

    def is_open(self):
        return self.video.isOpened()


# ####debug code######

# v = Video_reader("test2.mp4")
# i = 0
# print v.get_frames_count()
#while(v.is_open()):
#    print "i = " + str(i) + ", frame : "+ str(v.get_position_frames()) + ", time : " + str(v.get_position_in_ms())
#    v.read_frame()
#    i+=1
