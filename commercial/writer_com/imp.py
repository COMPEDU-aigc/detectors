
import json 
from ..base  import BaseRequest

import nltk
import string

class Imp(BaseRequest):
    
    def __init__(self, ): 
        
        url = "https://writer.com/wp-admin/admin-ajax.php"
        super(Imp, self).__init__(url=url )
        # self.
        
        self.headers .update({
            'content-type':'application/x-www-form-urlencoded; charset=UTF-8',
            'Origin': 'https://writer.com',
            'Referer': 'https://writer.com/ai-content-detector/',
            'X-Requested-With': 'XMLHttpRequest',
            "Authority": "writer.com",
            })

        self.method = "POST"
        
    def __call__(self, text ):

        text = text.replace("\n","")
        # text_list = nltk.word_tokenize(text)
        # text_list = text_list[:128]
        # text = "".join([" "+i if not i.startswith("'") and i not in string.punctuation else i for i in text_list]).strip()
        c_chunk = [512,450,300,200 ]
        for ck in c_chunk:
            text_x = text[:ck]
            info  = None 
            try :
                json_data = {
                    "inputs":text_x,"token":None, "action":"ai_content_detector_recaptcha"}
                info =  super(Imp, self).__call__( data=json_data )
                # print (len(text), "text")
            except :
                continue 
                
            
            return info 
        
    def format(self,content  ):
        
        '''
[{"label":"LABEL_0","score":0.8563475608825684},{"label":"LABEL_1","score":0.14365245401859283}]

        '''
        import json 
        content = content if type(content)==str else content.decode()
        info = json.loads(content )
        
        if "error" in info :
            raise json.JSONDecodeError(str(info), "", 0 )
        # print (content)
        info2 = { }
        for item in info :
            info2[ item["label"]]= item["score"]
            
        # print (info2,"info2") 
        # LABEL_0== robot 
        # LABEL_1== human 
        
        result =0 if  info2["LABEL_1"]>0.5 else 1
        probability = info2["LABEL_0"] 
        return {
            "result":result, #"real" "fake"
            "probability":probability ,
            "raw_result":info,
            }
