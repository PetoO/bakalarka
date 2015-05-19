__author__ = 'peto'

from parser_tcx import TCX_parser as tcx
from parser_gpx import GPX_parser as gpx
from parser_kml import KML_parser as kml
import numpy as np
import math
from scipy import interpolate
# from scipy import optimize
import time
import helper
# import sys


class Data_collection:
    def __init__(self, filename):
        # should determine which parser to use
        self.parsed_data = None
        try:
            if ".tcx" in filename.lower():
                parser = tcx(filename)
            elif ".gpx" in filename.lower():
                parser = gpx(filename)
            elif ".kml" in filename.lower():
                parser = kml(filename)

            self.parsed_data = parser.get_data()
        except:
            print ("Unknown Error while handlig data files!")
        self.sensors = []
        last_n = 0
        self.laps = []
        self.trackpoints = []
        self.to_kph = True
        # funckie pre interpolaciu rychlosti v danom case
        self.speed_interpolations = None
        # print self.parsed_data
        # ak sa data podarilo sparsovat mozem ich pripravit
        if self.parsed_data != None:
            # print self.parsed_data
            self.start_time = self.parsed_data[0]
            self.handle_data()

    def handle_data(self):

        for x in range(1, len(self.parsed_data)):
            # print len(self.parsed_data)
            # #print (self.parsed_data)
            self.laps.append(self.parsed_data[x])
            # print (self.laps)
            #print self.parsed_data[x]
            #self.laps[0]["Time"] = self.parsed_data[x][0]["Time"]
            self.handle_lap(self.parsed_data[x])
        # print self.trackpoints
        if len(self.trackpoints) != 0:
            self.calc_speed()
        # print self.trackpoints
        # for x in self.trackpoints:
        # print x
        return

    def handle_lap(self, lap):
        #print lap
        altitudes = []
        for i in range(0, len(lap)):
            #print lap
            trackpoint = {}
            if "Speed" in lap[i]:
                if self.to_kph:
                    trackpoint["Speed"] = round(float(lap[i]["Speed"] * 3.6), 1)
                else:
                    trackpoint["Speed"] = round(float(lap[i]["Speed"]), 1)
            trackpoint["Time"] = lap[i]["Time"]
            trackpoint["LongitudeDegrees"] = lap[i]["LongitudeDegrees"]
            trackpoint["LatitudeDegrees"] = lap[i]["LatitudeDegrees"]
            if "HeartRateBpm" in lap[i]:
                trackpoint["HeartRateBpm"] = lap[i]["HeartRateBpm"]
            altitudes.append(lap[i]["AltitudeMeters"])
            self.trackpoints.append(trackpoint)

        self.filter_altitude(altitudes)
        for i in reversed(xrange(0, len(altitudes))):
            self.trackpoints[len(self.trackpoints) - i - 1]["AltitudeMeters"] = altitudes[::-1][i]
        return

    # primitive filter
    # TODO improve this
    def filter_altitude(self, altitudes):
        buff = helper.Buff_avg(12)
        for i, a in enumerate(altitudes):
            altitudes[i] = buff.add_value(a)
        return altitudes

    # speed can differs from reality, it depends on frequency of gps data and its accuracy, so best option is to have speed data in your data file...
    # but file format like .gpx doesnt support this option, so speed calculation from gps coordinates is must in some cases
    # TODO improve this
    def calc_speed(self):
        buff = helper.Buff_avg(5, 1)
        for b in range(0, 5):
            buff.add_value(0)
        times = []
        speeds = []
        lap_times = []
        # for lap in self.laps:
        # # print lap
        #     lap_times.append(lap[0]["Time"])
        # for i in range(0, len(lap_times)):
        #     times = []
        #     speeds = []
        #     if i == len(lap_times) - 1:
        #         last_lap = True
        #     else:
        #         last_lap = False
        #     if last_lap:
        #         index1 = self.get_trackpoint_id(lap_times[i])
        #         index2 = len(self.trackpoints) - 1
        #     else:
        #         index1 = self.get_trackpoint_id(lap_times[i])
        #         index2 = self.get_trackpoint_id(lap_times[i + 1]) - 1
        for i in range(0, len(self.trackpoints)):
            # TODO now = if loop else loop - future maybe loop if else
            if "Speed" in self.trackpoints[i]:
                speeds.append(self.trackpoints[i]["Speed"])
                times.append(self.trackpoints[i]["Time"])
            else:
                self.trackpoints[i]["Speed"] = float(0)
                j = i + 1
                if j < len(self.trackpoints):
                    R = 6371  # km
                    dLat = math.radians(
                        (self.trackpoints[i]["LatitudeDegrees"] - self.trackpoints[j]["LatitudeDegrees"]))
                    dLon = math.radians(
                        (self.trackpoints[i]["LongitudeDegrees"] - self.trackpoints[j]["LongitudeDegrees"]))
                    lat1 = math.radians(self.trackpoints[i]["LatitudeDegrees"])
                    lat2 = math.radians(self.trackpoints[i]["LatitudeDegrees"])
                    a = math.sin(dLat / 2) * math.sin(dLat / 2) + math.sin(dLon / 2) * math.sin(dLon / 2) * math.cos(
                        lat1) * math.cos(lat2)
                    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
                    d = R * c

                    t = self.trackpoints[j]["Time"] - self.trackpoints[i]["Time"]
                    s = ((d * 1000000) / t)

                    speeds.append((buff.add_value(round(s * 3.6, 1))))
                    print speeds
                    times.append(self.trackpoints[i]["Time"])



        # interpolation

        # x =
        # y =
        # print len(y)
        # print len(x)
        print len(times)
        print len(speeds)
        print (times)
        print (speeds)
        self.speed_interpolation = interpolate.interp1d(np.array(times), np.array(speeds), "cubic")
        # print x
        #print y
        #print self.speed_interpolations[i](3000)


        # if len(speeds) >= 3:
        # for k in range(1, len(speeds) - 1):
        #        self.trackpoints[k + index1]["Speed"] = round(
        #            ((float(speeds[k]) + float(speeds[k - 1]) + float(speeds[k + 1])) / 3), 1)
        #        speeds[k] = round(((float(speeds[k]) + float(speeds[k - 1]) + float(speeds[k + 1])) / 3), 1)
        #    self.trackpoints[index2]["Speed"] = round(
        #        ((float(speeds[len(speeds) - 1]) + float(speeds[len(speeds) - 2])) / 2), 1)
        #print "interpolation = " + str(len(self.speed_interpolations))

    def get_trackpoint_id(self, time):
        x = 0
        for t in range(0, len(self.trackpoints) - 1):
            if time >= self.trackpoints[t]["Time"]:
                x = t
                continue
            else:
                return x
        return -1

    def get_lap_id(self, time):
        # print "time " + str(time)
        x = -1
        for t in range(0, len(self.laps)):
            # print "lap time " + str(self.laps[t]["Time"])
            if time >= self.laps[t][0]["Time"]:
                # print "True"
                x = t
                continue
            else:
                return x
        return x

    # this function returns all possible data at given time as dictionary
    def get_data_at(self, time):
        id = self.get_trackpoint_id(time)
        # print "id = " +  str(id)
        if id == -1:
            return None
        lap_id = self.get_lap_id(time)
        # print "lapid = " +  str(lap_id)
        if lap_id == -1:
            return None
        data = self.trackpoints[id]
        if id == len(self.trackpoints) - 1 or time == 0:
            return data

        # data1 = self.trackpoints[id + 1]
        # r1 = data["Speed"]
        # r2 = data1["Speed"]
        #t1 = data["Time"]
        #t2 = data1["Time"]
        # a = float(data["Speed"] + data1["Speed"])
        #b = float(data["Time"]+ data1["Time"]) / float(time)
        # data["Speed"] = round(((float(time - t1) / float(t2 - t1)) * float(r2 - r1)) + r1, 1)
        speed = round(float(self.speed_interpolation(time)), 1)
        if speed <= 0.0:
            speed = 0.0
        data["Speed"] = speed
        return data


# ####debug code######
#
#
#
# print "asdasd"
# for fas in range (0,10000000):
# pass
# fff=interpolate.interp1d(np.array([0, 0, 4731, 4734, 4739, 4743]), np.array([15.0, 23.2, 25.2, 25.7, 24.0, 23.5]), "cubic")
# for fas in range (0,10000000):
#     pass
# print "asdasdasdasdad"


# data = Data_collection("gui.py")
# a = time.time()
# data.get_data_at(25000)
# print time.time()-a
# a=time.time()
# data.get_data_at(45000)
# print time.time()-a
# a=time.time()
# data.get_data_at(105000)
# print time.time()-a
# coords=[]
# for i in range(0, len(data.trackpoints)):
# #sys.stdout.write(str(data.trackpoints[i]["LatitudeDegrees"])+","+str(data.trackpoints[i]["LongitudeDegrees"])+"|")
# #print str(data.trackpoints[i]["LatitudeDegrees"])+","+str(data.trackpoints[i]["LongitudeDegrees"])+"|",
#     coords.append((data.trackpoints[i]["LongitudeDegrees"],data.trackpoints[i]["LatitudeDegrees"]))

#sys.stdout.flush()

# a = time.time()
# b = time.time()
# last = 0
# d = True
# i = 0
# while (d):
#    if b - last > 0.5:
#        i+=1
#        #print str(round(((b - a) * 1000), 0)) + "  : " + str(data.get_data_at(round(((b - a) * 1000), 0)))
#        print data.get_data_at(round(((b - a) * 1000), 0))
#
#        last = b
#    b = time.time()
#    if i == 10000:
#        d=False
# while (d):
# data.get_data_at(round(((b - a) * 10000), 0))
#   i+=1
#   if i == 10000:
#        d=False
#for i in range(0, 1):
# print data.get_data_at(round(((i) * 100), 0))
#print time.time() - a

# x1 = [1., 0.88,  0.67,  0.50,  0.35,  0.27, 0.18,  0.11,  0.08,  0.04,  0.04,  0.02]
#y1 = [0., 13.99, 27.99, 41.98, 55.98, 69.97, 83.97, 97.97, 111.96, 125.96, 139.95, 153.95]

# x = np.array(x1)
#y = np.array(y1)

#new_length = 50
#new_x = np.linspace(x.min(), x.max(), new_length)
#new_y = sp.interpolate.interp1d(x, y, kind='cubic')(new_x)


#print new_x
#print new_y

from numpy import r_, sin
from scipy.signal import cspline1d, cspline1d_eval

#x = r_[0:10]
#dx = x[1]-x[0]
#newx = r_[-3:13:0.1]  # notice outside the original domain
#y = sin(x)
#cj = cspline1d(y)
#newy = cspline1d_eval(cj, newx, dx=dx,x0=x[0])
#print newx
#print newy

# import cv2
# import urllib
# import numpy as np
#
# def encode_coords(coords):
#     '''Encodes a polyline using Google's polyline algorithm
#
#     See http://code.google.com/apis/maps/documentation/polylinealgorithm.html
#     for more information.
#
#     :param coords: Coordinates to transform (list of tuples in order: latitude,
#     longitude).
#     :type coords: list
#     :returns: Google-encoded polyline string.
#     :rtype: string
#     '''
#
#     result = []
#
#     prev_lat = 0
#     prev_lng = 0
#
#     for x, y in coords:
#         lat, lng = int(y * 1e5), int(x * 1e5)
#
#         d_lat = _encode_value(lat - prev_lat)
#         d_lng = _encode_value(lng - prev_lng)
#
#         prev_lat, prev_lng = lat, lng
#
#         result.append(d_lat)
#         result.append(d_lng)
#
#     return ''.join(c for r in result for c in r)
#
# def _encode_value(value):
#     # Step 2 & 4
#     value = ~(value << 1) if value < 0 else (value << 1)
#
#     # Step 5 - 8
#     chunks = _split_into_chunks(value)
#
#     # Step 9-10
#     return (chr(chunk + 63) for chunk in chunks)
#
# def _split_into_chunks(value):
#     while value >= 32: #2^5, while there are at least 5 bits
#
#         # first & with 2^5-1, zeros out all the bits other than the first five
#         # then OR with 0x20 if another bit chunk follows
#         yield (value & 31) | 0x20
#         value >>= 5
#     yield value




#center='center=48.555224,19.538875&zoom=16&'
#marker="&markers=size:small%7Ccolor:0xFF0000%7C48.555246,19.538871&"
#path="path=color:0x0000ff|weight:5|48.555246,19.538871| 48.555224,19.538875| 48.555223,19.538876| 48.555222,19.538878| 48.555223,19.538878| 48.555226,19.538876| 48.555225,19.538883| 48.555219,19.538884| 48.555211,19.538878| 48.555221,19.53887| 48.555237,19.53886| 48.555248,19.538858| 48.555259,19.538851| 48.55527,19.538841| 48.555297,19.538844| 48.555321,19.538845| 48.555344,19.538833| 48.555364,19.538817| 48.555374,19.53881| 48.555384,19.5388| 48.555403,19.538787| 48.555439,19.538757| 48.555479,19.538722| 48.555504,19.538672| 48.555546,19.538591| 48.555593,19.538523| 48.555652,19.538497| 48.555716,19.538457| 48.555778,19.538392| 48.555851,19.538344| 48.55593,19.538296| 48.556011,19.538245| 48.556073,19.538167| 48.556141,19.538084| 48.556208,19.537999| 48.556275,19.537952| 48.556347,19.537931| 48.556412,19.537911| 48.556468,19.537848| 48.556514,19.537784| 48.556569,19.53771| 48.556623,19.53765| 48.556707,19.537626| 48.556785,19.537598| 48.556851,19.537538| 48.556914,19.537471| 48.556973,19.537412| 48.55704,19.537377| 48.557123,19.537337| 48.557191,19.537254| 48.55725,19.53718| 48.557319,19.537109| 48.55739,19.537052| 48.557472,19.537002| 48.557553,19.53694| 48.557634,19.536872| 48.55771,19.536803| 48.557789,19.536729| 48.557862,19.536656| 48.557937,19.536584| 48.558008,19.536519| 48.558076,19.53646| 48.55813,19.536417| 48.558186,19.536373| 48.558244,19.536331| 48.558287,19.536297| 48.558336,19.536257| 48.558381,19.536217| 48.558414,19.536189| 48.558447,19.536138| 48.558469,19.536064| 48.558513,19.53599| 48.558562,19.535902| 48.55861,19.535822| 48.558652,19.535741| 48.558687,19.535654| 48.558697,19.535547| 48.55873,19.535467| 48.558764,19.535382| 48.558799,19.535303| 48.558841,19.535233| 48.558884,19.535156| 48.558918,19.535074| 48.558947,19.534984| 48.558971,19.534895| 48.559003,19.534826| 48.559032,19.534763| 48.559062,19.534697| 48.559095,19.534634| 48.55912,19.534575| 48.559127,19.534515| 48.559134,19.53446| 48.559139,19.534399| 48.559147,19.534333| 48.559164,19.534259| 48.559187,19.534192| 48.559206,19.534132| 48.559221,19.534048| 48.559221,19.533976| 48.559222,19.533902| 48.559227,19.533835| 48.559263,19.533783| 48.559293,19.533716| 48.559319,19.533648| 48.559362,19.533582| 48.559415,19.533551| 48.559469,19.533524| 48.559525,19.533507| 48.559566,19.533443| 48.559612,19.533375| 48.55967,19.53333| 48.55973,19.533287| 48.559787,19.533239| 48.559836,19.533161| 48.559895,19.533079| 48.55996,19.533039| 48.560023,19.533004| 48.560092,19.532961| 48.560153,19.532904| 48.560217,19.532851| 48.560278,19.532841| 48.560349,19.532832| 48.560414,19.532788| 48.560469,19.532739| 48.560518,19.532693| 48.560572,19.53266| 48.560633,19.532632| 48.560699,19.532594| 48.56075,19.532534| 48.560802,19.532473| 48.560863,19.532425| 48.56093,19.532377| 48.561012,19.532314| 48.561059,19.532225| 48.561099,19.532141| 48.561131,19.532061| 48.561169,19.531979| 48.561224,19.531903| 48.561276,19.531836| 48.561311,19.531774| 48.561321,19.531736| 48.561328,19.531705| 48.561326,19.531673| 48.561327,19.53164| 48.561327,19.53164| 48.561327,19.53164| 48.561327,19.53164| 48.561327,19.53164| 48.561327,19.53164| 48.561327,19.53164| 48.561327,19.53164| 48.561327,19.53164| 48.561327,19.53164| 48.561327,19.53164| 48.561327,19.53164| 48.561327,19.53164| 48.561327,19.53164| 48.561327,19.53164| 48.561327,19.53164| 48.561327,19.53164| 48.561327,19.53164| 48.561327,19.53164| 48.561327,19.53164| 48.561327,19.53164| 48.561327,19.53164| 48.561327,19.53164| 48.561327,19.53164| 48.561327,19.53164| 48.561327,19.53164| 48.561327,19.53164| 48.561327,19.53164| 48.561327,19.53164| 48.561327,19.53164"
##path="path=weight:3%7Ccolor:orange%7Cenc:48.555246,19.538871|48.555223,19.538876|48.555223,19.538878|48.555225,19.538883|48.555211,19.538878|48.555237,19.53886|48.555259,19.538851|48.555297,19.538844|48.555344,19.538833|48.555374,19.53881|48.555403,19.538787|48.555479,19.538722|48.555546,19.538591|48.555652,19.538497|48.555778,19.538392|48.55593,19.538296|48.556073,19.538167|48.556208,19.537999|48.556347,19.537931|48.556468,19.537848|48.556569,19.53771|48.556707,19.537626|48.556851,19.537538|48.556973,19.537412|48.557123,19.537337|48.55725,19.53718|48.55739,19.537052|48.557553,19.53694|48.55771,19.536803|48.557862,19.536656|48.558008,19.536519|48.55813,19.536417|48.558244,19.536331|48.558336,19.536257|48.558414,19.536189|48.558469,19.536064|48.558562,19.535902|48.558652,19.535741|48.558697,19.535547|48.558764,19.535382|48.558841,19.535233|48.558918,19.535074|48.558971,19.534895|48.559032,19.534763|48.559095,19.534634|48.559127,19.534515|48.559139,19.534399|48.559164,19.534259|48.559206,19.534132|48.559221,19.533976|48.559227,19.533835|48.559293,19.533716|48.559362,19.533582|48.559469,19.533524|48.559566,19.533443|48.55967,19.53333|48.559787,19.533239|48.559895,19.533079|48.560023,19.533004|48.560153,19.532904|48.560278,19.532841|48.560414,19.532788|48.560518,19.532693|48.560633,19.532632|48.56075,19.532534|48.560863,19.532425|48.561012,19.532314|48.561099,19.532141|48.561169,19.531979|48.561276,19.531836|48.561321,19.531736|48.561326,19.531673|48.561327,19.53164|48.561327,19.53164|48.561327,19.53164|48.561327,19.53164|48.561327,19.53164|48.561327,19.53164|48.561327,19.53164|48.561327,19.53164|48.561327,19.53164|48.561327,19.53164|48.561327,19.53164|48.561327,19.53164|48.561327,19.53164|48.561327,19.53164|48.561327,19.53164"
#path="&path=color:0x00ff00Ff|weight:5%7Cenc:"+encode_coords(coords)
#api="&AIzaSyD0LgOSvwSgdKrp16kGeyDXgOfmD_pk9yg"
#size="&size=250x250"
#url = "https://maps.googleapis.com/maps/api/staticmap?maptype=terrain"+path+api+size+marker
#req = urllib.urlopen(url)
#arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
#img = cv2.imdecode(arr,-1) # 'load it as it is'

#cv2.imshow('lalala',img)
#if cv2.waitKey() & 0xff == 27: quit()

