#!/usr/bin/env python
# coding:utf-8
"""
USAGE:

apache_log_parser_split.py some_log_file

This script takes one command line argument: the name of a log file
to parse. Tt then parses the log file and generates a report which
assoctiates remote hosts with number of bytes transfrred to them.
"""


import sys


def dictify_logline(line):
	'''return a dictionary of the pertinet pieces if an apache combined log file
	Currently, the only fields we are interested in are remote host and butes sent
	but we are putting in ther just for good measure.
	'''

	split_line = line.split()
	return {'remote_host': split_line[0],
			'status': split_line[8],
			'bytes_sent': split_line[9],
	}


def generate_log_report(logfile):
	''' return a dictionary of format remote_host=>[list of bytes sent]

	This function takes a file object, iterates through all the lines in the file,
	and generates a report of the number of bytes transferred to each remote host
	for each hit on webserver.
	'''

	report_dict = {}
	for line in logfile:
		line_dict = dictify_logline(line)
		host = line_dict['remote_host']
		#line_dict = dictify_logline(line)
		#print line_dict
		try:
			bytes_sent = int(line_dict['bytes_sent'])
		except ValueError:
			##totally disregard anything we don't understand
			continue
		#report_dict.setdefault(line_dict['remote_host'], []).append(bytes_sent)
		report_dict[host] = report_dict.setdefault(host, 0) + bytes_sent
	return report_dict


if __name__=="__main__":
	if not len(sys.argv) > 1:
		print __doc__
		sys.exit(1)
	infile_name = sys.argv[1]
	try:
		print infile_name
		infile = open(infile_name, 'r')
		print infile
	except IOError:
		print "You must specify a valid file to parse"
		print __doc__
		sys.exit(1)
	log_report = generate_log_report(infile)
	print log_report
	infile.close()

