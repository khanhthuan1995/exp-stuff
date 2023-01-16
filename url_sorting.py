from typing import Literal
import re

def url_sorting(stream:Literal):
    extensions= ["7z","achee","action","adr","apk","arj","ascx","asmx","asp","aspx","axd","backup","bak","bat","bin","bkf","bkp","bok","cab","cer","cfg","cfm","cfml","cgi","cnf","conf","config","cpl","crt","csr","csv","dat","db","dbf","deb","dmg","dmp","doc","docx","drv","email","eml","emlx","env","exe","gadget","gz","html","ica","inf","ini","iso","jar","java","jhtml","json","jsp","key","log","lst","mai","mbox","mbx","md","mdb","msg","msi","nsf","ods","oft","old","ora","ost","pac","passwd","pcf","pdf","pem","pgp","php","php3","php4","php5","phtm","phtml","pkg","pl","plist","pst","pwd","py","rar","rb","rdp","reg","rpm","rtf","sav","sh","shtm","shtml","skr","sql","swf","sys","tar","tar.gz","tmp","toast","tpl","txt","url","vcd","vcf","wml","wpd","wsdl","wsf","xls","xlsm","xlsx","xml","xsd","yaml","yml","z","zip"]
    for extention in extensions:
        pass

text = "hello.js"
print(re.search("_(\d+)\.js$", text))