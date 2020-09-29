# -*- coding: utf-8 -*-
# clr.FindAssembly方法而不是clr.ADDReference方法，而且导入clr模块时，最好也把System模块导入，原因注释里已经说了，最后注意一点就是一定要把C#的命名空间当做模块导入进来。
import clr # clr是公共运行时环境，这个模块是与C#交互的核心
import sys

sys.path.append(r'd:\Code\Test\PythonCall\Lib')  # 加载c#dll文件路径

d = clr.FindAssembly('CallLibrary')  # 加载c#dll文件
#print(d)

a = clr.AddReference('CallLibrary')  # 实例化C#类库，这样可以调用,比如这个类库的来源Location
#print(a)
#from CallLibrary import *  # 导入命名空间
#from CallLibrary.Utils import * 
import CallLibrary as clib




class DotNetProj(object):
    def Call(self):
        clib.Class1().Start()
        print('')

    def Call_Code(self, code):
        clib.Class1().Start(code)
        print('')

    def Call_Return(self, code):
        ret = clib.Utils.CommonHelper().Start(code)
        print('')
        print(ret)

def __init__(self):
    pass

if __name__ == "__main__":
    proj = DotNetProj()
    proj.Call()
    proj.Call_Code('zjw')
    proj.Call_Return('zjwret')