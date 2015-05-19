__author__ = 'peto'
# this module handle parsing gpx. files , only supports one activity and track without pauses for now

from xml.dom import minidom
from datetime import datetime


class GPX_parser:
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
        trk = self.doc.getElementsByTagName("trk")
        # print trk
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
        track_elem = lap.getElementsByTagName("trkseg")
        if track_elem.length != None:
            for t in track_elem:
                trackpoints = t.getElementsByTagName("trkpt")
                if trackpoints != None:
                    for trackpoint in trackpoints:
                        track.append(self.get_trackpoint(trackpoint))
                        # data.append(track)
        return track

    def get_trackpoint(self, trackpoint):
        values = dict()
        if trackpoint.getElementsByTagName("time").length != 0:
            if self.start_time == 0:
                self.start_time = int(self.get_time(trackpoint.getElementsByTagName("time").item(0).firstChild.data))
                values["Time"] = 0
            else:
                values["Time"] = int(
                    self.get_time(trackpoint.getElementsByTagName("time").item(0).firstChild.data) - self.start_time)

        if trackpoint.getAttribute('lat') != "" and trackpoint.getAttribute('lon') != "":
            values["LatitudeDegrees"] = float(trackpoint.getAttribute('lat'))
            values["LongitudeDegrees"] = float(trackpoint.getAttribute('lon'))
        else:
            values["LatitudeDegrees"] = 0
            values["LongitudeDegrees"] = 0

        if trackpoint.getElementsByTagName("ele").length != 0:
            values["AltitudeMeters"] = float(trackpoint.getElementsByTagName("ele").item(0).firstChild.data)
        else:
            values["AltitudeMeters"] = 0

        # todo
        if trackpoint.getElementsByTagName("Speed").length != 0:
            values["Speed"] = float(trackpoint.getElementsByTagName("Speed").item(0).firstChild.data)
        # if not exists then no value
        # else:
        # values["Speed"] = 0
        if trackpoint.getElementsByTagName("HeartRateBpm").length != 0:
            values["HeartRateBpm"] = int(trackpoint.getElementsByTagName("HeartRateBpm").item(0).getElementsByTagName(
                "Value").item(0).firstChild.data)
        else:
            values["HeartRateBpm"] = 0
        # add extensions , heart rate, cadence ....
        # print values
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


