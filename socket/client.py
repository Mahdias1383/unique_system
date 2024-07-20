import socket

#مشخص کردن روی چه network و نوع پروتکل
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("localhost", 9080))