if ps -ef | grep "roboteye.py" | grep -v grep >/dev/null 2>&1; then
    echo "roboteye is already running"
    exit 0
else
    echo "**** starting roboteye  ****"
    nohup /home/pi/webapps/roboteye/roboteye/scripts/start_roboteye.sh > /home/pi/projects/logs/nohup_roboteye.out 2> /home/pi/projects/logs/nohup_roboteye.err < /dev/null &
fi