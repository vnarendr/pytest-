'''
Created on Aug 13, 2018

@author: narendra_v
'''
from vizuerapkg.mypkgmodules.attributes_file import Variables
import requests
import pdb

var = Variables()
 
class Http_Client():
    
    token_value = ''
    
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    def __init__(self):
        self.new_token = Http_Client.token_value
            
    def authorization(self, *args):
        '''
        authorization (email id and password is the mandatory)
        EmailId should be first argument followed by Password
        '''
        
        headers = {
            'Content-Type': "application/x-www-form-urlencoded",
            'Cache-Control': "no-cache"
        }
        Emailid = args[0] 
        Password = args[1]
        body =  'grant_type=password&username='+Emailid+'&password='+Password+'&client_id=PrezisionWeb&client_secret=YMTADCLWqMU3D78g35z6xnGV2Jwx9HtUkUdw7AnSBCVQ7CXy3JxF&scope=offline_access&isPwdEncrypted=false'
        url = var.token_url
        result = requests.post(url,body, headers = headers, verify = False )
        if (result.status_code == 404):
            token =  "Not Found :-- URL should be corrected "
            raise ValueError, self.token
         
        elif (result.status_code == 400):
            token =  result.json()
            raise ValueError,  result.json() 
        else:
            result = result.json()
            #token = {'token_type': result[0], 'access_token': result[1], 'expires_in' : result[2], 'refresh_token' : result[3] }
            token = result['token_type']+" "+result['access_token']
            
            Http_Client.token_value = token
         
        return token
    
    def current_token(self):
        Http_Client.token_value 
        return Http_Client.token_value
    
    def __post__(self,  *args):
        
        headers = {
            'Content-Type': "application/x-www-form-urlencoded",
            'Cache-Control': "no-cache",
            'Authorization' : Http_Client.token_value 
            }
        return requests.post( url = args[0], body = args[1], headers = headers, verify = False)
        #print result.json, result.status_code
        #json = result.json
        #print json
        '''
        status_code = result.status_code
        
        pdb.set_trace()
        if (result.status_code == 200):
            jsonData = result.json(), status_code
            
        elif (result.status_code == 404):
            jsonData =  status_code
        else:
            jsonData = result.json() , status_code
        '''
    def __get__(self, *args):
        
        headers = {
            'Authorization' : Http_Client.token_value
            }
        return requests.get(url = args[0], headers = headers, verify = False)
         
    

