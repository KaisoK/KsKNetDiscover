from netaddr import *
from multiprocessing import Queue, Process
import os, sys, subprocess, requests, socks, socket, ipaddress

#Hosts Discover

subprocess.run("clear")
print("-----DesoDeCalamare-----\n\n")

a = input("Select ip and subnet to start de scan (Ex: 0.0.0.0/24)\n\n-- ")

def NetDiscover(min, max):
    print(min, max)
    return False
    subnet = min, max

    print(' =================================================')
    print('       [!] Starting network Scan to %s            ' % str(subnet))  
    print(' =================================================')
    hosts_up = Queue()
    for host in IPNetwork(subnet):
        test = 'ping -c 1 -w2 %s >> /dev/null' % host

        response = os.system(test)
        if response == 0:
            print(' |   [!] Host %s is UP' % host)
            hosts_up.put(host)
        else:
            print(' |   [x] Host %s not avaliable' % host)
            pass
    print('')
    print(' =================================================')
    print('                [*] LIVE HOSTS                   ')
    print(' =================================================')
    while not hosts_up.empty():
        up = hosts_up.get()
        print('[+] %s ' % up)
        
#Multiprocessing
    
ip = ".".join(a.split('.')[0:-1]) + '.'
print(ip)

ListaIp = ["0", "64", "129", "193", "255"]
if __name__ == "__main__":
    
    procs = []
    q = Queue()
    for i in range(4):
        proc = Process(target=NetDiscover, args=(ip+ListaIp[i],ip+ListaIp[i+1]))
        procs.append(proc)

    for proc in procs:
        proc.start()

    for proc in procs:
        proc.join() 
