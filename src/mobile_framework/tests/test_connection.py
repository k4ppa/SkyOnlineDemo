
import unittest

from mobile_framework.tests.test_environment import TestEnvironment
from mobile_framework.android_device import AndroidDevice

class TestConnection(unittest.TestCase):
    

    def setUp(self):
        self.device = AndroidDevice("samsung_galaxy_tab_3")
        pass

    
    def tearDown(self):
        TestEnvironment.setSlotNumber(1)
        self.device.disconnect()
        pass

    
    def test_connect_device_to_the_server_with_success(self):
        print "TEST_CONNECT_DEVICE_TO_THE_SERVER_WITH_SUCCESS"
        isConnected = self.device.connect("Connect with the real server")
        
        self.assertEqual(isConnected, True, "Device connection to the server failed")
        pass
    
    
    def test_connect_device_should_fail_when_name_is_wrong(self):
        print "TEST_CONNECT_DEVICE_SHOULD_FAIL_WHEN_NAME_IS_WRONG"
        TestEnvironment.setServerName("WrongServerName")
        isConnected = self.device.connect("Connect with non existing server")
        
        self.assertEqual(isConnected, False, "Connection successful")
        pass
    
    
    def test_reserve_slot_should_fail_when_server_name_is_wrong(self):
        print "TEST_RESERVE_SLOT_SHOULD_FAIL_WHEN_SERVER_NAME_IS_WRONG"
        TestEnvironment.setServerName("WrongServerName")
        isConnected = self.device.connect("Connect with non existing server")
        
        self.assertEqual(isConnected, False, "Connection successful")
        pass
    
    
    def test_reserve_slot_should_fail_when_slot_number_is_wrong(self):
        print "TEST_SLOT_SHOULD_FAIL_WHEN_SLOT_NUMBER_IS_WRONG"
        TestEnvironment.setSlotNumber(10)
        isConnected = self.device.connect("Connect with the real server")
        
        self.assertEquals(isConnected, False, "Correct slot number")
        pass
    
    
    def test_disconnect_device_to_the_server(self):
        print "TEST_DISCONNECT_DEVICE_TO_THE_SERVER"
        isDisconnected = self.device.disconnect()  
         
        self.assertEqual(isDisconnected, True, "Device disconnection to the server failed")
        pass
    
    
    def test_start_application_by_name_should_be_successfull(self):
        print "TEST START APPLICATION BY NAME SHOULD BE SUCCESSFULL"
        self.device.connect("Connect with the real server")
        isStarted = self.device.start("it.sky.river")
        
        self.assertEqual(isStarted, True, "App not started")
        pass
   
   
    def test_stop_application(self):
        print "TEST STOP APPLICATION"
        self.device.connect("Connect with the real server")
        self.device.start("it.sky.river")
        isStopped = self.device.stop()
       
        self.assertEqual(isStopped, True, "App not stopped")
        pass
    
