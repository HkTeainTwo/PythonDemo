#!/usr/bin/python
#-*- coding: utf-8 -*-

import socket

host = "127.0.0.1"
port = 9921
addr = host,port
clients = {}

def stringPolishing(value):
    length = 6-len(value)
    for i in range(length):
        value = '0'+value
    return value

def decoderData(value,sock):
    position = 0
    print value

    try:
        commandLen = int(value[0:6])
        position += 6
        command = value[position:position+commandLen]
        print 'command',command
        position += commandLen

        if command=="login":
            nameLen = int(value[position:position+6])
            position += 6
            userName = value[position:position+nameLen]
            print 'userName'+userName
            sendData = ''
            for key in clients.keys():
                sendData += stringPolishing(str(len(key)))
                sendData += key
                clients[key].send('000005login'+stringPolishing(str(nameLen))+userName)
            sock.send('000010currPeople'+stringPolishing(str(len(clients)))+sendData)
            clients[userName] = sock
        elif command=="talk":
            for key in clients.keys():
                clients[key].send(value)
        elif command=="logout":
            nameLen = int(value[position:position+6])
            position += 6
            userName = value[position:position+nameLen]
            clients[userName].close()
            del clients[userName]
            for key in clients.keys():
                clients[key].send(value)
    except ValueError:
        sock.send("command error")

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(addr)
server.listen(999)

while True:
    clientSock,addrs = server.accept()
    
    print "client ip:" + str(addrs[0])
    print "client port:" + str(addrs[1])

    clientData = clientSock.recv(2000)
    decoderData(clientData,clientSock)