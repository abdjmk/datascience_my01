# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 03:33:45 2020

@author: DELL
"""

import glassdoor_scrapper_chrome as gs
import pandas as pd

path = "C:/git/datascience_my01/chromedriver"

df = gs.get_jobs ('data scientist',15, False, path, 15)


