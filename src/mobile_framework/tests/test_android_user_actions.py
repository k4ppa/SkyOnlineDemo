
import unittest

import stormtest.ClientAPI as StormTest

from mobile_framework.android_device import AndroidDevice
from win32con import DEVICE_DEFAULT_FONT


class Test(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        super(Test, self).setUpClass()
        self.device = AndroidDevice("samsung_galaxy_tab_3")
        self.device.start("it.sky.river")
        
        appLoaded = StormTest.WaitColorMatch((207,209,207), tolerances=(16,16,16), flatness=90, peakError=50, includedAreas=[1000,750,10,10], timeToWait=15)
        if not appLoaded:
            return False
        pass


    @classmethod
    def tearDownClass(cls):
        super(Test, cls).tearDownClass()
        cls.device.stop()
        pass
    
    
    def test_tap_using_mapped_text(self):
        print "TEST TAP MAPPED TEXT"
        
        isOpenPressed = self.device.tap(mappedText='OpenMenu')
        colorMatch = StormTest.WaitColorMatch((66,171,159), tolerances=(16,16,16), flatness=90, peakError=50, includedAreas=[420,300,10,10], timeToWait=10)
        isOpen = colorMatch[0][1]
        print "Open menu " + str(colorMatch)
        
        StormTest.WaitSec(1)
        
        isClosePressed = self.device.tap(mappedText='CloseMenu')
        colorNoMatch = StormTest.WaitColorNoMatch((41,100,168), tolerances=(16,16,16), flatness=90, peakError=50, includedAreas=[400,430,10,10], timeToWait=10)
        isClose = colorNoMatch[0][1]
        print "Close menu " + str(colorNoMatch)
        
        self.assertTrue(isOpenPressed, "Tap failed")
        self.assertTrue(isOpen, "Tap failed")
        self.assertTrue(isClosePressed, "Tap failed")
        self.assertTrue(isClose, "Tap failed")
        pass
    
    
    def test_tap_element_using_text(self):
        print "TEST TAP ELEMENT USING TEXT"
        self.device.tap(mappedText='OpenMenu')
        StormTest.WaitSec(4)
        
        isPressed = self.device.tap(text='Cinema')
        colorMatch = StormTest.WaitColorMatch((0,0,68), tolerances=(16,16,16), flatness=90, peakError=50, includedAreas=[600,140,10,10], timeToWait=10)
        isCinema = colorMatch[0][1]
        print "Open cinema " + str(colorMatch)
        
        StormTest.WaitSec(1)
        
        self.device.tap(mappedText='Home')
        #colorNoMatch = StormTest.WaitColorNoMatch((0,0,68), tolerances=(16,16,16), flatness=90, peakError=50, includedAreas=[400,430,10,10], timeToWait=15)
        colorMatch = StormTest.WaitColorMatch((40,120,178), tolerances=(16,16,16), flatness=90, peakError=50, includedAreas=[1000,750,10,10], timeToWait=10)
        StormTest.CaptureImageEx((0,0,1920,1080), "Screenshot")
        isHome = colorMatch[0][1]
        print "Return to Home " + str(colorMatch)
        #StormTest.WaitSec(6)
        
        self.assertTrue(isPressed, "Tap on Cinema failed")
        self.assertTrue(isCinema, "Tap on Cinema failed")
        pass
    
    
    def test_import_non_existent_device_commands_module_should_throw_an_exception(self):
        print "TEST IMPORT NON EXISTENT DEVICE COMMANDS MODULE SHOULD THROW AN EXCEPTION"
        
        self.assertRaises(ImportError, AndroidDevice, "samsung_galaxy_fake")
        pass
    
    
    def test_import_non_existent_app_commands_module_should_throw_an_exception(self):
        print "TEST IMPORT NON EXISTENT APP COMMANDS MODULE SHOULD THROW AN EXCEPTION"
        newDevice = AndroidDevice("samsung_galaxy_tab_3")
        
        self.assertRaises(ImportError, newDevice.start, "fake_app")
        pass
    
    @unittest.skip("demonstrating skipping")
    def test_swipe(self):
        print "TEST SWIPE"
        swipeDown = self.device.swipe([700, 700, 700, 200, 0])
        swipeUp = self.device.swipe([700, 200, 700, 700, 0])
        
        self.assertTrue(swipeDown, "Swipe failed")
        self.assertTrue(swipeUp, "Swipe failed")
        pass
    
    @unittest.skip("demonstrating skipping")
    def test_enter_email(self):
        print "TEST ENTER EMAIL"
        self.device.tap(mappedText='OpenMenu')
        self.device.tap(text='Indirizzo mail. Editing.')
        StormTest.WaitSec(2)
        isEmailEntered = self.device.enterText("fabio.clabot@altran.com")
        self.device.tap(mappedText='OpenAssistantMenu')
        self.device.tap(mappedText='CloseAssistantMenu')
        self.device.tap(mappedText='CloseMenu')
        
        self.assertTrue(isEmailEntered, "Fail to enter text")
        pass
    
    '''
    @unittest.expectedFailure
    def test_tap_element_using_desc(self):
        print "TEST TAP ELEMENT USING DESC"
        self.device.stop()
        StormTest.WaitSec(2)
        isPressed = self.device.tap(mappedText="Sky Online")
        StormTest.WaitSec(4)
        
        
        self.assertEqual(isPressed, True, "Tap failed")
        pass
    
    
    @unittest.expectedFailure
    def test_tap_element_using_index(self):
        print "TEST TAP ELEMENT USING INDEX"
        self.device.stop()
        StormTest.WaitSec(4)
        isPressed = self.device.tap(index=3)
        StormTest.WaitSec(4)
        
        self.device.start("it.sky.river")
        self.assertEqual(isPressed, True, "Tap failed")
        pass
    '''
    

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()