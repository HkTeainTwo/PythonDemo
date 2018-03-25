#!/usr/bin/python
#-*- coding: utf-8 -*-

import socket

host = "127.0.0.1"
port = 843
addr = host,port
policyFile = "<?xml version='1.0' ?><cross-domain-policy><allow-access-from domain='*'/></cross-domain-policy>"

print "policy server"
print "安全策略服务器"

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(addr)
server.listen(999)

while True:
    clientSock,addrs = server.accept()

    print "client ip:" + str(addrs[0])
    print "client port:" + str(addrs[1])

    data = clientSock.recv(2000)
    if "policy-file-request" in data:
        clientSock.send(policyFile)
    clientSock.close()