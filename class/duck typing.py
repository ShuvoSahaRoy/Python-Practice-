class PyCharm:
    def execute(self):
        print("Compile")
        print("run")


class MyEditor:

    def execute(self):
        print("Compile")
        print("Spell check")
        print("Running")
        print("Convention Check")


class Laptop:

    def code(self, ide):  # ide has a data type. and we defined it as pycharm or Myeditor
        ide.execute()


ide = MyEditor()

lap1 = Laptop()
lap1.code(ide)
