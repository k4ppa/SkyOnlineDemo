
import random
import logging
import stormtest.ClientAPI as StormTest


log = logging.getLogger("userAction")

def goToCatalog(device, catalogName):
    appCommands = device.getAppCommands()
    
    appCommands.openMenu()
    result, comment, image = appCommands.openCatalog(catalogName)
    return result, comment, image


def playRandomVideo(device):
    videoName = _pickRandomVideo()
    _findVideo(device, videoName)
    pass


def _pickRandomVideo():
    cinemaCatalog = ['limitless', 'divergent', 'maleficent', 'amazzonia', 'apocalypto', 'bears', 'bee movie', 'blood', 'butter', 'cellular'] 
    index = random.randrange(0, 10)
    
    return cinemaCatalog[index]


def _findVideo(device, videoName):
    appCommands = device.getAppCommands()
    
    if appCommands.openCatalogFind():
        device.enterText(videoName)
        device.tap(mappedText='Find')
        StormTest.WaitSec(6)
        match = StormTest.WaitColorMatch((233,235,233), (16,16,16), flatness=95, peakError=50, includedAreas=[404,633,8,7], timeToWait=60)
        StormTest.CaptureImageEx(None, 'PlayVideo', slotNo=True)[2]
        
        if not match[0][1]:
            comment = 'Match color failed on playing the video {0}'.format(match)
            log.error(comment)
            return False
    
        comment = 'Match color successful on playing the video {0}'.format(match)
        log.info(comment)
        return True
    return False
