# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 21:45:45 2013

@author: NotMark
"""

import socket

sock = socket.socket()

host = socket.gethostname()

port = 1010

sock.bind((host, port))

sock.listen(5)

while True:
    conn, addr = sock.accept()
    print 'Connection established with ', addr
    conn.send('Welcome to Ishymouse')
    
    conn.close()