class computer:
    def __init__(self,cpu,ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print("Config is ",self.cpu,self.ram)

com1 = computer('i5' , '8gb')
com2 = computer('i3','16gb')

com1.config()
com2.config()