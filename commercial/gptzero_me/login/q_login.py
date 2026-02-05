import requests 
import json 

proxy="http://47.87.143.109:9100"

import redis 

task = "gptzero"
def get_redis_connect():
    from redis.cluster import RedisCluster as Redis
    rc = Redis(host='155.69.151.252', port=6379)
    return rc 
def get_email_id_from_redis( ):
    rc = get_redis_connect()
    # step1_queue = "step1:q"+":"+task
    email = rc. lpop( step1_queue )
    email = email.decode("utf-8")
    print (type(email), email ,"type.email ") 
    return email 

step1_queue = "step1:q"
# +":"+task
step1_msg_prefix = "step1:token:"+task+":"
step2_queue = "step2:q"+":"+task
step2_msg_prefix = "step2:confirmlink:"+task+":"

def this_is_a_long_time_wait_from_redis_confirm_link(email ):
    rc = get_redis_connect()
    retry =100 
    while True and retry>0 :
        search = step2_msg_prefix+email
        v= rc.get(search)
        if v is None :
            time.sleep(1)
            retry-=1
        else:
            return v .decode("utf-8") 

def send_redis_noteice_wait_confirmlink(email ):
    rc = get_redis_connect()
    step1_queue_listen = "step1:listen"
    
    rc.rpush(step1_queue_listen,email)





class REX :
    
    def __init__(self):
        assert proxy is not None 
        proxies = {
           'http':proxy,
           'https': proxy,
        }
        self.sess  = requests.Session()
        self.sess.proxies.update(proxies)
        self.config ={}
        
        self.GREEN = "\033[92m"
        self.WARNING = "\033[93m"
        self.ENDCOLOR = "\033[0m"
        
        self.headers= {
            "apikey": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imx5ZHFoZ2R6aHZzcWxjb2JkZnhpIiwicm9sZSI6ImFub24iLCJpYXQiOjE2NzU3ODU5NjAsImV4cCI6MTk5MTM2MTk2MH0.RFSd4hpxbmvXbi4iGPQuoN_-1thYFdWayZXtihqBfUg",
            "authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imx5ZHFoZ2R6aHZzcWxjb2JkZnhpIiwicm9sZSI6ImFub24iLCJpYXQiOjE2NzU3ODU5NjAsImV4cCI6MTk5MTM2MTk2MH0.RFSd4hpxbmvXbi4iGPQuoN_-1thYFdWayZXtihqBfUg",
           'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
            }
            
    def regist(self):
        email = self.config["email"] 
        
        data= {
            "email":email,
            "password":"jl123456",
            "data":{
                "full_name":email.split("@")[0],
                "org":"",
                "email":email },
            "gotrue_meta_security":{}
            }
        
        
        url ="https://lydqhgdzhvsqlcobdfxi.supabase.co/auth/v1/signup"
        # headers= {
        #     "apikey": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imx5ZHFoZ2R6aHZzcWxjb2JkZnhpIiwicm9sZSI6ImFub24iLCJpYXQiOjE2NzU3ODU5NjAsImV4cCI6MTk5MTM2MTk2MH0.RFSd4hpxbmvXbi4iGPQuoN_-1thYFdWayZXtihqBfUg",
        #     "authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imx5ZHFoZ2R6aHZzcWxjb2JkZnhpIiwicm9sZSI6ImFub24iLCJpYXQiOjE2NzU3ODU5NjAsImV4cCI6MTk5MTM2MTk2MH0.RFSd4hpxbmvXbi4iGPQuoN_-1thYFdWayZXtihqBfUg",
        #    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        #     }
    
    
    
        response = self.sess .post(
            url = url , 
            headers=self.headers,
            data= json.dumps(data  ),
            # proxies=proxies,
             )
        
        print (dir(response) )
        
    
        if response.status_code ==200 :
            print (response.json() )
            
            return True 
        else:
            print (response)
            
            return False 
    
    def login(self):
        url = "https://lydqhgdzhvsqlcobdfxi.supabase.co/auth/v1/token?grant_type=password"
    

        data=  {
            "email":self.config["email"],
            "password":"jl123456",
            "data":{},"gotrue_meta_security":{}}
        
        response = self.sess .post(
            url = url , 
            headers=self.headers,
            data= json.dumps(data  ),
             )
                
        if response.status_code ==200 :
            cookie_dict = response . cookies.get_dict()
            print ("cookie_dict" , cookie_dict )
            
            return cookie_dict["sb-access-token"]
        else :
            raise Exception("step1 login ")
        
    def req(self,text):
        data={"document":text } 
        
        
        cookies = {
            'accessToken': self.config["accessToken"],
            # "AMP_MKTG":"JTdCJTdE",
            # "AMP":"JTdCJTIyZGV2aWNlSWQlMjIlM0ElMjIwMmIwNGNiYS1hNDkxLTQ2NWYtOWUyOC02NzgyODVjZTFkNjMlMjIlMkMlMjJzZXNzaW9uSWQlMjIlM0ExNjc3OTYzODg2NTI2JTJDJTIyb3B0T3V0JTIyJTNBZmFsc2UlMkMlMjJsYXN0RXZlbnRUaW1lJTIyJTNBMTY3Nzk2NDE2MzU2MiU3RA==",
             }
        url = "https://api.gptzero.me/v2/predict/text"

        response = self.sess .post(
            url = url , 
            headers=self. headers,
            cookies=cookies,
            json= data ,#json.dumps(data  ),
             )
        if response.status_code ==200 :
            print (response.json() )
            
            return True 
        else:
            print (response)
            
            raise Exception("step3 ")
        

    def run(self):
        email = get_email_id_from_redis()
        self.config["email"]=email 
        
        if self.regist ():
            # self.config["email"]= "gibas15265@youke1.com"
            # self.config["accessToken"]= "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJhdXRoZW50aWNhdGVkIiwiZXhwIjoxNjc4NTY2MDg2LCJzdWIiOiJjN2Y0NDgzZi01NGMwLTQ0Y2ItOGQyNC1jYmMyODQwMGFjYzUiLCJlbWFpbCI6ImpvbGl4YWg3NDRAd2lyb3V0ZS5jb20iLCJwaG9uZSI6IiIsImFwcF9tZXRhZGF0YSI6eyJwcm92aWRlciI6ImVtYWlsIiwicHJvdmlkZXJzIjpbImVtYWlsIl19LCJ1c2VyX21ldGFkYXRhIjp7ImVtYWlsIjoiam9saXhhaDc0NEB3aXJvdXRlLmNvbSIsImZ1bGxfbmFtZSI6ImpvbGl4YWg3NDQiLCJvcmciOiIifSwicm9sZSI6ImF1dGhlbnRpY2F0ZWQiLCJhYWwiOiJhYWwxIiwiYW1yIjpbeyJtZXRob2QiOiJwYXNzd29yZCIsInRpbWVzdGFtcCI6MTY3Nzk2MTI4Nn1dLCJzZXNzaW9uX2lkIjoiZWY4MDEzYTUtMGJkNy00MTFmLWJjYjUtYmIxMjYxZmU1N2Q2In0.9VBiqmgIz-JX2VgpZawQByfeBLj9K8i-0122Hy34UK0"
            
            
            print(self.GREEN + "waiting email ." + self.ENDCOLOR)
            #
            send_redis_noteice_wait_confirmlink(email=self.config["email" ] )
            #
            #
            link = this_is_a_long_time_wait_from_redis_confirm_link(email= self.config["email"] )
            print(self.GREEN + "get confirm link ." + self.ENDCOLOR)
            #
            print ("the link is ",link )
            if link :
                self.sess.get(link)
            
            time.sleep(2)
            
            token = self.login()
            
            self.config["accessToken"]= token 
            
            text = "Accepted file types: pdf, docx, txt Accepted file types: pdf, docx, txt Accepted file types: pdf, docx, txt, Accepted file types: pdf, docx, txt Accepted file types: pdf, docx, txt Accepted file types: pdf, docx, txt,Accepted file types: pdf, docx, txt Accepted file types: pdf, docx, txt Accepted file types: pdf, docx, txt"
            
            
            self.req(text=text)
            
            with open("success.list.jsonl","a") as f :
                f.write(json.dumps(self.config) )
                f.write("\n")
        
# regist(email="gibas15265@youke1.com")           

import time 


while True:    
    obj = REX()
    obj.run()







