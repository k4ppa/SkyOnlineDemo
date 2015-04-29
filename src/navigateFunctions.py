
import random
import logging
import stormtest.ClientAPI as StormTest

log = logging.getLogger("userAction")

def goToCatalog(device, catalogName):
    appCommands = device.getAppCommands()
    appCommands.openMenu() 
    
    if catalogName == "Sky TG24":
        return appCommands.openSkyTG24(catalogName)
    else:
        return appCommands.openCatalog(catalogName)
    pass


def playVideo(device, serviceInfo): 
    if serviceInfo['name'] == 'Sky TG24':
        return _playSkyTG24(device)
    
    videoName = _pickRandomVideo(device)
    if _findVideo(device, videoName):
        return _startVideo(device)
    return False


def _playSkyTG24(device):
    # waitColor match
    return device.tap(mappedText='PLAYSkyTG24')
    #waitColorMatch ?


def _pickRandomVideo(device):
    appCommands = device.getAppCommands()
    cinemaCatalog = appCommands.getCinemaCatalog() 
    index = random.randrange(0, 10)
    
    return cinemaCatalog[index]


def _findVideo(device, videoName):
    appCommands = device.getAppCommands()
    
    if appCommands.openCatalogFind():
        return appCommands.findSelectedVideo(videoName)
    return False


def _startVideo(device):
    return device.tap(mappedText='PLAY')
    # waitColomatch?
    
    
def stopVideo(device):
    device.tap(mappedText='closeVideo')
    device.tap(mappedText='closeVideo')
    
    match = StormTest.WaitColorMatch(color=(50,114,167), tolerances=(16,16,16), flatness=90, peakError=80, includedAreas=[430,80,10,10], timeToWait=60)
    image = StormTest.CaptureImageEx(None, 'Home', slotNo=True)[2]
    
    if not match[0][1]:
        comment = 'Match color failed on closing the video'
        log.error(comment)
        return False, comment, image
    
    comment = 'Match color successful on closing the video'
    log.info(comment)
    
    return True, comment, image



def closeApp(device):
    StormTest.BeginLogRegion('Close App')
    StormTest.WaitSec(2)
    device.tap(mappedText='Home')
    
    match = StormTest.WaitColorMatch(color=(233,235,233), tolerances=(16,16,16), flatness=95, peakError=15, includedAreas=[940,990,10,10], timeToWait=60)
    image = StormTest.CaptureImageEx(None, 'Home', slotNo=True)[2]
    
    if not match[0][1]:
        comment = 'Match color failed on returning to Home'
        log.error(comment)
        return False, comment, image
    
    comment = 'Match color successful on returning to Home'
    log.info(comment)
    
    device.stop()
    StormTest.EndLogRegion('Close App')
    return True, comment, image


