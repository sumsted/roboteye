if ps -ef | grep 'roboteye.py' >/dev/null 2>&1; then
    echo "roboteye is already running"
    exit 0
else
    echo "**** starting roboteye  ****"
    exec /webapps/roboteye/roboteye/scripts/start_roboteye.sh
fi