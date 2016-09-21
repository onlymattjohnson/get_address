#!/usr/bin/python

import geocoder
import sys

address = " ".join(sys.argv[1:])
g = geocoder.google(address)
print g.address