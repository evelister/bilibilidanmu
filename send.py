import time
import random
import requests
import json
api_key = 'face79da40a04027ad3d48257e548113'  


class SendLiveRoll():
    def __init__(self, roomid=None):
        self.roomid = roomid
        self.url = 'https://api.live.bilibili.com/ajax/msg'
        self.url2 = 'https://api.live.bilibili.com/msg/send'

        self.cookie = {'Cookie': '这里是cookie'}
        self.header = {'User-Agent': '这里是header'}

        self.data = {
            'roomid': self.roomid,
            'csrf_token': '0dfb974246881bbd222a58a5cdd8b01c',
            'visit_id': '697v0isf7xg0'
        }

    def getLiveRoll(self):
        html = requests.post(self.url, data=self.data)
        danmus = list(map(lambda ii: html.json()['data']['room'][ii]['text'], range(10)))
        self.msg = random.choice(danmus)
        print(self.msg)

    def sendLiveRoll(self):
        #self.msg = msg
        data = {
            'color': 65532,
            'fontsize': 25,
            'mode': 1,
            'msg': self.msg,
            'rnd': 1530953623,
            'roomid': self.roomid,
            'csrf_token': '0dfb974246881bbd222a58a5cdd8b01c'
        }
        html = requests.post(self.url2, data=data, cookies=self.cookie, headers=self.header)

    def tuling(self):
        url = 'http://www.tuling123.com/openapi/api?key='+api_key+'&info='+self.msg
        res = requests.get(url)
        res.encoding = 'utf-8'
        jd = json.loads(res.text)
        print(jd['text'])
        self.msg = jd['text']


if __name__ == "__main__":
    sendliveroll = SendLiveRoll(3643062)
    sendliveroll2 = SendLiveRoll()
    for a in range(1000):
        sendliveroll.getLiveRoll()
        sendliveroll.tuling()
        sendliveroll.sendLiveRoll()
        # sendliveroll2.getLiveRoll()
        # sendliveroll2.tuling()
        # sendliveroll2.sendLiveRoll()
        time.sleep(60)




