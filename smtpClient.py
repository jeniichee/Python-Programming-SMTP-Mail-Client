from socket import *


def smtp_client(port=1025, mailserver="127.0.0.1"):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope
    receiver = "you@gmail.com"
    sender = "me@gmail.com"

    # Create socket called clientSocket and establish a TCP connection with mailserver and port
    clientSocket = socket(AF_INET, SOCK_STREAM)

    # Fill in start
    # Fill in end

    clientSocket.connect((mailserver, port))

    recv = clientSocket.recv(1024).decode()  # response
    # print(recv) #You can use these print statement to validate return codes from the server.
    if recv[:3] != "220":
        print("220 reply not received from server.")

    # Send HELO command and print server response.
    heloCommand = "HELO Alice\r\n"
    print(heloCommand)
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    # print(recv1)
    if recv1[:3] != "250":
        print("250 reply not received from server.")

    # Send MAIL FROM command and handle server response.
    # Fill in start
    # Fill in end
    mailfromCommand = f"MAIL FROM:{sender}\r\n"
    clientSocket.send(mailfromCommand.encode())
    recv2 = clientSocket.recv(1024).decode()
    # print(recv2)
    if recv2[:3] != "250":
        print("250 reply not received from server.")

    # Send RCPT TO command and handle server response.
    # Fill in start
    # Fill in end
    rcptCommand = f"RCPT TO:{receiver}\r\n"
    clientSocket.send(rcptCommand.encode())
    recv3 = clientSocket.recv(1024).decode()
    # print(recv3)
    if recv3[:3] != "250":
        print("250 reply not received from server.")

    # Send DATA command and handle server response.
    # Fill in start
    # Fill in end
    dataCommand = f"DATA\r\n"
    clientSocket.send(dataCommand.encode())
    recv4 = clientSocket.recv(1024).decode()
    # print(recv4)
    if recv4[:3] != "354":
        print("354 reply not received from server.")

    # Send message data.
    # Fill in start
    # Fill in end
    clientSocket.send(msg.encode())

    # Message ends with a single period, send message end and handle server response.
    # Fill in start
    # Fill in end
    clientSocket.send(endmsg.encode())
    recv5 = clientSocket.recv(1024).decode()
    # print(recv5)
    if recv5[:3] != "250":
        print("250 reply not received from server.")

    # Send QUIT command and handle server response.
    # Fill in start
    # Fill in end
    quitCommand = "QUIT\r\n"
    clientSocket.send(quitCommand.encode())
    recv6 = clientSocket.recv(1024).decode()
    # print(recv6)

    clientSocket.close()


if __name__ == "__main__":
    smtp_client(1025, "127.0.0.1")
