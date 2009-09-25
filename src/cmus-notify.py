#!/usr/bin/env python
# -*- coding: utf-8 -*-
##
# cmus-notify
# author: nblock <nblock [at] archlinux [dot] us>
# version: git
# license: GPLv3
##
"""
a simple script to display cmus' status using libnotify

in cmus: ":set status_display_program=/path/to/cmus-notify.py"
"""

import os
import sys

#config
ICON="/usr/share/icons/oxygen/16x16/apps/tux.png"

# a simple class to interact with cmus
class cmus(object):
    def __init__(self):
        self.data = {}
        self.get_song_info()

    # get song information from cmus (parsing from commandline)
    def get_song_info(self):
        for pos in xrange(1, len(sys.argv), 2):
            self.data[sys.argv[pos]] = sys.argv[pos + 1].decode('utf-8')

        #correct duration
        dur = int(self.data["duration"])
        self.data["duration"] = str(dur/60) + ":" + str(dur%60)
    
    # get value per key 
    def get_data(self, key):
        if key in self.data:
            return self.data[key]
        return "fail"

if __name__ == "__main__":
    c = cmus()
    notify = "notify-send --icon=%s " % ICON
    head = "'cmus [%s]' " % c.get_data("status")
    info = "'%s - %s (%s) [%s]'" % (c.get_data("artist"),c.get_data("title"), c.get_data("duration"), c.get_data("album"))
    os.system(notify + head + info)

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
