
# coding: utf-8

# # Converting XML files of different extension into paragraphs.

# In[12]:

print("Converting the files.")
print("Loading the necessary files.")
from bs4 import BeautifulSoup
import re
import glob
import os
filetype = ("*.ttxt","*.dfxp","*.xml","*.txt","*.srt")


# In[15]:

if os.path.exists("Output"):
    pass
else:
    os.mkdir('Output')
for path in filetype:
    
    if path != "*.srt":
        for file in glob.glob(path):

            print("Working on: ", file)
            f = open(file,'r',encoding='utf-8')
            try:
                html_doc = f.read()
            except:
                f.close()
                print("Turning on Advanced Encoding")
                f = open(file,'r',encoding= 'utf-16')
                html_doc = f.read()
                #print(html_doc)
                print("Turning off Advanced Encoding")
            soup = BeautifulSoup(html_doc,'html.parser')
            text = soup.getText()
            out_name = "Output/"+os.path.splitext(file)[0] + ".txt"
            output = open(out_name,'w',encoding='utf-8')
            output.write(repr(re.sub(r'\s+'," ",(re.sub(r'\n'," ",text)))))
            output.close()
            f.close()
            
    else:
        for file in glob.glob(path):
            print("Working on: ", file)
            f = open(file,'r',encoding='utf-8')
            output = ""
            for line in f.readlines():
                if (re.match(r'^\D',line) != None):
                    output+=" " +(str(line.lstrip().rstrip()).strip("\\")).strip("...")
                    #print(re.sub(r'\\',"",line))
                    #print(line)
            f.close()
            out_name = "Output/"+os.path.splitext(file)[0] + ".txt"
            outputfile = open(out_name,'w',encoding='utf-8')
            outputfile.write(output)
            outputfile.close()
                
        


# In[ ]:



