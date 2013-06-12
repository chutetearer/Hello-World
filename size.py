#!/usr/bin/python
# -*- coding: utf-8 -*-

import wx
import os

class Example(wx.Frame):
           
    def __init__(self, *args, **kw):
        super(Example, self).__init__(*args, **kw) 
        self.InitUI()
        
    def InitUI(self):

        self.Bind(wx.EVT_SIZE, self.OnSize)
        self.SetSizeHints(minW = 250, minH = 150, maxW = 800, maxH = 450, incW = -1, incH = -1)
        self.SetSize((250, 380))
        self.SetTitle('Size Event Test- EVT')
        self.Centre()
        self.Show(True)  

    def OnSize(self, e):
        x, y = e.GetSize()
        print "x width",(str(x)),
        print " - y hight",(str(y))

def main():
    ex = wx.App()
    fr = Example(None)
    ex.MainLoop()    

if __name__ == '__main__':
    main()  
