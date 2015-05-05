
import stormtest.ClientAPI as StormTest
from stormtest import WarningCenter

'''
def _audioPresentTest():
    """
    Checks if audio is present
    Requires:
    - a Screen Definition file called AudioDetect.stscreen" 
    Returns:
    - result: boolean True or False
    - comment: a comment giving more details of the test result
    """

    SDO = StormTest.ScreenDefinition()
    try:
        SDO.Load('AudioDetect.stscreen')
        retSDO = StormTest.WaitScreenDefMatch(SDO)[0][1]
        result = retSDO.VerifyStatus
        actualAudio = retSDO.Regions[0].ActualAudio
        StormTest.WriteDebugLine('Result of Audio Detection is ' + str(result) + '. Actual audio level = ' + str(actualAudio))
        audioThreshold = retSDO.Regions[0].AudioThreshold
        comment = 'Audio Level = %0.3f, Audio Threshold = %0.3f' % (actualAudio, audioThreshold)
        print comment
        SDO.Close()
        return [result, comment]
    except:
        print 'Could not load AudioDetect.stscreen - exiting test'
        SDO.Close()
        return [False, 'Could not load AudioDetect.stscreen - exiting test']

'''
def _audioPresentTest():
    #print StormTest.GetAudioLevel(1)
    isPresent = StormTest.WaitAudioPresence(-95, 60)[0][1]
    if isPresent:
        return isPresent, 'Audio is present'
    else:
        return isPresent, 'Audio not present'


def _videoPresentTest():
    """
    Checks if video is present, by comparing screen colour against a black colour
    Requires:
    - a Screen Definition file called "DetectVideoPresence.stscreen"
    Returns:
    - result: boolean True or False
    - comment: a comment giving more details of the test result
    - image: a screenshot of the test
    """

    result = False
    repeat = 10
    count = 0
    SDO = StormTest.ScreenDefinition()
    try:
        SDO.Load('DetectVideoPresence.stscreen')
        while (result == False) and (count <= repeat):
            #note this SDO returns True when a match does *not* occur
            retSDO = StormTest.WaitScreenDefMatch(SDO)[0][1]
            result = retSDO.VerifyStatus
            StormTest.WriteDebugLine('Result of matching screen with black was ' + str(not result))
            count = count + 1
            if (result == False) and (count <= repeat):
                StormTest.WaitSec(4)
                StormTest.WriteDebugLine('Retry, count = ' + str(count))
        image = retSDO.Image
        image.Save('VideoPresent_%d_%t.jpeg')
        comment = 'Result of matching screen with black was ' + str(not result)
        SDO.Close()
        return [result, comment, image]
    except:
        print 'Could not load DetectVideoPresence.stscreen - exiting test'
        SDO.Close()
        return [False, 'Could not load DetectVideoPresence.stscreen - exiting test', image]


def _videoMotionTest():
    """
    Checks if there is motion present in the video
    SDO only allows threshold of 1% minumum, so we run it repeatedly for 5s and if it fails
    we check the actual motion against a threshold of 0.1%
    Requires:
    - a Screen Definition file "DetectMotion.stscreen" 
    Returns:
    - result: boolean True or False
    - comment: a comment giving more details of the test result
    - image: a screenshot of the test
    """

    result = False
    repeat = 6
    count = 0
    SDO = StormTest.ScreenDefinition()
    try:
        SDO.Load('DetectMotion.stscreen')
        #we check every 5 seconds for motion > 0.1%
        while (result == False) and (count <= repeat):
            retSDO = StormTest.WaitScreenDefMatch(SDO)[0][1]
            result = retSDO.VerifyStatus
            actualMotion = retSDO.Regions[0].ActualMotion
            StormTest.WriteDebugLine('Actual motion detected is ' + str(actualMotion))
            if actualMotion > 0.1:
                result = True
            count = count + 1

            StormTest.WriteDebugLine('Result of Motion Detection is ' + str(result))
            image = retSDO.Image
            image.Save('VideoMotion_%d_%t.jpeg')
            motionThreshold = 0.1
            comment = 'Motion Level = %0.3f, Motion Threshold = %0.3f' % (actualMotion, motionThreshold)
        SDO.Close()
        return [result, comment, image]
    except:
        print 'Could not load DetectMotion.stscreen - exiting test'
        SDO.Close()
        return [False, 'Could not load DetectMotion.stscreen - exiting test']
    
    
    
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
    pass



