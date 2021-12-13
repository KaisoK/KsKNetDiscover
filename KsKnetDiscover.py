from netaddr import *
import os, sys
import subprocess
from multiprocessing import Queue


def discover(subnet):
    print(' =================================================')
    print('       [!] Starting network Scan to %s            ' % str(subnet))  
    print(' =================================================')
    hosts_up = Queue()
    for host in IPNetwork(subnet):
        test = 'ping -c 1 -w2 %s >> /dev/null' % host
        #response,result = subprocess.run([test])

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


subnet = sys.argv[1]

discover(subnet)
