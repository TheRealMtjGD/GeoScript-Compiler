#!/bin/sh

gdpath=""
installpath=""

echo "Downloading GSLIB"
cmd /c echo "" > ghbuff
git clone https://github.com/TheRealMtjGD/GSLIB.git > ghbuff

echo "Installing GSLIB"
rem ghbuff
mv GSLIB ../Libraries

echo "Setting up config file"
echo "gd=$gdpath\nstdlib=$installpath/Libraries" > ../config.env

echo "Installing GeoScript"
cp -r ../ $installpath

echo "Installed :)"