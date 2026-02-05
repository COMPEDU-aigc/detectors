
import json 
from ..base  import BaseRequest
from ..utils import api_call 

import pandas as pd 
import numpy as np 

import random 
import os 
cur = os.path.dirname(__file__)
class Imp(BaseRequest):
    
    def __init__(self, ): 
        
        url = "https://api.gptzero.me/v2/predict/text"
        super(Imp, self).__init__(url=url )
        # self.
        
        self.cookies={"accessToken":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJhdXRoZW50aWNhdGVkIiwiZXhwIjoxNjc4MjY0MTIzLCJzdWIiOiIxN2M1MTJkZi0wYzg2LTQzMmEtOWU3Ni0wZjc5N2E4MjM1NzciLCJlbWFpbCI6InJlY2V0ZXk4OTBAd2lyb3V0ZS5jb20iLCJwaG9uZSI6IiIsImFwcF9tZXRhZGF0YSI6eyJwcm92aWRlciI6ImVtYWlsIiwicHJvdmlkZXJzIjpbImVtYWlsIl19LCJ1c2VyX21ldGFkYXRhIjp7ImVtYWlsIjoicmVjZXRleTg5MEB3aXJvdXRlLmNvbSIsImZ1bGxfbmFtZSI6InJlY2V0ZXk4OTAiLCJvcmciOiIifSwicm9sZSI6ImF1dGhlbnRpY2F0ZWQiLCJhYWwiOiJhYWwxIiwiYW1yIjpbeyJtZXRob2QiOiJwYXNzd29yZCIsInRpbWVzdGFtcCI6MTY3NzY1OTMyM31dLCJzZXNzaW9uX2lkIjoiOGJkMmFhMzktNDlmMi00ZGE0LWFlMGItZmM3ZTkyZTZjZGE1In0.thnop7Mbp9kCLC17q4I8ikDZkuOKk1bIopA8NjwXENQ"}
        
        self.headers .update({
            'content-type': 'application/json' ,

            # 'content-type':'application/x-www-form-urlencoded; charset=UTF-8',
            'Origin': 'https://app.gptzero.me',
            'Referer': 'https://app.gptzero.me',
            # 'X-Requested-With': 'XMLHttpRequest',
            "Authority": "api.gptzero.me",
            })

        self.method = "POST"
        
        # self.rate_limit = api_call.RateLimit(rate_limit=40, window_size=60, func_name="gptzero.me")
        
        with open(os.path.join(cur, "login", "token_activate.list.jsonl") ) as f :
            lines = f.readlines()
            data= [json.loads(line ) for line in lines ]
        
        
        self.account_list  =data  
        # self.access_token =  np.random.choice( self.account_list )["accessToken"]
    def __call__(self, text ):
        # print ("text", text )
        text = text[:20000-500]
        text = text.replace("`","'")
        text = text.replace("'",'"')
        json_data = {"document":text, }
        # print (text, "....text ",len(text) )
        # kwargs = {'data': json.dumps(json_data) }

        # for i in range(4):
        #     account_info_i  =random.randint(0,len( self.account_list)-1 ) 
        #     # print ("account_info_i", account_info_i, "-->", len( self.account_list) )
        #     account_info = self.account_list[account_info_i]
        #     # access_token = account_info["cookies"]["sb-access-token"]
        #     access_token = account_info["cookies"]["sb-access-token"]
        #     email  = account_info["email"]
        #     cookies = {
        #         # "accessToken":access_token,
        #         "accessToken4":access_token,
        #     }
        #
        #     flag = self.rate_limit.limit(account_id =email )
        #     if flag :
        #         return super(Imp, self).__call__( data=json.dumps(json_data) ,cookies=cookies  )
        #
        #
        # return super(Imp, self).__call__( data=json.dumps(json_data) ,cookies=cookies  )
        #
        account_info_i  =random.randint(0,len( self.account_list)-1 ) 
        # print ("account_info_i", account_info_i, "-->", len( self.account_list) )
        account_info = self.account_list[account_info_i]
        # access_token = account_info["cookies"]["sb-access-token"]
        access_token = account_info["cookies"]["sb-access-token"]
        email  = account_info["email"]
        
        # print ("access_token", type(access_token), "--?")
        # access_token="eyJhbGciOiJIUzI1NiIsImtpZCI6IkxQUGtRbDRKRlQvcmY5VkoiLCJ0eXAiOiJKV1QifQ.eyJhdWQiOiJhdXRoZW50aWNhdGVkIiwiZXhwIjoxNzA5OTIyNTIxLCJpYXQiOjE3MDkzMTc3MjEsImlzcyI6Imh0dHBzOi8vbHlkcWhnZHpodnNxbGNvYmRmeGkuc3VwYWJhc2UuY28vYXV0aC92MSIsInN1YiI6ImFjMTVjYTk4LTI5M2UtNDdjNi05MWI2LWVhNTNkYTk4MTc4MSIsImVtYWlsIjoiam9ybmJvd3JsQGdtYWlsLmNvbSIsInBob25lIjoiIiwiYXBwX21ldGFkYXRhIjp7InByb3ZpZGVyIjoiZ29vZ2xlIiwicHJvdmlkZXJzIjpbImdvb2dsZSJdfSwidXNlcl9tZXRhZGF0YSI6eyJhdmF0YXJfdXJsIjoiaHR0cHM6Ly9saDMuZ29vZ2xldXNlcmNvbnRlbnQuY29tL2EvQUNnOG9jS1hKWWJ2M0RnNXBMT05NRlFUOC1zTzJPc0RubnFHWF95STlYVXIzRHpPcEE9czk2LWMiLCJlbWFpbCI6Impvcm5ib3dybEBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiZnVsbF9uYW1lIjoiam9yIGJvd3JsIiwiaXNzIjoiaHR0cHM6Ly9hY2NvdW50cy5nb29nbGUuY29tIiwibmFtZSI6ImpvciBib3dybCIsInBob25lX3ZlcmlmaWVkIjpmYWxzZSwicGljdHVyZSI6Imh0dHBzOi8vbGgzLmdvb2dsZXVzZXJjb250ZW50LmNvbS9hL0FDZzhvY0tYSllidjNEZzVwTE9OTUZRVDgtc08yT3NEbm5xR1hfeUk5WFVyM0R6T3BBPXM5Ni1jIiwicHJvdmlkZXJfaWQiOiIxMTc1NDI1MDIwNDI3MDE2MjE1MTIiLCJzdWIiOiIxMTc1NDI1MDIwNDI3MDE2MjE1MTIifSwicm9sZSI6ImF1dGhlbnRpY2F0ZWQiLCJhYWwiOiJhYWwxIiwiYW1yIjpbeyJtZXRob2QiOiJvYXV0aCIsInRpbWVzdGFtcCI6MTcwOTMxNzcyMX1dLCJzZXNzaW9uX2lkIjoiMTRkNDJlNTctY2IwZS00MWEzLWJmMWQtYjU5OWZmYjA0MDEwIn0.vEZvUuNEYluQpGto7FuBcUxT3r86ENL--BkS-0oLDoQ"
        # access_token="eyJhbGciOiJIUzI1NiIsImtpZCI6IkxQUGtRbDRKRlQvcmY5VkoiLCJ0eXAiOiJKV1QifQ.eyJhdWQiOiJhdXRoZW50aWNhdGVkIiwiZXhwIjoxNzA5OTE5Njg5LCJpYXQiOjE3MDkzMTQ4ODksImlzcyI6Imh0dHBzOi8vbHlkcWhnZHpodnNxbGNvYmRmeGkuc3VwYWJhc2UuY28vYXV0aC92MSIsInN1YiI6ImFjMTVjYTk4LTI5M2UtNDdjNi05MWI2LWVhNTNkYTk4MTc4MSIsImVtYWlsIjoiam9ybmJvd3JsQGdtYWlsLmNvbSIsInBob25lIjoiIiwiYXBwX21ldGFkYXRhIjp7InByb3ZpZGVyIjoiZ29vZ2xlIiwicHJvdmlkZXJzIjpbImdvb2dsZSJdfSwidXNlcl9tZXRhZGF0YSI6eyJhdmF0YXJfdXJsIjoiaHR0cHM6Ly9saDMuZ29vZ2xldXNlcmNvbnRlbnQuY29tL2EvQUNnOG9jS1hKWWJ2M0RnNXBMT05NRlFUOC1zTzJPc0RubnFHWF95STlYVXIzRHpPcEE9czk2LWMiLCJlbWFpbCI6Impvcm5ib3dybEBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiZnVsbF9uYW1lIjoiam9yIGJvd3JsIiwiaXNzIjoiaHR0cHM6Ly9hY2NvdW50cy5nb29nbGUuY29tIiwibmFtZSI6ImpvciBib3dybCIsInBob25lX3ZlcmlmaWVkIjpmYWxzZSwicGljdHVyZSI6Imh0dHBzOi8vbGgzLmdvb2dsZXVzZXJjb250ZW50LmNvbS9hL0FDZzhvY0tYSllidjNEZzVwTE9OTUZRVDgtc08yT3NEbm5xR1hfeUk5WFVyM0R6T3BBPXM5Ni1jIiwicHJvdmlkZXJfaWQiOiIxMTc1NDI1MDIwNDI3MDE2MjE1MTIiLCJzdWIiOiIxMTc1NDI1MDIwNDI3MDE2MjE1MTIifSwicm9sZSI6ImF1dGhlbnRpY2F0ZWQiLCJhYWwiOiJhYWwxIiwiYW1yIjpbeyJtZXRob2QiOiJvYXV0aCIsInRpbWVzdGFtcCI6MTcwOTMxNDg4OX1dLCJzZXNzaW9uX2lkIjoiZjIxNjg2NjMtYTllOC00NjM5LWIxMzQtYjI1YTVmODJjMWUzIn0.ZtRoRQxnj7faSittomNgs3rP90PEhKy0CZe_HdZyn8w"
        # access_token="eyJhbGciOiJIUzI1NiIsImtpZCI6IkxQUGtRbDRKRlQvcmY5VkoiLCJ0eXAiOiJKV1QifQ.eyJhdWQiOiJhdXRoZW50aWNhdGVkIiwiZXhwIjoxNzA5OTIwODA5LCJpYXQiOjE3MDkzMTYwMDksImlzcyI6Imh0dHBzOi8vbHlkcWhnZHpodnNxbGNvYmRmeGkuc3VwYWJhc2UuY28vYXV0aC92MSIsInN1YiI6ImE0MWU0ZjI5LWIxM2UtNDI1Ny1iMTgzLTg5MzI0MjUxZWQ2YyIsImVtYWlsIjoibm9kYWJpcDUxMUB3aXJvdXRlLmNvbSIsInBob25lIjoiIiwiYXBwX21ldGFkYXRhIjp7InByb3ZpZGVyIjoiZW1haWwiLCJwcm92aWRlcnMiOlsiZW1haWwiXX0sInVzZXJfbWV0YWRhdGEiOnsiZW1haWwiOiJub2RhYmlwNTExQHdpcm91dGUuY29tIiwiZnVsbF9uYW1lIjoibm9kYWJpcDUxMSIsIm9yZyI6IiJ9LCJyb2xlIjoiYXV0aGVudGljYXRlZCIsImFhbCI6ImFhbDEiLCJhbXIiOlt7Im1ldGhvZCI6InBhc3N3b3JkIiwidGltZXN0YW1wIjoxNzA5MzE2MDA5fV0sInNlc3Npb25faWQiOiI0OTI2MDBkZC0zMGQwLTQ2ZDQtYjk2Zi1lNjlmZmRhNTgzMmIifQ.qrwIJyu6C9eXTFml2dCehWDBXjhq1pA19dIbg-Lq0Jk"
        # # access_token="eyJhbGciOiJIUzI1NiIsImtpZCI6IkxQUGtRbDRKRlQvcmY5VkoiLCJ0eXAiOiJKV1QifQ.eyJhdWQiOiJhdXRoZW50aWNhdGVkIiwiZXhwIjoxNzA5OTIwNDYwLCJpYXQiOjE3MDkzMTU2NjAsImlzcyI6Imh0dHBzOi8vbHlkcWhnZHpodnNxbGNvYmRmeGkuc3VwYWJhc2UuY28vYXV0aC92MSIsInN1YiI6IjQ2MmU3NGMzLWU1OWYtNDlmMy04MDUxLTFjMTMzZTQzYjRjNiIsImVtYWlsIjoibWloaW5pMTE4NUB2MnNzci5jb20iLCJwaG9uZSI6IiIsImFwcF9tZXRhZGF0YSI6eyJwcm92aWRlciI6ImVtYWlsIiwicHJvdmlkZXJzIjpbImVtYWlsIl19LCJ1c2VyX21ldGFkYXRhIjp7ImVtYWlsIjoibWloaW5pMTE4NUB2MnNzci5jb20iLCJmdWxsX25hbWUiOiJtaWhpbmkxMTg1Iiwib3JnIjoiIn0sInJvbGUiOiJhdXRoZW50aWNhdGVkIiwiYWFsIjoiYWFsMSIsImFtciI6W3sibWV0aG9kIjoicGFzc3dvcmQiLCJ0aW1lc3RhbXAiOjE3MDkzMTU2NjB9XSwic2Vzc2lvbl9pZCI6IjU2ZTE5Yzk0LTJhODItNDE2MC04ZDJiLTdjMmJhYzUzNjdjOCJ9.9VmtLl00zS0-StCxto5RqNsVKLweKQsr6UpXK05Y3gI"
        # access_token= "eyJhbGciOiJIUzI1NiIsImtpZCI6IkxQUGtRbDRKRlQvcmY5VkoiLCJ0eXAiOiJKV1QifQ.eyJhdWQiOiJhdXRoZW50aWNhdGVkIiwiZXhwIjoxNzA5OTIwOTg0LCJpYXQiOjE3MDkzMTYxODQsImlzcyI6Imh0dHBzOi8vbHlkcWhnZHpodnNxbGNvYmRmeGkuc3VwYWJhc2UuY28vYXV0aC92MSIsInN1YiI6IjYwNGY3YjFkLTk2NDEtNGZhYi1hZmQ1LTFjYmJhMjExNDdhZCIsImVtYWlsIjoic2Fib20zNzM2OEB3aXJvdXRlLmNvbSIsInBob25lIjoiIiwiYXBwX21ldGFkYXRhIjp7InByb3ZpZGVyIjoiZW1haWwiLCJwcm92aWRlcnMiOlsiZW1haWwiXX0sInVzZXJfbWV0YWRhdGEiOnsiZW1haWwiOiJzYWJvbTM3MzY4QHdpcm91dGUuY29tIiwiZnVsbF9uYW1lIjoic2Fib20zNzM2OCIsIm9yZyI6InNhYm9tMzczNjhAd2lyb3V0ZS5jb20ifSwicm9sZSI6ImF1dGhlbnRpY2F0ZWQiLCJhYWwiOiJhYWwxIiwiYW1yIjpbeyJtZXRob2QiOiJwYXNzd29yZCIsInRpbWVzdGFtcCI6MTcwOTMxNjE4NH1dLCJzZXNzaW9uX2lkIjoiOTM4MTNhNzktZjAzOS00N2JkLTk5OWEtNWY1NDg2YTY5NWZmIn0.nSFyLKcIqmulGTL3SBzwTK18rGTTpe0QlGVGHS-1wVM"
        # access_token="eyJhbGciOiJIUzI1NiIsImtpZCI6IkxQUGtRbDRKRlQvcmY5VkoiLCJ0eXAiOiJKV1QifQ.eyJhdWQiOiJhdXRoZW50aWNhdGVkIiwiZXhwIjoxNzA5OTIwOTg0LCJpYXQiOjE3MDkzMTYxODQsImlzcyI6Imh0dHBzOi8vbHlkcWhnZHpodnNxbGNvYmRmeGkuc3VwYWJhc2UuY28vYXV0aC92MSIsInN1YiI6IjYwNGY3YjFkLTk2NDEtNGZhYi1hZmQ1LTFjYmJhMjExNDdhZCIsImVtYWlsIjoic2Fib20zNzM2OEB3aXJvdXRlLmNvbSIsInBob25lIjoiIiwiYXBwX21ldGFkYXRhIjp7InByb3ZpZGVyIjoiZW1haWwiLCJwcm92aWRlcnMiOlsiZW1haWwiXX0sInVzZXJfbWV0YWRhdGEiOnsiZW1haWwiOiJzYWJvbTM3MzY4QHdpcm91dGUuY29tIiwiZnVsbF9uYW1lIjoic2Fib20zNzM2OCIsIm9yZyI6InNhYm9tMzczNjhAd2lyb3V0ZS5jb20ifSwicm9sZSI6ImF1dGhlbnRpY2F0ZWQiLCJhYWwiOiJhYWwxIiwiYW1yIjpbeyJtZXRob2QiOiJwYXNzd29yZCIsInRpbWVzdGFtcCI6MTcwOTMxNjE4NH1dLCJzZXNzaW9uX2lkIjoiOTM4MTNhNzktZjAzOS00N2JkLTk5OWEtNWY1NDg2YTY5NWZmIn0.nSFyLKcIqmulGTL3SBzwTK18rGTTpe0QlGVGHS-1wVM"
        cookies = {
            # "accessToken":access_token,
            "accessToken4":access_token,
            # "source":"dashboard",
            # # "author":"jor bowrl",
            # "title":"aaa",
            # "checkPlagiarism":"false",
            # "writing_stats_required":"true",
            # "interpretability_required":"false"
        }
        # print ("---->"*8 , json_data , cookies )
        return super(Imp, self).__call__( data=json.dumps(json_data) ,cookies=cookies  )

            



    def format(self,content  ):
        # print (content)
        # if content is None :
        #     return content
        
        '''
{
    "documents": [
        {
            "average_generated_prob": 1,
            "completely_generated_prob": 0.9752832361642448,
            "overall_burstiness": 13.855096817016602,
            "paragraphs": [
                {
                    "completely_generated_prob": 0.9752832361642448,
                    "num_sentences": 32,
                    "start_sentence_index": 0
                }
            ],
            "sentences": [
                {
                    "generated_prob": 1,
                    "perplexity": 12,
                    "sentence": "When I first heard about what a lot of people are calling the 'anti-transgender' law passed in Arkansas last week, it came as a complete surprise to me."
                },
                {
                    "generated_prob": 1,
                    "perplexity": 73,
                    "sentence": "I was one of the supporters behind Prop 8 .\\nAnd so I am quite surprised to hear of this new law passed in Kentucky."
                },
                {
                    "generated_prob": 1,
                    "perplexity": 30,
                    "sentence": "I don't know your situation, but if you are looking for an extreme level of religious liberty, you could probably take a closer look at this 'religious freedom' bill here:\\u00a0\\nAnd here's a more personal experience with this \\\"religious freedom\\\" bill:\\nAs a college student, I was forced to write a paper on how gay and transgender people were destroying gay marriage and why."
                }
            ]
        }
    ]
}

        '''
        import json 
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
            "raw_response":info_raw,
            }
