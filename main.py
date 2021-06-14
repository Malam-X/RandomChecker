# TNA - BlackHat Hacking Team

import sys, subprocess, socket, httplib, threading, re
from time import sleep
import random as ran
 
timeout = 5
socket.setdefaulttimeout(timeout)
port = int(80)
num_threads = 5
 
def logo():
    print('\n RANDOM CHECKER \n By DR4G0N5 - TNA \n')
   
if sys.platform == 'linux' or sys.platform == 'linux2':
    subprocess.call("clear", shell=True)
    logo()
else:
    subprocess.call("cls", shell=True)
    logo()
     
if len(sys.argv) not in [3,4]:
    print "[!] Usage: python main.py -random NUM"
    print "[!] Example : python main.py -random 10000"
    print "[!] Usage: python main.py -iprange RANGE"
    print "[!] Example: python main.py -iprange 192.168.1.1-255"
    sys.exit(1)
   
 
def randomIP():
    ran1 = ran.randrange(255) + 1
    ran2 = ran.randrange(255) + 1
    ran3 = ran.randrange(255) + 1
    ran4 = ran.randrange(255) + 1
    randIP = "%d.%d.%d.%d" % (ran1, ran2, ran3, ran4)
    return randIP
 
def getrange(iprange): 
    lst = [] 
    iplist = [] 
    iprange = iprange.rsplit(".",2) 
    if len(iprange[1].split("-",1)) ==2: 
            for i in range(int(iprange[1].split("-",1)[0]),int(iprange[1].split("-",1)[1])+1,1): 
                    lst.append(iprange[0]+"."+str(i)+".") 
            for ip in lst: 
                    for i in range(int(iprange[2].split("-",1)[0]),int(iprange[2].split("-",1)[1])+1,1): 
                            iplist.append(ip+str(i)) 
            return iplist 
    if len(iprange[1].split("-",1)) ==1: 
            for i in range(int(iprange[2].split("-",1)[0]),int(iprange[2].split("-",1)[1])+1,1): 
                    iplist.append(iprange[0]+"."+str(iprange[1].split("-",1)[0])+"."+str(i)) 
            return iplist 
 
def srvscan(lock, ip):
    try:
        if ran != 0:
            lock.acquire()
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, port))
        s.close()
        srvcheck(ip)
    except:
        pass
     
    if ran != 0:
        lock.release()
     
def srvcheck(ip):
    conn = httplib.HTTPConnection(ip, port)
    try:
        conn.request("HEAD", "/")
    except socket.timeout:
        print "\n[-] Server Timeout", ip
    except(KeyboardInterrupt, SystemExit):
        print "[!] Now exiting, thx for using this script!"
        sys.exit(1)
    r1 = conn.getresponse()
    conn.close()
    server = r1.getheader('Server')
    xpoweredby = r1.getheader('x-powered-by')
    date = r1.getheader('date')
     
    if xpoweredby == None:
        print "\n[+] Ip of server: "+ip
        print "[+] Server info: "+server
        print "[+] Server date: "+date
 
    else:
        print "\n[+] Ip of server: "+ip
        print "[+] Server info: "+server
        print "[+] Xpoweredby: "+xpoweredby
        print "[+] Server date: "+date
         
    if server:
        if re.search("microsoft", server.lower()):
            print "\t[!] IIS Found"
            webdav(ip)
         
        if re.search("apache", server.lower()) or re.search("a p a c h e", server.lower()):
            print "\t[!] Apache Found"
             
        if re.search("akamaighost", server.lower()):
            print "\t[!] AkamaiGHost Found"
             
        if re.search("nginx", server.lower()):
            print "\t[!] Nginx Found"
             
        if re.search("micro_httpd", server.lower()):
            print "\t[!] Micro_httpd Found"
             
        if re.search("plesklin", xpoweredby.lower()):
            print "\t[!] PleskLin Found"
             
        if re.search("cisco", server.lower()):
            print "\t[!] Cisco Found"
             
        if re.search("ipoffice", server.lower()):
            print "\t[!] IPOffice Found"
             
        if re.search("uc-httpd", server.lower()):
            print "\t[!] Uc-httpd Found"
             
        if re.search("rompager", server.lower()):
            print "\t[!] RomPager Found"
             
        if re.search("net-dk", server.lower()):
            print "\t[!] NET-DK Found"
             
        if re.search("mini_httpd", server.lower()):
            print "\t[!] Mini httpd Found"
             
        if re.search("sonicwall", server.lower()):
            print "\t[!] SonicWALL Found"
             
        if re.search("realtron", server.lower()):
            print "\t[!] Realtron WebServer Found"
             
        if re.search("goahead-webs", server.lower()):
            print "\t[!] GoAhead-Webs"
             
        if re.search("nyob", server.lower()):
            print "\t[!] NYOB Found"
             
def webdav(ip):
    print "[!] Checking for Web Dav exploit!\n"
    req = "OPTIONS / HTTP/1.1\r\n"
    req += "Host: " + ip + "\r\n"
    req += "Connection: close\r\n"
    req += "\r\n\r\n"
    print req
    s.send(req)
    data = s.recv(1024)
    s.close()
    r1 = re.compile('DAV')
    result = r1.findall(data)
    if result == []:
        print "[-] Sorry, Web Dav is not open!"
    else:
        print "[!] Web Dav Open!"
        return None
     
for arg in sys.argv[1:]:
    if arg.lower() == "-iprange":
        iprange = sys.argv[int(sys.argv[1:].index(arg))+2]
    if arg.lower() == "-random":
        number = sys.argv[int(sys.argv[1:].index(arg))+2]
         
         
try:
    if iprange:
        iplist = getrange(iprange)
        print "[!] Range Loaded:", iprange
except(NameError):
    iprange = 0
    pass
except(IndexError):
    print "[-] Misconfigured IPRANGE"
    sys.exit(1)
     
try:
    if number:
        print "[!] There is %s random IP for scan" % number
        number = int(number)
except(NameError):
    number = 0
    pass
 
                        
if __name__ == "__main__":
    print "[!] Port for checking: %s" % str(port)
    print "[!] Max. number of threads: %s" % num_threads
    print "[!] Let's start ...\n"
     
    if iprange != 0:
        for ip in iplist:
            #print "[!] Testing:", ip
            lock = threading.Lock()
            srvscan(lock, ip)
         
    if ran != 0:
        while number >= 0:
            for x in xrange(num_threads):
                lock = threading.Lock()
                threading.Thread(target = srvscan, args=(lock, randomIP())).start()
                sleep(1)
                number -= 1
        sleep(1)
     
    print "\n[!] Scanning finished!"
    sys.exit(1)
