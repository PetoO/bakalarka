__author__ = 'peto'

from cv2 import imdecode, imread
from urllib import urlopen
import numpy as np


class Google_map:
    def __init__(self, data):
        self.map_type = "terrain"
        self.url = ""
        self.api_key = "&key=AIzaSyD0LgOSvwSgdKrp16kGeyDXgOfmD_pk9yg"
        self.size = "&size=250x250"
        self.data = data
        self.zoom = "&zoom=15"
        self.coords = self.get_points()
        self.path = "&path=color:0x00ff00Ff|weight:5%7Cenc:" + self.encode_coords(self.coords)
        self.current_png = None
        self.no_map = imread("no_map.png")
        self.current_png = self.no_map
        # if len(coords)!=0:
        self.current_location = str(self.coords[0][0]) + "," + str(self.coords[0][1])
        self.center = 'center=48.555224,19.538875&zoom=16&'
        self.marker = "&markers=size:small%7Ccolor:0xFF0000%7C"
        self.timeout = 0


    def get_image(self, x, y):
        if self.timeout == 10:
            return self.no_map
        if (self.current_location == str(x) + "," + str(y) and self.current_png is not None):
            return self.current_png
        else:
            try:
                self.set_current_location(x, y)
                self.set_url()
                print self.url
                req = urlopen(self.url, timeout=10)
                arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
                self.current_png = imdecode(arr, -1)
                return self.current_png
            except:
                return self.no_map
                self.timeout += 1
                print self.timeout
        return None


    def set_map_type(self, type):
        self.map_type = type

    def set_center(self):
        self.center = "&center=" + self.current_location

    def set_api_key(self, key):
        self.api_key = "&key=" + str(key)
        return

    def set_url(self):
        self.url = "https://maps.googleapis.com/maps/api/staticmap?maptype=" + self.map_type + self.zoom + self.api_key + self.center + self.size + self.marker + self.current_location + self.path

    def add(self, to, term, value):
        return

    def set_zoom(self, zoom):
        self.zoom = "&zoom=" + str(int(zoom))

    def set_size(self, x, y):
        self.size = "&size=" + str(x) + "x" + str(y)

    def set_current_location(self, x, y):
        self.current_location = str(x) + "," + str(y)
        self.set_center()
        # 19.538871,48.555246
        return

    def get_points(self):
        coords = []
        for i in range(0, len(self.data.trackpoints) - 1):
            # sys.stdout.write(str(data.trackpoints[i]["LatitudeDegrees"])+","+str(data.trackpoints[i]["LongitudeDegrees"])+"|")
            # print str(data.trackpoints[i]["LatitudeDegrees"])+","+str(data.trackpoints[i]["LongitudeDegrees"])+"|",
            coords.append((self.data.trackpoints[i]["LongitudeDegrees"], self.data.trackpoints[i]["LatitudeDegrees"]))
        return coords

    def encode_coords(self, coords):
        '''Encodes a polyline using Google's polyline algorithm

        See http://code.google.com/apis/maps/documentation/polylinealgorithm.html
        for more information.

        :param coords: Coordinates to transform (list of tuples in order: latitude,
        longitude).
        :type coords: list
        :returns: Google-encoded polyline string.
        :rtype: string
        '''

        result = []

        prev_lat = 0
        prev_lng = 0

        for x, y in coords:
            lat, lng = int(y * 1e5), int(x * 1e5)

            d_lat = self._encode_value(lat - prev_lat)
            d_lng = self._encode_value(lng - prev_lng)

            prev_lat, prev_lng = lat, lng

            result.append(d_lat)
            result.append(d_lng)

        return ''.join(c for r in result for c in r)

    def _split_into_chunks(self, value):
        while value >= 32:  # 2^5, while there are at least 5 bits

            # first & with 2^5-1, zeros out all the bits other than the first five
            # then OR with 0x20 if another bit chunk follows
            yield (value & 31) | 0x20
            value >>= 5
        yield value

    def _encode_value(self, value):
        # Step 2 & 4
        value = ~(value << 1) if value < 0 else (value << 1)

        # Step 5 - 8
        chunks = self._split_into_chunks(value)

        # Step 9-10
        return (chr(chunk + 63) for chunk in chunks)




        # center='center=48.555224,19.538875&zoom=16&'
        # marker="&markers=color:green%7Clabel:G%7C19.538871,48.555246&"
        # #path="path=color:0x0000ff|weight:5|48.555246,19.538871| 48.555224,19.538875| 48.555223,19.538876| 48.555222,19.538878| 48.555223,19.538878| 48.555226,19.538876| 48.555225,19.538883| 48.555219,19.538884| 48.555211,19.538878| 48.555221,19.53887| 48.555237,19.53886| 48.555248,19.538858| 48.555259,19.538851| 48.55527,19.538841| 48.555297,19.538844| 48.555321,19.538845| 48.555344,19.538833| 48.555364,19.538817| 48.555374,19.53881| 48.555384,19.5388| 48.555403,19.538787| 48.555439,19.538757| 48.555479,19.538722| 48.555504,19.538672| 48.555546,19.538591| 48.555593,19.538523| 48.555652,19.538497| 48.555716,19.538457| 48.555778,19.538392| 48.555851,19.538344| 48.55593,19.538296| 48.556011,19.538245| 48.556073,19.538167| 48.556141,19.538084| 48.556208,19.537999| 48.556275,19.537952| 48.556347,19.537931| 48.556412,19.537911| 48.556468,19.537848| 48.556514,19.537784| 48.556569,19.53771| 48.556623,19.53765| 48.556707,19.537626| 48.556785,19.537598| 48.556851,19.537538| 48.556914,19.537471| 48.556973,19.537412| 48.55704,19.537377| 48.557123,19.537337| 48.557191,19.537254| 48.55725,19.53718| 48.557319,19.537109| 48.55739,19.537052| 48.557472,19.537002| 48.557553,19.53694| 48.557634,19.536872| 48.55771,19.536803| 48.557789,19.536729| 48.557862,19.536656| 48.557937,19.536584| 48.558008,19.536519| 48.558076,19.53646| 48.55813,19.536417| 48.558186,19.536373| 48.558244,19.536331| 48.558287,19.536297| 48.558336,19.536257| 48.558381,19.536217| 48.558414,19.536189| 48.558447,19.536138| 48.558469,19.536064| 48.558513,19.53599| 48.558562,19.535902| 48.55861,19.535822| 48.558652,19.535741| 48.558687,19.535654| 48.558697,19.535547| 48.55873,19.535467| 48.558764,19.535382| 48.558799,19.535303| 48.558841,19.535233| 48.558884,19.535156| 48.558918,19.535074| 48.558947,19.534984| 48.558971,19.534895| 48.559003,19.534826| 48.559032,19.534763| 48.559062,19.534697| 48.559095,19.534634| 48.55912,19.534575| 48.559127,19.534515| 48.559134,19.53446| 48.559139,19.534399| 48.559147,19.534333| 48.559164,19.534259| 48.559187,19.534192| 48.559206,19.534132| 48.559221,19.534048| 48.559221,19.533976| 48.559222,19.533902| 48.559227,19.533835| 48.559263,19.533783| 48.559293,19.533716| 48.559319,19.533648| 48.559362,19.533582| 48.559415,19.533551| 48.559469,19.533524| 48.559525,19.533507| 48.559566,19.533443| 48.559612,19.533375| 48.55967,19.53333| 48.55973,19.533287| 48.559787,19.533239| 48.559836,19.533161| 48.559895,19.533079| 48.55996,19.533039| 48.560023,19.533004| 48.560092,19.532961| 48.560153,19.532904| 48.560217,19.532851| 48.560278,19.532841| 48.560349,19.532832| 48.560414,19.532788| 48.560469,19.532739| 48.560518,19.532693| 48.560572,19.53266| 48.560633,19.532632| 48.560699,19.532594| 48.56075,19.532534| 48.560802,19.532473| 48.560863,19.532425| 48.56093,19.532377| 48.561012,19.532314| 48.561059,19.532225| 48.561099,19.532141| 48.561131,19.532061| 48.561169,19.531979| 48.561224,19.531903| 48.561276,19.531836| 48.561311,19.531774| 48.561321,19.531736| 48.561328,19.531705| 48.561326,19.531673| 48.561327,19.53164| 48.561327,19.53164| 48.561327,19.53164| 48.561327,19.53164| 48.561327,19.53164| 48.561327,19.53164| 48.561327,19.53164| 48.561327,19.53164| 48.561327,19.53164| 48.561327,19.53164| 48.561327,19.53164| 48.561327,19.53164| 48.561327,19.53164| 48.561327,19.53164| 48.561327,19.53164| 48.561327,19.53164| 48.561327,19.53164| 48.561327,19.53164| 48.561327,19.53164| 48.561327,19.53164| 48.561327,19.53164| 48.561327,19.53164| 48.561327,19.53164| 48.561327,19.53164| 48.561327,19.53164| 48.561327,19.53164| 48.561327,19.53164| 48.561327,19.53164| 48.561327,19.53164| 48.561327,19.53164"
        # #path="path=weight:3%7Ccolor:orange%7Cenc:48.555246,19.538871|48.555223,19.538876|48.555223,19.538878|48.555225,19.538883|48.555211,19.538878|48.555237,19.53886|48.555259,19.538851|48.555297,19.538844|48.555344,19.538833|48.555374,19.53881|48.555403,19.538787|48.555479,19.538722|48.555546,19.538591|48.555652,19.538497|48.555778,19.538392|48.55593,19.538296|48.556073,19.538167|48.556208,19.537999|48.556347,19.537931|48.556468,19.537848|48.556569,19.53771|48.556707,19.537626|48.556851,19.537538|48.556973,19.537412|48.557123,19.537337|48.55725,19.53718|48.55739,19.537052|48.557553,19.53694|48.55771,19.536803|48.557862,19.536656|48.558008,19.536519|48.55813,19.536417|48.558244,19.536331|48.558336,19.536257|48.558414,19.536189|48.558469,19.536064|48.558562,19.535902|48.558652,19.535741|48.558697,19.535547|48.558764,19.535382|48.558841,19.535233|48.558918,19.535074|48.558971,19.534895|48.559032,19.534763|48.559095,19.534634|48.559127,19.534515|48.559139,19.534399|48.559164,19.534259|48.559206,19.534132|48.559221,19.533976|48.559227,19.533835|48.559293,19.533716|48.559362,19.533582|48.559469,19.533524|48.559566,19.533443|48.55967,19.53333|48.559787,19.533239|48.559895,19.533079|48.560023,19.533004|48.560153,19.532904|48.560278,19.532841|48.560414,19.532788|48.560518,19.532693|48.560633,19.532632|48.56075,19.532534|48.560863,19.532425|48.561012,19.532314|48.561099,19.532141|48.561169,19.531979|48.561276,19.531836|48.561321,19.531736|48.561326,19.531673|48.561327,19.53164|48.561327,19.53164|48.561327,19.53164|48.561327,19.53164|48.561327,19.53164|48.561327,19.53164|48.561327,19.53164|48.561327,19.53164|48.561327,19.53164|48.561327,19.53164|48.561327,19.53164|48.561327,19.53164|48.561327,19.53164|48.561327,19.53164|48.561327,19.53164"
        # path="&path=weight:3%7Ccolor:orange%7Cenc:"+encode_coords(coords)
        # api="&AIzaSyD0LgOSvwSgdKrp16kGeyDXgOfmD_pk9yg"
        # url = "https://maps.googleapis.com/maps/api/staticmap?size=250x250&maptype=terrain&zoom=14"+path+api
        # req = urllib.urlopen(url)
        # arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
        # img = cv2.imdecode(arr,-1) # 'load it as it is'
        #
        # cv2.imshow('lalala',img)
        # if cv2.waitKey() & 0xff == 27: quit()