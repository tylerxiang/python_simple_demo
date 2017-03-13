# python的简单DEMO，共10题
###p1.py 
从<font color='red'><code>命令行参数</code></font>，输入姓名和性别，在屏幕上显示hello　姓名先生（或女士），例如：
命令行运行程序，输入 $ python p1.py 李四 女，结果显示：$ hello 李四女士

### p2.py 
使用双重循环，在屏幕上显示九九表，如果乘积小于10，在其前面补0，即：
1x1=01 1x2=02 … 1x9=09<br/>
2x1=02 2x2=04 … 2x9=18<br/>
…<br/>
9x1=09 9x2=18…9x9=81<br/>

### p3.py
从<font color='red'><code>命令行参数</code></font>输入以下10个数字，实现由小到大排序后在屏幕上显示出来<br/>
$python p3.py 25 13 67 821 9 43 046  345   33  721

### p4.py
读输入文件（每行一个数字），按由小到大顺序进行排序，将结果显示到屏幕<br/>
输入文件名：/datafile/d1.txt<br/>

###p5.py
读输入文件（datafile/d1.txt），每读一行将内容存入新生成的grade类中，并将grade存入列表中。文件读完后，在屏幕上显示列表中的全部grade内容

### p6.py
利用第5题中的文件格式与grade类格式，实现对学生成绩的增加、修改、删除、显示。程序启动后从datafile/d1.txt中读数据到列表中，主界面如下：<br/>
				学生成绩维护<br/>
			=========================<br/>
				L 显示<br/>
				A 增加<br/>
				D 删除<br/>
				E 修改<br/>
				Q 退出<br/>
按L，显示如下界面<br/>
			===========================<br/>
			显示学生成绩：<br/>
			学号		姓名		成绩<br/>
1			user1		82<br/>
2			user2		83<br/>
5			user3		85<br/>
按任意键返回主界面<br/>
<br/>
	按A，显示如下界面<br/>
			===========================<br/>
			添加学生成绩：<br/>
			学号：3		<br/>
      姓名：user3		<br/>
      成绩：83<br/>
			已成功添加，按任意键返回主界面<br/>
	按D，输入要删除的学号，显示如下界面<br/>
			===========================<br/>
			删除学生成绩：<br/>
			学号：3<br/>
			该学号已删除，按任意键返回主界面<br/>
如果学号错误，显示如下界面<br/>
		===========================<br/>
			删除学生成绩：<br/>
			学号：11<br/>
			该学生不存在，按任意键返回主界面<br/>
<br/>
按Q，将内存列表中的内容保存到文件/datafile/d11.txt中<br/>

###p7.py
利用6题中的界面、功能形式，访问sqltie数据库(/datafile/grade.db)，实现对学生成绩的增加、修改、删除、显示。<br/>
	表grade结构：<br/>
			id int,<br/>
			name varchar(10),<br/>
			value int<br/>

###p8.py
利用6题中的界面功能，编写C/S模式功能，即客户端通过Tcp/Ip访问服务器，服务器接收客户端的请求然后访问sqlite3数据库（同第7题），实现对成绩的增加、修改、删除、显示。<br/>
客户端运行<br/>
		$python p8c.py
服务端运行
	  $python p8s.py

###p9.py
使用第5题中的grade类结构对txt文本数据、xml数据及数据库表数据进行封装存取，使用第6题中的界面处理方式，将界面处理封装至抽象基类p9base中，在子类p9filetxt、p9filejson、p9filexml、p9db、p9sock中实现抽象方法load、save，在启动后、停止之前对数据文件或数据库及tcp连接进行处理。在p9base抽象类中实现数据处理的显示、增加、删除、修改功能。<br/>
函数功能列表：<br/>
名称					功能<br/>
====================================================================<br/>
 mainProc()				主循环，显示主菜单，键盘读取功能选择<br/>
 load()					  抽象方法，启动后执行，txt、json、xml等子类调用数据到列表中，db、tcp等子类建立连接<br/>
 save()				  	抽象方法，退出前执行，txt、json、xml等子类存贮列表中的数据，db、tcp等子类关闭连接<br/>
 input	(grade)		界面输入grade各项数据<br/>
 add()					  mainProc中调用，添加数据。界面调用input输入数据后，调用addAfter添加数据<br/>
 del()					  mainProc中调用，删除数据。界面输入要删除的ID后，调用delAfter删除数据<br/>
 edit()					  mainProc中调用，修改数据。界面输入要修改的ID后，调用editBefore通过此ID找到对应的grade，然后调用input修改grade，再调用editAfter，将原grade及修改后的grade存贮。<br/>
 list()					  mainProc中调用，显示数据。先调用listBefore，取得数据list，然后显示于界面。
 grade find(grade_id);		抽象方法，
 int addAfter(grade);	    抽象方法，					
 int delAfter(grade_id);	抽象方法，
 int editAfter(grade);	  抽象方法，
 grades listBefore();	    抽象方法，

###p10.py 
需要安装web模块，在ubuntu下安装<br/>
$cd web.py-0.37<br/>
$sudo python setup.py install<br/>

运行后，在浏览器中http://localhost:8080/显示数据列表
$python p10.py
