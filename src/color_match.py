
import logging
import stormtest.ClientAPI as StormTest


log = logging.getLogger("userAction")

def colorMatch(color, tolerances, flatness, peakError, includedAreas, timeToWait, imageName, comment):
    match = StormTest.WaitColorMatch(color=color, tolerances=tolerances, flatness=flatness, peakError=peakError, includedAreas=includedAreas, timeToWait=timeToWait)
    image = StormTest.CaptureImageEx(None, imageName, slotNo=True)[2]
    comment = comment + '{0}'.format(match)
    matched = match[0][1]
    
    _logColorMatch(matched, comment)
    return matched, comment, image
    

def _logColorMatch(matched, comment):
    if not matched:
        log.error(comment)
    else:
        log.info(comment)
    
    
def colorNoMatch(color, tolerances, flatness, peakError, includedAreas, timeToWait, imageName, comment):
    noMatch = StormTest.WaitColorNoMatch(color=color, tolerances=tolerances, flatness=flatness, peakError=peakError, includedAreas=includedAreas, timeToWait=timeToWait)
    image = StormTest.CaptureImageEx(None, imageName, slotNo=True)[2]
    comment = comment + '{0}'.format(noMatch)
    noMatched = noMatch[0][1]
    
    _logColorMatch(noMatched, comment + str(noMatch))
    return noMatched, comment, image
    
    