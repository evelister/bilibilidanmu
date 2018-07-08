import time
import random
import requests
import json
api_key = 'face79da40a04027ad3d48257e548113'#  984d9317b01041f188e571a83986f81d


class SendLiveRoll():
    def __init__(self, roomid=None):
        self.roomid = roomid
        self.url = 'https://api.live.bilibili.com/ajax/msg'
        self.url2 = 'https://api.live.bilibili.com/msg/send'

        self.cookie = {'Cookie': 'sid=li5j0m08; fts=1510365008; pgv_pvi=4303372288; rpdid=kwkwolisosdosowkxpqqw; LIVE_BUVID=29ce9d5374684a9cbb265a1014adb2dc; LIVE_BUVID__ckMd5=591cb6867ac978b6; buvid3=50F0CE61-B9F4-4DD3-82FC-AF87B14A4BBF31060infoc; Hm_lvt_9e2a88dc69e0e55c353597501d2a4bbc=1518526593; UM_distinctid=16363840388e2-00fc42ac740147-5b44271d-144000-163638403892e7; im_local_unread_5104114=0; im_seqno_5104114=2345; finger=edc6ecda; _cnt_dyn=undefined; _cnt_pm=0; _cnt_notify=0; uTZ=-480; BANGUMI_SS_23858_REC=200172; im_notify_type_5104114=0; CURRENT_QUALITY=80; BANGUMI_SS_24589_REC=231887; BANGUMI_SS_24571_REC=231926; BANGUMI_SS_24572_REC=231938; BANGUMI_SS_24567_REC=232169; BANGUMI_SS_24611_REC=232235; BANGUMI_SS_6012_REC=102951; BANGUMI_SS_5978_REC=202722; BANGUMI_SS_6260_REC=108850; stardustvideo=0; BANGUMI_SS_24625_REC=232407; _dfcaptcha=f4fd278e349104f4e80879e19b5edd66; BANGUMI_SS_22087_REC=232069; LIVE_PLAYER_TYPE=1; DedeUserID=5104114; DedeUserID__ckMd5=29fe08fdfef0bfb1; SESSDATA=7454bc76%2C1533544115%2Cb92fd689; bili_jct=0dfb974246881bbd222a58a5cdd8b01c; bp_t_offset_5104114=137927097981913870; Hm_lvt_8a6e55dbd2870f0f5bc9194cddf32a02=1530951954,1530951996,1530952121,1530952581; Hm_lpvt_8a6e55dbd2870f0f5bc9194cddf32a02=1530954482'}
        self.header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}

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
    sendliveroll2 = SendLiveRoll(16405)#8334996
    for a in range(1000):
        sendliveroll.getLiveRoll()
        sendliveroll.tuling()
        sendliveroll.sendLiveRoll()
        # sendliveroll2.getLiveRoll()
        # sendliveroll2.tuling()
        # sendliveroll2.sendLiveRoll()
        time.sleep(8)




