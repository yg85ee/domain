# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 13:26:04 2024

@author: ygkim
"""

from setupuptools import setup, find_packages

setup(
      name = 'domain',
      version = '0.0.1',
      descirption = 'make domain',
      url = 'https://github.com/yg85ee/domain',
      author='yg',
      packages=find_packages(),
      install_requires=['numpy'],
      )