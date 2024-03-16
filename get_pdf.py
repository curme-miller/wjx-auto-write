import pdfkit
 
url = input('请输入网址：')
file_name = input('请输入pdf文件名：')
pdfkit_options = {'encoding': 'UTF-8'}
pdfkit.from_url(url, '{}.pdf'.format(file_name), options=pdfkit_options)