# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 22:53:59 2018

@author: sharm
"""

import os
import re
import string
import math

DATA_DIR = 'enron'
target_names = ['ham', 'spam']

def get_data(DATA_DIR):
	subfolders = ['enron%d' % i for i in range(1,7)]

	data = []
	target = []
	for subfolder in subfolders:
		# spam
		spam_files = os.listdir(os.path.join(DATA_DIR, subfolder, 'spam'))
		for spam_file in spam_files:
			with open(os.path.join(DATA_DIR, subfolder, 'spam', spam_file), encoding="latin-1") as f:
				data.append(f.read())
				target.append(1)

		# ham
		ham_files = os.listdir(os.path.join(DATA_DIR, subfolder, 'ham'))
		for ham_file in ham_files:
			with open(os.path.join(DATA_DIR, subfolder, 'ham', ham_file), encoding="latin-1") as f:
				data.append(f.read())
				target.append(0)

	return data, target