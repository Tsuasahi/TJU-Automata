# TJU-Automat 天大简易选课脚本

1.clone/下载本repo, 登录账号进入选课页面 

![表格, Excel 描述已自动生成](media/950966d3386c2bd12a5ae0cd20a8257c.png)

2.在该网页F12或者右键-\>检查/审查元素等类似操作，将上边栏切换到网络/Network选项卡

![表格 描述已自动生成](media/bae49325d3238a31cfbd0a4a451326bc.png)

3.对要选的课进行选课操作，无须在意结果是成功、失败或者不在选课时间内

![文本 描述已自动生成](media/5d508f9ee56ec0ed9d607c55cf5f1803.png)

4.在刚才的选项卡中会出现一个(可能)std打头的，单击展开它

![表格 描述已自动生成](media/03a65e847ded245e257441c3c506996d.png)

![图形用户界面, 文本, 应用程序描述已自动生成](media/c0607afb0de344d52cc5ce967a6df5bf.png)

5.在右侧栏中找到请求URL/Request URL, 观察内容与config.txt/config内第一行是否相同, 不同则替换(不要打开自动换行)

![文本 描述已自动生成](media/7118badc1a0bc47840a32b4d99e0abf5.png)

![图形用户界面, 文本, 应用程序
描述已自动生成](media/887d0b53bb5692b93c37ba78debcadbe.png)

6.在右侧栏中找到表单数据/From Data的前几位数字，复制到config.txt/config内第一行(注意不要打开自动换行)

![文本 中度可信度描述已自动生成](media/c63703e6fed9cd470d9702bc68836910.png)

![文本 描述已自动生成](media/1e87cb67add07c255a08fe7b9c885cc4.png)
![图形用户界面, 文本 描述已自动生成](media/e5dfc295282e1148a3046e5e452de7be.png)

7.在右侧栏中找到cookie并右键-\>复制值/Copy Value，粘贴到config.txt/config内第二行(注意不要打开自动换行)，保存config.txt/config

![背景图案 中度可信度描述已自动生成](media/86a6254e3c5e09dcd053ff2acb9b8ef2.png)

8.双击run.bat/run运行脚本

![文本 描述已自动生成](media/1dbbf816d8de7c390ecaa9da176335ef.png)
