
import stormtest.ClientAPI as StormTest
import logging

from navigateFunctions import goToCatalog
from test import _startTest, _endTest, _videoMotionTest, _videoPresentTest,\
    _audioPresentTest
from navigateFunctions import _connectionError

log = logging.getLogger("userAction")

def catalogAvailability(galaxyTab3, serviceInfo):
    if _connectionError(galaxyTab3):
        log.error("App connection error: test aborted")
        return False
    
    StormTest.BeginLogRegion('catalogBrowsing')
    video = _startTest('catalogBrowsing')
    
    catalogName = serviceInfo['name']
    result, comment, image = goToCatalog(galaxyTab3, catalogName)
    
    _endTest('catalogBrowsing', serviceInfo, result, video, comment, image)
    StormTest.EndLogRegion('catalogBrowsing')
    return result


def audioVideoScenarios(galaxyTab3, serviceInfo):
    result1 = audioPresent(galaxyTab3, serviceInfo)
    result2 = videoMotion(galaxyTab3, serviceInfo)
    result3 = videoPresent(galaxyTab3, serviceInfo)
    return result1, result2, result3


def videoMotion(galaxyTab3, serviceInfo):
    StormTest.BeginLogRegion('videoMotion')
    video = _startTest('videoMotion')
    
    result, comment, image = _videoMotionTest()
    
    _endTest('videoMotion', serviceInfo, result, video, comment, image)
    StormTest.EndLogRegion('videoMotion')
    return result


def videoPresent(galaxyTab3, serviceInfo):
    StormTest.BeginLogRegion('videoPresent')
    video = _startTest('videoPresent')
    
    result, comment, image = _videoPresentTest()
    
    _endTest('videoPresent', serviceInfo, result, video, comment, image)
    StormTest.EndLogRegion('videoPresent')
    return result


def audioPresent(galaxyTab3, serviceInfo):
    StormTest.BeginLogRegion('audioPresent')
    video = _startTest('audioPresent')
    
    result, comment = _audioPresentTest()
    
    _endTest('audioPresent', serviceInfo, result, video, comment)
    StormTest.EndLogRegion('audioPresent')
    return result
    
    

    



