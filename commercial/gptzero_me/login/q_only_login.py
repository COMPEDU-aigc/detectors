import requests 
import json 

proxy="http://127.0.0.1:9100"

import os
import time 

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
            "apikey": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imx5ZHFoZ2R6aHZzcWxjb2JkZnhpIiwicm9sZSI6ImFub24iLCJpYXQiOjE2ODA5MTMyNDUsImV4cCI6MTk5NjQ4OTI0NX0.fiun9l_A2j_tHza1j8W_bEAHHj4NzS1PdpL3RX4-eWc",
            "authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imx5ZHFoZ2R6aHZzcWxjb2JkZnhpIiwicm9sZSI6ImFub24iLCJpYXQiOjE2ODA5MTMyNDUsImV4cCI6MTk5NjQ4OTI0NX0.fiun9l_A2j_tHza1j8W_bEAHHj4NzS1PdpL3RX4-eWc",
           'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
            }
            

    def login(self,email_str ):
        url = "https://lydqhgdzhvsqlcobdfxi.supabase.co/auth/v1/token?grant_type=password"
    

        data=  {
            "email":email_str,
            "password":"jl123456",
            "gotrue_meta_security":{}}
        
        response = self.sess .post(
            url = url , 
            headers=self.headers,
            data= json.dumps(data  ),
             )
                
        if response.status_code ==200 :
            cookie_dict = response . cookies.get_dict()
            response_dict = response.json()
             
            print ("cookie_dict" , cookie_dict )
            response_dict["cookies"]= cookie_dict
            return response_dict #cookie_dict["sb-access-token"]
        else :
            print ("response", response.status_code, "response-->", response.content)
            raise Exception("step1 login ")
        

    def run(self):
        with open("success.list.jsonl") as f :
            data= [  json.loads(x) for x in f.readlines()]

        exist_email = []
        if os.path.isfile("token_activate.list.jsonl") :
            with open("token_activate.list.jsonl") as ff :
                cc= [json.loads(x) for x in ff.readlines()]
                exist_email = [x["email"] for x in cc ] 
                exist_email = set(exist_email)
        
        print ("previous size", len(data) )
        data=  [x for x in data if x["email"] not in exist_email]
        print ("after exist size ", len(data) )
            
        # for item in data[:5]: 
        for iii, item in enumerate(data) :
            email_str = item ["email"]
            
            login_info  = self.login(email_str=email_str)
            login_info["email"]= email_str
            with open("token_activate.list.jsonl","a") as f :
                f.write(json.dumps(login_info) )
                f.write("\n")
            # print (token,"....")
            if iii%10 ==0:
                time.sleep(5)
# regist(email="gibas15265@youke1.com")           

import time 


# while True:    
obj = REX()
obj.run()







