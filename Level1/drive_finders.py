import os
class SystemDriveFinder:
    def __init__(self):
        pass#nothing is there in constructor
    def find_drives(self):
        print("this is the find drives method of system drive finder class")
        drives=[]#store all drives
        for x in range(65,91):
            if os.path.exists(chr(x)+":"):#os module communicating with operating system
                drives.append(chr(x))
        return drives
#if __name__=='__main__':
obj=SystemDriveFinder()
print(obj.find_drives())