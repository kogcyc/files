### make a transparent PNG ###

    convert -size 1920x1080 xc:none transparent_image.png

### make an environment variable ###

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

    https://github.com/themix-project/oomox-gtk-theme?tab=readme-ov-file

    ./change_color.sh -o zzz <(echo -e "
    BG=224466
    FG=ffffff
    BTN_BG=446688
    BTN_FG=ffffff
    HDR_BTN_BG=1a5fb4
    HDR_BTN_FG=ffffff
    HDR_BG=224466
    HDR_FG=ffffff
    SEL_BG=bb7700
    SEL_FG=ffffff
    TXT_BG=882211
    TXT_FG=ffffff
    WM_BORDER_FOCUS=777777
    WM_BORDER_UNFOCUS=777777
    ")

### git name email

    git config --global user.email "kogcyc@gmail.com"
    git config --global user.name "Matthew"
    
### add user to sudoers

    usermod -aG sudo username
