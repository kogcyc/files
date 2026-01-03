doas apk update

doas apk add networkmanager
doas apk add blueman
doas apk add networkmanager-wifi
doas apk add network-manager-applet
doas apk add networkmanager-bluetooth
doas rc-service networkmanager start

doas rc-update add networkmanager default
doas rc-service bluetooth start
doas rc-update add bluetooth default
bluetooth-applet &

doas apk add alsa-utils alsa-ucm-conf pulseaudio pulseaudio-alsa pavucontrol xfce4-pulseaudio-plugin mesa-gles mesa-egl
doas pulseaudio --start
pulseaudio --start
