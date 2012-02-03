#!/bin/sh

mkdir temp
mkdir temp/static
mkdir temp/media

virtualenv temp/ENV
source temp/ENV/bin/activate

sudo pip install REQUIREMENTS

git remote rm origin

git submodule init
git submodule update
