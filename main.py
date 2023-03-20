import socket

#  dig nyu.edu mx
#  mxa-00256a01.gslb.pphosted.com
#  A local smtp server is used here. It can be accessed on NYU-NET

mail_server = "smtp.nyu.edu"
server_port = 25


def main():
    socket_conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # get socket object
    socket_conn.connect((mail_server, server_port))  # connect to server
    tcp_resp = socket_conn.recv(1024).decode()  # get response
    print(tcp_resp)

    # Send HELO command to begin SMTP handshake.
    socket_conn.send("HELO nyu.edu\r\n".encode())
    print(socket_conn.recv(1024).decode())

    # Send MAIL FROM command and print response.

    socket_conn.send("MAIL FROM: Elon<elon.musk@nyu.edu>\r\n".encode())
    print(socket_conn.recv(1024).decode())

    # Send RCPT TO command and print server response.

    socket_conn.send("RCPT TO: joep@nyu.edu\r\n".encode())
    print(socket_conn.recv(1024).decode())

    # Send DATA command and print server response.

    socket_conn.send("DATA\r\n".encode())
    print(socket_conn.recv(1024).decode())

    # Send email data.

    socket_conn.send("SUBJECT: Python Assignment 1\r\n\r\n".encode())
    socket_conn.send("Birds aren't real🐦\r\n".encode())

    # Send message to close email message.

    socket_conn.send(".\r\n".encode())
    print(socket_conn.recv(1024).decode())

    # Send QUIT command and get server response.

    socket_conn.send("QUIT\r\n".encode())
    print(socket_conn.recv(1024).decode())

    socket_conn.close()


if __name__ == "__main__":
    main()

# That guy is interesting
