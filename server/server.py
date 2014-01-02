# -*- coding: utf-8 -*-


#id,name,pass,friends,offmsgs

#online list
#id,ip,loginTime

#server 
#types 登录，退出，注册，增，删好友，

 
import socket, traceback
from consolofun import show  
host = ''
port = 54321
  
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))

onUdic={}
class recvHander(object):
       def __init__(self):
          
       def run(self):
           
class onlineUser(object):
    def __init__(self,id,ip,time):
        self.id=id
        self.ip=ip
        self.time=time
while 1:
    try:
        message, address = s.recvfrom(8192)
        print "Got data from", address, ": ", message
        s.sendto(message, address)
    except (KeyboardInterrupt, SystemExit):
        raise
    except:
         traceback.print_exc()
def main(self):
    while 1:
      print 'minro>:)'
      cmd = sys.stdin.readline().strip()
      if cmd == 'show':

if __name__=="__main__":
     main()
    
