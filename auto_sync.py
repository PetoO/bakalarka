# to b&w
# mnozstvo ciernej (60%)aspon, vs mnozstvo ine farby musi byt vacsie ako
import cv2
import numpy as np
import sys


def sync(vr):
    print
    "Starting auto synchronization."
    a = 0
    a = _get_time(vr)
    if a == -1:
        return 0
    print
    "Synced to time " + str(a) + " ms."
    return a


def _get_time(vr):
    # data = "C:\Users\peto\Desktop\u.png"
    # im1 = cv2.imread(data,0)

    trshld = 0.75
    trshld1 = 0.60
    res = vr.get_frame_width() * vr.get_frame_height()
    t = 0
    tl = int((vr.get_frames_count() * 1000) / vr.get_fps())
    # im1 = None
    hst1 = None
    #im2 = vr.read_frame_at_time(t)
    im3 = None

    detected = False
    while not detected:
        t += 500
        if t >= tl:
            t = -1
            detected = True
            print
            "I did not find sync sequence!"
        #print t
        #print("as")
        try:
            pic = vr.read_frame_at_time(t)
            #print "readed"
            im1 = cv2.cvtColor(pic, cv2.COLOR_BGR2GRAY)
            #print "gray"
            #cv2.imshow("sss", im1 );
            #hst1 = cv2.calcHist([im1],[0],None,[256],[0,256]) #TODO sometimes fails
            hst1, _ = np.histogram(im1.ravel(), 256, [0, 256])
            #print "hst1"
        except:
            print
            "Unexpected error:", sys.exc_info()[0]
        if hst1[0] > (tl * trshld):
            ta = t
            while not detected:
                t += 100
                if t >= tl:
                    t = -1
                    detected = True
                    break
                if ta + 15000 <= t:
                    #zatemnena obrazovka by nemala byt dlhsia ako 15 sekund
                    break
                pic = vr.read_frame_at_time(t)
                im1 = cv2.cvtColor(pic, cv2.COLOR_BGR2GRAY)
                hst1, _ = np.histogram(im1.ravel(), 256, [0, 256])
                if hst1[0] < (tl * trshld1):
                    detected = True

                    #print "finded"

    return t