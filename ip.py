# -*- coding: utf-8 -*-
import socket
import requests

def getip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('1.2.4.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    msg = ("当前IP：" + ip)
    url = 'http://www.pushplus.plus/send?token=27e55baa41434cb9a07b6cfea2696044&content={}&template=markdown'.format(msg)
    reqp = requests.get(url)


if __name__ == "__main__":
    getip()
