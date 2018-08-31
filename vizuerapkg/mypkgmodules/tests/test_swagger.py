'''
Created on Aug 27, 2018

@author: narendra_v
'''
from vizuerapkg.mypkgmodules.attributes_file import Variables
from selenium import webdriver
from time import sleep
import xlsxwriter
import pytest
import xlrd 
import pdb
from vizuerapkg.mypkgmodules.tests.test_sample import resource


var = Variables()
module_dict = {}

class Test_Swagger():
    
    pytest.global_module_dict = module_dict
    
    '''
    def test_display_urllink(self):
        
        self.workbook = xlsxwriter.Workbook('swagger_template.xlsx')
        self.worksheet = self.workbook.add_worksheet('Dashboard')

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
                self.worksheet.write(row, col, key)
                self.worksheet.write(row, col + 1, item)
                row += 1
        print "Template -- Created Sucessfully"

        self.workbook.close()
    '''
    
    @pytest.fixture
    def global_variable(self):
    
        print pytest.module_dict
      
 
    def test_read_template(self):
        
        workbook = xlrd.open_workbook('swagger_template.xlsx')
        worksheet = workbook.sheet_by_name('Dashboard')
        module_dict = {}
        temp = []
        for i in range(1, worksheet.nrows):
            
            link = worksheet.cell(i,1).value
            resource = worksheet.cell(i,0).value
        
            if (resource != ''):#and len(resource) != 249):
        
                temp.append(link)
                key = resource
            else:
                module_dict[key] = temp
                temp = []
            
        module_dict[key] = temp
        
        pytest.module_dict = module_dict
        print pytest.module_dict
        
    
    @pytest.mark.parametrize('argument', [(var.common_url, global_variable)])
    def test_diff_in_common(self,argument):
        
        link_assigned = len(var.common_url)
        link_common = len(pytest.module_dict['resource_Common'])
        difference  = link_common - link_assigned  
        print "Difference between url and resorce name in variable class for 'resource_Common' API is", difference
        
    #@pytest.yield_fixture (params = [var.common_url, global_variable], autouse = True)
    
    @pytest.yield_fixture
    def link(self):
        print " setup before yield"#, var.common_url, pytest.module_dict
        
        temp = []
        link_assigned = len(var.common_url)
        link_common = len(pytest.module_dict['resource_Common'])
        difference  = link_common - link_assigned  
        print "Difference between url and resorce name in variable class for 'resource_Common' API is", difference
        resource_common = pytest.module_dict['resource_Common']
        for i in resource_common:
            temp.append(i)
        yield temp 
        
    @pytest.mark.usefixtures("global_variable")
    def test_link(self, link):
        print "after", link
        
    @pytest.mark.parametrize('argument', [var.all_privilage])
    def test_previlagedata(self, argument):
        ''' pass valid url as arguments
        '''
        print "tsting all previlages -----", var.all_privilage
        
        '''
        for i in range(len(link)):
            if(len(test)!= len(common)):
                test[i] = common[i]
            else:
                test[i] = common[i]
         '''
    
    
        
        
        
    '''
        link = argument[0]
        resource_common = pytest.module_dict['resource_Common']
        
        difference = len(argument[0]) - len(resource_common)
        
        print "Difference between url and resorce name in variable class for 'resource_Common' API is", difference
        
        return difference
    '''
    '''
    #@pytest.yield_fixture 
    def link(self, argument):
        print ("setup before yield")
        #link = argument[0]
        #resource_common = pytest.module_dict['resource_Common']
        #for i in resource_common:
        #    yield i 
    
    #@pytest.mark.parametrize('argument', [global_variable])
    
    def test_has_lines(self, argument):
        print ("test called"), 
    '''    
        
        
        #f = open("/etc/passwd")
        #yield f.readlines()
        #print ("teardown after yield")
        #f.close()   
        
    '''
        for i in range(len(resource_common)):
            yield i
     
        for i in test_assign_values_Common_resorces(self,argument):
        
            if(len(link)!= len(resource_common)):
            #print "Not equal" 
                link.append("difference")
                link[i] = resource_common[i]
            else:
                link[i] = resource_common[i]
    
    #@pytest.yield_fixture
    def passwd(self):
        print ("\nsetup before yield")
        f = open("/etc/passwd")
        yield f.readlines()
        print ("teardown after yield")
        f.close()
    
    def test_has_lines(self,passwd):
        print ("test called")
        assert passwd
    
        
        #print link
    
        

   '''         
        
            