
import json 
from ..base  import BaseRequest


class Imp(BaseRequest):

    def __init__(self, ): 

        url = "https://api.originality.ai/api/v2-tools/free-tools/ai-scan"
        super(Imp, self).__init__(url=url )
        # self.

        self.headers .update({
            # 'content-type':'application/x-www-form-urlencoded; charset=UTF-8',
            'Content-Type': 'application/json',
            # 'content-type':'application/x-www-form-urlencoded; charset=UTF-8',

            # 'Origin': 'https://api.sapling.ai',
            'Referer': 'https://tools.originality.ai',
            'Origin': 'https://tools.originality.ai',
            # 'X-Requested-With': 'XMLHttpRequest',
            "Authority": "api.originality.ai",
            })

        self.method = "POST"

    def _safe_str (self,text):
        return json.dumps( text.replace("\n","") )
    def __call__(self, text ):
        text = self._safe_str(text[:20000])
        json_data = {"content":text, }
        # try :
        return super(Imp, self).__call__( data=json.dumps(json_data) )
            # return super(Imp, self).__call__( data=json_data )
        # except :
        #     print (text )

    def format(self,content  ):
        # print (content)

        '''
{
    "score": 0.000002231274809805228,

}        

        '''
        import json 
        content = content if type(content)==str else content.decode()
        # print (content , "b.content " )
        info = json.loads(content )

        # classification==1 --> human 
        # classification==2  --> ai 

        result =1 if  info["ai"]>0.5 else 0 
        probability = info ["ai"]
        return {
            "result":result, #"real" "fake"
            "probability":probability ,
            "raw_response":info,
            }
