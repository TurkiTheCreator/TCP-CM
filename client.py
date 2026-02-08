import socket
import threading

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1' , 55555))

nickname = input("Choose your nickname: ")
if nickname == 'admin':
    password = input("Enter the password for admin: ")
def receive():
    while True:
        global stop_thread
        if stop_thread:
            break
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
                next_message = client.recv(1024).decode('ascii')
                if next_message == 'PASS':
                    client.send(password.encode('ascii'))
                    if client.recv(1024).decode('ascii') == 'REFUSE':
                        print("Connection refused! Wrong password.")
                        stop_thread  = True
                 elif next_message == 'BAN':
                        print("Connection refused! You are banned from the server.")
                        client.close()
                        stop_thread = True
            else:
                print(message)
        except Exception as e:
            print("An error occurred!", e)
            client.close()
            break


def write():
    while True:
        if stop_thread:
            break
        message = f'{nickname}: {input("")}'
        if message[len(nickname)+2:].startswith('/'):
            if nickname == 'admin':
            if message[len(nickname)+2:].startswith('/kick'):
                target_nickname = message[len(nickname)+2+6:]
                client.send(f'KICK {target_nickname}'.encode('ascii'))
                elif message[len(nickname)+2:].startswith('/ban'):
                    target_nickname = message[len(nickname)+2+5:]
                    client.send(f'BAN {target_nickname}'.encode('ascii'))
            else:
                print("Commands can only be executed by the admin!")

            break
        client.send(message.encode('ascii'))

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
