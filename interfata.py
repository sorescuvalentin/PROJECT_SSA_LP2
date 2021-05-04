import tkinter
import importlib
import text




class Executor:
    def __init__(self):
        self.root = tkinter.Tk()
        self.app = text.Application(master=self.root, on_reload=self.on_reload)
        self.app.mainloop()

    def on_reload(self):
        self.root.destroy()

        importlib.reload(text)

        self.root = tkinter.Tk()
        self.app = text.Application(master=self.root, on_reload=self.on_reload)
        self.app.mainloop()


if __name__ == '__main__':
    Executor()