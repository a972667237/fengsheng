from django.shortcuts import render, HttpResponse
import json
from ws4py.client.threadedclient import WebSocketClient
# Create your views here.
def getInfo(requests):
    getter = DummyClient("ws://47.52.108.234:1234?uid=602751&subscribe=1&ticks=636371924886132812&stock=&key=e7f518fabdf79fb873cae779ae033f7f", protocols=['chat'])
    getter.connect()
    getter.run_forever()
    result = {
        'code': '1',
        'all_info': getter.info
    }
    return HttpResponse(json.dumps(result), content_type="application/json")


class DummyClient(WebSocketClient):
    info = {}
    def opened(self):
        pass

    def closed(self, code, reason=None):
        pass

    def received_message(self, m):
        m = str(m)
        if m[0] is not '{':
            return
        m = json.loads(m)
        result = m['sb']
        for i in result:
            self.info[i['n']] = i['v']
            if len(self.info.keys()) == 7:
                self.close()