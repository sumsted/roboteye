if ps -ef | grep "mjpg-streamer" | grep -v grep >/dev/null 2>&1; then
    echo "mjpeg-streamer is already running"
    exit 0
else
    echo "**** starting mjpeg-streamer  ****"
    nohup /home/pi/webapps/roboteye/roboteye/scripts/start_mjpg.sh > /home/pi/projects/logs/nohup_mjpeg.out 2> /home/pi/projects/logs/nohup_mjpeg.err < /dev/null &
fi