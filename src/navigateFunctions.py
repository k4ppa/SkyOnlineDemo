
import random
import logging

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
    device.tap(mappedText='PLAYSkyTG24')
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
    # waitColormatch



