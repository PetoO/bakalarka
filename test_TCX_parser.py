from unittest import TestCase
from xml.dom import minidom
from parser_tcx import TCX_parser as tcx

__author__ = 'peto'


class TestTCX_parser(TestCase):
    def test_get_activity_name(self):
        self.parser = tcx("test0.tcx")
        self.activity = self.parser.get_activity_name()
        self.assertEqual(self.activity, "Running")

        self.parser = tcx("test1.tcx")
        self.activity = self.parser.get_activity_name()
        self.assertEqual(self.activity, "Biking")
