
import random
import logging
import stormtest.ClientAPI as StormTest
from color_match import colorMatch, colorNoMatch
from check_crash import checkCrash

log = logging.getLogger("userAction")

def goToCatalog(device, catalogName):
    appCommands = device.getAppCommands()
    if _connectionError():
        log.error("App connection error: test aborted")
        return False, "App connection error: test aborted", None
    if appCommands.openMenu():
        _checkLogin(device) 
        
        if catalogName == "Sky TG24":
            if checkCrash(device):
                return False, "", None
            else:
                return appCommands.openSkyTG24(catalogName)    
        else:
            if checkCrash(device):
                return False, "", None
            else:
                return appCommands.openCatalog(catalogName)
    else:
        checkCrash(device)
        return False, "", None
    pass


def _connectionError():
    result = colorMatch(color=(230,232,232), tolerances=(16,16,16), flatness=90, peakError=20, includedAreas=(810,470,10,10), timeToWait=30, imageName='ConnectionError', comment='Connection error')
    return result[0]


def _checkLogin(device):
    image = StormTest.CaptureImageEx((0,0,1920,1080), 'checkLogin')[0][2]
    resultString = StormTest.OCRImage(image, (237,58,140,31))[4]
    log.debug("OCR result: {0}".format(resultString))
    if resultString != 'Benvenuto':
        login(device)
    log.info('App logged in')
    pass


def login(device):
    log.warning('App not logged')
    __enterEmail(device)
    __enterPassword(device)
    device.tap(text='Accedi')
    StormTest.WaitSec(7)
    pass


def __enterEmail(device):
    email = 'fabio.clabot@altran.it'
    
    device.tap(text='Indirizzo mail. Editing.')
    colorMatch(color=(197,199,200), tolerances=(16,16,16), flatness=80, peakError=85, includedAreas=[1200,1000,10,10], timeToWait=60, imageName='enterEmail', comment='entering email for login')
    log.info('Enter email: {0}'.format(email))
    device.enterText(email)
    pass


def __enterPassword(device):
    password = 'altran123'
    
    device.tap(text='Enter password.. Double tap to edit.')
    colorMatch(color=(197,199,200), tolerances=(16,16,16), flatness=80, peakError=85, includedAreas=[1200,1000,10,10], timeToWait=60, imageName='enterPassword', comment='entering password for login')
    log.info('Enter password: {0}'.format(password))
    device.enterText(password)
    pass


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
    checkCrash(device)
    return result
    

def closeApp(device):
    StormTest.BeginLogRegion('Close App')
    StormTest.WaitSec(2)
    device.tap(mappedText='Home')
    
    result = colorMatch(color=(233,235,233), tolerances=(16,16,16), flatness=95, peakError=15, includedAreas=[940,990,10,10], timeToWait=60, imageName='CloseApp', comment='Match color on returning to home')
    if not result:
        device.tap(mappedText='Home')
        colorMatch(color=(233,235,233), tolerances=(16,16,16), flatness=95, peakError=15, includedAreas=[940,990,10,10], timeToWait=60, imageName='CloseApp', comment='Match color on returning to home')
    device.stop()
    StormTest.EndLogRegion('Close App')
    return result

