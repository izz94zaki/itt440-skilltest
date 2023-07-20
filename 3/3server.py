import socket

PORT = 8080

def convert_pressure(pressure_in_bar):
  pressure_in_atmosphere_standard = pressure_in_bar / 1.01325
  return pressure_in_atmosphere_standard

def main():
  server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  server_address = ("localhost", PORT)
  server_socket.bind(server_address)
  server_socket.listen(1)

  client_socket, client_address = server_socket.accept()
  pressure_in_bar = client_socket.recv(1024).decode("utf-8")
  pressure_in_atmosphere_standard = convert_pressure(float(pressure_in_bar))
 client_socket.sendall(str(pressure_in_atmosphere_standard).encode("utf-8"))

  client_socket.close()
  server_socket.close()

if __name__ == "__main__":
  main()
