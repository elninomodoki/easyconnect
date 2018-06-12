A simple program that automatically connects to the Internet after disconnecting which applies only to Ocean University of China.

自动登陆到校园网计费系统

下载easyconnect.py
填写其中的用户名密码并保存

windows系统下，利用计划任务功能实现自动登陆功能

打开计划任务
![图片说明](https://github.com/elninomodoki/easyconnect/blob/master/image/1.PNG)

点击创建基本任务
![图片说明](https://github.com/elninomodoki/easyconnect/blob/master/image/2.PNG)

为任务起一个名字，然后点击下一步
![图片说明](https://github.com/elninomodoki/easyconnect/blob/master/image/3.PNG)

在触发器中设置任务开始时间
![图片说明](https://github.com/elninomodoki/easyconnect/blob/master/image/4.PNG)
![图片说明](https://github.com/elninomodoki/easyconnect/blob/master/image/5.PNG)

设置任务执行的操作
![图片说明](https://github.com/elninomodoki/easyconnect/blob/master/image/6.PNG)

设置启动程序的位置
![图片说明](https://github.com/elninomodoki/easyconnect/blob/master/image/7.PNG)
注意：程序或脚本指的是执行这个任务的程序，这里选择python.exe，需带有完整的路径
添加参数指的是要运行的脚本
起始于指的是脚本所在的路径
脚本和脚本所在的路径必须分开写，否则无法运行。

把这一项勾选上，方便我们设置
![图片说明](https://github.com/elninomodoki/easyconnect/blob/master/image/8.PNG)

可以设置多个触发器
![图片说明](https://github.com/elninomodoki/easyconnect/blob/master/image/9.PNG)

任意设置
![图片说明](https://github.com/elninomodoki/easyconnect/blob/master/image/10.PNG)




