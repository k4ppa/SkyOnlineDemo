
import random
import logging
import stormtest.ClientAPI as StormTest
from color_match import colorMatch, colorNoMatch

log = logging.getLogger("userAction")

def goToCatalog(device, catalogName):
    appCommands = device.getAppCommands()
    if _connectionError():
        log.error("App connection error: test aborted")
        return False, "App connection error: test aborted", None
    appCommands.openMenu() 
    
    if catalogName == "Sky TG24":
        return appCommands.openSkyTG24(catalogName)
    else:
        return appCommands.openCatalog(catalogName)
    pass


def _connectionError():
    result = colorMatch(color=(230,232,232), tolerances=(16,16,16), flatness=90, peakError=20, includedAreas=(810,470,10,10), timeToWait=60, imageName='ConnectionError', comment='Connection error')
    return result [0]


def playVideo(device, serviceInfo): 
    StormTest.BeginLogRegion('Play Video')
    if serviceInfo['name'] == 'Sky TG24':
        isPlayed = _playSkyTG24(device)
        StormTest.EndLogRegion('Play Video')
        return isPlayed
        
    videoName = _pickRandomVideo(device)
    isPlayed = False
    if _findVideo(device, videoName):
        isPlayed = _startVideo(device)
    
    StormTest.EndLogRegion('Play Video')
    return isPlayed


def _playSkyTG24(device):
    device.tap(mappedText='PLAYSkyTG24')
    #StormTest.WaitSec(3)
    result = colorNoMatch(color=(41,116,168), tolerances=(16,16,16), flatness=90, peakError=80, includedAreas=[700,830,10,10], timeToWait=60, imageName='VideoPlayed', comment='Play video')
    print result
    return result[0]


def _pickRandomVideo(device):
    appCommands = device.getAppCommands()
    cinemaCatalog = appCommands.getCinemaCatalog() 
    index = random.randrange(0, len(cinemaCatalog)-1)
    
    return cinemaCatalog[index]


def _findVideo(device, videoName):
    appCommands = device.getAppCommands()
    
    if appCommands.openCatalogFind():
        return appCommands.findSelectedVideo(videoName)
    return False


def _startVideo(device):
    return device.tap(mappedText='PLAY')
    
    
def stopVideo(device):
    StormTest.BeginLogRegion('Stop Video')
    device.tap(mappedText='closeVideo')
    device.tap(mappedText='closeVideo')
    device.tap(text='No')
    
    result = colorMatch(color=(50,114,167), tolerances=(16,16,16), flatness=90, peakError=80, includedAreas=[430,80,10,10], timeToWait=60, imageName='StopVideo', comment='Match color on closing the video')
    StormTest.EndLogRegion('Stop Video')
    return result
    

def closeApp(device):
    StormTest.BeginLogRegion('Close App')
    StormTest.WaitSec(2)
    device.tap(mappedText='Home')
    
    result = colorMatch(color=(233,235,233), tolerances=(16,16,16), flatness=95, peakError=15, includedAreas=[940,990,10,10], timeToWait=60, imageName='CloseApp', comment='Match color on returning to home')
    device.stop()
    StormTest.EndLogRegion('Close App')
    return result

