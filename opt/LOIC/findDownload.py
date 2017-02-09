# coding:utf-8
import dpkt
import socket


def findDownload(pcap):
    for (ts, bu) in pcap:
	try:
	    eth = dpkt.ethernet.Ethernet(buf)
   	    ip = eth.data
	    src = socket.inet_ntoa(ip.src)
	    tcp = ip.data
	    http = dpkt.http.Request(tcp.data)
	    if http.method == 'GET':
		uri = http.uri.lower()
		if '.zop' in uri and 'loci' in uri:
		    print('[!]'+src+'Downloaded LOIC.')
	except:
	    pass

f = open('test.pcap')
pcap = dpkt.pcap.Reader(f)
findDownload(pcap)

