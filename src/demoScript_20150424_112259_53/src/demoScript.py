
import stormtest.ClientAPI as StormTest

from mobile_framework.android_device import AndroidDevice
from navigateFunctions import goToCatalog


if __name__ == '__main__':
    galaxyTab3 = AndroidDevice("samsung_galaxy_tab_3")
    galaxyTab3.connect('Warning center')
    galaxyTab3.start('it.sky.river')
    StormTest.WaitSec(6)
        
    serviceInfo = galaxyTab3.getServiceInfo()
    catalog = serviceInfo['name']
    
    goToCatalog(galaxyTab3, catalog)
    
    
    StormTest.WaitSec(3)
    galaxyTab3.disconnect()
    pass