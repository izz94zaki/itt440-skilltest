#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/socket.h>
#include <netinet/in.h>

int main() {
  int server_socket = socket(AF_INET, SOCK_STREAM, 0);
  if (server_socket == -1) {
    printf("Error creating socket\n");
    return 1;
  }

  struct sockaddr_in server_address;
  server_address.sin_family = AF_INET;
  server_address.sin_port = htons(9999);
  server_address.sin_addr.s_addr = INADDR_ANY;
  if (bind(server_socket, (struct sockaddr *) &server_address, sizeof(server_address)) == -1) {
    printf("Error binding socket\n");
    return 1;
  }

  listen(server_socket, 5);

  int client_socket = accept(server_socket, NULL, NULL);
  if (client_socket == -1) {
    printf("Error accepting connection\n");
    return 1;
  }

  int random_number = rand() % 900 + 100;

  char buffer[10];
  sprintf(buffer, "%d", random_number);
  write(client_socket, buffer, strlen(buffer));

  close(client_socket);
  close(server_socket);

  return 0;
}
