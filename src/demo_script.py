
import stormtest.ClientAPI as StormTest

from mobile_framework.android_device import AndroidDevice
from scenario import catalogAvailability, videoMotion, videoPresent,\
    audioPresent
from navigateFunctions import playVideo, stopVideo



def audioVideoScenarios(galaxyTab3, serviceInfo):
    results= []
    
    result = audioPresent(galaxyTab3, serviceInfo)
    results.append(result)
    result = videoMotion(galaxyTab3, serviceInfo)
    results.append(result)
    result = videoPresent(galaxyTab3, serviceInfo)
    results.append(result)
    return results


if __name__ == '__main__':
    results= []
      
    galaxyTab3 = AndroidDevice("samsung_galaxy_tab_3")
    galaxyTab3.connect('Warning center')
    galaxyTab3.start('it.sky.river')
    StormTest.WaitSec(6)
        
    serviceInfo = galaxyTab3.getServiceInfo()
        
    result = catalogAvailability(galaxyTab3, serviceInfo)
    results.append(result)
    
    if playVideo(galaxyTab3, serviceInfo):
        results = audioVideoScenarios(galaxyTab3, serviceInfo)
    stopVideo(galaxyTab3)
    
    print results
    if False in results:
        retVal = StormTest.TM.FAIL
    else:
        retVal = StormTest.TM.PASS
    
    galaxyTab3.disconnect()
    StormTest.ReturnTestResult(retVal, False)
    pass


