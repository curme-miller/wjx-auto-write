from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import random,time,pretty_errors,glob,sys
class WJX(object):
    def __init__(self,web_driver,all_questions_number):
        self.driver = web_driver
        self.all_questions_number = all_questions_number
    def read_proportion(self):
        excel_files = glob.glob('./*.xlsx')
        if len(excel_files) != 1:
            print('excel文件只能是1个 或 不是".xlsx"文件 或 python文件执行路径不对!!!')
            sys.exit()
        excel = pd.read_excel(excel_files[0])
        self.question_pro = []
        for n in range(len(excel)):
            self.question_pro.append([x for x in excel.iloc[n].values if x == x])
    def find_questions(self):
        self.questions = []
        for num in range(self.all_questions_number):
            self.questions.append(self.driver.find_element(By.ID,'div{}'.format(num+1)))
    def questions_classification(self):
        self.single_questions = []
        self.multiple_questions = []
        self.single_questions_pro = []
        self.multiple_questions_pro = []
        for question in self.questions:
            if question.find_elements(By.CLASS_NAME,'jqradio') == []:
                elements = question.find_elements(By.CLASS_NAME,'jqcheck')
                self.multiple_questions.append(elements)
                self.multiple_questions_pro.append(self.question_pro[self.questions.index(question)])
            else:
                elements = question.find_elements(By.CLASS_NAME,'jqradio')
                self.single_questions.append(elements)
                self.single_questions_pro.append(self.question_pro[self.questions.index(question)])
    def choose_single(self):
        for num in range(len(self.single_questions)):
            time.sleep(1)
            self.single_questions_pro[num].pop(0)
            index_number = [i for i in range(len(self.single_questions_pro[num]))]
            choice_number = random.choices(index_number,self.single_questions_pro[num],k=1)[0]
            self.single_questions[num][choice_number].click()
    def choose_multiple(self):
        for num in range(len(self.multiple_questions)):
            time.sleep(1)
            self.multiple_questions_pro[num].pop(0)
            index_number = [i for i in range(len(self.multiple_questions_pro[num]))]
            choose_number = random.randint(1,len(self.multiple_questions_pro[num]))
            selected_numbers = random.choices(index_number,self.multiple_questions_pro[num],k=choose_number)
            selected_numbers = set(selected_numbers)
            for n in selected_numbers:
                self.multiple_questions[num][n].click()
    def submitdata(self):
        element = self.driver.find_element(By.ID,'ctlNext')
        element.click()
    def exit(self):
        self.driver.close()
if __name__ == '__main__':
    url = input('请输入网址(http...)：')
    all_questions_number = int(input('总共有几题(填数字)：'))
    input_number = int(input('需要几份(填数字):'))
    print('开始填写，耐心等待~')
    chrome_options =webdriver.ChromeOptions()
    chrome_options.add_argument('--headless=new')
    chrome_options.add_argument('--disable-gpu')
    for num in range(input_number):
        driver = webdriver.Chrome(options=chrome_options)
        driver.implicitly_wait(10)
        driver.get(url)
        wjx = WJX(driver,all_questions_number)
        wjx.read_proportion()
        wjx.find_questions()
        wjx.questions_classification()
        wjx.choose_single()
        wjx.choose_multiple()
        time.sleep(2)
        wjx.submitdata()
        time.sleep(2)
        wjx.exit()
        print('已填完第{}份'.format(num+1))
        time.sleep(2)
    print('填写完成！！！')
