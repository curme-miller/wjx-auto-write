import pdfkit
 
url = "https://www.wjx.cn/vm/hkM2i8g.aspx"

pdfkit_options = {'encoding': 'UTF-8'}

pdfkit.from_url(url,'./questionnaire.pdf',options=pdfkit_options)

