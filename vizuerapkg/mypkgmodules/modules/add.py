import pytest
import pdb 

x = ''
y = ''

@pytest.fixture(scope ='module')
def add(x, y):
    pdb.set_trace()
    
    x + y
    