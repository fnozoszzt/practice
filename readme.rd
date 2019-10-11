#淘宝商品链接分析

##1.项目概述
设定关键词，抓取前若干页搜索结果中的符合特定要求的商品

##2.项目实现
经分析，淘宝的搜索页和商品页，是需要登陆才能访问的。同时，搜索结果和发货信息，都是js渲染出来的，不是html网页上带的
*登陆，即http访问的时候需带有cookie表示用户信息，如果不带或者带错，会提示登陆信息*
*渲染，即网页上信息是初始没有的，运行js后，才展示出来*

因此，程序在运行前，需要准备好cookie文件（更完美的方式是自动输入帐号密码进行验证）
同时，抓取需使用带渲染功能的抓取器，可选的有phantomjs，chromeheadless等
我用chromeheadless来做

淘宝搜索结果，在翻页的时候，发现url中变化的是s=参数
我们在构造翻页链接的时候，直接拼这个参数


##3.部署运行

###本地环境
本地需安装python，python安装selenium和beautifulsoup库，本地存放一个文件chromedriver，这个文件从网上下载即可。本地需放一个cookie文件。本地需先建一个page文件夹和index文件夹
###运行方式
先运行python step1.py，提示输入搜索关键词和页数
运行后，会产生link.list文件

再运行python step2.py，会生成output.txt
output.txt就是我们要的结果





