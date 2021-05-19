import tkinter
import importlib
import text




class Executor:
    def __init__(self):
        self.root = tkinter.Tk()
        self.on_reload()

    def on_reload(self):
        self.root.destroy()
        importlib.reload(text)



if __name__ == '__main__':
    Executor()