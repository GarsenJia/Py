# -*- coding: utf-8 -*- 
import wx
import wx.xrc


class MyFrame1(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"This is trivial!", pos=wx.DefaultPosition,
                          size=wx.Size(500, 300), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        self.m_textCtrl1 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.Point(-1, -1), wx.Size(400, -1), 0)
        bSizer1.Add(self.m_textCtrl1, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        gSizer1 = wx.GridSizer(0, 2, 0, 0)

        self.m_button1 = wx.Button(self, wx.ID_ANY, u"I'm feeling lucky", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer1.Add(self.m_button1, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_button2 = wx.Button(self, wx.ID_ANY, u"copy to clipboard", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer1.Add(self.m_button2, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_button3 = wx.Button(self, wx.ID_ANY, u"add to MyFavorite", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer1.Add(self.m_button3, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_button4 = wx.Button(self, wx.ID_ANY, u"choose one from MyFavorite", wx.DefaultPosition, wx.DefaultSize,
                                   0)
        gSizer1.Add(self.m_button4, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_button5 = wx.Button(self, wx.ID_ANY, u"remove from MyFavorite", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer1.Add(self.m_button5, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_button6 = wx.Button(self, wx.ID_ANY, u"clear MyFavorite", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer1.Add(self.m_button6, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        bSizer1.Add(gSizer1, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.Bind(wx.EVT_CLOSE, self.saveAll)
        self.m_button1.Bind(wx.EVT_BUTTON, self.generate)
        self.m_button2.Bind(wx.EVT_BUTTON, self.copyto)
        self.m_button3.Bind(wx.EVT_BUTTON, self.add)
        self.m_button4.Bind(wx.EVT_BUTTON, self.favoritegenerate)
        self.m_button5.Bind(wx.EVT_BUTTON, self.remove)
        self.m_button6.Bind(wx.EVT_BUTTON, self.clear)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def saveAll(self, event):
        event.Skip()

    def generate(self, event):
        event.Skip()

    def copyto(self, event):
        event.Skip()

    def add(self, event):
        event.Skip()

    def favoritegenerate(self, event):
        event.Skip()

    def remove(self, event):
        event.Skip()

    def clear(self, event):
        event.Skip()