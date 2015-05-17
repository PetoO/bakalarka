__author__ = 'peto'
# this module handle parsing tcx. files , only supports one activity and track without pauses for now

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


