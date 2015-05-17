__author__ = 'peto'

import time
import data_collection as dc
import video_reader as vr
import video_writer as vw
# todo
# import simple_frame_handler as sfh


class Video_compose():
    def __init__(self, file, video, handler="simple_frame_handler", output="output.avi"):
        self.playback_speed = 1  # todo
        self.data_start_time = 0
        self.video_start_time = 0
        self.precision = 0.5
        self.curr_frame = 0
        self.frames_count = 0
        print "Creating data collection from given file."
        self.data_collection = dc.Data_collection(file)
        print "Data collection created."
        self.video_reader = vr.Video_reader(video)
        self.video_writer = vw.Video_writer(video, self.video_reader.get_fps(), self.video_reader.get_frame_width(),
                                            self.video_reader.get_frame_height(), output)
        self.frames_count = self.video_reader.get_frames_count()
        # preparation for custom frame handler, now only simple handler for development purposes
        # importing handler, finding class from string name, it must satisfy some criteria such as same name for class and
        self.handler = None
        self.load_handler(handler)
        # self.handler = sfh.Simple_frame_handler(self.video_reader, self.data_collection)

    def load_handler(self, handler=""):
        # pass
        # TODO exception ok?
        if handler == "":
            handler = "simple_frame_handler"
        hndl = __import__(handler)
        try:
            hndl = __import__(handler)
            new = getattr(hndl, handler.capitalize())
            self.handler = new(self.video_reader, self.data_collection)
        except ImportError:
            print ImportError.message
        else:
            return

    def set_playback_speed(self, speed=1):
        self.playback_speed = int(speed)

    def set_data_start_time(self, time):
        print "Data start time set to " + str(time) + " ms."
        self.data_start_time = time

    def set_video_start_time(self, time):
        print "Video start time set to " + str(time) + " ms."
        self.video_start_time = time

    def start_composing(self):
        print "Starting composing video."
        # frames_count = self.video_reader.get_frames_count()
        self.video_reader.set_position_in_ms(self.video_start_time)
        print "Setting position to 0."
        # + or - to time
        data = self.data_collection.get_data_at(self.video_reader.get_position_in_ms() - self.data_start_time)
        print "Getting first data."
        a = time.time()
        b = self.video_reader.get_position_in_ms()
        last = 0
        # print "For cycle begining."
        for i in range(0, int(self.frames_count)):
            #print "Handling frame:" + str(i)
            self.curr_frame += 1
            # curr_video_time = self.video_reader.get_position_in_ms()
            if i % self.playback_speed is not 0:
                self.video_reader.read_frame()
                continue
            frame = self.handle_frame(self.video_reader.read_frame(), data)
            if frame is None:
                print "Frame is None"
                break
            #print "Writing frame"
            self.write_frame(frame)
            # print b
            if b - last > self.precision:
                data = self.data_collection.get_data_at(self.video_reader.get_position_in_ms() - self.data_start_time)
                last = b
            b = self.video_reader.get_position_in_ms()
        print time.time() - a
        self.video_writer.finish_video(self.playback_speed == 1)
        return

    def quit_composing(self):
        self.video_writer.quit()
        self.video_reader.set_position_frame(0)

    def handle_frame(self, frame, data):
        if frame is not None:
            return self.handler.create_frame(frame, data)
        return None

    def write_frame(self, frame):
        self.video_writer.write_frame(frame)

    def get_handled_frame(self, time):
        self.video_reader.set_position_in_ms(time)
        data = self.data_collection.get_data_at(self.video_reader.get_position_in_ms() - self.data_start_time)
        return self.handle_frame(self.video_reader.read_frame(), data)



        # ####debug code######

        # a= time.time()
        # v=Video_compose("test2.tcx", "test2.mp4")
        # print time.time()-a
        #v.start_composing()
        #print time.time()-a