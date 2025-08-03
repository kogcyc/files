
### install python modules

    pip3 install markdown python-frontmatter jinja2 rich --break-system-packages

### install color-picker

    sudo apt install color-picker

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

    sudo cp -r .themes/darkRed /usr/share/themes


### add to mousepad schemes ###

    cd /usr/share/gtksourceview-4/styles/
    sudo wget https://kogcyc.github.io/files/kanonikal.xml

### how to install oomox ###

    git clone https://github.com/themix-project/oomox-gtk-theme.git

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
    SEL_FG=ffffff       <<--- controls the color of the text under desktop icons
    TXT_BG=882211
    TXT_FG=ffffff
    WM_BORDER_FOCUS=777777
    WM_BORDER_UNFOCUS=777777
    ")



    https://github.com/PapirusDevelopmentTeam/papirus-folders?tab=readme-ov-file#script-usage

    sudo add-apt-repository ppa:papirus/papirus
    sudo apt-get update
    sudo apt-get install papirus-folders

    papirus-folders -C brown --theme Papirus-Dark


    cd ~/.themes/
    cd black/
    cd xfwm4/
    cp close-active.xpm safe.store

    for f in close-inactive.xpm close-prelight.xpm close-pressed.xpm; do     cp -v close-active.xpm "$f"; done

    for f in maximize-*.xpm; do     [ "$f" != "maximize-active.xpm" ] && cp -v maximize-active.xpm "$f"; done

    for f in hide-*.xpm; do     [ "$f" != "hide-active.xpm" ] && cp -v hide-active.xpm "$f"; done



### git name email

    git config --global user.email "kogcyc@gmail.com"
    git config --global user.name "Matthew"
    
### add user to sudoers

    sudo usermod -aG sudo username

### make a copy of a repostory

    git clone https://github.com/kogcyc/v3.git
    cd v3
    git remote remove origin
    make new repository (v4)
    git remote add origin https://github.com/kogcyc/v4.git
    git push -u origin main

### add custom actions to Thunar

    xclip -selection clipboard -i %f
    xclip -selection clipboard -o > %f
    xclip -selection clipboard -t $(file -b --mime-type %f) -i %f

### install Handbrake

    sudo apt install handbrake 
    sudo apt install libdvdcss2 
    sudo dpkg-reconfigure libdvd-pkg


