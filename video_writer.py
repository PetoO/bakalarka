__author__ = 'peto'
from cv2 import VideoWriter_fourcc, VideoWriter
import moviepy.video.io.ffmpeg_tools as mv
from os import path, remove
import shutil

# test
# import picture as pc
# import wx
# from threading import Thread
# test

class Video_writer():
    def __init__(self, videosource, fps, width, height, result):
        print("Initializing video writer.")
        self.audiofile = "tempaudio.mp3"
        self.videosource = videosource
        self.tempresult = "tempres.avi"
        try:
            if path.exists(self.tempresult):
                remove(self.tempresult)
        except WindowsError:
            print "Tempresult is being used"


        self.result = result
        fourcc = VideoWriter_fourcc(*'XVID')
        self.out = VideoWriter(self.tempresult, fourcc, fps, (int(width), int(height)))

    def get_audio_clip(self):
        if path.exists(self.audiofile):
            remove(self.audiofile)
        mv.ffmpeg_extract_audio(self.videosource, self.audiofile)
        return

    def merge_audio_video(self):
        print("Merging audio and video.")
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


    def finish_video(self, sound=True):
        print("Finishing video.")
        self.out.release()
        if sound:
            self.merge_audio_video()
        else:
            shutil.copy2(self.tempresult, self.result)
        remove(self.tempresult)

    def quit(self):
        print("Quiting.")
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