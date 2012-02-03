#!/bin/sh

mkdir temp
virtualenv temp/ENV
source temp/ENV/bin/activate

sudo pip install REQUIREMENTS