import json 

import numpy as np 



with open("token_activate.list.jsonl") as f :
    data=[json.loads(x) for x in f.readlines()]
    
    
fial_f = []

for item in data :
    faile=  False
    try:
        access_token = account_info["cookies"]["sb-access-token"]
        faile = access_token is None 
    except :
        faile =True 
        
    fial_f.append(faile)
    
    
print (np.unique( fial_f , return_counts=True ))