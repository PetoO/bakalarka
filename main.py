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
import google_map
from PIL import ImageDraw, Image

data_file = ""
video_file = ""
dir_path = ""
output = "output.avi"
timer = 0
curr_time = 0
data_time = 0
video_compose = None
frame = None
frame_handlers = ["simple_frame_handler", "simple_moto_handler"]
blocked_GUI = False
locked_data = False
data_lock_time = 0
graph = True
mapp = None

#
# video_file = "C:\Users\peto\Desktop\hero.mp4"
# data_file = "C:\Users\peto\Desktop\hero.tcx"
# #
# # video_file = "VIRB.MP4"
# # #data_file = "test1.tcx"
# # data_file = "VIRB.GPX"
# # # video_file =  "SampleVideo.mp4"
# dir_path = 'C:\Users\peto\Desktop\output.avi'


class main_frame(main.main_frame):
    def __init__(self, parent):
        main.main_frame.__init__(self, parent)
        global data_file
        global video_file
        global video_compose
        if data_file != "" and video_file != "":
            video_compose = vc.Video_compose(data_file, video_file, "simple_frame_handler",
                                             'C:\\Users\\peto\\Desktop\\output.avi')
        self.show_status_bar(False)
        self.block_GUI()
        # todo delete
        #self.init_after_vd_load()


    def plot_graph(self):
        global data_time
        global video_compose
        global graph
        global mapp
        global locked_data
        print locked_data
        print( data_lock_time)
        if graph:
            if locked_data:
                self.graph.draw(video_compose.data_collection.speed_interpolation, video_compose.data_collection.times,
                                video_compose.data_collection.speeds, video_compose.data_collection.max_speed,
                                (self.data_slider.GetValue() + curr_time - data_lock_time))
            else:
                self.graph.draw(video_compose.data_collection.speed_interpolation, video_compose.data_collection.times,
                                video_compose.data_collection.speeds, video_compose.data_collection.max_speed,
                                data_time)
        else:
            if locked_data:
                data = video_compose.data_collection.get_data_at(
                    self.data_slider.GetValue() + curr_time - data_lock_time)
            else:
                data = video_compose.data_collection.get_data_at(data_time)
            img = self.get_bitmap(mapp.get_image(data["LatitudeDegrees"], data["LongitudeDegrees"]))
            self.map_pic.SetBitmap(img)


    def init_after_vd_load(self):
        global mapp
        global video_compose
        global curr_time

        self.show_status_bar(False)
        self.time_slider.SetRange(0, video_compose.video_reader.get_frames_count() - 1)
        video_compose.video_reader.set_position_in_ms(curr_time)
        self.time_slider.SetValue(int(video_compose.video_reader.get_position_frames()))
        self.data_slider.SetRange(0, int(video_compose.data_collection.end_time))
        timestr = help.time_from_ms(int(video_compose.data_collection.end_time))

        self.data_end_time.SetLabelText(timestr)
        timestr = help.time_from_ms(int((float(video_compose.video_reader.get_frames_count()) / float(
            video_compose.video_reader.get_fps())) * 1000))
        self.end_time.SetLabelText(timestr)
        mapp = google_map.Google_map(video_compose.data_collection)
        mapp.set_size(400, 400)
        mapp.set_zoom(18)

        self.update_sync()
        self.show_graph_or_map(True)


    def update_sync(self):
        global data_time
        global curr_time
        global video_compose
        global locked_data
        timestr = help.time_from_ms(int(curr_time))
        self.curr_time.SetLabelText(timestr)
        if not locked_data:
            video_compose.set_data_start_time(curr_time - data_time)
        self.plot_graph()
        self.show_frame()

    # Handlers for main_frame events.
    def time_sliderOnScroll(self, event):
        # TODO: Implement time_sliderOnScroll
        pass

    def time_sliderOnScrollChanged(self, event):
        # TODO
        global curr_time
        video_compose.video_reader.set_position_frame(self.time_slider.GetValue())
        curr_time = video_compose.video_reader.get_position_in_ms()
        # timestr = help.time_from_ms(int(video_compose.data_collection.end_time))
        self.update_sync()

    def prevD_buttonOnButtonClick(self, event):
        global curr_time
        # curr_time -= 2000
        # if curr_time < 0:
        # curr_time = 0
        value = self.time_slider.GetValue()
        video_compose.video_reader.set_position_frame(value - 60)
        self.time_slider.SetValue(value - 60)
        curr_time = video_compose.video_reader.get_position_in_ms()
        self.update_sync()

    def prev_buttonOnButtonClick(self, event):
        global curr_time
        # curr_time -= 150
        # if curr_time < 0:
        # curr_time = 0
        value = self.time_slider.GetValue()
        video_compose.video_reader.set_position_frame(value - 7)
        self.time_slider.SetValue(value - 7)
        curr_time = video_compose.video_reader.get_position_in_ms()
        self.update_sync()

    def next_buttonOnButtonClick(self, event):
        global curr_time
        value = self.time_slider.GetValue()
        video_compose.video_reader.set_position_frame(value + 7)
        self.time_slider.SetValue(value + 7)
        curr_time = video_compose.video_reader.get_position_in_ms()
        self.update_sync()

    def nextD_buttonOnButtonClick(self, event):
        global curr_time
        value = self.time_slider.GetValue()
        video_compose.video_reader.set_position_frame(value + 60)
        self.time_slider.SetValue(value + 60)
        curr_time = video_compose.video_reader.get_position_in_ms()
        self.update_sync()

    def data_sliderOnScrollChanged(self, event):
        global data_time
        data_time = self.data_slider.GetValue()
        self.data_curr_time.SetLabelText(help.time_from_ms(data_time))
        self.update_sync()

    def data_lockOnCheckBox(self, event):
        self.lock_data()

    def lock_data(self):
        global data_lock_time
        global locked_data
        global curr_time
        global data_time
        if self.data_lock.IsChecked():
            self.data_slider.Enable(False)
            locked_data = True
            data_lock_time = curr_time
        else:
            self.data_slider.Enable(True)
            # todo
            data_time = self.data_slider.GetValue() + curr_time - data_lock_time
            self.data_slider.SetValue(data_time)
            locked_data = False
        self.update_sync()

    def set_start_time_buttonOnButtonClick(self, event):
        global timer
        global curr_time
        global data_time
        timer = curr_time - data_time
        self.time_spinner.SetValue(timer)
        video_compose.set_data_start_time(timer)
        self.show_frame()

    def time_spinnerOnSpinCtrl(self, event):
        global timer
        timer = self.time_spinner.GetValue()
        video_compose.set_data_start_time(-timer)
        self.show_frame()

    def time_spinnerOnTextEnter(self, event):
        global timer
        timer = self.time_spinner.GetValue()
        video_compose.set_data_start_time(-timer)
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

    def show_graph_or_map(self, type):
        global graph
        graph = type
        self.graph_button.Enable(not type)
        self.map_button.Enable(type)
        self.map_pic.Show(not type)
        self.graph.Show(type)
        self.plot_graph()
        self.Refresh()
        self.Fit()
        self.Layout()

    def graph_buttonOnButtonClick(self, event):
        self.show_graph_or_map(True)

    def map_buttonOnButtonClick(self, event):
        self.show_graph_or_map(False)

    def pic1OnLeftUp(self, event):
        self.pic1Text.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHT))
        self.pic2Text.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BACKGROUND))
        global video_compose
        global frame_handlers
        video_compose.load_handler(frame_handlers[0])
        self.show_frame()
        self.Refresh()

    def pic1TextOnLeftUp(self, event):
        self.pic1Text.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHT))
        self.pic2Text.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BACKGROUND))
        global video_compose
        global frame_handlers
        video_compose.load_handler(frame_handlers[0])
        self.show_frame()
        self.Refresh()

    def pic2OnLeftUp(self, event):
        self.pic1Text.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BACKGROUND))
        self.pic2Text.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHT))
        global video_compose
        global frame_handlers
        video_compose.load_handler(frame_handlers[1])
        self.show_frame()
        self.Refresh()

    def pic2TextOnLeftUp(self, event):
        self.pic1Text.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BACKGROUND))
        self.pic2Text.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHT))
        global video_compose
        global frame_handlers
        video_compose.load_handler(frame_handlers[1])
        self.show_frame()
        self.Refresh()

    def show_frame(self):
        # TODO
        global video_compose
        global timer
        global frame
        global curr_time

        if video_compose is not None:
            #frame = video_compose.video_reader.read_frame_at_time(curr_time)
            frame = video_compose.get_handled_frame(curr_time)
            #frame = cv2.resize(frame, (0, 0), fx=0.26, fy=0.26)
            frame = help.scale_image(frame, 540, 255)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            # img = Image.fromarray(frame)
            img = self.get_bitmap(frame)
            self.video_image.SetBitmap(img)
            self.Refresh()
            self.Fit()
            self.Layout()

    def get_bitmap(self, array):
        height, width = array.shape[:2]
        image = wx.EmptyImage(width, height)
        image.SetData(array.tostring())
        bitmap = image.ConvertToBitmap()
        return bitmap

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
            cf = int(video_compose.video_reader.curr_frame)
            self.statusBar.SetValue(cf)
            num = int((100.0 / fc) * cf)
            if num > 100:
                num = 100
            self.statusBarPercentage.SetLabelText(str(num) + "%")
            time.sleep(1)
        self.statusBar.SetValue(0)
        self.statusBarPercentage.SetLabelText(str(0) + "%")
        self.show_status_bar(False)
        self.block_GUI(True)


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
        # self.pic3.Enable(type)
        self.pic1Text.Enable(type)
        self.pic2Text.Enable(type)
        # self.pic3Text.Enable(type)
        self.data_lock.Enable(type)
        if type:
            if self.graph.IsShown:
                self.map_button.Enable(type)
            else:
                self.graph_button.Enable(type)
                self.plot_graph()
        else:
            self.graph_button.Enable(type)
            self.map_button.Enable(type)

    def show_status_bar(self, type):
        self.statusBar.Show(type)
        self.statusBarText.Show(type)
        self.statusBarPercentage.Show(type)
        self.main_button.Show(not type)
        self.cancel_button.Show(type)
        self.Fit()
        self.Layout()

    def cancel_buttonOnButtonClick(self, event):
        global video_compose
        video_compose.cancel_composing()
        self.show_status_bar(False)
        self.block_GUI(True)
        self.statusBar.SetValue(0)
        self.statusBarPercentage.SetLabelText(str(0) + "%")


class choose_files(main.choose_files):
    def __init__(self, parent):
        main.choose_files.__init__(self, parent)
        self.parent = parent
        self.autosync = False
        self.err = err_dialog(self)

    def show_error(self, type, text):
        self.err.MakeModal(type)
        self.err.Show(type)
        self.MakeModal(not type)
        self.err.label.SetLabelText(text)
        self.err.Layout()

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
        self.autosync = self.m_checkBox1.IsChecked()

    def m_button3OnButtonClick(self, event):
        global data_file
        global video_file
        global video_compose
        global dir_path
        global timer
        global locked_data
        global curr_time
        if data_file != "" and video_file != "" and dir_path != "":
            output = ""
            if self.m_textCtrl1.GetValue() == "":
                output = os.path.normpath(os.path.join(dir_path, 'output.avi'))
            else:
                output = os.path.normpath(os.path.join(dir_path, self.m_textCtrl1.GetValue() + ".avi"))
            video_compose = vc.Video_compose(data_file, video_file, "simple_frame_handler", output)

            if video_compose.data_collection.parsed_data is None:
                video_compose.quit_composing()
                video_compose = None
                # todo show error
                self.show_error(True, "Invalid data file!")
                return

            if video_compose.video_reader is None:
                video_compose.quit_composing()
                video_compose = None
                # todo show error
                self.show_error(True, "Invalid video file!")
                return

            self.Hide()
            self.parent.block_GUI(True)
            self.MakeModal(False)
            if self.autosync:
                timer = auto_sync.sync(video_compose.video_reader)
                curr_time = timer
                self.parent.time_spinner.SetValue(int(timer))
                video_compose.set_data_start_time(int(timer))
                self.parent.data_lock.SetValue(True)
                locked_data = True
                self.parent.data_slider.Enable(False)
            self.parent.block_GUI(True)
            self.parent.init_after_vd_load()

    def choose_filesOnClose(self, event):
        # if data_file == "" and video_file == "" and dir_path == "":
        self.parent.Close()
        self.MakeModal(False)
        event.Skip()


class err_dialog(main.error_dialog):
    def __init__(self, parent):
        main.error_dialog.__init__(self, parent)
        self.parent = parent

    # Handlers for error_dialog events.
    def error_dialogOnClose(self, event):
        self.parent.MakeModal(True)
        self.Hide()


    def buttonOnButtonClick(self, event):
        self.MakeModal(False)
        self.parent.MakeModal(True)
        self.Close()


app = wx.App(False)  # Create a new app, don't redirect stdout/stderr to a window.
frame1 = main_frame(None)
frame1.Show(True)
app.SetTopWindow(frame1)
frame = choose_files(frame1)
frame.MakeModal(True)
frame.Show(True)
app.MainLoop()