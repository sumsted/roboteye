if ps -ef | grep "mjpg-streamer" | grep -v grep >/dev/null 2>&1; then
    echo "mjpeg-streamer is already running"
    exit 0
else
    echo "**** starting mjpeg-streamer  ****"
    exec /webapps/roboteye/roboteye/scripts/start_mjpeg.sh
fi