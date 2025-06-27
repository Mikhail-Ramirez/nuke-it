import time
import board
import digitalio
import usb_hid

from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

# ───────── HID SETUP ─────────
kbd    = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)

# ───────── SWITCH ON D2 ─────────
sw = digitalio.DigitalInOut(board.D2)
sw.direction = digitalio.Direction.INPUT
sw.pull      = digitalio.Pull.UP   # pressed == LOW

prev = False

# ───────── MAIN LOOP ─────────
while True:
    cur = not sw.value
    if cur and not prev:
        # 1) announce start
        layout.write('echo "Nuke it..."\n')
        time.sleep(0.05)

        # 2) hide our keystrokes
        layout.write('stty -echo\n')
        time.sleep(0.02)

        # 3) delete old repo
        layout.write('REPO=$(git remote get-url origin); DIR=$(basename "$PWD")\n')  
        layout.write('cd ..\n')                                                    
        layout.write('rm -rf "$DIR"\n')                                              
        layout.write('clear\n')                                                      

        # 4) print ASCII nuke art top-down
        layout.write("cat << 'NUKE'\n")
        layout.write("          _ ._  _ , _ ._\n")
        layout.write("        (_ ' (   )_  .__)\n")
        layout.write("      ( (  (    )   )  ) _)\n")
        layout.write("     (__ (_   (_ . _) _) ,__)\n")
        layout.write("         ~~\\ ' . /~~\n")
        layout.write("              ;   ;\n")
        layout.write("              /   \\\n")
        layout.write("_____________/_ __ \\\\_____________\n")
        layout.write("NUKE\n")
        time.sleep(0.05)

        # 5) clone fresh and cd in
        layout.write('git clone "$REPO"\n')   
        layout.write('cd "$DIR"\n')           
        time.sleep(0.05)

        # 6) restore echo so you see the results
        layout.write('stty echo\n')

        # 7) lock out so it doesn’t retrigger mid-run
        time.sleep(1.0)

    prev = cur
    time.sleep(0.01)
