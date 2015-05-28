# -*- coding: utf-8 -*- 

# ##########################################################################
## Python code generated with wxFormBuilder (version Jun  5 2014)
## http://www.wxformbuilder.org/
##
###########################################################################

import wx
import wx.xrc
import matplotlib

matplotlib.use('WXAgg')
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.figure import Figure

###########################################################################
## Class main_frame
###########################################################################

class main_frame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(-1, -1), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
        self.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOWTEXT))
        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_INACTIVEBORDER))

        self.m_statusBar1 = self.CreateStatusBar(1, wx.ST_SIZEGRIP, wx.ID_ANY)
        self.m_menubar1 = wx.MenuBar(0)
        self.SetMenuBar(self.m_menubar1)

        bSizer4 = wx.BoxSizer(wx.VERTICAL)

        fgSizer1 = wx.FlexGridSizer(1, 3, 0, 0)
        fgSizer1.SetFlexibleDirection(wx.BOTH)
        fgSizer1.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        bSizer41 = wx.BoxSizer(wx.VERTICAL)

        bSizer41.SetMinSize(wx.Size(530, -1))
        self.video_image = wx.StaticBitmap(self, wx.ID_ANY, wx.NullBitmap, wx.Point(0, 0), wx.Size(-1, -1), 0)
        # self.video_image.SetMinSize( wx.Size( 540, 255 ) )

        bSizer41.Add(self.video_image, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)

        self.m_staticline11 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        bSizer41.Add(self.m_staticline11, 0, wx.EXPAND | wx.ALL, 5)

        bSizer51 = wx.BoxSizer(wx.VERTICAL)

        self.time_slider = wx.Slider(self, wx.ID_ANY, 0, 0, 100, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL)
        self.time_slider.SetMinSize(wx.Size(540, -1))
        self.time_slider.SetMaxSize(wx.Size(-1, 25))

        bSizer51.Add(self.time_slider, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        gSizer41 = wx.GridSizer(0, 2, 0, 0)

        self.curr_time = wx.StaticText(self, wx.ID_ANY, u"00:00:000", wx.DefaultPosition, wx.DefaultSize, 0)
        self.curr_time.Wrap(-1)
        gSizer41.Add(self.curr_time, 0, wx.ALL, 5)

        self.end_time = wx.StaticText(self, wx.ID_ANY, u"00:00:000", wx.DefaultPosition, wx.DefaultSize, 0)
        self.end_time.Wrap(-1)
        gSizer41.Add(self.end_time, 0, wx.ALL | wx.ALIGN_RIGHT, 5)

        bSizer51.Add(gSizer41, 0, wx.EXPAND, 5)

        bSizer41.Add(bSizer51, 0, wx.EXPAND, 5)

        gSizer32 = wx.GridSizer(0, 4, 0, 0)

        self.prevD_button = wx.Button(self, wx.ID_ANY, u"<<", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer32.Add(self.prevD_button, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.prev_button = wx.Button(self, wx.ID_ANY, u"<", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer32.Add(self.prev_button, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.next_button = wx.Button(self, wx.ID_ANY, u">", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer32.Add(self.next_button, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.nextD_button = wx.Button(self, wx.ID_ANY, u">>", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer32.Add(self.nextD_button, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        bSizer41.Add(gSizer32, 0, wx.EXPAND, 5)

        bSizer9 = wx.BoxSizer(wx.VERTICAL)

        self.data_slider_label = wx.StaticText(self, wx.ID_ANY, u"Data Slider", wx.DefaultPosition, wx.DefaultSize, 0)
        self.data_slider_label.Wrap(-1)
        bSizer9.Add(self.data_slider_label, 0, wx.ALL, 5)

        self.data_slider = wx.Slider(self, wx.ID_ANY, 0, 0, 100, wx.DefaultPosition, wx.Size(-1, -1), wx.SL_HORIZONTAL)
        self.data_slider.SetMinSize(wx.Size(540, -1))

        bSizer9.Add(self.data_slider, 0, wx.ALL, 5)

        gSizer101 = wx.GridSizer(0, 2, 0, 0)

        self.data_curr_time = wx.StaticText(self, wx.ID_ANY, u"00:00:000", wx.DefaultPosition, wx.DefaultSize, 0)
        self.data_curr_time.Wrap(-1)
        gSizer101.Add(self.data_curr_time, 0, wx.ALL, 5)

        self.data_end_time = wx.StaticText(self, wx.ID_ANY, u"00:00:000", wx.DefaultPosition, wx.DefaultSize, 0)
        self.data_end_time.Wrap(-1)
        gSizer101.Add(self.data_end_time, 0, wx.ALL | wx.ALIGN_RIGHT, 5)

        self.data_lock = wx.CheckBox(self, wx.ID_ANY, u"Lock data", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer101.Add(self.data_lock, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.set_start_time_button = wx.Button(self, wx.ID_ANY, u"Synchronize!", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer101.Add(self.set_start_time_button, 0, wx.ALL | wx.ALIGN_RIGHT, 5)

        bSizer9.Add(gSizer101, 0, wx.EXPAND, 5)

        bSizer41.Add(bSizer9, 1, wx.EXPAND, 5)

        fgSizer1.Add(bSizer41, 1, wx.EXPAND, 5)

        bSizer7 = wx.BoxSizer(wx.VERTICAL)

        gSizer311 = wx.GridSizer(0, 2, 0, 0)

        self.start_time_label = wx.StaticText(self, wx.ID_ANY, u"Data and video delay in ms", wx.DefaultPosition,
                                              wx.DefaultSize, 0)
        self.start_time_label.Wrap(-1)
        gSizer311.Add(self.start_time_label, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.time_spinner = wx.SpinCtrl(self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS,
                                        -100000, 100000, 0)
        gSizer311.Add(self.time_spinner, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        bSizer7.Add(gSizer311, 0, wx.EXPAND, 5)

        self.m_staticline3 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        bSizer7.Add(self.m_staticline3, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND, 5)

        gSizer8 = wx.GridSizer(0, 1, 0, 0)

        self.playback_speed_label = wx.StaticText(self, wx.ID_ANY, u"Playback speed >>", wx.DefaultPosition,
                                                  wx.DefaultSize, 0)
        self.playback_speed_label.Wrap(-1)
        gSizer8.Add(self.playback_speed_label, 0, wx.ALL, 5)

        bSizer7.Add(gSizer8, 0, 0, 5)

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

        gSizer102 = wx.GridSizer(0, 2, 0, 0)

        self.graph_button = wx.Button(self, wx.ID_ANY, u"Show graph", wx.DefaultPosition, wx.DefaultSize, 0)
        self.graph_button.Enable(False)

        gSizer102.Add(self.graph_button, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.map_button = wx.Button(self, wx.ID_ANY, u"Show map", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer102.Add(self.map_button, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        bSizer7.Add(gSizer102, 0, wx.EXPAND, 5)

        fgSizer2 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer2.SetFlexibleDirection(wx.BOTH)
        fgSizer2.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.map_pic = wx.StaticBitmap(self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size(400, 400), 0)
        fgSizer2.Add(self.map_pic, 0, wx.ALL, 5)

        self.graph = GraphPanel(self)
        fgSizer2.Add(self.graph, 0, wx.ALL, 5)

        bSizer7.Add(fgSizer2, 1, wx.EXPAND, 5)

        fgSizer1.Add(bSizer7, 0, 0, 5)

        #TODO
        # self.m_panel5 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        # bSizer7.Add( self.m_panel5, 1, wx.ALL|wx.EXPAND, 5 )


        bSizer8 = wx.BoxSizer(wx.VERTICAL)

        self.m_scrolledWindow1 = wx.ScrolledWindow(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                                   wx.HSCROLL | wx.VSCROLL)
        self.m_scrolledWindow1.SetScrollRate(5, 5)
        self.m_scrolledWindow1.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOWTEXT))
        self.m_scrolledWindow1.SetMinSize(wx.Size(250, 10))

        gSizer7 = wx.GridSizer(7, 2, 0, 1)

        self.pic1 = wx.StaticBitmap(self.m_scrolledWindow1, wx.ID_ANY,
                                    wx.Bitmap(u"simple_frame_handler/images/simple.png", wx.BITMAP_TYPE_ANY),
                                    wx.DefaultPosition, wx.DefaultSize, 0)
        self.pic1.SetMinSize(wx.Size(160, 90))

        gSizer7.Add(self.pic1, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.pic1Text = wx.StaticText(self.m_scrolledWindow1, wx.ID_ANY, u"Simple", wx.DefaultPosition, wx.DefaultSize,
                                      0)
        self.pic1Text.Wrap(-1)
        self.pic1Text.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHT))

        gSizer7.Add(self.pic1Text, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.pic2 = wx.StaticBitmap(self.m_scrolledWindow1, wx.ID_ANY,
                                    wx.Bitmap(u"simple_moto_handler/images/moto.png", wx.BITMAP_TYPE_ANY),
                                    wx.DefaultPosition, wx.DefaultSize, 0)
        self.pic2.SetMinSize(wx.Size(160, 90))

        gSizer7.Add(self.pic2, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.pic2Text = wx.StaticText(self.m_scrolledWindow1, wx.ID_ANY, u"Moto", wx.DefaultPosition, wx.DefaultSize,
                                      0)
        self.pic2Text.Wrap(-1)
        self.pic2Text.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BACKGROUND))

        gSizer7.Add(self.pic2Text, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        # self.pic3 = wx.StaticBitmap(self.m_scrolledWindow1, wx.ID_ANY, wx.Bitmap(u"1.png", wx.BITMAP_TYPE_ANY),
        #                             wx.DefaultPosition, wx.DefaultSize, 0)
        # self.pic3.SetMinSize(wx.Size(160, 90))
        #
        # gSizer7.Add(self.pic3, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

        # self.pic3Text = wx.StaticText(self.m_scrolledWindow1, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize,
        #                               0)
        # self.pic3Text.Wrap(-1)
        # self.pic3Text.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BACKGROUND))
        #
        # gSizer7.Add(self.pic3Text, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

        gSizer7.AddSpacer(( 0, 0), 1, wx.EXPAND, 5)

        gSizer7.AddSpacer(( 0, 0), 1, wx.EXPAND, 5)

        gSizer7.AddSpacer(( 0, 0), 1, wx.EXPAND, 5)

        gSizer7.AddSpacer(( 0, 0), 1, wx.EXPAND, 5)

        gSizer7.AddSpacer(( 0, 0), 1, wx.EXPAND, 5)

        gSizer7.AddSpacer(( 0, 0), 1, wx.EXPAND, 5)

        gSizer7.AddSpacer(( 0, 0), 1, wx.EXPAND, 5)

        gSizer7.AddSpacer(( 0, 0), 1, wx.EXPAND, 5)

        self.m_scrolledWindow1.SetSizer(gSizer7)
        self.m_scrolledWindow1.Layout()
        gSizer7.Fit(self.m_scrolledWindow1)
        bSizer8.Add(self.m_scrolledWindow1, 1, wx.EXPAND | wx.ALL | wx.ALIGN_RIGHT, 5)

        self.m_staticline9 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        bSizer8.Add(self.m_staticline9, 0, wx.EXPAND | wx.ALL, 5)

        self.statusBar = wx.Gauge(self, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL)
        self.statusBar.SetValue(0)
        self.statusBar.SetMinSize(wx.Size(400, -1))

        bSizer8.Add(self.statusBar, 0, wx.ALL | wx.EXPAND, 5)

        bSizer8.AddSpacer(( 400, 0), 0, wx.EXPAND, 0)

        gSizer10 = wx.GridSizer(0, 2, 0, 0)

        self.statusBarText = wx.StaticText(self, wx.ID_ANY, u"Working", wx.DefaultPosition, wx.DefaultSize, 0)
        self.statusBarText.Wrap(-1)
        gSizer10.Add(self.statusBarText, 0, wx.ALL | wx.ALIGN_RIGHT, 5)

        self.statusBarPercentage = wx.StaticText(self, wx.ID_ANY, u"0%", wx.DefaultPosition, wx.DefaultSize, 0)
        self.statusBarPercentage.Wrap(-1)
        gSizer10.Add(self.statusBarPercentage, 0, wx.ALL, 5)

        bSizer8.Add(gSizer10, 0, wx.EXPAND, 5)

        self.main_button = wx.Button(self, wx.ID_ANY, u"Stick data with video", wx.DefaultPosition, wx.DefaultSize, 0)
        self.main_button.SetFont(wx.Font(18, 74, 90, 90, False, "Arial"))
        self.main_button.SetMinSize(wx.Size(400, 50))

        bSizer8.Add(self.main_button, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.cancel_button = wx.Button(self, wx.ID_ANY, u"CANCEL", wx.DefaultPosition, wx.DefaultSize, 0)
        self.cancel_button.SetFont(wx.Font(18, 74, 90, 90, False, "Arial"))
        self.cancel_button.SetMinSize(wx.Size(400, 50))

        bSizer8.Add(self.cancel_button, 0, wx.ALL, 5)

        fgSizer1.Add(bSizer8, 1, wx.EXPAND, 5)

        bSizer4.Add(fgSizer1, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer4)
        self.Layout()
        bSizer4.Fit(self)

        # Connect Events
        self.Bind(wx.EVT_CLOSE, self.main_frameOnClose)
        self.time_slider.Bind(wx.EVT_SCROLL, self.time_sliderOnScroll)
        self.time_slider.Bind(wx.EVT_SCROLL_CHANGED, self.time_sliderOnScrollChanged)
        self.prevD_button.Bind(wx.EVT_BUTTON, self.prevD_buttonOnButtonClick)
        self.prev_button.Bind(wx.EVT_BUTTON, self.prev_buttonOnButtonClick)
        self.next_button.Bind(wx.EVT_BUTTON, self.next_buttonOnButtonClick)
        self.nextD_button.Bind(wx.EVT_BUTTON, self.nextD_buttonOnButtonClick)
        self.data_slider.Bind(wx.EVT_SCROLL_CHANGED, self.data_sliderOnScrollChanged)
        self.data_lock.Bind(wx.EVT_CHECKBOX, self.data_lockOnCheckBox)
        self.set_start_time_button.Bind(wx.EVT_BUTTON, self.set_start_time_buttonOnButtonClick)
        self.set_start_time_button.Bind(wx.EVT_KEY_DOWN, self.set_start_time_buttonOnKeyDown)
        self.time_spinner.Bind(wx.EVT_SPINCTRL, self.time_spinnerOnSpinCtrl)
        self.time_spinner.Bind(wx.EVT_TEXT_ENTER, self.time_spinnerOnTextEnter)
        self.pb_radioBtn1.Bind(wx.EVT_RADIOBUTTON, self.pb_radioBtn1OnRadioButton)
        self.pb_radioBtn2.Bind(wx.EVT_RADIOBUTTON, self.pb_radioBtn2OnRadioButton)
        self.pb_radioBtn3.Bind(wx.EVT_RADIOBUTTON, self.pb_radioBtn3OnRadioButton)
        self.pb_radioBtn4.Bind(wx.EVT_RADIOBUTTON, self.pb_radioBtn4OnRadioButton)
        self.graph_button.Bind(wx.EVT_BUTTON, self.graph_buttonOnButtonClick)
        self.map_button.Bind(wx.EVT_BUTTON, self.map_buttonOnButtonClick)
        self.pic1.Bind(wx.EVT_LEFT_UP, self.pic1OnLeftUp)
        self.pic1Text.Bind(wx.EVT_LEFT_UP, self.pic1TextOnLeftUp)
        self.pic2.Bind(wx.EVT_LEFT_UP, self.pic2OnLeftUp)
        self.pic2Text.Bind(wx.EVT_LEFT_UP, self.pic2TextOnLeftUp)
        # self.pic3.Bind( wx.EVT_LEFT_UP, self.pic3OnLeftUp )
        # self.pic3Text.Bind( wx.EVT_LEFT_UP, self.pic3TextOnLeftUp )
        self.main_button.Bind(wx.EVT_BUTTON, self.main_buttonOnButtonClick)
        self.cancel_button.Bind(wx.EVT_BUTTON, self.cancel_buttonOnButtonClick)

    def __del__(self):
        pass


    # Virtual event handlers, overide them in your derived class
    def main_frameOnClose(self, event):
        event.Skip()

    def time_sliderOnScroll(self, event):
        event.Skip()

    def time_sliderOnScrollChanged(self, event):
        event.Skip()

    def prevD_buttonOnButtonClick(self, event):
        event.Skip()

    def prev_buttonOnButtonClick(self, event):
        event.Skip()

    def next_buttonOnButtonClick(self, event):
        event.Skip()

    def nextD_buttonOnButtonClick(self, event):
        event.Skip()

    def data_sliderOnScrollChanged(self, event):
        event.Skip()

    def data_lockOnCheckBox(self, event):
        event.Skip()

    def set_start_time_buttonOnButtonClick(self, event):
        event.Skip()

    def set_start_time_buttonOnKeyDown(self, event):
        event.Skip()

    def time_spinnerOnSpinCtrl(self, event):
        event.Skip()

    def time_spinnerOnTextEnter(self, event):
        event.Skip()

    def pb_radioBtn1OnRadioButton(self, event):
        event.Skip()

    def pb_radioBtn2OnRadioButton(self, event):
        event.Skip()

    def pb_radioBtn3OnRadioButton(self, event):
        event.Skip()

    def pb_radioBtn4OnRadioButton(self, event):
        event.Skip()

    def graph_buttonOnButtonClick(self, event):
        event.Skip()

    def map_buttonOnButtonClick(self, event):
        event.Skip()

    def pic1OnLeftUp(self, event):
        event.Skip()

    def pic1TextOnLeftUp(self, event):
        event.Skip()

    def pic2OnLeftUp(self, event):
        event.Skip()

    def pic2TextOnLeftUp(self, event):
        event.Skip()

    # def pic3OnLeftUp( self, event ):
    #     event.Skip()
    #
    # def pic3TextOnLeftUp( self, event ):
    #     event.Skip()

    def main_buttonOnButtonClick(self, event):
        event.Skip()

    def cancel_buttonOnButtonClick(self, event):
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

        self.SetSizer(bSizer3)
        self.Layout()

        self.Centre(wx.BOTH)

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

        self.label = wx.StaticText(self, wx.ID_ANY, u"ERROR", wx.DefaultPosition, wx.DefaultSize, 0)
        self.label.Wrap(-1)
        bSizer6.Add(self.label, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.button = wx.Button(self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer6.Add(self.button, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.SetSizer(bSizer6)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.Bind(wx.EVT_CLOSE, self.error_dialogOnClose)
        self.button.Bind(wx.EVT_BUTTON, self.buttonOnButtonClick)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def error_dialogOnClose(self, event):
        event.Skip()

    def buttonOnButtonClick(self, event):
        event.Skip()


class GraphPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, wx.ID_ANY, wx.DefaultPosition, wx.Size(400, 400), wx.TAB_TRAVERSAL)
        self.figure = Figure(figsize=(5, 5), facecolor=(0.95686274509, 0.96862745098, 0.98823529411))
        self.axes = self.figure.add_subplot(111)
        self.canvas = FigureCanvas(self, -1, self.figure)
        self.Fit()
        self.first = True
        self.abc = None

    def draw(self, interpolation, times, speeds, max_speed, curr_value):
        if self.first:
            self.axes.set_xlabel("Time in seconds")
            self.axes.set_ylabel("Speed in kph")
            self.axes.axhline(0, color='k', linewidth=2)
            self.abc = self.axes.axvline(curr_value, color='r')
            self.axes.plot(times, interpolation(times))
            tt = []
            a1 = 0
            a2 = times[len(times) - 1]
            for i in range(0, 9):
                tt.append(int(a2 / 9000.0 * float(i)))
            self.axes.set_xticklabels(tt, range(0, len(tt) - 1))
            self.axes.set_ylim(-1, max_speed + 1)
            self.first = False
        else:
            self.abc.set_xdata(curr_value)
            self.canvas.draw()

