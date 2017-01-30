sleep 30s;
sudo -u pi epiphany -a -i --profile ~/.config file://home/pi/webapps/roboteye/roboteye/static/index.html --display=:0 &
sleep 15s;
xte "key F11" -x:0