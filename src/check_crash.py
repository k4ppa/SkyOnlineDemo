
from color_match import colorMatch


def checkCrash(device):
    result = colorMatch(color=(40,40,40), tolerances=(16,16,16), flatness=95, peakError=20, includedAreas=(820,590,10,10), timeToWait=10, imageName='Crash', comment='Crash happened?')
    if result[0]:
        device.tap(text='OK')
        #StormTest.WaitSec(5)
        return True
    return False