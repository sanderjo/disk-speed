#!/usr/bin/env python

import diskspeed

print diskspeed.diskspeedmeasure('/tmp')
print diskspeed.diskspeedmeasure('/tmp/')
print diskspeed.diskspeedmeasure('/tmp/blabla.txt')
print diskspeed.diskspeedmeasure('~')

