
import json 
from ..base  import BaseRequest

# from nltk.tokenize.treebank import TreebankWordDetokenizer
import nltk
import string



class Imp(BaseRequest):
    
    def __init__(self, ): 
        
        # curl -X POST http://155.69.146.109:51031/predictions/gpt2_detector -T   /tmp/a.txt
        url = "http://155.69.146.109:51049/predictions/detect_gpt"
        self.url1 = url 
        url = "http://155.69.150.9:42250/predictions/detect_gpt"
        self.url2 = url 

        
        super(Imp, self).__init__(url=url,proxies=None )
        # self.
        
        self.method = "POST"
#         {
#   "req_id": "2ad0cd73-fb2a-43d6-a37a-1081886779d9",
#   "prob": "73.47%",
#   "label": 0
# }%  
    def __call__(self, text ):
        # json_data = {"data":text, }
        # kwargs = {'data': json.dumps(json_data) }
        import random 
        if random.randint(0,1)==1:
            self.url = self.url1 
        else :
            self.url = self.url2
        
        
        text_list= nltk.word_tokenize(text)
        tokens = text_list[:250]
        text= "".join([" "+i if not i.startswith("'") and i not in string.punctuation else i for i in tokens]).strip()
        
        # print ("text", text )
        
        text = text.encode("utf-8")

        return super(Imp, self).__call__( data=text  )

    def format(self,content  ):
        print (content)
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
        probability = probability.replace("%","")
        probability = float(probability)/100
        return {
            "result": content["label"],
            "probability":probability ,
            }
