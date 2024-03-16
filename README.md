# 这是可以填写问卷调查的python web自动化代码，可以设置每个选项比例
## 文件说明 rgb(68,207,247)
### wjx.py rgb(204,255,0)
* 这是自动填写问卷星的python代码
* 这里使用的是python3
* 只能填写有单选题和多选题的问卷调查
    - [x] 单选题
    - [x] 多选题
    - [ ] 填空题
> [!TIP]
> 如果你想设置每个选项大约占的比例，那么请在与"wjx.py"同一个文件夹下添加一个Excel文件.详见"question_radio.xlsx文件.如果不设置，就以大约平均的比例进行选择.
### get_pdf.py rgb(204,255,0)
* 这是获取网页版问卷调查的python代码

## 使用的关键python库 rgb(68,207,247)
```
selenium, time, random, pretty_errors
```

## 需要安装Chrome Driver rgb(68,207,247)
打开网址：
> https://chromedriver.chromium.org/
选择适合你Chrome版本的Driver,然后下载安装
