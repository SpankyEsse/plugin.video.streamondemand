# -*- coding: utf-8 -*-
# ------------------------------------------------------------
# streamondemand 5
# Copyright 2015 tvalacarta@gmail.com
# http://blog.tvalacarta.info/plugin-xbmc/pelisalacarta/
#
# Distributed under the terms of GNU General Public License v3 (GPLv3)
# http://www.gnu.org/licenses/gpl-3.0.html
# ------------------------------------------------------------
# This file is part of pelisalacarta 4.
#
# pelisalacarta 4 is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# pelisalacarta 4 is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with pelisalacarta 4.  If not, see <http://www.gnu.org/licenses/>.
# --------------------------------------------------------------------------------
# Channels and Servers update from main menu
# --------------------------------------------------------------------------------

import os
import re
import sys
import time

from core import config
from core import logger
from core import scrapertools

from core.item import Item
from platformcode import platformtools


def update_from_menu(item):

    try:
        from core import update_channels
    except:
        logger.info("streamondemand.library_service Error in update_channels")
    # ----------------------------------------------------------------------

    # -- Update servertools and servers from repository streamondemand ------
    try:
        from core import update_servers
    except:
        logger.info("streamondemand.library_service Error in update_servers")
    # ----------------------------------------------------------------------

    return 


