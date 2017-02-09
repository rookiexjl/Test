# coding:utf-8
from timer import Timer
from redis import Redis
rdb = Redis()

with Timer() as t:
	rbd.lpush('foo','bar')
print "=> elasped lpush:%s s" % t.secs


with Timer as t:
	rbd.lpop('foo')
print "=> elasped lpop: %s s" % t.secs
