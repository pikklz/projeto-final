import addbookwindow

def acrescentarLivro(self):
    addbookwindow.Addwindow()


def removerLivro(self):
    pass


def copy(self):
    self.editor.event_generator('<<Copy>>')


def cut(self):
    self.editor.event_generator('<<Cut>>')


def paste(self):
    self.editor.event_generator('<<Paste>>')


def ajuda():
    pass
