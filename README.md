# Nuke-It

A kill it all and try again switch powered by a CircuitPython-flashed XIAO SAMD21 (or any CircuitPython-compatible board). (CAD Model will be uploaded as soon as I remember)

---

## 🔧 Requirements

1. **Hardware**  
   - [Seeeduino XIAO (SAMD21) or similar board](https://circuitpython.org/board/seeeduino_xiao/)  
   - [A momentary or toggle switch] (https://www.amazon.com/dp/B07BTRK5SP?ref=ppx_yo2ov_dt_b_fed_asin_title&th=1)
   - USB-C (or USB-Micro) cable **with data** support  

2. **Firmware**  
   - Latest CircuitPython UF2 for your board: download from the link above and flash via drag-and-drop in bootloader mode.

3. **Libraries**  
   - Copy `adafruit_hid` from the CircuitPython library bundle into `CIRCUITPY/lib/` so you have:
     ```
     CIRCUITPY/
     ├─ code.py
     └─ lib/
        └─ adafruit_hid/
           ├ adafruit_hid/__init__.mpy
           ├ adafruit_hid/keyboard.mpy
           ├ adafruit_hid/keycode.mpy
           └ adafruit_hid/keyboard_layout_us.mpy
     ```

---

## Setup

1. **Flash** your board with the CircuitPython UF2.  
2. **Copy** your `code.py` (the nuke-it script) into the **root** of the freshly-mounted `CIRCUITPY` drive.  
3. **Wire** your switch:
   ```txt
   XIAO D2 ───┐
              └── SWITCH ─── GND
4. **Eject/safely** remove the CIRCUITPY drive so the firmware reloads. Then replug (it could prob be wifi enabled but im lazy + power yk).
5. Program normally until critical failure and you determine it is time to **play god**
