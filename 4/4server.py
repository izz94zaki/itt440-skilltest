import socket
import threading
import random

# List of quotes
quotes = [
    "Be yourself; everyone else is already taken. - Oscar Wilde",
    "Two things are infinite: the universe and human stupidity; and I'm not sure about the universe. - Albert Einstein",
    "Be the change that you wish to see in the world. - Mahatma Gandhi",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
    "The only way to do great work is to love what you do. - Steve Jobs",
    "In three words I can sum up everything I've learned about life: it goes on. - Robert Frost",
    "You miss 100% of the shots you don't take. - Wayne Gretzky"
]

def handle_client(client_socket):
    quote = random.choice(quotes).encode()
    client_socket.send(quote)
    client_socket.close()

def main():
    host = "127.0.0.1"
    port = 8888

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)

    print("Server listening on {}:{}".format(host, port))

    while True:
        client_socket, address = server_socket.accept()
        print("Accepted connection from {}:{}".format(address[0], address[1]))

        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    main()
