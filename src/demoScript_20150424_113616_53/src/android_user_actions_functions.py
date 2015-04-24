
import logging

import stormtest.ClientAPI as StormTest


log = logging.getLogger("userAction")

def _tapWithText(text):
    log.info("Tap on element with text {0}".format(text))
    return StormTest.PressButton("TAPELEMENT:text:{0}".format(text))
    
    
def _tapWithDesc(desc):
    log.info("Tap on element with desc {0}".format(desc))
    return StormTest.PressButton("TAPELEMENT:desc:{0}".format(desc))
    
    
def _tapWithIndex(index):
    log.info("Tap on element with index {0}".format(index))
    return StormTest.PressButton("TAPELEMENT:index:{0}".format(index))