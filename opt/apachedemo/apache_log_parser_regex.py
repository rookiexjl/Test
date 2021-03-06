#!/usr/bin/env python
# coding:utf-8
"""
USAGE:

apache_log_parser_regex.py some_log_file

This script takes one command line argument: the name of a log file
to parse. It then parses the log file and generates report which
associtates remote hosts with number of bytes transferred to them.
"""

import sys
import re


log_line_re = re.compile(r'''(?P<remote_host>\S+) #IP ADDRESS
							 \s+ #whitespace
							 \S+ #remote logname		
							 \s+ #whitespace
							 \S+ #remote user
							 \s+ #whitespace
							 \[[^\[\]]+\] #time
							 \s+ #whitespace
							 "[^"]+" #first line of request
							 \s+ #whitespace
							 (?P<status>\d+)
							 \s+ #whitespace
							 (?P<bytes_sent>-|\d+)
							 \s* #whitespace
							 ''', re.VERBOSE)


def dictify_logline(line):
	'''return a dictionary of the pertinet pieces of an apacche combined log file

	Currently, the onely flelds we are interested inare remote host and bytes sent,
	but we are putting status in there just for good measure.
	'''
	m = log_line_re.match(line)
	if m:
		groupdict = m.groupdict()
		if groupdict['bytes_sent'] == '_':
			groupfict['bytes_sent'] = 'O'
		return groupdict
	else:
		return {'remote_host': None,
				'status':None,
				'bytes_sent': "O",
		}

def generate_log_report(logfile):
	'''return a dictionary of format remote_host =>[list of bytes sent]

	This function takes a file object, iterates through all the lines in the file,
	and generates a report of the number of bytes transferred to each remote host
	for each hit on the webserver.
	'''
	report_dict = {}
	for line in logfile:
		line_dict = dictify_logline(line)
		try:
			bytes_sent= int(line_dict['bytes_sent'])
		except ValueError:
			##totally disregard anything we don;t understand
			continue
		report_dict.setdefault(line_dict['remote_host'], []).append(bytes_sent)
	return report_dict


if __name__ == '__main__':
	if not len(sys.argv) > 1:
		print __doc__
		sys.exit(1)
	infile_name = sys.argv[1]
	try:
		infile = open(infile_name, 'r')
	except IOError:
		print "You must specify a valid file to parse"
		print __doc__
		sys.exit(1)
	loh_report = generate_log_report(infile)
	print log_report
	infile.close()


	
