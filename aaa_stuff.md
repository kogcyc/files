
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
    BG=113322
    FG=ffffff

    HDR_BG=113322
    HDR_FG=ffffff

    BTN_BG=113322
    BTN_FG=ffffff

    HDR_BTN_BG=559999
    HDR_BTN_FG=ffffff

    SEL_BG=002211
    SEL_FG=ffffff

    TXT_BG=113322
    TXT_FG=ffffff

    WM_BORDER_FOCUS=113322
    WM_BORDER_UNFOCUS=113322

    # Accent/active state (added)
    ACCENT_BG=559999
    ACCENT_FG=ffffff

    # Optional extras
    HOVER_BG=224455
    HOVER_FG=ffffff
    DISABLED_BG=445566
    DISABLED_FG=888888
    ")

    https://github.com/PapirusDevelopmentTeam/papirus-folders?tab=readme-ov-file#script-usage

    sudo add-apt-repository ppa:papirus/papirus
    sudo apt-get update
    sudo apt-get install papirus-folders

    papirus-folders -C brown --theme Papirus-Dark

    cd ~/.themes/
    cd black/
    cd xfwm4/

    get kogcyc.github.io/files/xfwm4.tar.gz and read the readme



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

    xclip -selection clipboard -i %f	               file -> clipboard
    xclip -selection clipboard -o > %f	               clipboard -> file
    xclip -selection clipboard -t $(file …) -i %f	   imageFile -> clipboard    NOTE: this will not paste a JPEG into GIMP

### install Handbrake

    sudo apt install handbrake 
    sudo apt install libdvdcss2 
    sudo dpkg-reconfigure libdvd-pkg


