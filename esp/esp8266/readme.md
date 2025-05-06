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
    
### write the MicroPython bin file to your ESP8266

    esptool.py --chip esp8266 --baud 460800 write_flash --flash_size=detect 0 some_file_name.bin
