import socket

def main():
    host = "127.0.0.1"
    port = 8888

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    quote = client_socket.recv(4096).decode()
    print("Quote of the day: {}".format(quote))

    client_socket.close()

if __name__ == "__main__":
    main()
