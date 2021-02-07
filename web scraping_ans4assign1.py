#!/usr/bin/env python
# coding: utf-8

# In[2]:


from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[3]:


page=requests.get('https://bookpage.com/reviews')


# In[4]:


page.text


# In[7]:


soup=BeautifulSoup(page.text,'html.parser')
print(soup.prettify())


# In[8]:


BOOK_NAME=[]
AUTHOR_NAME=[]
GENRE=[]
REVIEW=[]


# In[10]:


book=soup.find_all(['h4'])
book[0:5]


# In[11]:


for b in book:
    BOOK_NAME.append(b.get_text())
BOOK_NAME[0:5]


# In[12]:


author=soup.find_all('p',class_='sans bold')
author[0:5]


# In[13]:


for a in author:
    AUTHOR_NAME.append(a.get_text())
AUTHOR_NAME[0:5]


# In[14]:


genre=soup.find_all('p',class_="genre-links hidden-phone")
genre[0:5]


# In[15]:


for g in genre:
    GENRE.append(g.get_text())
GENRE[0:5]


# In[24]:


review=soup.find_all('p',class_='excerpt')
review[0:5]


# In[25]:


for r in review:
    REVIEW.append(r.get_text())
REVIEW[0:5]


# In[26]:


BOOKPAGE=pd.DataFrame({})
BOOKPAGE['NAME OF BOOK']=BOOK_NAME[0:5]
BOOKPAGE['NAME OF AUTHOR']=AUTHOR_NAME[0:5]
BOOKPAGE['GENRE OF THE BOOK']=GENRE[0:5]
BOOKPAGE['REVIEWS']=REVIEW[0:5]


# In[27]:


BOOKPAGE


# In[ ]:




