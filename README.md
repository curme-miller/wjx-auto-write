# 这是可以自动填写问卷调查的python🐍代码(需要稍微等待)
## I.文件说明
### wjx.py
* 这是自动填写问卷星的python代码
* 这里使用的是python3
* 只能填写含有单选题和多选题的问卷调查
    - [x] 单选题
    - [x] 多选题
    - [ ] 填空题
* 需要设置每个选项大约占的比例，请在与"wjx.py"同一个文件夹下添加一个Excel文件.
格式如下：

|题目序号| 选项1 | 选项2 | 选项3 | 选项4 | ...|
|---|---|---|---|---|---|
| 1 | 0.2 | 0.5 | 0.1 | 0.2 |
| 2 | 0.2 | 0.3 | 0.5 |
| 3 | 0.3 | 0.7 |
| ... |

> [!CAUTION]
> 有且只能有一个Excel文件,需要按照自己的问卷调查设置好Excel文件

### get_pdf.py
* 这是获取网页版问卷调查的python代码

## II.使用的主要python库
```
selenium, time, random, pretty_errors, pandas, glob, sys
```

## III.需要安装Chrome Driver
打开网址：
- 125以后的版本：[chromedriver](https://googlechromelabs.github.io/chrome-for-testing/#canary) 选择适合你Chrome版本的Driver,然后下载安装.
- 114以前的版本：[chromedriver](https://chromedriver.storage.googleapis.com/index.html) 选择适合你Chrome版本的Driver,然后下载安装.

> **免责声明：**
> 本代码只作为学习与参考之用，不得用作商业等其他用途.
