# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 13:09:03 2017

@author: Silas
"""

class Cube:

    def dimensions(self,posx,posy,posz):
        
        verts = (-1+posx,-1+posy,-1+posz),(1+posx,-1+posy,-1+posz),(1+posx,1+posy,-1+posz),(-1+posx,1+posy,-1+posz),(-1+posx,-1+posy,1+posz),(1+posx,-1+posy,1+posz),(1+posx,1+posy,1+posz),(-1+posx,1+posy,1+posz)

        return verts
        