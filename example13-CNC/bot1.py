import socket 


if __name__ == "__main__":
    print("[+] Connecting with server")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("192.168.0.11", 8085))
    run_bot = True
    while run_bot:
        communicate_bot = True
        while  communicate_bot:
            msg = s.recv(1024)
            msg = msg.decode()
            print("command center said: ", msg)
            if msg == "exit":
                communicate_bot = False
        # ans = input("[+] do you want to remain connected: ")
        ans = "connected"
        if ans == "no":
            status = "disconnected"
            s.send(status.encode())
            run_bot = False
        else:
            status = "conntected".encode()
            s.send(status)
    s.close()