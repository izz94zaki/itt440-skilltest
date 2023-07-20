#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/socket.h>
#include <netinet/in.h>

int main() {
  int client_socket = socket(AF_INET, SOCK_STREAM, 0);
  if (client_socket == -1) {
    printf("Error creating socket\n");
    return 1;
  }

  struct sockaddr_in server_address;
  server_address.sin_family = AF_INET;
  server_address.sin_port = htons(9999);
  server_address.sin_addr.s_addr = inet_addr("127.0.0.1");
  if (connect(client_socket, (struct sockaddr *) &server_address, sizeof(server_address)) == -1) {
    printf("Error connecting to server\n");
    return 1;
  }

  char buffer[10];
  int bytes_received = read(client_socket, buffer, sizeof(buffer));
  if (bytes_received == -1) {
    printf("Error receiving data from server\n");
    return 1;
  }

  printf("Random number: %d\n", atoi(buffer));

  close(client_socket);

  return 0;
}
