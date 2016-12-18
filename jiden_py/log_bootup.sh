#!/bin/bash
### BEGIN INIT INFO
# Provides:             log_bootup.sh
# Required-Start:       $all
# Required-Stop:
# Default-Start:        2 3 4 5
# Default-Stop:         0 1 6
# Short-Description:    Write to log at bootup
### END INIT INFO

HOME_DIR_LOG="/home/pi/jiden/logs/jiden.log"
OPEN_BRACK="["
CLOSE_BRACK="]:"
DATE_TIME=`date +"%D %T"`
MESSAGE=$OPEN_BRACK$DATE_TIME$CLOSE_BRACK" System boot up <br />"

if [ ! -f "$HOME_DIR_LOG" ]; then
    touch $HOME_DIR_LOG
    echo $MESSAGE >> "$HOME_DIR_LOG"

else
    echo $MESSAGE >> "$HOME_DIR_LOG"
fi

