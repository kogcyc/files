## Openbox configuration

How wifi works

    there is a file here:

    /etc/wpa/wpa_supplicant.conf

    network={
	  ssid="install_example"
	  psk=65a4e30515bbb1fe81b4f6aeabe84090e4b79093d6c1855e6d10b4cffac7f073
    }

    network={
	  ssid="coffee_shop"
	  psk="123maple"
    }

    the first entry, "install_example" was created when you install Alpine Linux

    the second entry, "coffee_shop" was created, by you, when you went to the coffee shop

    the easist way to edit it (add SSIDs to it) is this:
	
    doas nano /etc/wpa_supplicant/wpa_supplicant.conf

Main Openbox config file

    ~/.config/openbox/rc.xml

Openbox "root menu" file

    ~/.config/openbox/menu.xml

Openbox autostart file (user-level)

    ~/.config/openbox/autostart


Tint2 config location

    ~/.config/tint2/tint2rc

GTK theme selection file

    ~/.config/gtk-3.0/settings.ini

    [Settings]
    gtk-theme-name=Adwaita
    gtk-icon-theme-name=Papirus
    gtk-font-name=Sans 10
    gtk-cursor-theme-name=Adwaita

    changes will occur on next startx

Wallpaper setting

    feh



xsetroot (solid colors)



Kitty config file

    ~/.config/kitty/kitty.conf

Openbox theme directory

    ~/.local/share/themes


Set typeface/font of 'root menu'

    look for this stanza in ~/.config/openbox/rc.xml
    
    <font place="MenuItem">
      <name>Inconsolata-Nerd</name>
      <size>13</size>
      <!-- font size in points -->
      <weight>normal</weight>
      <!-- 'bold' or 'normal' -->
      <slant>normal</slant>
      <!-- 'italic' or 'normal' -->
    </font>

Syntax highlighting themes om Mousepad

    /usr/share/gtksourceview-3.0/styles/ <- where mousepad looks for the theme to display them in Preferences
    /usr/share/gtksourceview-4/styles/ <- where is finds the themes 

How to check laptop battery

    acpi b

You configured

Colors

Fonts

Explicit control outside of .Xresources

XTerm

XTerm resource configuration

~/.Xresources


Working font example

XTerm*faceName: Inconsolata Regular
XTerm*faceSize: 12


Other XTerm topics

Cursor color

Foreground/background colors

Font fallback behavior

Starting XTerm with a larger default font

Why glyph metrics can cause visual “double width” surprises

No true letter-spacing control in XTerm

XFCE4 Terminal (running under Openbox)

Settings backend

Uses xfconf (not flat files)

Query / set values

xfconf-query -c xfce4-terminal -lv
xfconf-query -c xfce4-terminal -p /color-background -s "#334444"


Important discovery

Requires a working dbus-launch

Installing dbus-x11 fixed failures on Alpine




Observed behavior

Styles are detected

Selection sometimes does not apply (GTK / theme interaction)

Font control

Separate from syntax colors

GTK-dependent

Networking (Alpine Linux)

wpa_supplicant config

Can use plain-text passwords

Multiple network entries allowed

Network selection

Alpine does not prompt by default

Requires explicit tooling or config changes

Power & hardware

Battery percentage (CLI)

cat /sys/class/power_supply/BAT0/capacity


(device name may vary)

USB port speed detection

lsusb -t

xhci_hcd / 5000M indicates USB 3

General Openbox realities (confirmed)

Openbox:

Is a window manager, not a desktop environment

Does not manage:

wallpaper

panels

networking

power

Is happiest when paired with small, explicit tools (your preferred mode)

Meta-feature 😌

You successfully:

Built a useful Openbox desktop on Alpine

Navigated GTK vs Xresources vs xfconf

Assembled a system that rewards understanding rather than hiding it

If you’d like, next we can:

turn this into a personal Openbox field manual

extract a minimal “known-good” Alpine + Openbox recipe

or diagram which subsystem owns what (WM vs GTK vs X11 vs dbus)

You did the hard part: you cared enough to make it coherent.
