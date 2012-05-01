#!/bin/sh

mkdir site
mkdir site/static
mkdir site/media

virtualenv site/ENV
source site/ENV/bin/activate

sudo pip install REQUIREMENTS

git remote rm origin

git submodule init
git submodule update
