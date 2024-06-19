# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 13:23:13 2024

@author: ygkim
"""

import numpy as np

def makeGrid(lx,nx):
    dx = lx/nx
    x = np.linspace(-lx/2,lx/2-dx,nx)
    return x
    
def makeFGrid(lx,nx,a=2*np.pi):
    dx = lx/nx
    lfx = a/dx  
    dfx = lfx/nx
    
    fx = np.linspace(-lfx/2,lfx/2-dfx,nx)
    return fx
        
        


def makeGrid2(lx,nx,ly=0,ny=0):
    if ly==0:
        ly = lx
    if ny==0:
        ny = nx

    dx = lx/nx
    dy = ly/ny
    
    x1 = np.linspace(-lx/2,lx/2-dx,nx)
    y1 = np.linspace(-ly/2,ly/2-dy,ny)
    
    x,y = np.meshgrid(x1,y1)
    return x,y
    
def makeFGrid2(lx,nx,ly=0,ny=0,a=2*np.pi):
    if ly==0:
        ly = lx
    if ny==0:
        ny = nx

    dx = lx/nx
    dy = ly/ny

    lfx = a/dx
    lfy = a/dy
    
    dfx = lfx/nx
    dfy = lfy/ny
    
    fx1 = np.linspace(-lfx/2,lfx/2-dfx,nx)
    fy1 = np.linspace(-lfy/2,lfy/2-dfy,ny)
    
    fx,fy = np.meshgrid(fx1,fy1)
    return fx,fy
        
