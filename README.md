# sspider
异步高效可扩展的爬虫框架


基于dockers 的云部署 支持分布式大型网站高效抓取

框架的优势：

1.异步协程框架，

2.自由扩展，发展成自己的风格

3.docker 部署，可以用rancher 等容器管理工具部署我们的项目

### 文件功能介绍



公共文件模块
commom 

function 公用的函数库
settings 公共的配置信息 比如 redis mysql kafka ES 等
spider_settings 爬虫信息配置文件 比如 example 项目爬虫  example2 example3 等等 每个爬虫都是不一样的，全部通用是不可能的，但是每个项目的爬虫还是有通用的比如 url、头文件、任务队列等

spiders 爬虫的主要逻辑文件 

案例是 example 项目 demo 爬虫 你可能会有 

example2 项目 demo1  demo2 demo3等爬虫 自行扩展