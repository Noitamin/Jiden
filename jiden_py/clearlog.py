import subprocess

clear_log_cmd = "rm -rf /home/pi/jiden/logs/*"
clear_log = subprocess.Popen(clear_log_cmd, shell=True, stdout=subprocess.PIPE)
clear_log.communicate()

