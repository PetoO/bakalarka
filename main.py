__author__ = 'peto'

import wx
import video_compose as vc
import cv2
import helper as help
import auto_sync
import os
import gui as main
import thread
import time


data_file = ""
video_file = ""
dir_path = ""
output = "output.avi"
timer = 0
curr_time = 0
video_compose = None
frame = None
autosync = False
frame_handlers = ["simple_frame_handler", "simple_frame_handler2", "simple_frame_handler"]
blocked_GUI = False
#
# video_file = "C:\Users\peto\Desktop\hero.mp4"
# data_file = "C:\Users\peto\Desktop\hero.tcx"
# dir_path = 'C:\Users\peto\Desktop\output.avi'


class main_frame(main.main_frame):
    def __init__(self, parent):
        main.main_frame.__init__(self, parent)
        global data_file
        global video_file
        global video_compose
        self.working = progress_dialog(self)
        if data_file != "" and video_file != "":
            video_compose = vc.Video_compose(data_file, video_file, "simple_frame_handler",
                                             'C:\\Users\\peto\\Desktop\\output.avi')

            video_compose.set_data_start_time(timer)
            self.show_frame()
            self.time_slider.SetRange(0, video_compose.video_reader.get_frames_count())
        self.show_status_bar(False)


    # Handlers for main_frame events.
    def time_sliderOnScroll(self, event):
        # TODO: Implement time_sliderOnScroll
        pass

    def time_sliderOnScrollChanged(self, event):
        global curr_time
        video_compose.video_reader.set_position_frame(self.time_slider.GetValue())
        curr_time = video_compose.video_reader.get_position_in_ms()
        print
        curr_time

        self.show_frame()

    def prevD_buttonOnButtonClick(self, event):
        global curr_time
        curr_time -= 2000
        if curr_time < 0:
            curr_time = 0
            # self.time_spinner.SetValue(0)
        self.time_slider.SetValue(video_compose.video_reader.get_position_frames())
        self.show_frame()
        # todo show frame

    def prev_buttonOnButtonClick(self, event):
        global curr_time
        curr_time -= 150
        if curr_time < 0:
            curr_time = 0
            # self.time_spinner.SetValue(0)
        self.time_slider.SetValue(video_compose.video_reader.get_position_frames())
        self.show_frame()
        # todo show frame

    def next_buttonOnButtonClick(self, event):
        global curr_time
        curr_time += 150
        # self.time_spinner.SetValue(curr_time)
        self.time_slider.SetValue(video_compose.video_reader.get_position_frames())
        #todo show frame
        self.show_frame()

    def nextD_buttonOnButtonClick(self, event):
        global curr_time
        curr_time += 2000
        # self.time_spinner.SetValue(curr_time)
        self.time_slider.SetValue(video_compose.video_reader.get_position_frames())
        # todo show frame
        self.show_frame()

    def set_start_time_buttonOnButtonClick(self, event):
        global timer
        timer = video_compose.video_reader.get_position_in_ms()
        self.time_spinner.SetValue(timer)
        video_compose.set_data_start_time(timer)
        self.show_frame()

    def time_spinnerOnSpinCtrl(self, event):
        global timer
        timer = self.time_spinner.GetValue()
        video_compose.set_data_start_time(timer)
        self.show_frame()

    def time_spinnerOnTextEnter(self, event):
        global timer
        timer = self.time_spinner.GetValue()
        video_compose.set_data_start_time(timer)
        self.show_frame()

    def main_buttonOnButtonClick(self, event):
        print "start button"
        global data_file
        global video_file
        global video_compose
        global timer
        # if data_file=="" or video_file =="":
        if video_compose != None:
            video_compose.set_data_start_time(timer)
            # self.working.Show(True)
            #thread.start_new_thread(self.working.update, (video_compose,))
            self.block_GUI(False)
            self.show_status_bar(True)
            thread.start_new_thread(self.update, ())
            thread.start_new_thread(video_compose.start_composing, ())
            #video_compose.start_composing()


    def pb_radioBtn1OnRadioButton(self, event):
        global video_compose
        video_compose.set_playback_speed()

    def pb_radioBtn2OnRadioButton(self, event):
        global video_compose
        video_compose.set_playback_speed(2)

    def pb_radioBtn3OnRadioButton(self, event):
        global video_compose
        video_compose.set_playback_speed(5)

    def pb_radioBtn4OnRadioButton(self, event):
        global video_compose
        video_compose.set_playback_speed(10)

    def pic1OnLeftUp(self, event):
        self.pic1Text.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHT))
        self.pic2Text.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BACKGROUND))
        self.pic3Text.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BACKGROUND))
        global video_compose
        global frame_handlers
        video_compose.load_handler(frame_handlers[0])
        self.show_frame()
        self.Refresh()

    def pic1TextOnLeftUp(self, event):
        self.pic1Text.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHT))
        self.pic2Text.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BACKGROUND))
        self.pic3Text.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BACKGROUND))
        global video_compose
        global frame_handlers
        video_compose.load_handler(frame_handlers[0])
        self.show_frame()
        self.Refresh()

    def pic2OnLeftUp(self, event):
        self.pic1Text.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BACKGROUND))
        self.pic2Text.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHT))
        self.pic3Text.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BACKGROUND))
        global video_compose
        global frame_handlers
        video_compose.load_handler(frame_handlers[1])
        self.show_frame()
        self.Refresh()

    def pic2TextOnLeftUp(self, event):
        self.pic1Text.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BACKGROUND))
        self.pic2Text.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHT))
        self.pic3Text.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BACKGROUND))
        global video_compose
        global frame_handlers
        video_compose.load_handler(frame_handlers[1])
        self.show_frame()
        self.Refresh()


    def pic3OnLeftUp(self, event):
        self.pic1Text.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BACKGROUND))
        self.pic2Text.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BACKGROUND))
        self.pic3Text.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHT))
        global video_compose
        global frame_handlers
        video_compose.load_handler(frame_handlers[2])
        self.show_frame()
        self.Refresh()

    def pic3TextOnLeftUp(self, event):
        self.pic1Text.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BACKGROUND))
        self.pic2Text.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BACKGROUND))
        self.pic3Text.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHT))
        global video_compose
        global frame_handlers
        video_compose.load_handler(frame_handlers[2])
        self.show_frame()
        self.Refresh()


    def show_frame(self):
        global video_compose
        global timer
        global frame
        global curr_time
        # timer = strftime("%H:%M:%S +0000", curr_time)
        timestr = help.time_from_ms(int(curr_time))
        # self.m_staticText6.SetLabelText("00:00:000")
        self.curr_time.SetLabelText(timestr)

        if video_compose is not None:
            video_compose.set_data_start_time(timer)
            #frame = video_compose.video_reader.read_frame_at_time(curr_time)
            frame = video_compose.get_handled_frame(curr_time)
            #frame = cv2.resize(frame, (0, 0), fx=0.26, fy=0.26)
            frame = help.scale_image(frame, 540, 255)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = self.GetBitmap(frame)
            self.video_image.SetBitmap(img)
            self.Refresh()
            self.Fit()
            self.Layout()

    def GetBitmap(self, array, width=1920, height=1080, colour=(0, 0, 0)):
        height, width = frame.shape[:2]
        image = wx.EmptyImage(width, height)
        # image = wx.Image()
        image.SetData(array.tostring())
        wxBitmap = image.ConvertToBitmap()  # OR:  wx.BitmapFromImage(image)
        return wxBitmap

    def update(self):
        self.statusBarPercentage.Show(True)
        self.statusBar.Show(True)
        self.statusBarText.Show(True)
        self.Refresh()
        global video_compose
        fc = int(video_compose.frames_count)
        print fc
        self.statusBar.SetRange(fc)
        cf = 0
        while cf < fc:
            cf = int(video_compose.curr_frame)
            self.statusBar.SetValue(cf)
            self.statusBarPercentage.SetLabelText(str(int((100.0 / fc) * cf)) + "%")
            time.sleep(1)
        self.statusBarPercentage.Show(False)
        self.statusBar.Show(False)
        self.statusBarText.Show(False)
        self.Refresh()

    def block_GUI(self, type=False):
        self.time_slider.Enable(type)
        self.prev_button.Enable(type)
        self.prevD_button.Enable(type)
        self.next_button.Enable(type)
        self.nextD_button.Enable(type)
        self.set_start_time_button.Enable(type)
        self.time_spinner.Enable(type)
        self.pb_radioBtn1.Enable(type)
        self.pb_radioBtn2.Enable(type)
        self.pb_radioBtn3.Enable(type)
        self.pb_radioBtn4.Enable(type)
        self.pic1.Enable(type)
        self.pic2.Enable(type)
        self.pic3.Enable(type)
        self.pic1Text.Enable(type)
        self.pic2Text.Enable(type)
        self.pic3Text.Enable(type)

    def show_status_bar(self, type):
        self.statusBar.Show(type)
        self.statusBarText.Show(type)
        self.statusBarPercentage.Show(type)
        self.Fit()
        self.Layout()


class choose_files(main.choose_files):
    def __init__(self, parent):
        main.choose_files.__init__(self, parent)
        self.parent = parent

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
        global timer
        global autosync
        if data_file != "" and video_file != "" and dir_path != "":
            output = ""
            if self.m_textCtrl1.GetValue() == "":
                output = os.path.normpath(os.path.join(dir_path, 'output.avi'))
            else:
                output = os.path.normpath(os.path.join(dir_path, self.m_textCtrl1.GetValue() + ".avi"))
            video_compose = vc.Video_compose(data_file, video_file, "simple_frame_handler", output)
            if video_compose.data_collection.parsed_data == None:
                video_compose.quit_composing()
                # todo show error
                return

            self.Hide()
            self.parent.block_GUI(True)
            self.MakeModal(False)
            if autosync:
                timer = auto_sync.sync(video_compose.video_reader)
                self.parent.time_spinner.SetValue(int(timer))
                video_compose.set_data_start_time(int(timer))
            self.parent.show_frame()
            self.parent.time_slider.SetRange(0, video_compose.video_reader.get_frames_count())
            timestr = help.time_from_ms((int(video_compose.video_reader.get_frames_count()) // int(
                video_compose.video_reader.get_fps())) * 1000)
            self.parent.end_time.SetLabelText(timestr)

    def choose_filesOnClose(self, event):
        if data_file == "" and video_file == "" and dir_path == "":
            self.parent.Close()

        self.MakeModal(False)
        event.Skip()


class error_dialog(main.error_dialog):
    def __init__(self, parent):
        main.error_dialog.__init__(self, parent)
        self.parent = parent

    # Handlers for error_dialog events.
    def prev_buttonOnButtonClick(self, event):
        self.Close()


class progress_dialog(main.progress_dialog):
    def __init__(self, parent):
        main.progress_dialog.__init__(self, parent)
        self.parent = parent

    def update(self, vc):
        fc = int(vc.frames_count)
        print fc
        self.m_gauge1.SetRange(fc)
        cf = 0
        while cf < fc:
            cf = int(vc.curr_frame)
            self.m_gauge1.SetValue(cf)
            time.sleep(1)
        self.parent.working.Hide()


app = wx.App(False)  # Create a new app, don't redirect stdout/stderr to a window.
frame1 = main_frame(None)
frame1.Show(True)
app.SetTopWindow(frame1)
frame = choose_files(frame1)
frame.MakeModal(True)
frame.Show(True)
app.MainLoop()