import xlrd
import pdb
from vizuerapkg.mypkgmodules.attributes_file import Variables

var = Variables()

 

'''
customer_data_file = 'swagger_template2.xlsx'
customers = pd.read_excel(customer_data_file,
sheetname=0,
header=0,
index_col=False,
keep_default_na=True
)
print customers.head()

area_dict = dict(zip(customers.resource, customers.link))
print area_dict
'''
workbook = xlrd.open_workbook('swagger_template.xlsx')
worksheet = workbook.sheet_by_name('Dashboard')
module_dict = {}

#value_list = []
#temp = [121,4,4,4]
#print temp
#del temp[:]
#print 'tt' , temp
#module_dict = {a : b for a, b in zip(col_a, col_b)}
#print module_dict
#key = []
#temp = []

temp = []
#links = []
#resources = {}
module_dict = {}
#resourceKey = ''
#length = 0
#rowmas = worksheet.nrows
#print rowmas
#print worksheet.nrows
for i in range(1, worksheet.nrows):
    link = worksheet.cell(i,1).value
    resource = worksheet.cell(i,0).value
    #resources[resourceKey] = links
   
    if (resource != ''):#and len(resource) != 249):
    #if resource != xlrd.empty_cell.value :#and resource == True:
        temp.append(link)
        key = resource
    else:
        module_dict[key] = temp
        temp = []
        #key = []
#print key, temp
module_dict[key] = temp
#print module_dict['resource_Common']
common = module_dict.get('resource_Common')
#test = [var.all_privilage,var.event_type,var.country,var.Entity_type,var.sectors,var.profile_maturity_level,var.section_type ,var.section_classification, var.user_types ,var.expense_type,var.question_classification   ,var.time_line,var.zone_type,var.event_type_attribute ,var.event_subtype_attribute,var.ticket_type,var.ticket_status,var.ticket_entity_type,var.time_zones ,var.store_kpi_parameters,var.encode_password_url,var.previlage_on_urertype_url ,var.role_usertype ,var.cost_type ,var.common_page,"23","23","23","23","23","23"]
test = [var.all_privilage,var.event_type,var.country,var.Entity_type,var.sectors,var.profile_maturity_level,var.section_type ,var.section_classification, var.user_types ,var.expense_type,var.question_classification   ,var.time_line,var.zone_type,var.event_type_attribute ,var.event_subtype_attribute,var.ticket_type,var.ticket_status,var.ticket_entity_type,var.time_zones ,var.store_kpi_parameters,var.encode_password_url,var.previlage_on_urertype_url ,var.role_usertype ,var.cost_type ,var.common_page]

#for i in range(len(test)):
#    print test[i]
#print len(test), len(common) 
        
def assign(self):
    print len(common) , len(test)
    
    difference = len(common) - len(test)
    print "Difference between url and resorce name in variable class for 'resource_Common' API is", difference

    for i in range(len(common)):
        yield i

for i in assign(i):
    if(len(test)!= len(common)):
        #print "Not equal" 
        test.append("difference")
        test[i] = common[i]
    else:
        test[i] = common[i]
     
assign(common) 
print test

 
#var.all_privilage = common[i] 
#print common[30]
#for key, value in enumerate(common, start = 0) :
#    print key, common[key]#, value, commo
    
    #var.all_privilage = value
#print var.all_privilage
    



'''
#print module_dict['resource_LongTermInvestment']

#print resources#['resource_LongTermInvestment']

        #del temp[:]
        #del key[:]
    #module_dict[key[0]] = temp
    #k = key
        #print k[0] , len(k)        
        #print  resource, temp , type(str(k))
    

        
          
#print module_dict['resource_Roles']


    #module_dict[resource] = temp
#print module_dict
        #print "value",link, resource 
        #temp.append(link)
        #print temp
    
    '''
'''
for i in range(1 , worksheet.nrows):
 
    module_name_key = (worksheet.cell(i,0).value)
    url_name_value = (worksheet.cell(i,1).value)
    temp.append(url_name_value)
    if url_name_value ==  '' :
        #print temp, i
        module_dict[i] = temp
        #print temp,module_dict
        #print module_dict
        #print temp
        del temp[:]
'''  
    
#print module_dict
        
    
#print row[0], len(temp)
    #module_dict[row[0]] = temp

    

#print module_dict['resource_Articles']
    #print temp

    
    

'''
    #print row[0], "te", [row[1]] , len(row[0])
    
    
 
    #print row[0]
    #temp.append(row[0])

    
    #temp.append(row[1])
     
    #module_dict[row[0]] = temp
    #print i 
#print module_dict 
    
    #module_name_key = (worksheet.cell(i,0).value)
    #url_name_value = (worksheet.cell(i,1).value)
'''
'''

    
    
#print module_dict
#print module_dict['resource_Zones']
   
   # url_name =  worksheet.cell(i,1 )
   
    #temp.append(url_name)
#print temp
#module_dict[module_name.value] = temp
#print module_dict, type(module_dict)
#for key, value in module_dict.items():
#    print key, value


#data = get_data('swagger_template.xlsx')
#sheet = data['Dashboard']
#cell3 = sheet.cell(1,1)
#print cell3
#print sheet 

#s = simplejson.dumps(sheet)
 

 
#for col_index in xrange(1, len(sheet)):
#    print col_index
#pdb.set_trace()
#coll =  data['Dashboard']
#for i in coll:
#    print i
     

#data2 = simplejson.dumps(data)

    



#@pytest.fixture
def testing():
    print ' i am in fixture'

#@pytest.mark.userfixtures('testing')
def test_testing(testing):
    print 'i am in test'



the_iterable = [('sequence', var.all_privilage), ('of', 3), ('items', 0)]

#@pytest.mark.parametrize('arg1, arg2', the_iterable)
def test_name(arg1, arg2):
    # Code here makes use of each item of `the_iterable` in turn, passed
    # in as `argument_name`.
    pass

#@pytest.fixture(params=['sequence', 'of', 'items', 'etc.']) # Etc.
def test_name(argument_name):
    # Code here makes use of each item of `params` in turn, passed
    # in as `argument_name`.
    pass

def pytest_generate_tests(metafunc):
    if 'argument_name' in metafunc.fixturenames:
        metafunc.parametrize("argument_name", the_iterable)

def test_name1(argument_name):
    # Code here makes use of each item of `the_iterable` in turn, passed
    # in as `argument_name`.
    pass


#the_iterable = ['sequence', 'of', 'items', 'etc.'] # Etc.

#@pytest.mark.parametrize('argument_name', the_iterable, ids=['list', 'of', 'id-names'])
def test_name2(argument_name):
    pass


#@pytest.mark.usefixtures('add')
def test_adding(add):
    print add
   
    assert add(2,3) == int(5)

def pytest_namespace():
    return {'my_global_variable': 0}

#@pytest.fixture
def data():
    global val
    val = 20 
    

def test(data):
    print val
'''

 