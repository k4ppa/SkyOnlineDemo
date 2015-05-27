
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
                    'PLAY':{'x':270,'y':520,'time':0},
                    'closeVideo':{'x':1265,'y':15,'time':0},
                    'PLAYSkyTG24':{'x':170,'y':270,'time':0},
                    #'':{'x':, 'y':, 'time':}
                    } 
        self._cinemaCatalog = ['the wire ep.1', 'the wire ep.2',
                               'the wire ep.3', 'the wire ep.4',
                               'the wire ep.5', 'the wire ep.6',
                               'the wire ep.7', 'the wire ep.8',
                               'the wire ep.9', 'the wire ep.10',
                               'the wire ep.11', 'the wire ep.12',
                               'the wire ep.13', 
                               '1992 ep.1', '1992 ep.2',
                               '1992 ep.3', '1992 ep.4',
                               '1992 ep.5', '1992 ep.6',
                               '1992 ep.7', '1992 ep.8',
                               '1992 ep.9', '1992 ep.10',
                               'big love ep.1', 'big love ep.2',
                               'big love ep.3',
                               'borgia ep.1', 'borgia ep.2',
                               'borgia ep.3', 'borgia ep.4',
                               'borgia ep.5', 'borgia ep.6',
                               'borgia ep.7', 'borgia ep.8',
                               'borgia ep.9', 'borgia ep.10',
                               'borgia ep.11', 'borgia ep.12',
                               'borgia ep.13', 'borgia ep.14',
                               'the royals ep.1', 'the royals ep.2',
                               'the royals ep.3', 'the royals ep.4',
                               'the royals ep.5', 'the royals ep.6',
                               'the royals ep.7', 'the royals ep.8',
                               'the royals ep.9', 'the royals ep.10',
                               'the fall ep.1', 'the fall ep.2',
                               'the fall ep.3',
                               'banshee ep.1', 'banshee ep.2',
                               'banshee ep.3', 'banshee ep.4',
                               'banshee ep.5',
                               'the knick ep.2', 'the knick ep.3',
                               'the knick ep.4', 'the knick ep.5',
                               'the knick ep.6', 'the knick ep.7',
                               'the knick ep.8', 'the knick ep.9',
                               'the knick ep.10',
                               'band of brothers ep.1', 'band of brothers ep.2',
                               'band of brothers ep.3', 'band of brothers ep.4',
                               'band of brothers ep.5', 'band of brothers ep.6', 
                               'band of brothers ep.7', 'band of brothers ep.8', 
                               'band of brothers ep.9', 'band of brothers ep.10',
                               'the listener ep.1', 'the listener ep.2', 
                               'the listener ep.3', 'the listener ep.4', 
                               'the listener ep.5', 'the listener ep.6', 
                               'the listener ep.7', 'the listener ep.8', 
                               'the listener ep.9', 'the listener ep.10', 
                               'the listener ep.11', 'the listener ep.12',
                               'the walking dead ep.1', 'the walking dead ep.2', 
                               'the walking dead ep.3', 'the walking dead ep.4', 
                               'the walking dead ep.5', 'the walking dead ep.6', 
                               'the walking dead ep.7', 'the walking dead ep.8', 
                               'the walking dead ep.9', 'the walking dead ep.10'     
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
    
    
    def openSkyTG24(self, catalogName):
        self._device.tap(text=catalogName)
        
        match = StormTest.WaitColorMatch(color=(233,235,233), tolerances=(16,16,16), flatness=95, peakError=15, includedAreas=[322,362,7,7], timeToWait=60)
        image = StormTest.CaptureImageEx(None, 'Catalog', slotNo=True)[2]
        
        if not match[0][1]:
            comment = 'Match color failed on opening {0} catalog {1}'.format(catalogName, match)
            log.error(comment)
            return False, comment, image
    
        comment = 'Match color successful on opening {0} catalog {1}'.format(catalogName, match)
        log.info(comment)
        return True, comment, image
    
    
    def openCatalog(self, catalogName):
        self._device.tap(text=catalogName)     
         
        StormTest.WaitSec(5)
        
        match1 = StormTest.WaitColorNoMatch(color=(41,116,168), tolerances=(16,16,16), flatness=10, peakError=85, includedAreas=[495,280,663,445], timeToWait=60)
        image = StormTest.CaptureImageEx(None, 'Catalog', slotNo=True)[2]
        
        if not match1[0][1]:
            comment = 'No match color of the poster failed on opening {0} catalog {1}'.format(catalogName, match1)
            log.error(comment)
            return False, comment, image
    
        comment = 'No match color of the poster successful on opening {0} catalog {1}'.format(catalogName, match1)
        log.info(comment)
        
        
        # match color sulla barra del menu blu
        match2 = StormTest.WaitColorMatch(color=(15,15,75), tolerances=(16,16,16), flatness=95, peakError=20, includedAreas=[1770,140,10,10], timeToWait=60)
        image = StormTest.CaptureImageEx(None, 'Catalog2', slotNo=True)[2]
        
        if not match2[0][1]:
            comment = 'Match color of the dark blue menu failed on opening {0} catalog {1}'.format(catalogName, match2)
            log.error(comment)
            return False, comment, image
    
        comment = 'Match color of the dark blue menu successful on opening {0} catalog {1}'.format(catalogName, match2)
        log.info(comment)
        
        if match1 and match2:
            return True, comment, image
        else:
            return False, comment, image
        
        
    def openCatalogFind(self):
        self._device.tap(text="Cerca nel catalogo. Double tap to edit.")
        
        StormTest.WaitSec(5)
        
        match = StormTest.WaitColorMatch((197,199,200), tolerances=(16,16,16), flatness=80, peakError=85, includedAreas=[1200,1000,10,10], timeToWait=60)
        StormTest.CaptureImageEx(None, 'Keyboard', slotNo=True)[2]
        
        if not match[0][1]:
            comment = 'Match color failed on opening the keyboard {0}'.format(match)
            log.error(comment)
            return False
    
        comment = 'Match color successful on opening the keyboard catalog {0}'.format(match)
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
        
        
        
        
    