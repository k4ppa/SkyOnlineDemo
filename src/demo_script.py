
import stormtest.ClientAPI as StormTest

from mobile_framework.android_device import AndroidDevice
from scenario import catalogAvailability, audioVideoScenarios
from navigateFunctions import playVideo, stopVideo, closeApp
from recharge_device import rechargeDevice


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
        StormTest.WaitSec(20)
        result1, result2, result3 = audioVideoScenarios(galaxyTab3, serviceInfo)
        results.append(result1)
        results.append(result2)
        results.append(result3)
        stopVideo(galaxyTab3)
    
    rechargeDevice(galaxyTab3)
    closeApp(galaxyTab3)    
    
    print results
    if False in results:
        retVal = StormTest.TM.FAIL
    else:
        retVal = StormTest.TM.PASS
    
    galaxyTab3.disconnect()
    StormTest.ReturnTestResult(retVal, False)
    pass


