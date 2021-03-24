from ..backends.wecom import WeCom


class Client:
    def __init__(self):
        corpid = 'ww918354e3468dc0cc'
        corpsecret = 'Dq-Gjv1GiqsoLcGfIqCJeVKH2j69eBZsP92P3LzgX3s'
        agentid = '1000002'
        self.wecom = WeCom(corpid=corpid, corpsecret=corpsecret, agentid=agentid)

    def send_msg(self, users, msg):
        self.wecom.send_text(users, msg)
