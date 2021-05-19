
import importlib
import text




class Executor:
    def __init__(self):
        self.on_reload()

    def on_reload(self):
         importlib.reload(text)


if __name__ == '__main__':
    Executor()