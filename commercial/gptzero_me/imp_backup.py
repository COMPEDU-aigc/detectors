
import json 
from ..base  import BaseRequest
from ..utils import api_call 

import pandas as pd 
import numpy as np 

import random 
import os 

# from io import StringIO
import io 
import requests 
import string 
import copy 

cur = os.path.dirname(__file__)
class Imp(BaseRequest):
    
    def __init__(self, ): 
        
        url = "https://api.gptzero.me/v2/predict/text"
        super(Imp, self).__init__(url=url )
        # self.
        
        self.cookies={"accessToken":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJhdXRoZW50aWNhdGVkIiwiZXhwIjoxNjc4MjY0MTIzLCJzdWIiOiIxN2M1MTJkZi0wYzg2LTQzMmEtOWU3Ni0wZjc5N2E4MjM1NzciLCJlbWFpbCI6InJlY2V0ZXk4OTBAd2lyb3V0ZS5jb20iLCJwaG9uZSI6IiIsImFwcF9tZXRhZGF0YSI6eyJwcm92aWRlciI6ImVtYWlsIiwicHJvdmlkZXJzIjpbImVtYWlsIl19LCJ1c2VyX21ldGFkYXRhIjp7ImVtYWlsIjoicmVjZXRleTg5MEB3aXJvdXRlLmNvbSIsImZ1bGxfbmFtZSI6InJlY2V0ZXk4OTAiLCJvcmciOiIifSwicm9sZSI6ImF1dGhlbnRpY2F0ZWQiLCJhYWwiOiJhYWwxIiwiYW1yIjpbeyJtZXRob2QiOiJwYXNzd29yZCIsInRpbWVzdGFtcCI6MTY3NzY1OTMyM31dLCJzZXNzaW9uX2lkIjoiOGJkMmFhMzktNDlmMi00ZGE0LWFlMGItZmM3ZTkyZTZjZGE1In0.thnop7Mbp9kCLC17q4I8ikDZkuOKk1bIopA8NjwXENQ"}
        
        self.headers .update({
            # 'content-type': 'application/json' ,

            # 'content-type':'application/x-www-form-urlencoded; charset=UTF-8',
            'Origin': 'https://app.gptzero.me',
            'Referer': 'https://app.gptzero.me',
            # 'X-Requested-With': 'XMLHttpRequest',
            "Authority": "api.gptzero.me",
            })

        self.method = "POST"
        
        self.rate_limit = api_call.RateLimit(rate_limit=40, window_size=60, func_name="gptzero.me")
        
        with open(os.path.join(cur, "login", "token_activate.list.jsonl") ) as f :
            lines = f.readlines()
            data= [json.loads(line ) for line in lines ]
        
        
        self.account_list  =data  
        # self.access_token =  np.random.choice( self.account_list )["accessToken"]
    
    def _get_accessToken(self):
        cookies =None 
        for i in range(4):
            account_info_i  =random.randint(0,len( self.account_list)-1 ) 
            # print ("account_info_i", account_info_i, "-->", len( self.account_list) )
            account_info = self.account_list[account_info_i]
            # access_token = account_info["cookies"]["sb-access-token"]
            access_token = account_info["cookies"]["sb-access-token"]
            email  = account_info["email"]
            cookies = {
                # "accessToken":access_token,
                "accessToken4":access_token,
            }
        
            flag = self.rate_limit.limit(account_id =email )
            if flag :
                return cookies 
        # even use up, return     
        return cookies 



    def __call__(self, text ):
        # _= self.headers.pop('Content-Type',None)
        # print ("text", text )
        text = text[:20000-500]
        json_data = {"document":text, }
        cookies = self._get_accessToken ()

        try :
            response = self.__call_imp__( data=json.dumps(json_data) ,cookies=cookies  )
            content = response.content 
            print ("response.text", response.status_code)
            return self.format(content =content,flag="response.text" )
        except requests.exceptions.HTTPError as ex :
            print ("ex->", str(ex) )
            if "403 Client Error" in str(ex) :
                try :
                    response=  self.__call_file__( text ,cookies )
                    content = response.content 
                    print ("response.file", response.status_code)
                    return self.format(content =content,flag="response.file" )

                except requests.exceptions.HTTPError as ex :
                    print ("ex->", str(ex) )
                    return None 
        return None 

                

    def __call_file__(self, text ,cookies ):
        ex_url = self. url
        ex_header = copy.deepcopy( self. headers )
        _= self.headers.pop('Content-Type',None)
        self.url = 'https://api.gptzero.me/v2/predict/files'
        filename = ''.join(random.sample(string.ascii_letters + string.digits, 16))
        filename = filename+".txt"
        # print ("filename", filename)
        files = {'files': (filename, str(text), 'text/plain')}
        data = {'writing_stats_required': True }

        response= self.__call_imp__(files=files, data=data , cookies=cookies)

        # content = response.content 
        self. url = ex_url 
        self.headers.update(ex_header)
        return response 
    
    def __call_imp__(self, **kwargs):
    
        response = requests.post (self.url ,
                                proxies=self.proxies,
                                headers= self. headers, 
                                timeout =self.timeout, 
                                **kwargs )
        # print (response.request.headers )
        response.raise_for_status()
        # print ("response", response.status_code)
        # return response.content
        return response





    def format(self,content,flag=None  ):
        # print (content)
        # raise Exception("stop ")
        if content is None :
            return content
        
        content = content if type(content)==str else content.decode()
        # print (content , "b.content " )
        info_raw = json.loads(content )
        info = info_raw ["documents"][0]
        
        # classification==1 --> human 
        # classification==2  --> ai 
        
        result =1 if  info["average_generated_prob"]>0.8 else 0
        probability = info ["average_generated_prob"]
        return {
            "result":result, #"real" "fake"
            "probability":probability ,
            "flag":flag,
            "raw_response":info_raw,
            }
