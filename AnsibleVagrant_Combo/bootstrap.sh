#!/bin/sh

# Bootstrapping steps. Here we create needed directories on the guest
mkdir -p ~/.ssh
mkdir -p ~/.ansible
mkdir -p ~/.config
mkdir -p ~/.config/openstack
sudo apt-get update
sudo apt-get install python3-pip -y
sudo -H pip3 install --upgrade ansible
sudo update-alternatives --install /usr/bin/python python /usr/bin/python2.7 1
sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.6 2
sudo update-alternatives --set python /usr/bin/python3.6
pip3 install python-openstackclient
