
# coding: utf-8

# In[2]:


import PyPDF2


# In[3]:


import PyPDF2
pdf_file = open('Who_Moved_My_Cheese.pdf', 'rb')
read_pdf = PyPDF2.PdfFileReader(pdf_file)
number_of_pages = read_pdf.getNumPages()
page = read_pdf.getPage(0)
page_content = page.extractText()
page_content


# In[4]:


t=number_of_pages
z=""
for i in range(0,t):
    page = read_pdf.getPage(i)
    page_content = page.extractText()
    z= z +"\n"+ page_content
print(z)
my_file=z
    
    


# In[5]:


import spacy
nlp= spacy.load('en')


# In[6]:


nlp1= spacy.load('en')
doc_file = nlp(my_file)


# In[7]:


for tken in doc_file.sents:
    print(tken.text)


# In[12]:


person= set()
list_to_set=""
for tken in doc_file.ents:
    if tken.label_ == 'PERSON':
        y=tken.text.split('\n')
        list_to_set= "".join(y)
        person.add(list_to_set)


# In[13]:


person


# In[14]:


person_string= " ".join(person)


# In[15]:


person_string


# In[16]:


# Search Function For Person:
x= input(" Enter Name To Be Searched")
if x in person_string.lower():
    print("Person Is Available")
else:
    print("not found")


# In[17]:


per_str=""
for k in person:
    if k!= " ":
        per_str = per_str  + " " + k
per_str


# In[18]:


import re
reg_per = re.findall(r'[A-Z][a-z]*',per_str)
filter = re.findall(r'[A-Z][A-Z]*', per_str)


# In[19]:


filter


# In[20]:


filter_name = set()
for name in reg_per:
    if name not in filter and name!="The": #Remove the stopwords
        filter_name.add(name)


# In[21]:


filter_name


# In[23]:


filter_name_list= []
for i in filter_name:
    filter_name_list.append(i)
    


# In[24]:


#Search Function
print("The Name Of The Charectars are\n")
for i in filter_name_list:
    t=i.lower()
    print(t)
x=input("Enter The Name To Be Searched")
if x in filter_name_list:
    print(" The Name Is Available", x)
else:
    print(" Not Found")


# In[21]:


place= set()
list_to_set_1=""
for tken in doc_file.ents:
    if tken.label_ == 'GPE':
        y_1=tken.text.split('\n')
        list_to_set_1= "".join(y_1)
        place.add(list_to_set_1)


# In[22]:


place


# In[28]:


from gensim.summarization.summarizer import summarize
from gensim.summarization import keywords
 
import requests
t=number_of_pages
z=""
for i in range(0,t):
    page = read_pdf.getPage(i)
    page_content = page.extractText()
    z= z +"\n"+ page_content
#print(z)
my_file=z
print ('Summary:')   
print (summarize(str(my_file), ratio=0.01))

