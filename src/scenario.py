
import stormtest.ClientAPI as StormTest

from stormtest import WarningCenter
from navigateFunctions import goToCatalog


results = {}

def _startTest(eventName):
    """
    For starting a specific test. Starts a StormTest test step, and starts a video log
    Arguments:
    - eventName - the name of the Warning Center event generated for this specific test
    """
   
    StormTest.BeginTestStep(eventName)
    video = StormTest.StartVideoLog(prefix=eventName)[0][2]
    return video


def _endTest(eventName, serviceInfo, result, video, comment=None, screenshot=None, sendEvent = True, displayName = ""):
    """
    For ending a specific test. 
    Stores the result, and captures a screenshot if one was not passed in. 
    Stops the video log.
    Sends an event to Warning Center.
    Completes the StormTest test step.
    Arguments:
    - eventName - the name of the Warning Center event generated for this specific test. This must be one of the
       event names from the data model - see programmer's guide.
    - result - the result (True or False) of the test
    - video - the name of the video log
    - comment - a comment to appear for this event
    - screenshot - a screenshot to appear for this event
    - sendEvent - boolean indicating whether to actually send an event to Warning Center
    - displayName - this can be used to send back a more detailed service name, different from the service name
       received from GetTestRun. It allows to differentiate between different events on the same service type.
    """

    global results
    
    results[eventName] = result
   
    if screenshot is None:
        screenshot = StormTest.CaptureImageEx(None,eventName + '_%d_%t.jpeg')[0][3]
    StormTest.StopVideoLog()

    if result:
        testStepResult = StormTest.TM.PASS
    else:
        testStepResult = StormTest.TM.FAIL

    serviceInfoToSend = serviceInfo
    if displayName != "":
        serviceInfoToSend['name'] = displayName

    if sendEvent:
        origServiceName = serviceInfo['name']
        if displayName != "":
            serviceInfo['name'] = displayName
        WarningCenter.SendEvent(name=eventName,
                value=result,
                service=serviceInfo,
                screenshot=screenshot,
                video=video)
        serviceInfo['name'] = origServiceName
    StormTest.EndTestStep(eventName, testStepResult, comment)


def catalogAvailability(galaxyTab3, serviceInfo):
    StormTest.BeginLogRegion('catalogBrowsing')
    video = _startTest('catalogBrowsing')
    
    catalogName = serviceInfo['name']
    result, comment, image = goToCatalog(galaxyTab3, catalogName)
    
    _endTest('catalogBrowsing', serviceInfo, result, video, comment, image)
    StormTest.EndLogRegion('catalogBrowsing')
    pass


def videoMotion(galaxyTab3, serviceInfo):
    #StormTest.BeginLogRegion('videoMotion')
    #video = _startTest('videoMotion')
    
    #result, comment, image = videoMotionTest(galaxyTab3)
    
    #_endTest('videoMotion', serviceInfo, result, video, comment, image)
    #StormTest.EndLogRegion('videoMotion')
    pass


def videoPresent(galaxyTab3, serviceInfo):
    #StormTest.BeginLogRegion('videoPresent')
    #video = _startTest('videoPresent')
    
    #result, comment, image = videoPresentTest(galaxyTab3)
    
    #_endTest('videoPresent', serviceInfo, result, video, comment, image)
    #StormTest.EndLogRegion('videoPresent')
    pass


def audioPresent(galaxyTab3, serviceInfo):
    #StormTest.BeginLogRegion('audioPresent')
    #video = _startTest('audioPresent')
    
    #result, comment, image = audioPresentTest(galaxyTab3)
    
    #_endTest('audioPresent', serviceInfo, result, video, comment, image)
    #StormTest.EndLogRegion('audioPresent')
    pass
    
    
    



