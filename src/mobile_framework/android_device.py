
import logging

import stormtest.ClientAPI as StormTest

from mobile_framework.mobile_device import MobileDevice
from mobile_framework.android_user_actions_functions import _tapWithText, _tapWithIndex, _tapWithDesc
from mobile_framework.common_user_actions_functions import _loadDeviceCommands, _loadAppCommands


log = logging.getLogger("userAction")

class AndroidDevice(MobileDevice):
    
    def __init__(self, deviceName):
        MobileDevice.__init__(self)
        
        self._deviceName = deviceName
        self._appName = ''
        self._commandsModuleName = "mobile_framework.mapped_commands.android_commands.{0}".format(self._deviceName)
        
        self._appCommands = _loadDeviceCommands(self._commandsModuleName)
        pass
    
    
    def start(self, appName=''):
        self._appName = appName
        self._appCommands = _loadAppCommands(self, appName, self._commandsModuleName)
                             
        self.connect('')
                          
        self._userActionLog.info("Started application %s" % self._appName)
        return StormTest.PressButton("START-ANDROID:" + self._appName)

    
    def stop(self):
        self._userActionLog.info("Stopped application %s" % self._appName)
        if not StormTest.PressButton("STOP-ANDROID"):
            self._userActionLog.error("Stop application failed. Disconnection will continue")
        pass

    
    def tap(self, mappedText=None, text=None, desc=None, index=None):
        if text:
            return _tapWithText(text)
        
        if desc:
            return _tapWithDesc(desc)
        
        if index:
            return _tapWithIndex(index)
        
        return super(AndroidDevice, self).tap(self._appCommands, mappedText)
    
    
    def swipe(self, coordinates=[0, 0, 0, 0, 0]):
        log.info("Swipe from ({0}, {1}) to ({2}, {3}) with time {4}".format(coordinates[0], coordinates[1], coordinates[2], coordinates[3], coordinates[4]))
        return StormTest.PressButton("SWIPE:{0}:{1}:{2}:{3}:{4}".format(coordinates[0], coordinates[1], coordinates[2], coordinates[3], coordinates[4]))
        
    
    def getAppCommands(self):
        return self._appCommands
    
    
    def recharge(self, rechargeTime):
        time = str(rechargeTime)
        StormTest.PressButton("LOCK:{0}".format(time))
        StormTest.WaitSec(rechargeTime + 20)
        StormTest.PressButton('SWIPE:1000:400:500:400')
        StormTest.WaitSec(5)
        pass




