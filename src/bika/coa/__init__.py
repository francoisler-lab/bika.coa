# -*- coding: utf-8 -*-
#
# This file is part of BIKA.COA
#
# Copyright 2019 by it's authors.

import logging

PRODUCT_NAME = "bika.coa"
PROFILE_ID = "profile-{}:default".format(PRODUCT_NAME)
logger = logging.getLogger(PRODUCT_NAME)


def initialize(context):
    """Initializer called when used as a Zope 2 product."""

    logger.info("*** Initializing BIKA.COA ***")
