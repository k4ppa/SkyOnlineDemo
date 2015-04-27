
import stormtest.ClientAPI as StormTest

from mobile_framework.android_device import AndroidDevice
from scenario import catalogAvailability, videoMotion, videoPresent,\
    audioPresent
from navigateFunctions import playVideo, stopVideo



def audioVideoScenarios(galaxyTab3, serviceInfo):
    results = []
    
    result1 = audioPresent(galaxyTab3, serviceInfo)
    results.append(result)
    result2 = videoMotion(galaxyTab3, serviceInfo)
    results.append(result)
    result3 = videoPresent(galaxyTab3, serviceInfo)
    results.append(result)
    return result1, result2, result3


if __name__ == '__main__':
    results= []
      
    galaxyTab3 = AndroidDevice("samsung_galaxy_tab_3")
    galaxyTab3.connect('Warning center')
    galaxyTab3.start('it.sky.river')
    StormTest.WaitSec(6)
        
    serviceInfo = galaxyTab3.getServiceInfo()
        
    result = catalogAvailability(galaxyTab3, serviceInfo)
    results.append(result)
    
    if results[0] and playVideo(galaxyTab3, serviceInfo):
        result1, result2, result3 = audioVideoScenarios(galaxyTab3, serviceInfo)
        results.append(result1)
        results.append(result2)
        results.append(result3)
    stopVideo(galaxyTab3)
    
    print results
    if False in results:
        retVal = StormTest.TM.FAIL
    else:
        retVal = StormTest.TM.PASS
    
    galaxyTab3.disconnect()
    StormTest.ReturnTestResult(retVal, False)
    pass


