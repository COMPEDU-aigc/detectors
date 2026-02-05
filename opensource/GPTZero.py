
import json 
from ..base  import BaseRequest


class Imp(BaseRequest):
    
    def __init__(self, ): 
        
        # curl -X POST http://155.69.146.109:51031/predictions/gpt2_detector -T   /tmp/a.txt
        url = "http://10.96.187.160:41039/predictions/gptzero"
        url = "http://10.96.186.98:50421/predictions/gptzero"
        url = "http://127.0.0.1:8000/predictions/gptzero"

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
        
    def __call__(self, text ):
        # json_data = {"data":text, }
        # kwargs = {'data': json.dumps(json_data) }
        text = text.encode("utf-8")

        return super(Imp, self).__call__( data=text  )

    def format(self,content  ):
# {
#   "Perplexity": 47,
#   "Perplexity per line": 295.1111111111111,
#   "Burstiness": 898,
#   "label": 1,
#   "label_text": "The Text is written by Human.",
#   "id": "273e2dff-7a54-4766-8520-69f60ed392ae"
# }% 
        print (content)
        content = content.decode() if type(content) !=str else content 
        content = json.loads(content)
        

        # probability = content ["prob"]
        return {
            "result": 1-content["label"] ,
            "probability":None ,
            "raw":content,
            }
