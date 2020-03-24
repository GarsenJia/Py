# -*- coding: utf-8 -*-
import wx
import noname
import random
import pyperclip as clip

save = []
favorite = []
f = open("./input.txt", encoding='utf-8')
line = f.readline()
line = f.readline()
while line:
    save.append(line)
    line = f.readline()
    if line == "favorite:\n":
        line = f.readline()
        break
while line:
    favorite.append(line)
    line = f.readline()
f.close()


class TFrame(noname.MyFrame1):

    def __init__(self, parent):
        noname.MyFrame1.__init__(self, parent)

    def saveAll(self, event):
        f = open("input.txt", "w", encoding='utf-8')
        f.seek(0)
        f.truncate()
        f.writelines("save:\n")
        for s in save:
            f.writelines(s)
        f.writelines("favorite:\n")
        for s in favorite:
            f.writelines(s)
        f.close()
        wx.Exit()


    def generate(self, event):
        s = save[random.randint(0, len(save) - 1)]
        self.m_textCtrl1.SetValue(s)

    def copyto(self, event):
        s = self.m_textCtrl1.Value
        clip.copy(s)

    def add(self, event):
        s = self.m_textCtrl1.Value
        if(s in save and not(s in favorite)):
            favorite.append(self.m_textCtrl1.Value)

    def generatefavorite(self, event):
        try:
            s = favorite[random.randint(0, len(favorite) - 1)]
            self.m_textCtrl1.SetValue(s)
        except:
            self.m_textCtrl1.SetValue("MyFavorite is empty!")
        finally:
            pass

    def remove(self, event):
        try:
            s = self.m_textCtrl1.Value
            favorite.remove(s)
        except:
            self.m_textCtrl1.SetValue("Not in MyFavorite!")

    def clear(self, event):
        favorite.clear()


def main():
    app = wx.App(False)
    frame = TFrame(None)
    frame.Show(True)
    app.MainLoop()


if __name__ == '__main__':
    main()
