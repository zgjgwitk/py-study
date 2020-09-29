# -*- coding: utf-8 -*-
import clr # clr是公共运行时环境，这个模块是与C#交互的核心
import sys

LibPath = 'd:\\Code\\Test\\PythonCall\\Lib'
LibFileName = 'CallLibrary'
AssName = 'CallLibrary'
AssNamespace = 'CallLibrary'
RunMethod1 = 'Class1().Start'
RunMethod2 = 'Utils.CommonHelper().Start'
RunMethod3 = 'Utils.CommonHelper.StaticMethod'
Param_1 = 'Zjw'

sys.path.append(LibPath)  # 加载c#dll文件路径

d = clr.FindAssembly(LibFileName)  # 加载c#dll文件
#print(d)

a = clr.AddReference(AssName)  # 实例化C#类库，这样可以调用,比如这个类库的来源Location
#print(a)

lib1 = __import__(AssNamespace)

res = eval('lib1.'+RunMethod1)(Param_1)
print('\n执行结果:{0}'.format(res))

res = eval('lib1.'+RunMethod2)(Param_1)
print('\n执行结果:{0}'.format(res))

res = eval('lib1.'+RunMethod3)()
print('\n执行结果:{0}'.format(res))