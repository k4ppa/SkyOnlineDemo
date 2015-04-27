
import random
import logging


log = logging.getLogger("userAction")

def goToCatalog(device, catalogName):
    appCommands = device.getAppCommands()
    
    appCommands.openMenu()
    result, comment, image = appCommands.openCatalog(catalogName)
    return result, comment, image


def playRandomVideo(device):
    videoName = _pickRandomVideo(device)
    if _findVideo(device, videoName):
        return _startVideo(device)
    return False


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
    
    
def stopRandomVideo(device):
    device.tap(mappedText='closeVideo')
    device.tap(mappedText='closeVideo')
    # waitColormatch



