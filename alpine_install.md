
🔹 Step 1: Boot Alpine Extended ISO

At the boot prompt, choose the default option.
Login as root (no password).

🔹 Step 2: Run the installer

    setup-alpine

Follow prompts:

- Keymap: us or your choice
- Hostname: e.g. tricorder
- Network: use wlan0, provide SSID/pass
- Mirror: choose closest
- Timezone: e.g. America/Los_Angeles
- Disk: choose sys mode to install to disk
- At end: reboot

🔹 Step 3: After reboot, log in as root

Update everything:

    apk update
    apk upgrade

Enable community repo:

this might require installing nano, so that is included here:

    apk add nano

    nano /etc/apk/repositories

Uncomment the ***community*** line like:

    http://dl-cdn.alpinelinux.org/alpine/v3.19/community

Save + exit. Then:

    apk update

🔹 Step 4: Create your user

    adduser matt (may have been done during setup-alpine)
    addgroup matt wheel 
    addgroup matt audio 
    addgroup matt video 
    addgroup matt input 
    addgroup matt tty
    apk add doas
    echo "permit persist :wheel" > /etc/doas.d/doas.conf

🔹 Step 5: Install X11 and XFCE (no display manager)

    setup-xorg-base
    apk add xfce4 xfce4-terminal dbus elogind gvfs udisks2 polkit thunar-volman
    rc-update add dbus
    rc-update add elogind
    rc-update add polkit

🔹 Step 6: Install sound system

    apk add alsa-utils alsa-ucm-conf pulseaudio pulseaudio-alsa pavucontrol xfce4-pulseaudio-plugin 

🔹 Step 7: Configure XFCE launch for matt

Switch to your user:

    su - matt

Create .xinitrc:

    echo "pulseaudio --start &" > ~/.xinitrc
    echo "exec startxfce4" >> ~/.xinitrc
    chmod +x ~/.xinitrc

🔹 Step 8: (Optional) Add swap file for 1GB RAM

As root:

    dd if=/dev/zero of=/swapfile bs=1M count=512
    chmod 600 /swapfile
    mkswap /swapfile
    swapon /swapfile
    echo "/swapfile none swap sw 0 0" >> /etc/fstab

🔹 Step 9: Reboot and log in as matt

    reboot

Log in as matt, then run:

    startx

You should see XFCE, PulseAudio running, and pavucontrol ready.



 
