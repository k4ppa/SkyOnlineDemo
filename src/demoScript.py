
import stormtest.ClientAPI as StormTest

from mobile_framework.android_device import AndroidDevice
from navigateFunctions import goToCatalog
from stormtest import WarningCenter


def _startTest(eventName):
    """
    For starting a specific test. Starts a StormTest test step, and starts a video log
    Arguments:
    - eventName - the name of the Warning Center event generated for this specific test
    """
   
    StormTest.BeginTestStep(eventName)
    video = StormTest.StartVideoLog(prefix=eventName)[0][2]
    return video


def _endTest(eventName, result, video, comment=None, screenshot=None, sendEvent = True, displayName = ""):
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


if __name__ == '__main__':
    galaxyTab3 = AndroidDevice("samsung_galaxy_tab_3")
    galaxyTab3.connect('Warning center')
    galaxyTab3.start('it.sky.river')
    StormTest.WaitSec(6)
        
    serviceInfo = galaxyTab3.getServiceInfo()
    catalog = serviceInfo['name']
    
    video = _startTest('catalogBrowsing')
    result, comment, image = goToCatalog(galaxyTab3, catalog)
    _endTest('catalogBrowsing', result, video, comment, image)
    
    
    StormTest.WaitSec(3)
    galaxyTab3.disconnect()
    pass