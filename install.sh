#!/bin/bash

sudo mkdir /usr/share/muse
sudo cp -R * /usr/share/muse
mkdir {~/.config,~/.config/autostart}
sudo mv /usr/share/muse/muse.desktop ~/.config/autostart/muse.desktop
sudo chmod 777 ~/.config/autostart/muse.desktop
sudo chmod +x /usr/share/muse/muse.py
