
import stormtest.ClientAPI as StormTest

from navigateFunctions import goToCatalog
from test import _startTest, _endTest, _videoMotionTest, _videoPresentTest,\
    _audioPresentTest


def catalogAvailability(galaxyTab3, serviceInfo):
    StormTest.BeginLogRegion('catalogBrowsing')
    video = _startTest('catalogBrowsing')
    
    catalogName = serviceInfo['name']
    result, comment, image = goToCatalog(galaxyTab3, catalogName)
    
    _endTest('catalogBrowsing', serviceInfo, result, video, comment, image)
    StormTest.EndLogRegion('catalogBrowsing')
    return result


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
    
    

    



