# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 20:55:19 2022

@author: sshuv
"""

from bing_image_downloader import downloader

items = ['bangladeshi hospital', 'proverty of bangladesh india']
    
for item in items:
    downloader.download(item, limit=200,  output_dir=r'D:\image classification\zzz Random Photos\downloads', \
                        adult_filter_off=True, force_replace=False, timeout=10, verbose=True)