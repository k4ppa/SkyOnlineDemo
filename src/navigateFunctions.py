
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
    return _findVideo(device, videoName)


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
