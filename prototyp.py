__author__ = 'peto'

import video_compose as vc
from time import time
import auto_sync as async

# video = "C:\Users\peto\Desktop\hero.mp4"
# data = "C:\Users\peto\Desktop\hero.tcx"
# video = 'C:\\Users\\peto\\Desktop\\autosync.mp4'
# data = "C:\\Users\\peto\\Desktop\\autosync.tcx"
video = 'autosync.mp4'
data = "autosync.tcx"

a = time()
v = vc.Video_compose(data, video, "simple_frame_handler",
                     'C:\Users\peto\Desktop\output.avi')  # pripravim si data a spracujem co potrebujem
ts = async.sync(v.video_reader)
v.set_data_start_time(
    ts)  # synchronizacia dat s videom, v podstate je to rozdiel medzi zaciatkom nahravania dat a nahravania videa
# v.set_video_start_time(7000)
# pre nastavenia casu videa je potrebne spravit oseknutie zvuku napr, upravit metody niektore atd
print
time() - a
v.start_composing()  # render videa

print
time() - a