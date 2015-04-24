
import stormtest.ClientAPI as StormTest

from mobile_framework.android_device import AndroidDevice


if __name__ == '__main__':
    galaxyTab3 = AndroidDevice()
    galaxyTab3.connect('Warning center')
    galaxyTab3.start('sky.it.river')
        
    serviceInfo = galaxyTab3.getServiceInfo()
    catalog = serviceInfo['name']
    
    galaxyTab3.tap(mappedText='OpenMenu')
    galaxyTab3.tap(text=catalog)
    
    
    StormTest.WaitSec(3)
    galaxyTab3.disconnect()
    pass