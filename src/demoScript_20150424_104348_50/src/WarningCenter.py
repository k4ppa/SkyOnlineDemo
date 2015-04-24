#!/usr/bin/python
#############################################################################
# Copyright (c) 2008-2014 Silicon & Software Systems Ltd.(S3 Group).
# All rights reserved.
# This source code and any compilation or derivative thereof is the
# proprietary information of Silicon & Software Systems Ltd. and is
# confidential in nature.
# Use of this source code is subject to the terms of the applicable
# Silicon & Software Systems Ltd. license agreement.
#
# Under no circumstances is this component (or portion thereof) to be in any
# way affected or brought under the terms of any Open Source License without
# the prior express written permission of Silicon & Software Systems Ltd.
#
# For the purpose of this clause, the term Open Source Software/Component
# includes:
#
# (i) any software/component that requires as a condition of use, modification
#     and/or distribution of such software/component, that such software/
#     component:
#    a.  be disclosed or distributed in source code form;
#    b.  be licensed for the purpose of making derivative works; and/or
#    c.  can be redistributed only free of enforceable intellectual property
#        rights (e.g. patents); and/or
# (ii) any software/component that contains, is derived in any manner (in whole
#      or in part) from, or statically or dynamically links against any
#      software/component specified under (i).
#
#  -----------------------------------------------------
#  http://www.s3group.com
#  -----------------------------------------------------
#
#  MODULE: WarningCenter
#
#  DESCRIPTION: The warningcenter module provides APIs for test scripts to send
#               events to WarningCenter
#
###############################################################################
##
## @file warningcenter.py
## @brief This module provides APIs for user to to send events to WarningCenter

################################################################################
# Import modules
################################################################################

import warning_center_api as _warning_center

def SendEvent(name,
              value,
              service,
              screenshot=None,
              video=None,
              tags=None):
    """Send an event to WarningCenter.

    @return A list: [Result, status, reason]

    @param name       (string) Name of the event such as "videoMotion"
    @param value      (string, boolean or number) The value of the event
    @param service    (dictionary) The service that generated the event
    @param screenshot (string) Screenshot of the event
    @param video      (string) Video of the event
    @param tags       (list of strings) Tags to attach to the event
    """
    return _warning_center.SendEvent(name, value, service, screenshot=screenshot, video=video, tags=tags)
    
def GetTestRun():
    """Getter for the TestRun

    @return A dict representation of the Test Run or None if running in developer mode
    """
    return _warning_center.GetTestRun()    