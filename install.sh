#!/bin/bash

clear

apt-get update

apt-get upgrade -y

apt-get install -y python

pip install -r $HOME/EBomber/config/requirements

ln -s $HOME/EBomber/start.sh $HOME/EBomber.sh

clear