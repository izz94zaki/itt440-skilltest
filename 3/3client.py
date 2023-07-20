import socket

PORT = 8080

def main():
  client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  server_address = ("localhost", PORT)
  client_socket.connect(server_address)

  pressure_in_bar = input("Enter the pressure in bar: ")
  client_socket.sendall(pressure_in_bar.encode("utf-8"))
  pressure_in_atmosphere_standard = client_socket.recv(1024).decode("utf-8")
  print("The pressure in atmosphere-standard is: " + pressure_in_atmosphere_standard)

  client_socket.close()

if __name__ == "__main__":
  main()
