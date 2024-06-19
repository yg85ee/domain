# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 13:23:13 2024

@author: ygkim
"""

import numpy as np

def makeGrid(lx,nx,ly=0,ny=0):
    if ly==0:
        ly = lx
    if ny==0:
        ny = nx

    dx = lx/nx
    dy = ly/ny
    
    x1 = np.linspace(-lx/2,lx/2-dx,nx)
    y1 = np.linspace(-ly/2,ly/2-dy,ny)
    
    x,y = np.meshgrid(x1,y1)

    
    