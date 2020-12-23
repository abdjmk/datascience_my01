# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 03:33:45 2020

@author: DELL
"""

import glassdoor_scrapper_chrome as gs
import pandas as pd

path = "E:/git/datascience_my01/chromedriver"

df = gs.get_jobs (200, False, path, 15)
#'data scientist' temporarily take out

df.to_csv('glassdoor_jobs_1.csv', index = False)
