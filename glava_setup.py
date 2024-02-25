import time
import os

#Verify that hard drve is plugged in and working before executing this script
#This script must be run inside the glava folder after cloning the repo
#You will be prompted to input Y in this script

os.system("sudo apt install meson")
os.system("sudo apt-get update")
os.system("sudo apt-get install libgl1-mesa-dev libpulse0 libpulse-dev libxext6 libxext-dev libxrender-dev libxcomposite-dev liblua5.3-dev liblua5.3 lua-lgi lua-filesystem libobs0 libobs-dev meson build-essential gcc")
os.system("meson build --prefix /usr")
os.system("ninja -C build")
os.system("sudo ninja -C build install")
os.system("cp -r /media/user/2bb69c45-33e8-4b8b-a5f4-dd330073b172/@home/int3rlud3/Desktop/initial_boot/glava_config/glava /home/user/.config")
os.system("glava --desktop --force-mod=radial & glava --desktop & glava --desktop --force-mod=bars")