
import json 
from ..base  import BaseRequest


import nltk
import string



class Imp(BaseRequest):
    
    def __init__(self, ): 
        
        url = "https://api.sapling.ai/api/v1/aidetect"
        super(Imp, self).__init__(url=url )
        # self.
        
        self.headers .update({
            'content-type':'application/x-www-form-urlencoded; charset=UTF-8',
            'Origin': 'https://www.scribbr.com',
            'Referer': 'https://www.scribbr.com/',
            # 'X-Requested-With': 'XMLHttpRequest',
            # "Authority": "detectgpt.ericmitchell.ai",
            })

        self.method = "POST"
        
    def __call__(self, text ):
        # text_list = nltk.word_tokenize(text)
        # text_list = text_list[:200
        # text = "".join([" "+i if not i.startswith("'") and i not in string.punctuation else i for i in text_list]).strip()
        text = text[:2000]
        ## the website mondatory ask under 256 token 
        json_data = {"text":text, }
        # kwargs = {'data': json.dumps(json_data) }

        return super(Imp, self).__call__( data=json.dumps(json_data) )

    def format(self,content  ):
        # print (content)
        
        '''
{
  "message": "ai content detection successfully",
  "traceID": "2731314140776280833",
  "code": "AI_CONTENT_DETECTION_SUCCESS",
  "data": {
    "modelID": "ai-writer-detector-v1.0",
    "scores": {
      "fake": 0.0002,
      "real": 0.9998
    }
  },
  "status": 200,
  "flags": {
    "sessExT": "2023-09-20T05:52:44.978Z"
  }
}
        '''
        import json 
        content = content if type(content)==str else content.decode()
        # print (content , "b.content " )
        info = json.loads(content )
        if "status" in info and str(info ["status"])=="200":
        
            # classification==1 --> human 
            # classification==2  --> ai 
            
            result =1 if  info ["data"]["scores"]["fake"]>0.5 else 0
            probability = info ["data"]["scores"]["fake"]
        else:
            raise Exception("error in return ")
            result = -1 
            probability = None 
        
        return {
            "result":result, #"real" "fake"
            "probability":probability ,
            "raw_result":info,
            }
