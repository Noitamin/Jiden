import subprocess
import sys

new_pass = str(sys.argv[1])
print new_pass

chpass_cmd = "echo pi:" + new_pass + " | chpasswd"
rc = subprocess.Popen(chpass_cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

rc_output = rc.communicate()

if rc_output[1] != '':
    print "chpasswd failed"

