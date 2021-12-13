#!/usr/bin/env python3

import multiprocessing
import subprocess
import os


subprocess.run("clear")
print("-----DesoDeCalamareV2-----\n\n")

a = input("Select ip and subnet to start de scan (Ex: 0.0.0.0/24)\n\n-- ")

def churumbel( job_q, results_q ):

    DEVNULL = open(os.devnull,'w')

    while True:

        ip = job_q.get()

        if ip is None: break

        try:

            subprocess.check_call(['ping','-c1',ip],stdout=DEVNULL)
            results_q.put(ip)

        except:

            pass

separador = ".".join(a.split('.')[0:-1]) + '.'

if __name__ == '__main__':

    pool_size = 255

    jobs = multiprocessing.Queue()
    results = multiprocessing.Queue()

    pool = [ multiprocessing.Process(target=churumbel, args=(jobs,results)) for i in range(pool_size) ]

    for p in pool:
        p.start()

    for i in range(1,255):
        jobs.put(separador + '{0}'.format(i))
        
    for p in pool:
        jobs.put(None)

    for p in pool:
        p.join()

    while not results.empty():
        ip = results.get()
        print(ip)
