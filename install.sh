#!/bin/sh

if [ `whoami` != 'root' ]
then
echo "This script must be run as root."
exit 1;
fi
echo "<<=======J.A.R.V.I.S =======>>"
echo "------------Installing dependecies------------"
sudo apt-get install portaudio19-dev
sudo apt-get install libespeak1
pip3 install -r requirements.txt
if [ $? -eq 0 ]
then
echo "Dependencies installed successfully"
echo "Run python chat.py to converse with JARVIS"
else
echo "Error"
fi

