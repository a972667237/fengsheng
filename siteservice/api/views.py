from django.shortcuts import render, HttpResponse
import json
import socket

# Create your views here.
def getInfo(requests):
    getter = infoGetter()
    result = {
        'code': '1',
        'all_info': getter.get()
    }
    return HttpResponse(json.dumps(result), content_type="application/json")

class infoGetter:
    def __init__(self):
        self.host = '121.40.248.45'
        self.port = 7782
        self.message = "0=dy|1=1000|5={}\n"
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.host, self.port))
    def get(self):
        result = {}
        aim_list = ["LLSsp9", "Oilsp8RMB", "LLSsp9RMB", "Oilsp9", "DC_OKCoin", "DC_OKCoin_MN"]
        for i in aim_list:
            commond = self.message.format(i)
            try:
                self.socket.sendall(commond)
                recv = self.socket.recv(4096)
                print (recv)
            except:
                result[i] = "error"
        self.socket.close()
        return result

