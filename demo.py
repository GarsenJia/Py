# -*- coding: utf-8 -*-
import wx
import noname
import random

list = []
favorite = []
#f = open("input.txt")
f = open("input.txt", encoding='utf-8')
line = f.readline()
while line:
    list.append(line)
    line = f.readline()
f.close()

class TFrame(noname.MyFrame1):

    def __init__(self, parent):
        noname.MyFrame1.__init__(self, parent)
        trivial = list

    def generate(self, event):
        s = list[random.randint(0, len(list))]
        self.m_textCtrl1.SetValue(s)


def main():
    app = wx.App(False)
    frame = TFrame(None)
    frame.Show(True)
    app.MainLoop()

if __name__ == '__main__':
    main()