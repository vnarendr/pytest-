from vizuerapkg.Http_services.http_client import Http_Client
from vizuerapkg.mypkgmodules.modules.common import Common_Task
from vizuerapkg.mypkgmodules.tests.test_common import Testing
from vizuerapkg.mypkgmodules.attributes_file import Variables


class vizuerapkg(Http_Client, Common_Task, Variables, Testing):

    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

viz = vizuerapkg()