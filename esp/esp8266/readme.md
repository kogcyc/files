# ESP8266 MicroPython Quickstart (Ubuntu)

This guide gets a WeMos D1 mini (or any ESP8266) running MicroPython on Ubuntu/Debian with the commands you provided.

> **Hardware prep (bootloader mode)**
> - If your board has **FLASH** and **RESET** buttons: **Hold FLASH (GPIO0)**, **tap RESET**, keep holding FLASH ~1s, then release.
> - If no buttons: connect **GPIO0 → GND** while resetting/powering the board.

---

## 1) Add user to `dialout` group
```bash
sudo usermod -aG dialout $USER
```
Log out/in or reboot for changes.

---

## 2) Install `esptool`
```bash
pip3 install esptool --break-system-packages
```

---

## 3) Find the serial port
```bash
ls /dev/tty* | grep USB
```
Example: `/dev/ttyUSB0`.

---

## 4) Erase flash
```bash
esptool -p /dev/ttyUSB0 erase_flash
```
---

## 5) Find flash size
```bash
esptool -p /dev/ttyUSB0 flash-id
```
---

## 6) Flash MicroPython firmware
Firmware file: `ESP8266_GENERIC-FLASH_2M_ROMFS-20250809-v1.26.0.bin`
```bash
esptool -p /dev/ttyUSB0 write-flash --flash-size=detect 0x00000 ESP8266_GENERIC-FLASH_2M_ROMFS-20250809-v1.26.0.bin
```
Reset or power cycle the board after flashing.

---

## 7) Install Thonny
```bash
sudo apt install thonny
```
Select **MicroPython (ESP8266)** in Thonny and the correct port.

---

## 8) Blink test
```python
import machine
import time

led = machine.Pin(2, machine.Pin.OUT)

while True:
    led.value(1)
    time.sleep(0.5)
    led.value(0)
    time.sleep(0.5)
```

---

## Troubleshooting
- **Permission denied**: re-login after adding `dialout`.
- **No connection**: confirm bootloader mode, check wiring.
- **Wrong firmware size**: use the correct build for your flash size.
