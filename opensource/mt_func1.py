
import json 
from ..base  import BaseRequest


class Imp(BaseRequest):
    
    def __init__(self, ): 
        
        # curl -X POST http://155.69.146.109:51031/predictions/gpt2_detector -T   /tmp/a.txt
        # url = "http://155.69.146.223:40300/predictions/simpleai_qa"
        # url = "http://127.0.0.1:8000/predictions/simpleai_qa"
        # url = "http://155.69.150.9:42250/predictions/simpleai_qa"
        # self.url1 = url 
        # url = "http://155.69.146.223:40300/predictions/simpleai_qa"
        # self.url2 = url 

        # url = "http://155.69.146.109:51049/predictions/simpleai"
        # url = "http://10.96.187.160:41039/predictions/simpleai_qa"
        # self.url1 = url 
        # url = "http://10.96.187.160:41039/predictions/simpleai_qa"
        # self.url2 = url 
        url = "http://127.0.0.1:8000/predictions/see4231_saved_models_extract_rm_languagemodel"
        self.url1 = url 
        url = "http://10.96.183.249:61050/predictions/see4231_saved_models_extract_rm_languagemodel"
        self.url2 = url 

        
        
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
        
    # def __call__(self, text ):
    #     # json_data = {"data":text, }
    #     # kwargs = {'data': json.dumps(json_data) }
    #     import random 
    #     if random.randint(0,1)==1:
    #         self.url = self.url1 
    #     else :
    #         self.url = self.url2
    #
    #
    #     text = str(text).encode("utf-8")
    #     print ("test--->",text ,type(text))
    #
    #     return super(Imp, self).__call__( data=text  )
    #
    # def format(self,content  ):
    #     print (content)
    #     content = content.decode() if type(content) !=str else content 
    #     content = json.loads(content)
    #
    #
    #     probability = content ["prob"]
    #     return {
    #         "result":1 if content["label"]=="chatgpt" else 0 , #"real" "fake"
    #         "probability":probability ,
    #                     "raw":content,
    #
    #         }
    def __call__(self, text ):
        # json_data = {"data":text, }
        # kwargs = {'data': json.dumps(json_data) }
        import random 
        if random.randint(0,1)==1:
            self.url = self.url1 
        else :
            self.url = self.url2

        if text is None or len(text) <=0 :
            return self.format(content=None)

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
        

        probability = content ["prob"]
        return {
            "result":1 if content["label"]=="chatgpt" else 0 , #"real" "fake"
            "probability":probability ,
            "raw":content,
            }

