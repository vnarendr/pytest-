'''
Created on Aug 13, 2018

@author: narendra_v
'''
from vizuerapkg.Http_services.http_client import Http_Client
import pdb

http = Http_Client()

class Statuscode_Error(Exception):
    pass 

class Common_Task():
    
    def __init__(self ):
        pass
         
    def __authorization__(self, *args):
        result = http.authorization(*args)
        return result
        
    def __getdetails__(self, *args):
        result = http.__get__(*args)
        print '*INFO*' , result.json()
        return result.status_code
        

                                   
        
             
        
        