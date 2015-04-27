
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
        self._cinemaCatalog = ['limitless', 'divergent', 
                               'maleficent', 'amazzonia', 
                               'apocalypto', 'bears', 
                               'bee movie', 'blood', 
                               'butter', 'cellular'
                               ]
        pass
    
    
    def getCommands(self):
        allCommands = self._appCommands.copy()
        allCommands.update(self._commands)
        return allCommands
    
    
    def getCinemaCatalog(self):
        return self._cinemaCatalog
    
    
    def openMenu(self):
        self._device.tap(mappedText='OpenMenu')
        match = StormTest.WaitColorMatch((41,100,168), tolerances=(16,16,16), flatness=90, peakError=10, includedAreas=[400,430,10,10], timeToWait=30)
        
        if not match[0][1]:
            log.error('Match color failed on opening the menu {0}'.format(match))
            return False
    
        log.info('Match color successful on opening the menu {0}'.format(match))
        return True
    
    
    def openCatalog(self, catalogName):
        self._device.tap(text=catalogName)     
        
        StormTest.WaitSec(5)
        
        match = StormTest.WaitColorNoMatch((41,116,168), tolerances=(16,16,16), flatness=10, peakError=85, includedAreas=[495,280,663,445], timeToWait=60)
        image = StormTest.CaptureImageEx(None, 'Cinema', slotNo=True)[2]
        
        if not match[0][1]:
            comment = 'No match color failed on opening {0} catalog {1}'.format(catalogName, match)
            log.error(comment)
            return False, comment, image
    
        comment = 'No match color successful on opening {0} catalog {1}'.format(catalogName, match)
        log.info(comment)
        return True, comment, image
        
        
    def openCatalogFind(self):
        self._device.tap(text="Cerca nel catalogo. Double tap to edit.")
        
        StormTest.WaitSec(5)
        
        match = StormTest.WaitColorMatch((197,199,200), tolerances=(16,16,16), flatness=80, peakError=85, includedAreas=[1200,1000,10,10], timeToWait=60)
        StormTest.CaptureImageEx(None, 'Keyboard', slotNo=True)[2]
        
        if not match[0][1]:
            comment = 'Match color failed on opening the keyboard {0}'.format(match)
            log.error(comment)
            return False
    
        comment = 'Match color successful on opening the keyboardcatalog {0}'.format(match)
        log.info(comment)
        return True
    
    
    def findSelectedVideo(self, videoName):
        self._device.enterText(videoName)
        self._device.tap(mappedText='Find')
        
        match = StormTest.WaitColorMatch((233,235,233), (16,16,16), flatness=95, peakError=50, includedAreas=[404,633,8,7], timeToWait=60)
        StormTest.CaptureImageEx(None, 'PlayVideo', slotNo=True)[2]
        
        if not match[0][1]:
            comment = 'Match color failed on playing the video {0}'.format(match)
            log.error(comment)
            return False
    
        comment = 'Match color successful on playing the video {0}'.format(match)
        log.info(comment)
        return True
        
        
        
        
    