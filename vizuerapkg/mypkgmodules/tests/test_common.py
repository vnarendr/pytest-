'''
Created on Aug 13, 2018

@author: narendra_v
'''
import urllib3
from vizuerapkg.mypkgmodules.modules.common import Common_Task
from vizuerapkg.mypkgmodules.attributes_file import Variables
from vizuerapkg.Http_services.http_client import Http_Client
import pdb

import pytest

#--- Remove SSL Certification error using urllib3----- 
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

var = Variables()
common = Common_Task()
http = Http_Client()
http.current_token()

class Testing():
    
    #*** fixuture user 
    # -- @pytest.mark.skip: --- To skip specific test execution 
    # ---- @pytest.mark.skip(reason="Addition has been deactivated because of issue #123")  --- you can specify with the reasion 
    # -- py.test -svv -k test_token cmmmand to execute single test  ( -K is used for run specific test in test file )
    # -- (pytest --show-capture=no test_common.py) will print with (. as pass )
    # -pytest -k test_token -rs ( PRINT THE SKIPPED SPECIFIC TEST WITH REASION (-RS)
    ######################################################
    '''
     Some options
     -x                    Stop after first failure
     -k "expression"       Only run tests that match expession (and fixtures)
     -s                    Do not capture output
     -rs                   Show extra summary info for SKIPPED
     -r chars              Show extra test summary info as specified by chars:
                           (f)ailed, (E)error, (s)skipped, (x)failed, (X)passed
                           (w)pytest-warnings (p)passed, (P)passed with output,
                           (a)all except pP.
    
     -v                    Verbose
     -q, --quiet           Less verbose
    
     -l, --showlocals      Show local variables in tracebacks
     #@pytest.mark.skip(reason="Addition has been deactivated because of issue #123")
     '''
    #################################################################
        
    @pytest.mark.parametrize('argument', [(var.username, var.password)])
    def test_authorization(self,argument):
        ''' pass keyword with username and password
        '''
        result = common.__authorization__(argument[0],argument[1])
        token_result = http.current_token()
        assert result == token_result
        
    @pytest.mark.parametrize('argument', [var.all_privilage])
    def test_previlagedata(self, argument):
        ''' pass valid url as arguments
        '''
        assert common.__getdetails__(argument) == var.status_code
        
    @pytest.mark.parametrize('argument', [var.event_type])
    def test_eventtype(self, argument):
        ''' pass valid url as arguments
        '''
        assert common.__getdetails__(argument) == var.status_code
        
    @pytest.mark.parametrize('argument', [var.country])
    def test_country(self, argument):
        ''' pass valid url as arguments
        '''
        assert common.__getdetails__(argument) == var.status_code

    @pytest.mark.parametrize('argument', [var.Entity_type])
    def test_entity_type(self, argument):
        ''' pass valid url as arguments
        '''
        assert common.__getdetails__(argument) == var.status_code
    
    @pytest.mark.parametrize('argument', [var.sectors])
    def test_sectors(self, argument):
        ''' pass valid url as arguments
        '''
        assert common.__getdetails__(argument) == var.status_code
        
    @pytest.mark.parametrize('argument', [var.profile_maturity_level])
    def test_profile_maturity_level(self, argument):
        ''' pass valid url as arguments
        '''
        assert common.__getdetails__(argument) == var.status_code
        
    @pytest.mark.parametrize('argument', [var.section_type])
    def test_section_type(self, argument):
        ''' pass valid url as arguments
        '''
        assert common.__getdetails__(argument) == var.status_code
        
    
    @pytest.mark.parametrize('argument', [var.section_classification])
    def test_section_classification(self, argument):
        ''' pass valid url as arguments
        '''
        assert common.__getdetails__(argument) == var.status_code
        
        
    @pytest.mark.parametrize('argument', [var.user_types])
    def test_user_types(self, argument):
        ''' pass valid url as arguments
        '''
        assert common.__getdetails__(argument) == var.status_code
        
        
    @pytest.mark.parametrize('argument', [var.expense_type])
    def test_expense_type(self, argument):
        ''' pass valid url as arguments
        '''
        assert common.__getdetails__(argument) == var.status_code
    
    @pytest.mark.parametrize('argument', [var.question_classification])
    def test_question_classification(self, argument):
        ''' pass valid url as arguments
        '''
        assert common.__getdetails__(argument) == var.status_code
        
    @pytest.mark.parametrize('argument', [var.time_line])
    def test_time_line(self, argument):
        ''' pass valid url as arguments
        '''
        assert common.__getdetails__(argument) == var.status_code
        
    @pytest.mark.parametrize('argument', [(var.zone_type, var.chain_id)])
    def test_zone_type(self, argument):
        ''' pass valid url as arguments with Chain id
        example: url =  https://api.prezision.evry/V1/Common/ZoneType , chain_id = 3  
        '''
        argument  = argument[0]+'/'+str(argument[1])
        assert common.__getdetails__(argument) == var.status_code
        
    @pytest.mark.parametrize('argument', [(var.event_type_attribute, var.event_id)])
    def test_event_type_attribute(self, argument):
        ''' pass valid url as arguments with event_id
        example: url =  https://api.prezision.evry/V1/Common/evem_type , event_id = 3  
        '''
        argument  = argument[0]+'/'+str(argument[1])
        assert common.__getdetails__(argument) == var.status_code

    @pytest.mark.parametrize('argument', [(var.event_subtype_attribute, var.event_subtypeid)])
    def test_event_subtype_attribute(self, argument):
        ''' pass valid url as arguments with event_subtypeid
            example: url =  https://api.prezision.evry/V1/Common/subtype_attribute , event_subtype_id = 3  
        '''
        argument  = argument[0]+'/'+str(argument[1])
        assert common.__getdetails__(argument) == var.status_code

    @pytest.mark.parametrize('argument', [var.ticket_type])
    def test_ticket_type(self, argument):
        ''' pass valid url as arguments
        '''
        assert common.__getdetails__(argument) == var.status_code

    @pytest.mark.parametrize('argument', [var.ticket_status])
    def test_ticket_status(self, argument):
        ''' pass valid url as arguments
        '''
        assert common.__getdetails__(argument) == var.status_code
    
    @pytest.mark.parametrize('argument', [var.ticket_entity_type])
    def test_ticket_entity_type(self, argument):
        ''' pass valid url as arguments
        '''
        assert common.__getdetails__(argument) == var.status_code
    
    @pytest.mark.parametrize('argument', [var.time_zones])
    def test_time_zones(self, argument):
        ''' pass valid url as arguments
        '''
        assert common.__getdetails__(argument) == var.status_code
    
    @pytest.mark.parametrize('argument', [var.store_kpi_parameters])
    def test_store_kpi_parameters(self, argument):
        ''' pass valid url as arguments
        '''
        assert common.__getdetails__(argument) == var.status_code
    
    @pytest.mark.parametrize('argument', [(var.encode_password_url, var.encode_password)])
    def test_encode_password(self, argument):
        ''' pass valid url as arguments with encode_password
            example: url =  https://api.prezision.evry/V1/Common/encode_password_url , encode_password = abc  
        '''
        argument  = argument[0]+'/'+str(argument[1])
        assert common.__getdetails__(argument) == var.status_code

    @pytest.mark.parametrize('argument', [(var.previlage_on_urertype_url, var.user_types)])
    def test_previlage_on_urertype(self, argument):
        ''' pass valid url as arguments with user_types
            example: url =  https://api.prezision.evry/V1/Common/previlage_on_urertype_url , user_types = superuser  
        '''
        argument  = argument[0]+'/'+str(argument[1])
        assert common.__getdetails__(argument) == var.status_code

    @pytest.mark.parametrize('argument', [(var.role_usertype, var.user_types)])
    def test_rolename_of_urertype(self, argument):
        ''' pass valid url as arguments with user_types
            example: url =  https://api.prezision.evry/V1/Common/role_usertype , encode_password = superuser  
        '''
        argument  = argument[0]+'/'+str(argument[1])
        assert common.__getdetails__(argument) == var.status_code
        
    @pytest.mark.parametrize('argument', [var.cost_type])
    def test_cost_type(self, argument):
        ''' pass valid url as arguments   
        '''
        assert common.__getdetails__(argument) == var.status_code
        
    #@pytest.mark.parametrize('argument', [var.common_page])
    @pytest.mark.skip(reason = 'Not implemented ')
    def test_common_page(self, argument):
        ''' pass valid url as arguments   
        '''
        assert common.__getdetails__(argument) == var.status_code
        
