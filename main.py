import tkinter as tk
import socket
import threading

root = tk.Tk()
root.title("Device Client")
root.geometry('320x175')

def inp(bt):
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ip = '192.168.1.143'
        server_address = (ip, 5200)
        client.connect(server_address)
        message = bt
        client.sendall(message.encode('utf-8'))
        client.close()
    except Exception as e:
        print("Error:", e)

hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)

# Set up the server socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (local_ip, 4000)
server.bind(server_address)

def server_list():
    server.listen(5)
    print(f"Connect to ip: {local_ip}")
    print(f"Listening...")
    while True:
        client, address = server.accept()
        data = client.recv(1024)
        print(data.decode('utf-8'))
        client.close()

# Start the server in a separate thread
t1 = threading.Thread(target=server_list)
t1.daemon = True
t1.start()

bt1 = tk.Button(root, width=10, height=5, text="1", command= lambda: inp("BT1"))
bt1.place(y=1, x=1)
bt2 = tk.Button(root, width=10, height=5, text="2", command= lambda: inp("BT2"))
bt2.place(y=1, x=80)
bt3 = tk.Button(root, width=10, height=5, text="3", command= lambda: inp("BT3"))
bt3.place(y=1, x=160)
bt4 = tk.Button(root, width=10, height=5, text="4", command= lambda: inp("BT4"))
bt4.place(y=1, x=240)
bt5 = tk.Button(root, width=10, height=5, text="5", command= lambda: inp("BT5"))
bt5.place(y=88, x=1)
bt6 = tk.Button(root, width=10, height=5, text="6", command= lambda: inp("BT6"))
bt6.place(y=88, x=80)
bt7 = tk.Button(root, width=10, height=5, text="7", command= lambda: inp("BT7"))
bt7.place(y=88, x=160)
bt8 = tk.Button(root, width=10, height=5, text="8", command= lambda: inp("BT8"))
bt8.place(y=88, x=240)

root.mainloop()
