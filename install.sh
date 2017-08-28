#!/usr/bin/env bash
echo "***********************************************"
echo "***************** install *********************"
echo "***********************************************"

echo "***********************************************"
echo "---  apt update e upgrade---"
echo "***********************************************"
sudo apt-get -y update

echo "***********************************************"
echo "---apt-get -y install sudo---"
apt-get -y install sudo
echo "***********************************************"


echo "***********************************************"
echo "---OS dependencies---"
echo "***********************************************"
sudo apt-get -y install python3-pip
sudo apt-get -y install python3-dev python3-setuptools
sudo apt-get -y install git
sudo apt-get -y install supervisor
# .....
# .....
# .....
# .....

echo "***********************************************"
echo "---install dependencies (including django)  ---"
echo "***********************************************"
pip install --upgrade pip
pip install -r requirements.txt
