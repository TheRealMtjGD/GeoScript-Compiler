@echo off

echo "Downloading GSLIB"
cmd /c echo "" > ghbuff
cmd /c git clone https://github.com/TheRealMtjGD/GSLIB.git > ghbuff

echo "Installing GSLIB"
rem ghbuff
move GSLIB ../Libraries

echo "Setting up config file"
cmd /c echo "gd=C:/Users/AppData/{{PUBLIC}}/Local/GeometryDash\nstdlib=C:/Users/Public/AppData/Local/Programs/GeoScript/Libraries" > ../config.env

echo "Installing GeoScript"
robocopy ../ C:/Users/Public/AppData/Local/Programs/GeoScript

echo "Installed :)"