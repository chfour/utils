#!/bin/bash

delay=10

echo "put your mouse wherever you need to click"
sleep 4
eval $(xdotool getmouselocation --shell)

sleep 1

while true; do
    echo "clicking"
    xdotool mousemove $X $Y click 1 mousemove restore
    echo "waiting $delay sec"
    sleep "$delay"
done
