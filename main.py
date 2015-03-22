# -*- coding: utf-8 -*- 

# ##########################################################################
# # Python code generated with wxFormBuilder (version Jun  5 2014)
# # http://www.wxformbuilder.org/
# #
# # PLEASE DO "NOT" EDIT THIS FILE!
# ##########################################################################

import wx
import wx.xrc

# ##########################################################################
## Class MyFrame1
###########################################################################

import video_compose as vc
import cv2
import helper as help
import auto_sync
import os

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


class MyFrame1(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(648, 647), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_INACTIVEBORDER))

        self.m_statusBar1 = self.CreateStatusBar(1, wx.ST_SIZEGRIP, wx.ID_ANY)
        self.m_menubar1 = wx.MenuBar(0)
        self.SetMenuBar(self.m_menubar1)

        bSizer4 = wx.BoxSizer(wx.VERTICAL)

        self.m_bitmap1 = wx.StaticBitmap(self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_bitmap1.SetMinSize(wx.Size(540, 350))

        bSizer4.Add(self.m_bitmap1, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_staticline1 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        bSizer4.Add(self.m_staticline1, 0, wx.EXPAND | wx.ALL, 5)

        bSizer5 = wx.BoxSizer(wx.VERTICAL)

        self.m_slider1 = wx.Slider(self, wx.ID_ANY, 0, 0, 100, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL)
        self.m_slider1.SetMinSize(wx.Size(640, -1))

        bSizer5.Add(self.m_slider1, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        gSizer4 = wx.GridSizer(0, 2, 0, 0)

        self.m_staticText6 = wx.StaticText(self, wx.ID_ANY, u"0 ", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText6.Wrap(-1)
        gSizer4.Add(self.m_staticText6, 0, wx.ALL, 5)

        self.m_staticText7 = wx.StaticText(self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText7.Wrap(-1)
        gSizer4.Add(self.m_staticText7, 0, wx.ALL | wx.ALIGN_RIGHT, 5)

        bSizer5.Add(gSizer4, 1, wx.EXPAND, 5)

        bSizer4.Add(bSizer5, 1, wx.EXPAND, 5)

        gSizer3 = wx.GridSizer(0, 4, 0, 0)

        self.m_button7 = wx.Button(self, wx.ID_ANY, u"<<", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer3.Add(self.m_button7, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_button4 = wx.Button(self, wx.ID_ANY, u"<", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer3.Add(self.m_button4, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_button5 = wx.Button(self, wx.ID_ANY, u">", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer3.Add(self.m_button5, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_button6 = wx.Button(self, wx.ID_ANY, u">>", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer3.Add(self.m_button6, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_panel2 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        gSizer3.Add(self.m_panel2, 1, wx.EXPAND | wx.ALL, 5)

        self.m_panel31 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        gSizer3.Add(self.m_panel31, 1, wx.EXPAND | wx.ALL | wx.ALIGN_RIGHT, 5)

        self.m_panel41 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        gSizer3.Add(self.m_panel41, 1, wx.EXPAND | wx.ALL, 5)

        self.m_button8 = wx.Button(self, wx.ID_ANY, u"Set data start time", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer3.Add(self.m_button8, 0, wx.ALL | wx.ALIGN_RIGHT, 5)

        bSizer4.Add(gSizer3, 1, wx.EXPAND, 5)

        self.m_staticline2 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        bSizer4.Add(self.m_staticline2, 0, wx.EXPAND | wx.ALL, 5)

        gSizer31 = wx.GridSizer(0, 4, 0, 0)

        self.m_panel4 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        gSizer31.Add(self.m_panel4, 1, wx.EXPAND | wx.ALL, 5)

        self.m_staticText3 = wx.StaticText(self, wx.ID_ANY, u"Data start time in video in ms", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.m_staticText3.Wrap(-1)
        gSizer31.Add(self.m_staticText3, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_spinCtrl1 = wx.SpinCtrl(self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS,
                                       -100000, 100000, 0)
        gSizer31.Add(self.m_spinCtrl1, 1, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_button1 = wx.Button(self, wx.ID_ANY, u"Stick data with video", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer31.Add(self.m_button1, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        bSizer4.Add(gSizer31, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer4)
        self.Layout()

        # Connect Events
        self.m_slider1.Bind(wx.EVT_SCROLL, self.m_slider1OnScroll)
        self.m_slider1.Bind(wx.EVT_SCROLL_CHANGED, self.m_slider1OnScrollChanged)
        self.m_button7.Bind(wx.EVT_BUTTON, self.m_button7OnButtonClick)
        self.m_button4.Bind(wx.EVT_BUTTON, self.m_button4OnButtonClick)
        self.m_button5.Bind(wx.EVT_BUTTON, self.m_button5OnButtonClick)
        self.m_button6.Bind(wx.EVT_BUTTON, self.m_button6OnButtonClick)
        self.m_button8.Bind(wx.EVT_BUTTON, self.m_button8OnButtonClick)
        self.m_spinCtrl1.Bind(wx.EVT_SPINCTRL, self.m_spinCtrl1OnSpinCtrl)
        self.m_spinCtrl1.Bind(wx.EVT_TEXT_ENTER, self.m_spinCtrl1OnTextEnter)
        self.m_button1.Bind(wx.EVT_BUTTON, self.m_button1OnButtonClick)

        global data_file
        global video_file
        global video_compose
        if data_file != "" and video_file != "":
            video_compose = vc.Video_compose(data_file, video_file, "simple_frame_handler",
                                             'C:\Users\peto\Desktop\output.avi')

            video_compose.set_data_start_time(time)
            self.show_frame()
            self.m_slider1.SetRange(0, video_compose.video_reader.get_frames_count())


    def __del__(self):
        pass


    def m_button7OnButtonClick(self, event):
        global curr_time
        curr_time -= 2000
        if curr_time < 0:
            curr_time = 0
            #self.m_spinCtrl1.SetValue(0)
        self.m_slider1.SetValue(video_compose.video_reader.get_position_frames())
        self.show_frame()
        #todo show frame


    def m_button6OnButtonClick(self, event):
        global curr_time
        curr_time += 2000
        #self.m_spinCtrl1.SetValue(curr_time)
        self.m_slider1.SetValue(video_compose.video_reader.get_position_frames())
        #todo show frame
        self.show_frame()


    def m_button8OnButtonClick(self, event):
        global time
        time = video_compose.video_reader.get_position_in_ms()
        self.m_spinCtrl1.SetValue(time)
        video_compose.set_data_start_time(time)
        self.show_frame()


    # Virtual event handlers, overide them in your derived class
    def m_slider1OnScroll(self, event):
        global curr_time
        #


    def m_slider1OnScrollChanged(self, event):
        global curr_time
        video_compose.video_reader.set_position_frame(self.m_slider1.GetValue())
        curr_time = video_compose.video_reader.get_position_in_ms()
        print
        curr_time
        self.show_frame()


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
            working = MyDialog31(self)
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


#############################################################################################################################################
## Class Choose files
###############################################################################################################################################################



class ChooseFiles(wx.Dialog):
    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                           size=wx.Size(438, 219), style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer3 = wx.BoxSizer(wx.VERTICAL)

        gSizer41 = wx.GridSizer(5, 2, 0, 0)

        self.m_staticText1 = wx.StaticText(self, wx.ID_ANY, u"Choose video file", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1.Wrap(-1)
        gSizer41.Add(self.m_staticText1, 0, wx.ALL, 5)

        self.video_filePicker = wx.FilePickerCtrl(self, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*",
                                                  wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE)
        self.video_filePicker.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_MENU))

        gSizer41.Add(self.video_filePicker, 1, wx.ALL | wx.EXPAND, 5)

        self.m_staticText2 = wx.StaticText(self, wx.ID_ANY, u"Choose data file", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText2.Wrap(-1)
        gSizer41.Add(self.m_staticText2, 0, wx.ALL, 5)

        self.data_filePicker = wx.FilePickerCtrl(self, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*",
                                                 wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE)
        gSizer41.Add(self.data_filePicker, 1, wx.ALL | wx.EXPAND, 5)

        self.m_staticText21 = wx.StaticText(self, wx.ID_ANY, u"Save To", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText21.Wrap(-1)
        gSizer41.Add(self.m_staticText21, 0, wx.ALL, 5)

        self.m_dirPicker1 = wx.DirPickerCtrl(self, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition,
                                             wx.DefaultSize, wx.DIRP_DEFAULT_STYLE)
        gSizer41.Add(self.m_dirPicker1, 0, wx.ALL, 5)

        self.m_staticText22 = wx.StaticText(self, wx.ID_ANY, u"Save as", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText22.Wrap(-1)
        gSizer41.Add(self.m_staticText22, 0, wx.ALL, 5)

        self.m_textCtrl1 = wx.TextCtrl(self, wx.ID_ANY, u"output", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer41.Add(self.m_textCtrl1, 0, wx.ALL, 5)

        self.m_panel5 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        gSizer41.Add(self.m_panel5, 1, wx.EXPAND | wx.ALL, 5)

        self.m_checkBox1 = wx.CheckBox(self, wx.ID_ANY, u"Auto sync with black screen.", wx.DefaultPosition,
                                       wx.DefaultSize, 0)
        gSizer41.Add(self.m_checkBox1, 0, wx.ALL, 5)

        bSizer3.Add(gSizer41, 1, wx.EXPAND, 5)

        self.m_button3 = wx.Button(self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer3.Add(self.m_button3, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.SetSizer(bSizer3)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.video_filePicker.Bind(wx.EVT_FILEPICKER_CHANGED, self.video_filePickerOnFileChanged)
        self.data_filePicker.Bind(wx.EVT_FILEPICKER_CHANGED, self.data_filePickerOnFileChanged)
        self.m_dirPicker1.Bind(wx.EVT_DIRPICKER_CHANGED, self.m_dirPicker1OnDirChanged)
        self.m_checkBox1.Bind(wx.EVT_CHECKBOX, self.m_checkBox1OnCheckBox)
        self.m_button3.Bind(wx.EVT_BUTTON, self.m_button3OnButtonClick)

        self.parent = parent

    def __del__(self):
        pass


    # Virtual event handlers, overide them in your derived class
    def m_checkBox1OnCheckBox(self, event):
        global autosync
        autosync = self.m_checkBox1.IsChecked()


    def video_filePickerOnFileChanged(self, event):
        global video_file
        video_file = event.GetPath()
        print(video_file)

    def data_filePickerOnFileChanged(self, event):
        global data_file
        data_file = event.GetPath()
        print(data_file)

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


    def m_dirPicker1OnDirChanged(self, event):
        global dir_path
        dir_path = event.GetPath()
        print(dir_path)


###########################################################################
## Class MyDialog3
###########################################################################

# class MyDialog3(wx.Dialog):
#     def __init__(self, parent):
#         wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
#                            size=wx.Size(300, 90), style=wx.DEFAULT_DIALOG_STYLE)
#
#         self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
#
#         bSizer6 = wx.BoxSizer(wx.VERTICAL)
#
#         self.m_staticText4 = wx.StaticText(self, wx.ID_ANY, u"ERROR", wx.DefaultPosition, wx.DefaultSize, 0)
#         self.m_staticText4.Wrap(-1)
#         bSizer6.Add(self.m_staticText4, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)
#
#         self.m_button4 = wx.Button(self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0)
#         bSizer6.Add(self.m_button4, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)
#
#         self.SetSizer(bSizer6)
#         self.Layout()
#
#         self.Centre(wx.BOTH)
#
#         # Connect Events
#         self.m_button4.Bind(wx.EVT_BUTTON, self.m_button4OnButtonClick)
#
#     def __del__(self):
#         pass
#
#
#     # Virtual event handlers, overide them in your derived class
#     def m_button4OnButtonClick(self, event):
#         event.Skip()
#
#
class MyDialog31(wx.Dialog):
    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                           size=wx.Size(206, 84), style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer5 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText5 = wx.StaticText(self, wx.ID_ANY, u"Working", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText5.Wrap(-1)
        bSizer5.Add(self.m_staticText5, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_gauge1 = wx.Gauge(self, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL)
        self.m_gauge1.SetValue(0)
        bSizer5.Add(self.m_gauge1, 0, wx.ALL, 5)

        self.SetSizer(bSizer5)
        self.Layout()

        self.Centre(wx.BOTH)

    def __del__(self):
        pass

#
# class main(MyFrame1):
#     def __init__(self, f):
#         MyFrame1.__init__(self, f)
#
#     def Show(self, b):
#         super.Show(b)


app = wx.App(False)  # Create a new app, don't redirect stdout/stderr to a window.
frame1 = MyFrame1(None)
frame1.Show(True)
frame = ChooseFiles(frame1)
frame.Show(True)
app.MainLoop()


