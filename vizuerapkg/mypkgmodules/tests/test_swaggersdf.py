
from selenium import webdriver
from time import sleep
import xlsxwriter
import pytest

    
class Swagger_test(object):
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
        
    
    
    #def __init__(self):
        
    #    self.workbook = xlsxwriter.Workbook('swagger_template.xlsx')
    #    self.worksheet = self.workbook.add_worksheet('Dashboard')
        
        
    def test_display_urllink(self):
        
        self.workbook = xlsxwriter.Workbook('swagger_template.xlsx')
        self.worksheet = self.workbook.add_worksheet('Dashboard')
        print "link"
        driver = webdriver.Chrome(var.driver_path)
        driver.maximize_window()
        driver.get(var.swagger_url)
        sleep(3)
        module = []
        resoucemoduel = {}
        
        parent = '//*[@id="resources"]/li'
        attributes = driver.find_elements_by_xpath(parent)
        for  key in (attributes):
            module_name = key.get_attribute('id')
            module.append(module_name)
            child_xpath = driver.find_elements_by_xpath('//*[@id="'+str(module_name)+'"]/ul/li/ul/li/div/h3/span[2]/a')
            #print module_name , '--->',len(child_xpath)#, child_xpath.get_attribute("href")
            temp = []
            for index in range(len(child_xpath)):
                link_xpath = driver.find_elements_by_xpath('//*[@id="'+str(module_name)+'"]/ul/li['+str(index+1)+']/ul/li/div/h3/span[2]/a')
                for url in link_xpath:
                    swagger_url = 'http://api.prezision.evry'
                    url = swagger_url+str(url.get_attribute('text'))
                    temp.append(url)
            resoucemoduel[module_name] = temp #print resoucemoduel['resource_Articles']  #print resoucemoduel['resource_Zones']
        row = 0
        col = 0
        for key in resoucemoduel.keys():
            row += 1
           
            self.worksheet.write(row, col, key)
            for item in resoucemoduel[key]:
                self.worksheet.write(row, col + 1, item)
                row += 1

        self.workbook.close()
            
#sw = Swagger_test()
#sw.api_link()


   