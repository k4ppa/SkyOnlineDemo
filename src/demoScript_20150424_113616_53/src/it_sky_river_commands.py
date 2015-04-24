
import logging
import stormtest.ClientAPI as StormTest

from mobile_framework.mapped_commands.android_commands.samsung_galaxy_tab_3.device_commands import DeviceCommands


log = logging.getLogger("userAction")

class AppCommands(DeviceCommands):
    
    
    def __init__(self, device):
        DeviceCommands.__init__(self)
        
        self._device = device
        self._appCommands = {
                    'OpenMenu':{'x':30, 'y':50, 'time':0},
                    'CloseMenu':{'x':320,'y':50,'time':0},
                    'Home':{'x':630,'y':55,'time':1},
                    #'':{'x':, 'y':, 'time':}
                    } 
        pass
    
    
    def getCommands(self):
        allCommands = self._appCommands.copy()
        allCommands.update(self._commands)
        return allCommands
    
    
    def openMenu(self):
        self._device.tap(mappedText='OpenMenu')
        match = StormTest.WaitColorNoMatch((41,100,168), tolerances=(16,16,16), flatness=90, peakError=10, includedAreas=[400,430,10,10], timeToWait=30)
        
        if not match[0][1]:
            log.error('Match color failed on opening the menu {0}'.format(match))
            return False
    
        log.info('Match color successful on opening the menu {0}'.format(match))
        return True
    
    
    def openCatalog(self, catalogName):
        self._device.tap(text=catalogName)
        StormTest.WaitSec(5)
        StormTest.CaptureImageEx((0,0,1600,900), 'Screenshot.jpg')
        pass
        
        
        
        
        
        
        
    