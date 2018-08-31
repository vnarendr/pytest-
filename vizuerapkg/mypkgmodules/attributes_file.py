'''
Created on Aug 13, 2018

@author: narendra_v
'''
import sys
from selenium import webdriver 
from time import sleep
import xlwt
import xlrd
 
username ='vsuperuser@gmail.com'
password = 'abc'
url = ''
body = ''
token_url = 'https://api.prezision.evry/connect/token'

#------------------Common ------------------------#

all_privilage = ''
event_type = ''
country= ''
Entity_type= ''
sectors= ''
profile_maturity_level= ''
section_type = ''
section_classification= ''
user_types = ''
expense_type = ''
question_classification   = ''
time_line= ''
zone_type= ''
event_type_attribute = ''
event_subtype_attribute= ''
ticket_type= ''
ticket_status= ''
ticket_entity_type= ''
time_zones = ''
store_kpi_parameters= ''
encode_password_url= ''
previlage_on_urertype_url = ''
role_usertype = ''
cost_type = ''
common_page= ''        





class Variables():
    
    #token = ''
    
    
    
    def __init__(self):
        self.username = username
        self.password = password
        self.token_url = token_url
        self.body = body
        #self.token = Variables.token
        self.status_code = 200
        
        # --------------------------Id ----------------------------------------------#
        self.chain_id = 23  # (specify the chain id  )
        self.event_id = 1 # ( 1 - 5 Event exist -- Master record )
        self.event_subtypeid = 1
        self.encode_password = 'abc'
        self.user_types = 'superuser'
        
        #----------------------------------Swagger -- URL ----------------------------------------#
        
        self.driver_path = 'D:/Python/working_example/Angularjs_testing_pytest/vizuerapkg/mypkgmodules/chromedriver.exe'
        self.swagger_url = 'http://api.prezision.evry/services/help/#/'
        self.path = 'D:/Python/working_example/Angularjs_testing_pytest/vizuerapkg/mypkgmodules/tests/swagger_template.xls'
        #D:/Python/working_example/Angularjs_testing_pytest/vizuerapkg/mypkgmodules/swagger_template.xls' 
         
        # ----------------------- Common -##- Resource URL's -------------------------------------#
        '''
        self.all_privilage = 'https://api.prezision.evry/V1/Common/Privileges'
        self.event_type = 'https://api.prezision.evry/V1/Common/EventType'
        self.country = 'https://api.prezision.evry/V1/Common/Country'
        self.Entity_type = 'https://api.prezision.evry/V1/Common/EntityType'
        self.sectors = 'https://api.prezision.evry/V1/Common/Sectors'
        self.profile_maturity_level ='https://api.prezision.evry/V1/Common/ProfileMaturityLevel'
        self.section_type = 'https://api.prezision.evry/V1/Common/SectionType'
        self.section_classification = 'https://api.prezision.evry/V1/Common/SectionClassification'
        self.user_types = 'https://api.prezision.evry/V1/Common/UserType'
        self.expense_type = 'https://api.prezision.evry/V1/Common/ExpenseType'
        self.question_classification = 'https://api.prezision.evry/V1/Common/QuestionClassification'   
        self.time_line = 'https://api.prezision.evry/V1/Common/TimeLine'
        self.zone_type = 'https://api.prezision.evry/V1/Common/ZoneType'
        self.event_type_attribute = 'https://api.prezision.evry/V1/Common/EventTypeAttribute'
        self.event_subtype_attribute = 'https://api.prezision.evry/V1/Common/EventSubTypeAttribute'
        self.ticket_type= 'https://api.prezision.evry/V1/Common/TicketType'
        self.ticket_status= 'https://api.prezision.evry/V1/Common/TicketStatus'
        self.ticket_entity_type = 'https://api.prezision.evry/V1/Common/TicketEntityType'
        self.time_zones = 'https://api.prezision.evry/V1/Common/TimeZones'
        self.store_kpi_parameters = 'https://api.prezision.evry/V1/Common/StoreKPIParameters'
        self.encode_password_url = 'https://api.prezision.evry/V1/Common/Encode?password='
        self.previlage_on_urertype_url ='https://api.prezision.evry/V1/Common/PrivilegesOnUserType?userType='
        self.role_usertype = 'https://api.prezision.evry/V1/Common/RoleUserType?userType='
        self.cost_type = 'https://api.prezision.evry/V1/Common/CostType'
        self.common_page = 'https://api.prezision.evry/V1/Common/Page'
        '''
        
        self.all_privilage = all_privilage
        self.event_type = event_type
        self.country = country
        self.Entity_type = Entity_type
        self.sectors = sectors
        self.profile_maturity_level =profile_maturity_level
        self.section_type = section_type 
        self.section_classification = section_classification
        self.user_types =  user_types 
        self.expense_type = expense_type
        self.question_classification = question_classification   
        self.time_line = time_line
        self.zone_type = zone_type
        self.event_type_attribute = event_type_attribute 
        self.event_subtype_attribute = event_subtype_attribute
        self.ticket_type= ticket_type
        self.ticket_status= ticket_status
        self.ticket_entity_type = ticket_entity_type
        self.time_zones = time_zones 
        self.store_kpi_parameters = store_kpi_parameters
        self.encode_password_url = encode_password_url
        self.previlage_on_urertype_url =previlage_on_urertype_url 
        self.role_usertype = role_usertype 
        self.cost_type = cost_type 
        self.common_page = common_page
        self.common_url = [all_privilage,event_type,country,Entity_type,sectors,profile_maturity_level,section_type ,section_classification, user_types ,expense_type,question_classification   ,time_line,zone_type,event_type_attribute ,event_subtype_attribute,ticket_type,ticket_status,ticket_entity_type,time_zones ,store_kpi_parameters,encode_password_url,previlage_on_urertype_url ,role_usertype ,cost_type ,common_page] 
    
 
        
             

#var = Variables()
#var.get_url()
     
#Variables(username, password,token_url, body)
    
        
