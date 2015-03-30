__author__ = 'peto'

import wx
import video_compose as vc
import cv2
import helper as help
import auto_sync
import os
import gui as main

#data_file = "hero.tcx"
#video_file = "hero.mp4"
data_file = ""
video_file = ""
dir_path = ""
output = "output.avi"
time = 0
curr_time = 0
video_compose = None
frame = None
autosync = False


class main_frame(main.main_frame):
    def __init__(self, parent):
        main.main_frame.__init__(self, parent)
        global data_file
        global video_file
        global video_compose
        if data_file != "" and video_file != "":
            video_compose = vc.Video_compose(data_file, video_file, "simple_frame_handler",
                                             'C:\\Users\\peto\\Desktop\\output.avi')

            video_compose.set_data_start_time(time)
            self.show_frame()
            self.m_slider1.SetRange(0, video_compose.video_reader.get_frames_count())

    # Handlers for main_frame events.
    def m_slider1OnScroll(self, event):
        # TODO: Implement m_slider1OnScroll
        pass

    def m_slider1OnScrollChanged(self, event):
        global curr_time
        video_compose.video_reader.set_position_frame(self.m_slider1.GetValue())
        curr_time = video_compose.video_reader.get_position_in_ms()
        print
        curr_time
        self.show_frame()

    def m_button7OnButtonClick(self, event):
        global curr_time
        curr_time -= 2000
        if curr_time < 0:
            curr_time = 0
            #self.m_spinCtrl1.SetValue(0)
        self.m_slider1.SetValue(video_compose.video_reader.get_position_frames())
        self.show_frame()
        #todo show frame

    def m_button4OnButtonClick(self, event):
        global curr_time
        curr_time -= 150
        if curr_time < 0:
            curr_time = 0
            #self.m_spinCtrl1.SetValue(0)
        self.m_slider1.SetValue(video_compose.video_reader.get_position_frames())
        self.show_frame()
        #todo show frame

    def m_button5OnButtonClick(self, event):
        global curr_time
        curr_time += 150
        #self.m_spinCtrl1.SetValue(curr_time)
        self.m_slider1.SetValue(video_compose.video_reader.get_position_frames())
        #todo show frame
        self.show_frame()

    def m_button6OnButtonClick(self, event):
        global curr_time
        curr_time += 2000
        # self.m_spinCtrl1.SetValue(curr_time)
        self.m_slider1.SetValue(video_compose.video_reader.get_position_frames())
        #todo show frame
        self.show_frame()

    def m_button8OnButtonClick(self, event):
        global time
        time = video_compose.video_reader.get_position_in_ms()
        self.m_spinCtrl1.SetValue(time)
        video_compose.set_data_start_time(time)
        self.show_frame()

    def m_spinCtrl1OnSpinCtrl(self, event):
        global time
        time = self.m_spinCtrl1.GetValue()
        video_compose.set_data_start_time(time)
        self.show_frame()

    def m_spinCtrl1OnTextEnter(self, event):
        global time
        time = self.m_spinCtrl1.GetValue()
        video_compose.set_data_start_time(time)
        self.show_frame()

    def m_button1OnButtonClick(self, event):
        global data_file
        global video_file
        global video_compose
        global time
        #if data_file=="" or video_file =="":
        if video_compose != None:
            video_compose.set_data_start_time(time)
            working = progress_dialog(self)
            working.Show(True)
            video_compose.start_composing()
            working.Hide()

    def show_frame(self):
        global video_compose
        global time
        global frame
        global curr_time
        #time = strftime("%H:%M:%S +0000", curr_time)
        timestr = help.time_from_ms(int(curr_time))
        #self.m_staticText6.SetLabelText("00:00:000")
        self.m_staticText6.SetLabelText(timestr)

        if video_compose is not None:
            video_compose.set_data_start_time(time)
            #frame = video_compose.video_reader.read_frame_at_time(curr_time)
            frame = video_compose.get_handled_frame(curr_time)
            frame = cv2.resize(frame, (0, 0), fx=0.26, fy=0.26)
            img = self.GetBitmap(frame)
            self.m_bitmap1.SetBitmap(img)
            self.Refresh()

    def GetBitmap(self, array, width=1920, height=1080, colour=(0, 0, 0)):
        #
        height, width = frame.shape[:2]
        image = wx.EmptyImage(width, height)
        #image = wx.Image()
        image.SetData(array.tostring())
        wxBitmap = image.ConvertToBitmap()  # OR:  wx.BitmapFromImage(image)
        return wxBitmap


class choose_files(main.Choose_files):
    def __init__(self, parent):
        main.Choose_files.__init__(self, parent)

    # Handlers for Choose_files events.
    def video_filePickerOnFileChanged(self, event):
        global video_file
        video_file = event.GetPath()
        print(video_file)

    def data_filePickerOnFileChanged(self, event):
        global data_file
        data_file = event.GetPath()
        print(data_file)

    def m_dirPicker1OnDirChanged(self, event):
        global dir_path
        dir_path = event.GetPath()
        print(dir_path)


    def m_checkBox1OnCheckBox(self, event):
        global autosync
        autosync = self.m_checkBox1.IsChecked()

    def m_button3OnButtonClick(self, event):
        global data_file
        global video_file
        global video_compose
        global dir_path
        global time
        global autosync
        if data_file != "" and video_file != "" and dir_path != "":
            output = ""
            if self.m_textCtrl1.GetValue() == "":
                # output = dir_path + "\\" + "output.avi"
                output = os.path.normpath(os.path.join(dir_path, 'output.avi'))
            else:
                #output = dir_path + "\\" + self.m_textCtrl1.GetValue() + ".avi"
                output = os.path.normpath(os.path.join(dir_path, self.m_textCtrl1.GetValue() + ".avi"))
            # 'C:\Users\peto\Desktop\output.avi'
            video_compose = vc.Video_compose(data_file, video_file, "simple_frame_handler",
                                             output)

            self.Hide()
            if autosync:
                time = auto_sync.sync(video_compose.video_reader)
                self.parent.m_spinCtrl1.SetValue(int(time))
                video_compose.set_data_start_time(int(time))
            self.parent.show_frame()
            self.parent.m_slider1.SetRange(0, video_compose.video_reader.get_frames_count())
            timestr = help.time_from_ms((int(video_compose.video_reader.get_frames_count()) // int(
                video_compose.video_reader.get_fps())) * 1000)
            self.parent.m_staticText7.SetLabelText("00:00:000")
            self.parent.m_staticText7.SetLabelText(timestr)


class error_dialog(main.error_dialog):
    def __init__(self, parent):
        main.error_dialog.__init__(self, parent)

    # Handlers for error_dialog events.
    def m_button4OnButtonClick(self, event):
        # TODO: Implement m_button4OnButtonClick
        pass


class progress_dialog(main.progress_dialog):
    def __init__(self, parent):
        main.progress_dialog.__init__(self, parent)


app = wx.App(False)  # Create a new app, don't redirect stdout/stderr to a window.
frame1 = main_frame(None)
frame1.Show(True)
frame = choose_files(frame1)
frame.Show(True)
app.MainLoop()