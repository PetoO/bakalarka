__author__ = 'peto'
from cv2 import VideoWriter_fourcc, VideoWriter
import moviepy.video.io.ffmpeg_tools as mv
from os import path, remove

# test
# import picture as pc
# import wx
# from threading import Thread
# test

class Video_writer():
    def __init__(self, videosource, fps, width, height, result):
        print
        "Initializing video writer."
        self.audiofile = "tempaudio.mp3"
        self.videosource = videosource
        self.tempresult = "tempres.avi"
        self.result = result
        fourcc = VideoWriter_fourcc(*'XVID')
        self.out = VideoWriter(self.tempresult, fourcc, fps, (int(width), int(height)))

        # test
        #self.img=pc.app()
        #self.start = False
        #self.app = wx.App(False)  # Create a new app, don't redirect stdout/stderr to a window.
        #self.frame = pc.picture(None)  # A Frame is a top-level window.
        #myThreadOb = MyThread(self.frame, self.app)
        #myThreadOb.start()
        # #test

    def start_window(self):
        pass
        # test
        # app = wx.App(False)  # Create a new app, don't redirect stdout/stderr to a window.
        # self.frame = pc.picture(None)  # A Frame is a top-level window.
        # self.frame.Show(True)  # Show the frame.
        # app.MainLoop()
        #test

    def get_audio_clip(self):
        if path.exists(self.audiofile):
            remove(self.audiofile)
        mv.ffmpeg_extract_audio(self.videosource, self.audiofile)
        return

    def merge_audio_video(self):
        print
        "Merging audio and video."
        self.get_audio_clip()
        mv.ffmpeg_merge_video_audio(self.tempresult, self.audiofile, self.result)
        remove(self.audiofile)

    def write_frame(self, frame):
        # test
        #if not self.start:
        #    self.start_window()
        #self.frame.DisplayNext(frame)
        #self.img.set_img(frame)
        #test

        #cv2.imshow('prototype',frame)
        self.out.write(frame)

    def finish_video(self):
        print
        "Finishing video."
        self.out.release()
        self.merge_audio_video()
        remove(self.tempresult)

    def quit(self):
        print
        "Quiting."
        self.out.release()
        if path.exists(self.audiofile):
            remove(self.audiofile)
        if path.exists(self.tempresult):
            remove(self.tempresult)

            # ####debug code######

            # v = Video_writer("video.avi")
            #v.get_audio_clip()
            #v.merge_audio_video()

            # class MyThread(Thread):
            # def __init__(self, frame,app):
            #         ''' Constructor. '''
            #         Thread.__init__(self)
            #         self.frame = frame
            #         self.app = app
            #         print "ideeeeem111111111111111"
            #
            #     def run(self):
            #         self.frame.Show(True)  # Show the frame.
            #         self.app.MainLoop()
            #         print "ideeeeem"