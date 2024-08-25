
sudo chown -R matt:matt /media/matt/TERRA/green1

sudo find /home/matt -user matt \( -name "*.pdf" -o -name "*.svg" -o -name "*.SVG" -o -name "*.py" -o -name "*.odt" \) -not \( -path "/home/matt/.local/*" -o -path "/home/matt/snap/*" -o -path "/home/matt/.cache/*" \) | rsync -R --files-from=- / /media/matt/TERRA/green1
