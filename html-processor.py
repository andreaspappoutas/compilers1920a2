import re

def function(m): #antikatastasi &amp, &gt, &lt kai &nbsp

    if (m.group(0)=='&amp;'):
        return '&'
    elif (m.group(0)=='&gt;'):
        return '>'
    elif (m.group(0)=='&lt;'):
        return '<'
    else:
        return ' '  


#Erotimata

rexp = re.compile('<title>(.+?)</title>') #proto erotima otidipote meta3i <title></title>
rexp2 = re.compile('<!--.*?-->',re.DOTALL) #deutero apolifi sxolion
rexp3 = re.compile(r'<(s(?:cript|tyle)).*?>.*?</\1>',re.DOTALL) #trito <script></script> kai <style></style>
rexp4 = re.compile(r'<a.+?href="(.*?)".*?>(.*?)</a>',re.DOTALL)#tetarto periexomeno <a></a> kai href
rexp5_1 = re.compile(r'<.+?>|</.+?>',re.DOTALL) # ta tags <>
rexp5_2 = re.compile(r'<.+?/>',re.DOTALL) #ta tags </>
rexp6 = re.compile(r'&(amp|gt|lt|nbsp);') #keimeno me &amp, &gt, &lt kai &nbsp
rexp7 = re.compile(r'\s+') #whitespace



with open('testpage.txt','r') as fp: 
    text = fp.read() #dievazoume to testpage.txt
    m = rexp.search(text)
    print(m.group(1))
    text = rexp2.sub(' ',text)
    text = rexp3.sub(' ',text)
    for m in rexp4.finditer(text):
        print('{}    {}'.format(m.group(1),m.group(2)))
    text = rexp5_1.sub(' ',text)
    text = rexp5_2.sub(' ',text)
    text = rexp6.sub(function,text)
    text = rexp7.sub(' ',text)
    print(text)
    
