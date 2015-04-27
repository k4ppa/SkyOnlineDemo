
import os
import logging.config

import stormtest.ClientAPI as StormTest

from mobile_framework.connect_functions import _getTestRunConfiguration
from mobile_framework.connect_functions import _setUpEnvironment
from mobile_framework.connect_functions import _establishConnection
from mobile_framework.common_user_actions_functions import _tapWithMappedText


class MobileDevice(object):
    
    def __init__(self):
        self._server = ""
        self._description = ""
        self._slot = 0
        self._serviceInfo = None
        
        path = os.path.abspath('')
        #print path
        #path = path[:path.rfind("mobile_framework")]
        #print path
        path = path.replace('\\', '/')
        logging.config.fileConfig(path + '/mobile_framework/log.conf')
        
        self._connectionLog = logging.getLogger('connection')
        self._userActionLog = logging.getLogger('userAction')
        pass

    
    def connect(self, description=''):
        self._connectionLog.info(description)
        self._connectionLog.info("Started connection with the server")    
        self._serviceInfo = _getTestRunConfiguration()['service']
        
        self._server, self._slot = _setUpEnvironment()
        self._connectionLog.debug("server:slot = {}:{}".format(self._server, self._slot))
        return _establishConnection(self._server, self._slot, description)     
    
    
    def disconnect(self):
        StormTest.BeginLogRegion('Close Connection')
        self._connectionLog.info("Closing connection with the server")
        logging.shutdown()
        isClosed = StormTest.ReleaseServerConnection()
        StormTest.EndLogRegion('Close Connection')
        return isClosed
    
    
    def tap(self, appCommands, mappedText=None):       
        commands = appCommands.getCommands()  
        if mappedText:
            return _tapWithMappedText(commands, mappedText)
        
        
    def enterText(self, text):
        specialChars = ['@']
        upperChars = ['A', 'B', 'C']
        
        for c in text:
            if c in specialChars:
                if not self.tap(mappedText='Sym'):
                    return False
                StormTest.WaitSec(1)
                if not  self.tap(mappedText=c):
                    return False
                StormTest.WaitSec(1)
                if not self.tap(mappedText='Sym'):
                    return False
                StormTest.WaitSec(1)
                continue
            if c in upperChars:
                if not self.tap(mappedText='Shift'):
                    return False
                StormTest.WaitSec(1)
                if not self.tap(mappedText=c):
                    return False
                StormTest.WaitSec(1)
                continue
            if not self.tap(mappedText=c):
                return False
            StormTest.WaitSec(1)
        return True 


    def getServiceInfo(self):
        return self._serviceInfo
    
    
    def getAssistanceMenu(self):
        return self._assistanceMenu
