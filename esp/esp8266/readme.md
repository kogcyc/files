### add your user to dialout

    sudo usermod -aG dialout $USER

    NOTE: on my Ubuntu system this only works if I reboot

    running the command:

       groups

    will confirm that

## erase your ESP8266

    esptool.py --chip esp8266 erase_flash
    -OR-
    esptool.py --port /dev/tty??? erase_flash

    I like the first way when I'm getting started because it looks for a working port
    
