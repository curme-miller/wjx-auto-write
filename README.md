# 这是可以自动填写问卷调查的python代码(需要稍微等待)
## I.文件说明
### wjx.py
* 这是自动填写问卷星的python代码
* 这里使用的是python3
* 只能填写含有单选题和多选题的问卷调查
    - [x] 单选题
    - [x] 多选题
    - [ ] 填空题
* 需要设置每个选项大约占的比例，请在与"wjx.py"同一个文件夹下添加一个Excel文件,格式与"question_radio.xlsx文件一样
> [!CAUTION]
> 有且只能有一个Excel文件,需要按照自己的问卷调查设置好Excel文件

> [!TIP]
>  可以在虚拟机上运行，这样就不影响电脑的使用了

### get_pdf.py
* 这是获取网页版问卷调查的python代码

## II.使用的主要python库
```
selenium, time, random, pretty_errors, pandas, glob, sys
```

## III.需要安装Chrome Driver
打开网址：
> https://chromedriver.chromium.org/
选择适合你Chrome版本的Driver,然后下载安装
