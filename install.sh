#!/bin/bash

sudo mkdir /usr/share/muse
sudo cp {muse.py,quotes.txt,LICENSE,README.md} /usr/share/muse
sed '$ i\/etc/init.d/muse.sh || exit 1' /etc/rc.local > /tmp/muse-rc.local
sudo mv /tmp/muse-rc.local /etc/rc.local
sudo cp muse.sh /etc/init.d
sudo chmod +x /etc/init.d/muse.sh
sudo update-rc.d muse.sh defaults
