find /home/matt -user matt \( -name "*.pdf" -o -name "*.svg" -o -name "*.SVG" -o -name "*.py" \) | grep -v "/home/matt/.local" | grep -v "/home/matt/snap" | grep -v "/home/matt/.cache" | rsync -R --files-from=- / /media/matt/HITACHI230/xxx