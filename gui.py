# -*- coding: utf-8 -*- 

# ##########################################################################
## Python code generated with wxFormBuilder (version Jun  5 2014)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

# ##########################################################################
## Class main_frame
###########################################################################

class main_frame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(1496, 647), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
        self.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOWTEXT))
        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_INACTIVEBORDER))

        self.m_statusBar1 = self.CreateStatusBar(1, wx.ST_SIZEGRIP, wx.ID_ANY)
        self.m_menubar1 = wx.MenuBar(0)
        self.SetMenuBar(self.m_menubar1)

        bSizer4 = wx.BoxSizer(wx.VERTICAL)

        gSizer15 = wx.GridSizer(1, 3, 0, 15)

        bSizer41 = wx.BoxSizer(wx.VERTICAL)

        bSizer41.SetMinSize(wx.Size(530, -1))
        self.m_bitmap11 = wx.StaticBitmap(self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size(540, 350), 0)
        self.m_bitmap11.SetMinSize(wx.Size(540, 350))
        self.m_bitmap11.SetMaxSize(wx.Size(540, 350))

        bSizer41.Add(self.m_bitmap11, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_staticline11 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        bSizer41.Add(self.m_staticline11, 0, wx.EXPAND | wx.ALL, 5)

        bSizer51 = wx.BoxSizer(wx.VERTICAL)

        self.m_slider11 = wx.Slider(self, wx.ID_ANY, 0, 0, 100, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL)
        self.m_slider11.SetMinSize(wx.Size(640, -1))

        bSizer51.Add(self.m_slider11, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        gSizer41 = wx.GridSizer(0, 2, 0, 0)

        self.m_staticText61 = wx.StaticText(self, wx.ID_ANY, u"00:00:000", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText61.Wrap(-1)
        gSizer41.Add(self.m_staticText61, 0, wx.ALL, 5)

        self.m_staticText71 = wx.StaticText(self, wx.ID_ANY, u"00:00:000", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText71.Wrap(-1)
        gSizer41.Add(self.m_staticText71, 0, wx.ALL | wx.ALIGN_RIGHT, 5)

        bSizer51.Add(gSizer41, 1, wx.EXPAND, 5)

        bSizer41.Add(bSizer51, 1, wx.EXPAND, 5)

        gSizer32 = wx.GridSizer(0, 4, 0, 0)

        self.m_button71 = wx.Button(self, wx.ID_ANY, u"<<", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer32.Add(self.m_button71, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_button41 = wx.Button(self, wx.ID_ANY, u"<", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer32.Add(self.m_button41, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_button51 = wx.Button(self, wx.ID_ANY, u">", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer32.Add(self.m_button51, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_button61 = wx.Button(self, wx.ID_ANY, u">>", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer32.Add(self.m_button61, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_panel21 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        gSizer32.Add(self.m_panel21, 1, wx.EXPAND | wx.ALL, 5)

        self.m_panel311 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        gSizer32.Add(self.m_panel311, 1, wx.EXPAND | wx.ALL | wx.ALIGN_RIGHT, 5)

        self.m_panel411 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        gSizer32.Add(self.m_panel411, 1, wx.EXPAND | wx.ALL, 5)

        self.m_button81 = wx.Button(self, wx.ID_ANY, u"Set data start time", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer32.Add(self.m_button81, 0, wx.ALL | wx.ALIGN_RIGHT, 5)

        bSizer41.Add(gSizer32, 1, wx.EXPAND, 5)

        gSizer151 = wx.GridSizer(0, 2, 0, 0)

        bSizer41.Add(gSizer151, 1, wx.EXPAND, 5)

        gSizer15.Add(bSizer41, 1, wx.EXPAND, 5)

        bSizer7 = wx.BoxSizer(wx.VERTICAL)

        gSizer311 = wx.GridSizer(0, 2, 0, 0)

        self.m_staticText31 = wx.StaticText(self, wx.ID_ANY, u"Data start time in video in ms", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText31.Wrap(-1)
        gSizer311.Add(self.m_staticText31, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_spinCtrl11 = wx.SpinCtrl(self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS,
                                        -100000, 100000, 0)
        gSizer311.Add(self.m_spinCtrl11, 1, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        bSizer7.Add(gSizer311, 0, wx.EXPAND, 5)

        self.m_staticline3 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        bSizer7.Add(self.m_staticline3, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND, 5)

        gSizer8 = wx.GridSizer(0, 1, 0, 0)

        self.m_staticText13 = wx.StaticText(self, wx.ID_ANY, u"Playback speed >>", wx.DefaultPosition, wx.DefaultSize,
                                            0)
        self.m_staticText13.Wrap(-1)
        gSizer8.Add(self.m_staticText13, 0, wx.ALL, 5)

        bSizer7.Add(gSizer8, 0, wx.EXPAND, 5)

        gSizer9 = wx.GridSizer(0, 4, 0, 0)

        self.pb_radioBtn1 = wx.RadioButton(self, wx.ID_ANY, u"Normal", wx.DefaultPosition, wx.DefaultSize, 0)
        self.pb_radioBtn1.SetValue(True)
        gSizer9.Add(self.pb_radioBtn1, 0, wx.ALL, 5)

        self.pb_radioBtn2 = wx.RadioButton(self, wx.ID_ANY, u"2X", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer9.Add(self.pb_radioBtn2, 0, wx.ALL, 5)

        self.pb_radioBtn3 = wx.RadioButton(self, wx.ID_ANY, u"5X", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer9.Add(self.pb_radioBtn3, 0, wx.ALL, 5)

        self.pb_radioBtn4 = wx.RadioButton(self, wx.ID_ANY, u"10x", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer9.Add(self.pb_radioBtn4, 0, wx.ALL, 5)

        bSizer7.Add(gSizer9, 0, wx.EXPAND, 5)

        self.m_staticline8 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        bSizer7.Add(self.m_staticline8, 0, wx.ALL | wx.EXPAND, 5)

        self.m_panel5 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer7.Add(self.m_panel5, 1, wx.ALL | wx.EXPAND, 5)

        gSizer15.Add(bSizer7, 1, wx.EXPAND, 5)

        bSizer8 = wx.BoxSizer(wx.VERTICAL)

        self.m_scrolledWindow1 = wx.ScrolledWindow(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                                   wx.HSCROLL | wx.VSCROLL)
        self.m_scrolledWindow1.SetScrollRate(5, 5)
        self.m_scrolledWindow1.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOWTEXT))
        self.m_scrolledWindow1.SetMinSize(wx.Size(10, 10))

        gSizer7 = wx.GridSizer(7, 2, 0, 1)

        self.pic1 = wx.StaticBitmap(self.m_scrolledWindow1, wx.ID_ANY, wx.Bitmap(u"1.png", wx.BITMAP_TYPE_ANY),
                                    wx.DefaultPosition, wx.DefaultSize, 0)
        self.pic1.SetMinSize(wx.Size(160, 90))

        gSizer7.Add(self.pic1, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.pic1Text = wx.StaticText(self.m_scrolledWindow1, wx.ID_ANY, u"Simple", wx.DefaultPosition, wx.DefaultSize,
                                      0)
        self.pic1Text.Wrap(-1)
        self.pic1Text.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHT))

        gSizer7.Add(self.pic1Text, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.pic2 = wx.StaticBitmap(self.m_scrolledWindow1, wx.ID_ANY, wx.Bitmap(u"1.png", wx.BITMAP_TYPE_ANY),
                                    wx.DefaultPosition, wx.DefaultSize, 0)
        self.pic2.SetMinSize(wx.Size(160, 90))

        gSizer7.Add(self.pic2, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.pic2Text = wx.StaticText(self.m_scrolledWindow1, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize,
                                      0)
        self.pic2Text.Wrap(-1)
        self.pic2Text.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BACKGROUND))

        gSizer7.Add(self.pic2Text, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.pic3 = wx.StaticBitmap(self.m_scrolledWindow1, wx.ID_ANY, wx.Bitmap(u"1.png", wx.BITMAP_TYPE_ANY),
                                    wx.DefaultPosition, wx.DefaultSize, 0)
        self.pic3.SetMinSize(wx.Size(160, 90))

        gSizer7.Add(self.pic3, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.pic3Text = wx.StaticText(self.m_scrolledWindow1, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize,
                                      0)
        self.pic3Text.Wrap(-1)
        self.pic3Text.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BACKGROUND))

        gSizer7.Add(self.pic3Text, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

        gSizer7.AddSpacer(( 0, 0), 1, wx.EXPAND, 5)

        gSizer7.AddSpacer(( 0, 0), 1, wx.EXPAND, 5)

        gSizer7.AddSpacer(( 0, 0), 1, wx.EXPAND, 5)

        gSizer7.AddSpacer(( 0, 0), 1, wx.EXPAND, 5)

        gSizer7.AddSpacer(( 0, 0), 1, wx.EXPAND, 5)

        gSizer7.AddSpacer(( 0, 0), 1, wx.EXPAND, 5)

        gSizer7.AddSpacer(( 0, 0), 1, wx.EXPAND, 5)

        gSizer7.AddSpacer(( 0, 0), 1, wx.EXPAND, 5)

        self.m_scrolledWindow1.SetSizer(gSizer7 )
        self.m_scrolledWindow1.Layout()
        gSizer7.Fit(self.m_scrolledWindow1)
        bSizer8.Add(self.m_scrolledWindow1, 1, wx.EXPAND | wx.ALL, 5)

        self.m_staticline9 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        bSizer8.Add(self.m_staticline9, 0, wx.EXPAND | wx.ALL, 5)

        self.statusBar = wx.Gauge(self, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL)
        self.statusBar.SetValue(0)
        bSizer8.Add(self.statusBar, 0, wx.ALL | wx.EXPAND, 5)

        gSizer10 = wx.GridSizer(0, 2, 0, 0)

        self.statusBarText = wx.StaticText(self, wx.ID_ANY, u"Working", wx.DefaultPosition, wx.DefaultSize, 0)
        self.statusBarText.Wrap(-1)
        gSizer10.Add(self.statusBarText, 0, wx.ALL | wx.ALIGN_RIGHT, 5)

        self.statusBarPercentage = wx.StaticText(self, wx.ID_ANY, u"0%", wx.DefaultPosition, wx.DefaultSize, 0)
        self.statusBarPercentage.Wrap(-1)
        gSizer10.Add(self.statusBarPercentage, 0, wx.ALL, 5)

        bSizer8.Add(gSizer10, 0, wx.EXPAND, 5)

        self.m_button11 = wx.Button(self, wx.ID_ANY, u"Stick data with video", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button11.SetFont(wx.Font(18, 74, 90, 90, False, "Arial"))
        self.m_button11.SetMinSize(wx.Size(250, 50))
        self.m_button11.SetMaxSize(wx.Size(100, 500))

        bSizer8.Add(self.m_button11, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        gSizer15.Add(bSizer8, 1, wx.EXPAND, 5)

        bSizer4.Add(gSizer15, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer4 )
        self.Layout()

        # Connect Events
        self.Bind(wx.EVT_CLOSE, self.main_frameOnClose)
        self.m_slider11.Bind(wx.EVT_SCROLL, self.m_slider1OnScroll)
        self.m_slider11.Bind(wx.EVT_SCROLL_CHANGED, self.m_slider1OnScrollChanged)
        self.m_button71.Bind(wx.EVT_BUTTON, self.m_button7OnButtonClick)
        self.m_button41.Bind(wx.EVT_BUTTON, self.m_button4OnButtonClick)
        self.m_button51.Bind(wx.EVT_BUTTON, self.m_button5OnButtonClick)
        self.m_button61.Bind(wx.EVT_BUTTON, self.m_button6OnButtonClick)
        self.m_button81.Bind(wx.EVT_BUTTON, self.m_button8OnButtonClick)
        self.m_spinCtrl11.Bind(wx.EVT_SPINCTRL, self.m_spinCtrl1OnSpinCtrl)
        self.m_spinCtrl11.Bind(wx.EVT_TEXT_ENTER, self.m_spinCtrl1OnTextEnter)
        self.pb_radioBtn1.Bind(wx.EVT_RADIOBUTTON, self.pb_radioBtn1OnRadioButton)
        self.pb_radioBtn2.Bind(wx.EVT_RADIOBUTTON, self.pb_radioBtn2OnRadioButton)
        self.pb_radioBtn3.Bind(wx.EVT_RADIOBUTTON, self.pb_radioBtn3OnRadioButton)
        self.pb_radioBtn4.Bind(wx.EVT_RADIOBUTTON, self.pb_radioBtn4OnRadioButton)
        self.pic1.Bind(wx.EVT_LEFT_UP, self.pic1OnLeftUp)
        self.pic1Text.Bind(wx.EVT_LEFT_UP, self.pic1TextOnLeftUp)
        self.pic2.Bind(wx.EVT_LEFT_UP, self.pic2OnLeftUp)
        self.pic2Text.Bind(wx.EVT_LEFT_UP, self.pic2TextOnLeftUp)
        self.pic3.Bind(wx.EVT_LEFT_UP, self.pic3OnLeftUp)
        self.pic3Text.Bind(wx.EVT_LEFT_UP, self.pic3TextOnLeftUp)
        self.m_button11.Bind(wx.EVT_BUTTON, self.m_button1OnButtonClick)

    def __del__(self):
        pass


    # Virtual event handlers, overide them in your derived class
    def main_frameOnClose(self, event):
        event.Skip()

    def m_slider1OnScroll(self, event):
        event.Skip()

    def m_slider1OnScrollChanged(self, event):
        event.Skip()

    def m_button7OnButtonClick(self, event):
        event.Skip()

    def m_button4OnButtonClick(self, event):
        event.Skip()

    def m_button5OnButtonClick(self, event):
        event.Skip()

    def m_button6OnButtonClick(self, event):
        event.Skip()

    def m_button8OnButtonClick(self, event):
        event.Skip()

    def m_spinCtrl1OnSpinCtrl(self, event):
        event.Skip()

    def m_spinCtrl1OnTextEnter(self, event):
        event.Skip()

    def pb_radioBtn1OnRadioButton(self, event):
        event.Skip()

    def pb_radioBtn2OnRadioButton(self, event):
        event.Skip()

    def pb_radioBtn3OnRadioButton(self, event):
        event.Skip()

    def pb_radioBtn4OnRadioButton(self, event):
        event.Skip()

    def pic1OnLeftUp(self, event):
        event.Skip()

    def pic1TextOnLeftUp(self, event):
        event.Skip()

    def pic2OnLeftUp(self, event):
        event.Skip()

    def pic2TextOnLeftUp(self, event):
        event.Skip()

    def pic3OnLeftUp(self, event):
        event.Skip()

    def pic3TextOnLeftUp(self, event):
        event.Skip()

    def m_button1OnButtonClick(self, event):
        event.Skip()
    

###########################################################################
## Class choose_files
###########################################################################

class choose_files(wx.Dialog):
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

        self.SetSizer(bSizer3 )
        self.Layout()

        self.Centre(wx.BOTH )
        
        # Connect Events
        self.Bind(wx.EVT_CLOSE, self.choose_filesOnClose)
        self.video_filePicker.Bind(wx.EVT_FILEPICKER_CHANGED, self.video_filePickerOnFileChanged)
        self.data_filePicker.Bind(wx.EVT_FILEPICKER_CHANGED, self.data_filePickerOnFileChanged)
        self.m_dirPicker1.Bind(wx.EVT_DIRPICKER_CHANGED, self.m_dirPicker1OnDirChanged)
        self.m_checkBox1.Bind(wx.EVT_CHECKBOX, self.m_checkBox1OnCheckBox)
        self.m_button3.Bind(wx.EVT_BUTTON, self.m_button3OnButtonClick)

    def __del__(self):
        pass


    # Virtual event handlers, overide them in your derived class
    def choose_filesOnClose(self, event):
        event.Skip()

    def video_filePickerOnFileChanged(self, event):
        event.Skip()

    def data_filePickerOnFileChanged(self, event):
        event.Skip()

    def m_dirPicker1OnDirChanged(self, event):
        event.Skip()

    def m_checkBox1OnCheckBox(self, event):
        event.Skip()

    def m_button3OnButtonClick(self, event):
        event.Skip()
    

###########################################################################
## Class error_dialog
###########################################################################

class error_dialog(wx.Dialog):
    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                           size=wx.Size(300, 90), style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer6 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText4 = wx.StaticText(self, wx.ID_ANY, u"ERROR", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText4.Wrap(-1)
        bSizer6.Add(self.m_staticText4, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_button4 = wx.Button(self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer6.Add(self.m_button4, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.SetSizer(bSizer6 )
        self.Layout()

        self.Centre(wx.BOTH )
        
        # Connect Events
        self.Bind(wx.EVT_CLOSE, self.error_dialogOnClose)
        self.m_button4.Bind(wx.EVT_BUTTON, self.m_button4OnButtonClick)

    def __del__(self):
        pass


    # Virtual event handlers, overide them in your derived class
    def error_dialogOnClose(self, event):
        event.Skip()

    def m_button4OnButtonClick(self, event):
        event.Skip()
    

###########################################################################
## Class progress_dialog
###########################################################################

class progress_dialog(wx.Dialog):
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

        self.SetSizer(bSizer5 )
        self.Layout()

        self.Centre(wx.BOTH)

    def __del__(self):
        pass
    

