
import json 
from ..base  import BaseRequest


class Imp(BaseRequest):
    
    def __init__(self, ): 
        
        # curl -X POST http://155.69.146.109:51031/predictions/gpt2_detector -T   /tmp/a.txt
        # url = "http://155.69.146.109:51031/predictions/gpt2_detector"
        # url = "http://155.69.150.9:42250/predictions/gpt2_detector"
            # "http://155.69.146.223:40300/predictions/t5_generation",
        url = [
            "http://155.69.146.109:61050/predictions/t5_generation",
            "http://155.69.146.109:61050/predictions/t5_generation",
            "http://155.69.146.109:61050/predictions/t5_generation1",
            "http://155.69.150.9:42250/predictions/t5_generation",
            "http://155.69.150.9:42250/predictions/t5_generation",
            "http://155.69.150.9:42250/predictions/t5_generation",
            "http://155.69.150.9:42250/predictions/t5_generation",
            "http://127.0.0.1:8000/predictions/t5_generation",
            ]
        # url = [
        #     "http://155.69.150.9:42250/predictions/t5_generation",
        #     "http://155.69.150.9:42250/predictions/t5_generation",
        #     "http://155.69.150.9:42250/predictions/t5_generation",
        #     "http://155.69.150.9:42250/predictions/t5_generation",
        #     "http://127.0.0.1:8000/predictions/t5_generation",
        #     ]

        self.url_list = url 

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
        x_len = random.randint(0, len(self.url_list)-1 )
        self.url  = self.url_list[x_len]
        
        text = text.encode("utf-8")
        text = text[:1000]

        ret_list =  super(Imp, self).__call__( data=text  )
        
        ret = {
            "raw":text ,
            "mutate_list":ret_list , 
            }
        return ret
        

    def format(self,content  ):
        # print (content)
        content = content.decode() if type(content) !=str else content 
        content = json.loads(content)
        return content 
        #
        # # if "content" =="Accepted":
        # #     result="real"
        # #     probability="1"
        # # else:
        # #     result="fake"
        # #     probability="0"
        # #
        #
        # probability = content ["prob"]
        # return {
        #     "result":1 if content["label"]=="Fake" else 0 , #"real" "fake"
        #     "probability":probability ,
        #     "raw":content,
        #
        #     }
