__author__ = 'peto'
# this module handle parsing .kml files , only supports one activity and track without pauses for now

from xml.dom import minidom
from datetime import datetime


class KML_parser:
    def __init__(self, filename):
        self.filename = filename
        try:
            self.doc = minidom.parse(filename)
        except IOError:
            self.doc = None
            print
            "File doesn't exists or is invalid."
            return None
        self.start_time = 0

    def get_data(self):
        if self.doc == None:
            return
        data = []
        data.append(self.start_time)
        trk = self.doc.getElementsByTagName("gx:MultiTrack")
        for tr in trk:
            data.append(self.get_lap(tr))
        data[0] = self.start_time
        return data


    def get_lap(self, lap):
        data = []
        values = dict()
        tracks = []
        track = []

        data.append(values)
        track_elem = lap.getElementsByTagName("gx:Track")
        if track_elem.length != None:
            for t in track_elem:
                times = t.getElementsByTagName("when")
                coords = t.getElementsByTagName("gx:coord")
                if times != None:
                    for t in range(0, len(times)):
                        if t < len(coords):
                            track.append(self.get_trackpoint(times[t], coords[t]))
                            # data.append(track)
        return track

    def get_trackpoint(self, time, coord):
        values = dict()
        if self.start_time == 0:
            self.start_time = int(self.get_time(time.firstChild.data))
            values["Time"] = 0
        else:
            values["Time"] = int(self.get_time(time.firstChild.data) - self.start_time)
        print self.start_time

        lon, lat, ele = coord.firstChild.data.split()
        values["LatitudeDegrees"] = float(lat)
        values["LongitudeDegrees"] = float(lon)
        values["AltitudeMeters"] = float(ele)

        #
        # if trackpoint.getElementsByTagName("time").length != 0:
        #
        # if  trackpoint.getAttribute('lat') != "" and trackpoint.getAttribute('lon') != "":
        # values["LatitudeDegrees"] = float(trackpoint.getAttribute('lat'))
        #     values["LongitudeDegrees"] = float(trackpoint.getAttribute('lon'))
        # else:
        #     values["LatitudeDegrees"] = 0
        #     values["LongitudeDegrees"] = 0
        #
        # if trackpoint.getElementsByTagName("ele").length != 0:
        #     values["AltitudeMeters"] = float(trackpoint.getElementsByTagName("ele").item(0).firstChild.data)
        # else:
        #     values["AltitudeMeters"] = 0
        return values

    def get_time(self, time):
        ms = 0
        if "." in time:
            times = time.split(".")
            dt = datetime.strptime(times[0], "%Y-%m-%dT%H:%M:%S")
            ms = int(times[1][:-1])
        else:
            dt = datetime.strptime(time, "%Y-%m-%dT%H:%M:%SZ")
        a = dt - datetime.utcfromtimestamp(0)
        t = int(a.total_seconds() * 1000)
        t += ms
        # print t
        return t


