### make a transparent PNG ###

    convert -size 1920x1080 xc:none transparent_image.png

### make and environment variable ###

    export MY_VAR=bigLONGstring
put it in .bashrc if you want it permanent

### install python github module ###

    sudo apt install python3-github

### how to fix LightDM ###

    [greeter]
    background = /aaa/camo1.png
    theme-name = green
    icon-theme-name = ePapirus-Dark
    user-background = false
    position = 50%,center 35%,center

    sudo mousepad /etc/lightdm/lightdm-gtk-greeter.conf

    cd /usr/share/themes/
    sudo thunar

### add to mousepad schemes ###

    cd /usr/share/gtksourceview-4/styles/
    sudo wget https://kogcyc.github.io/files/kanonikal.xml

### how to install oomox ###

    git clone https://github.com/themix-project/oomox.git --recursive
    cd oomox/
    sudo apt update && sudo apt install -y libgtk-3-dev python3-gi libgdk-pixbuf2.0-dev sassc librsvg2-bin libglib2.0-bin
    make -f po.mk install
    pip3 install colorz colorthief haishoku pystache PyYAML --break-system-packages
    ./gui.sh 
