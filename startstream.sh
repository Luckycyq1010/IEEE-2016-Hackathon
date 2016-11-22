 #raspivid -t 999999 --hflip -o - -w 512 -h 512 -fps 15 | nc 155.246.162.52  8082

#raspivid -n -w 854 -h 480 -fps 20 -t 9999999 -o - | \
# nc -u 155.246.162.52 8086

# raspivid -t 999999 -b 2000000 -o - | gst-launch-1.0 -e -vvv fdsrc ! h264parse ! rtph264pay pt=96 config-interval=5 ! udpsink host=155.246.162.52 port=5000


raspivid -t 999999 -h 640 -w 480 -fps 25 -rot 270 -b 2000000 -o - | gst-launch-1.0 -v fdsrc ! h264parse !  rtph264pay config-interval=1 pt=96 ! gdppay ! tcpserversink host=ieee.littlebencreations.com port=5000

