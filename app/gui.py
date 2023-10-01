import wx


class GUIApp(wx.App):
    def __init__(self):
        super().__init__(clearSigInt=True)
        self.InitFrame()

    def InitFrame(self):
        frame = MainFrame(parent=None, title='Main Frame', pos=(100, 100))
        frame.Show()


class MainFrame(wx.Frame):
    def __init__(self, parent, title, pos):
        super().__init__(parent=parent, title=title, pos=pos)
        self.OnInit()

    def OnInit(self):
        MainPanel(parent=self)


class MainPanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent=parent)

        wx.StaticText(self, id=wx.ID_ANY, label='Welcome!', pos=(20, 20))
