# -*- coding: utf-8 -*- 

# ##########################################################################
# # Python code generated with wxFormBuilder (version Jun  5 2014)
# # http://www.wxformbuilder.org/
# #
# # PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.media
import wx.animate
import numpy
import cv2


###########################################################################
## Class picture
###########################################################################

class picture(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(500, 300), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        gSizer1 = wx.GridSizer(0, 2, 0, 0)

        self.m_bitmap1 = wx.StaticBitmap(self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer1.Add(self.m_bitmap1, 0, wx.ALL, 5)

        self.m_mediaCtrl1 = wx.media.MediaCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize)
        self.m_mediaCtrl1.SetPlaybackRate(1)
        self.m_mediaCtrl1.SetVolume(1)
        gSizer1.Add(self.m_mediaCtrl1, 0, wx.ALL, 5)

        self.m_animCtrl1 = wx.animate.AnimationCtrl(self, wx.ID_ANY, wx.animate.NullAnimation, wx.DefaultPosition,
                                                    wx.DefaultSize, wx.animate.AC_DEFAULT_STYLE)
        gSizer1.Add(self.m_animCtrl1, 0, wx.ALL, 5)

        self.SetSizer(gSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

    def __del__(self):
        pass

    def DisplayNext(self, Img, event=None):
        # load the image
        self.MaxImageSize = 200
        #Img = self.PilImageToWxBitmap(Img)
        Img = cv2.resize(Img, (0, 0), fx=0.26, fy=0.26)
        Img = self.GetBitmap(Img)
        # scale the image, preserving the aspect ratio
        # W = Img.GetWidth()
        # H = Img.GetHeight()
        # if W > H:
        #     NewW = self.MaxImageSize
        #     NewH = self.MaxImageSize * H / W
        # else:
        #     NewH = self.MaxImageSize
        #     NewW = self.MaxImageSize * W / H
        # Img = Img.Scale(NewW, NewH)

        # convert it to a wx.Bitmap, and put it on the wx.StaticBitmap
        #self.m_bitmap1.SetBitmap(wx.BitmapFromImage(Img))
        self.m_bitmap1.SetBitmap(Img)

        # You can fit the frame to the image, if you want.
        #self.Fit()
        #self.Layout()
        self.Refresh()


    def PilImageToWxImage(self, myPilImage, copyAlpha=False):
        if copyAlpha:  # Make sure there is an alpha layer copy.

            myWxImage = wx.EmptyImage(*myPilImage.size)
            myPilImageCopyRGBA = myPilImage.copy()
            myPilImageCopyRGB = myPilImageCopyRGBA.convert('RGB')  # RGBA --> RGB
            myPilImageRgbData = myPilImageCopyRGB.tostring()
            myWxImage.SetData(myPilImageRgbData)
            myWxImage.SetAlphaData(myPilImageCopyRGBA.tostring()[3::4])  # Create layer and insert alpha values.
        else:  # The resulting image will not have alpha.

            myWxImage = wx.EmptyImage(*myPilImage.size)
            myPilImageCopy = myPilImage.copy()
            myPilImageCopyRGB = myPilImageCopy.convert('RGB')  # Discard any alpha from the PIL image.
            myPilImageRgbData = myPilImageCopyRGB.tostring()
            myWxImage.SetData(myPilImageRgbData)
        return myWxImage


    def PilImageToWxBitmap(self, myPilImage):
        return self.WxImageToWxBitmap(self.PilImageToWxImage(myPilImage))

    def WxImageToWxBitmap(self, myWxImage):
        return myWxImage.ConvertToBitmap()

    def WxBitmapToWxImage(self, myBitmap):
        return wx.ImageFromBitmap(myBitmap)

    def GetBitmap(self, array, width=1920, height=1080, colour=(0, 0, 0)):
        image = wx.EmptyImage(width, height)
        image.SetData(array.tostring())
        wxBitmap = image.ConvertToBitmap()  # OR:  wx.BitmapFromImage(image)
        return wxBitmap


class app:
    def __init__(self):
        app = wx.App(False)  # Create a new app, don't redirect stdout/stderr to a window.
        self.frame = picture(None)  # A Frame is a top-level window.
        self.frame.Show(True)  # Show the frame.
        app.MainLoop()

    def set_img(self, img):
        self.frame.DisplayNext(img)