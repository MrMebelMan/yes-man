#!/usr/bin/env bash

sleep 10

DISPLAY=:0 feh -T -Z /home/aasa/yesman/yesman_fullscream.jpg &
while :; do
  kill -9 `ps aux | grep python | tr -s ' ' | awk -F' ' '{print $2}' | head -1`
  python3 /home/aasa/yesman/yesman.py
done

