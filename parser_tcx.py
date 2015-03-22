__author__ = 'peto'
# this module handle parsing tcx. files , only supports one activity and track without pauses for now

from xml.dom import minidom
from datetime import datetime


class TCX_parser:
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

    def get_activity(self):
        if self.doc == None:
            return
        data = []
        self.start_time = int(self.get_time(self.get_activity_id()))
        data.append(self.get_activity_name())
        data.append(self.start_time)
        activity = self.doc.getElementsByTagName("Activity")
        laps = activity.item(0).getElementsByTagName("Lap")
        for lap in laps:
            data.append(self.get_lap(lap))
        return data

    def get_activity_name(self):
        if self.doc == None:
            return
        activity = self.doc.getElementsByTagName("Activity")
        if activity.length != 0:
            return str(activity.item(0).getAttribute("Sport"))
        return ""

    def get_activity_id(self):
        if self.doc == None:
            return
        activity = self.doc.getElementsByTagName("Activity")
        id = activity.item(0).getElementsByTagName("Id").item(0).firstChild.data
        return id

    def get_lap(self, lap):
        data = []
        values = dict()
        track = []

        # getting information about given lap
        if lap.getElementsByTagName("TotalTimeSeconds") != None:
            values["TotalTimeSeconds"] = float(lap.getElementsByTagName("TotalTimeSeconds").item(0).firstChild.data)
        if lap.getElementsByTagName("DistanceMeters") != None:
            values["DistanceMeters"] = float(lap.getElementsByTagName("DistanceMeters").item(0).firstChild.data)

        data.append(values)
        track_elem = lap.getElementsByTagName("Track")
        if track_elem.length != None:
            trackpoints = track_elem.item(0).getElementsByTagName("Trackpoint")
            if trackpoints != None:
                for trackpoint in trackpoints:
                    track.append(self.get_trackpoint(trackpoint))
        data.append(track)
        return data

    def get_trackpoint(self, trackpoint):
        values = dict()
        if trackpoint.getElementsByTagName("Time").length != 0:
            values["Time"] = int(
                self.get_time(trackpoint.getElementsByTagName("Time").item(0).firstChild.data) - self.start_time)
        if trackpoint.getElementsByTagName("Position").length != 0:
            values["LatitudeDegrees"] = float(trackpoint.getElementsByTagName("Position").item(0).getElementsByTagName(
                "LatitudeDegrees").item(0).firstChild.data)
            values["LongitudeDegrees"] = float(trackpoint.getElementsByTagName("Position").item(0).getElementsByTagName(
                "LongitudeDegrees").item(0).firstChild.data)
        else:
            values["LatitudeDegrees"] = 0
            values["LongitudeDegrees"] = 0
        if trackpoint.getElementsByTagName("AltitudeMeters").length != 0:
            values["AltitudeMeters"] = float(trackpoint.getElementsByTagName("AltitudeMeters").item(0).firstChild.data)
        else:
            values["AltitudeMeters"] = 0
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


# ####debug code######

# parser= TCX_parser("test5.tcx")
# parser.get_activity()


