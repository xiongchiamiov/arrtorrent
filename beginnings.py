#!/usr/bin/env python

import sys
from PySide import QtGUI
from rtorrent import RtorrentProxy

client = RtorrentProxy('http://localhost')
client.updateTransfers()
for transfer in client.transfers:
	print transfer['name']
	print "\t size: %s" % transfer['size']
	print "\t done: %s" % transfer['down_total']
	print "\t d/u:  %s/%s" % (transfer['down_rate'], transfer['up_rate'])
	
	
