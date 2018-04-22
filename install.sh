#!/bin/bash

sudo mkdir {/usr/share/muse,/usr/share/muse/img}
sudo cp {muse.py,quotes.txt,LICENSE,README.md} /usr/share/muse
cp muse.desktop ~/.config/autostart
cd img
sudo cp {1.png,2.png,3.png,4.png,5.png,6.png} /usr/share/muse/img
sudo chmod +x /usr/share/muse/muse.py
