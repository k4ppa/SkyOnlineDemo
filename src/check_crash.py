
from color_match import colorMatch
import stormtest.ClientAPI as StormTest
import logging

log = logging.getLogger("userAction")

def checkCrash(device):
    result = colorMatch(color=(48,50,48), tolerances=(4,4,4), flatness=99, peakError=10, includedAreas=(820,590,10,10), timeToWait=10, imageName='Crash', comment='Crash happened?')
    StormTest.WaitSec(5)
    if result[0]:
        log.error('CRASH!')
        device.tap(text='OK')
        return True
    return False