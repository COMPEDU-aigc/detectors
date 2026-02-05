
import json 
from ..base  import BaseRequest


class Imp(BaseRequest):
    
    def __init__(self, ): 
        
        # curl -X POST http://155.69.146.109:51031/predictions/gpt2_detector -T   /tmp/a.txt
        # url = "http://155.69.146.109:51031/predictions/gpt2_detector"
        # url = "http://155.69.150.9:42250/predictions/gpt2_detector"
        url = "http://10.96.186.98:50421/predictions/gpt2_detector"
        self.url1 = url 
        url = "http://10.96.186.98:50421/predictions/gpt2_detector"

        # url = "http://10.96.183.249:61050/predictions/gpt2_detector"
        self.url2 = url 
        # curl -X POST http://10.96.187.160:41039/predictions/gpt2_detector -T   /tmp/a.txt 

        super(Imp, self).__init__(url=url,proxies=None )
        # self.
        
        self.headers .update({
            # 'content-type':'application/x-www-form-urlencoded; charset=UTF-8',
            # 'Origin': 'https://app.copyleaks.com',
            # 'Referer': 'https://app.copyleaks.com/v1/scan/ai/embedded',
            # 'X-Requested-With': 'XMLHttpRequest',
            # "Authority": "app.copyleaks.com",
            })

        self.method = "POST"
        
#         {
#   "label": "Real",
#   "prob": 0.77068692445755
# }%   
    def __call__(self, text ):
        import random 
        if random.randint(0,2)==1:
            self.url = self.url1 
        else :
            self.url = self.url2

        if text is None or len(text) <=0 :
            return self.format(content=None)

        # json_data = {"data":text, }
        # kwargs = {'data': json.dumps(json_data) }
        text = text.encode("utf-8")

        return super(Imp, self).__call__( data=text  )

    def format(self,content  ):
        # print (content)
        if content is None :
            return {
                "result": -1 ,
                "probability":None  ,
                "raw":None,
                }

        content = content.decode() if type(content) !=str else content 
        content = json.loads(content)
        
        # if "content" =="Accepted":
        #     result="real"
        #     probability="1"
        # else:
        #     result="fake"
        #     probability="0"
        #

        probability = content ["prob"]
        return {
            "result":1 if content["label"]=="Fake" else 0 , #"real" "fake"
            "probability":probability ,
            "raw":content,

            }
