class Demo:

    def __init__(self, value):
        self.value = value # Instance Variable

    def show(self):
        local_var = 10 # Local Variable

        print("Local Variable:",local_var)
        print("Instance Variable:",self.value)

        #Build in Functions
        print("Length using built in function:",len("Ayush"))

#Driver Code
obj = Demo(34)
obj.show()