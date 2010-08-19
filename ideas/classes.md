[foo] - foo can be calculated using other attributes
*foos - a list of foos
foo (?) - I'm not sure exactly what this is

Torrent:
	name
	.torrent file
	size
	uploaded
	downloaded
	upload rate
	download rate
	[ratio]
	[completion time]
	[% done]
	*peers
	directory
	priority
	DHT
	*files
	*trackers
	*chunks
	*transfer

File:
	filename
	% complete
	priority
	size
	chunks total
	chunks downloaded

Peer:
	IP
	upload rate (to)
	download rate (from)
	peer (reported down)
	connection (local/remote, encrypted?)
	remote client info
	local client info
	# of queued incoming pieces
	# of queued outgoing pieces
	% done
	# of the piece at front of request queue
	snubbed?
	failed (?)
	client

Tracker:
	url
	enabled?
	seeders
	leechers

Chunk:
	# seen
	downloaded/missing/queued/downloading

Transfer:
	*pieces (?)

Client:
	*torrents
	rtorrent version
	libtorrent version
	host/port
	upload throttle
	download throttle
	upload rate
	download rate
	listening port
	used upload slots
	max upload slots
	used download slots
	max download slots
	# http requests
	max concurrent http requests
	handshakes
	open sockets
	max open sockets
	open files
	max open files
