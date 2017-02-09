# coding:utf-8
# 实现自动目录同步，直到完成，然
# 后会发生一个邮件告知任务已完成
# 把A目录里面的东西同步到B目录中

from subprocess import call
import sys
import time

"""this motivated rsync tries to synchronize forever"""

source = "/opt/sync_dir_A/" # Note the trailing slash
target = "/opt/sync_dir_B"
rsync = "rsync"
arguments = "-av"
cmd = "%s %s %s %s" % (rsync, arguments,source, target)
def sync():
    while True:
	ret = call(cmd, shell=True)
	if ret != 0:
	    print "resubmitting rsync"
	    time.sleep(30)
	else:
	    print "rsync war succesful"
	    #subprocess.call("mail -s 'jobs done' bofh@example.com", shell=True)
	    sys.exit(0)

sync()

	

