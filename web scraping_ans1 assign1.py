#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[3]:


from bs4 import BeautifulSoup
import requests


# In[4]:


page=requests.get('https://en.wikipedia.org/wiki/Main_Page')


# In[5]:


page.content


# this is the whole source code for the above main page of wikipedia

# In[6]:


soup=BeautifulSoup(page.content,'html.parser')


# In[7]:


print(soup.prettify())


# prettify function is used to present the data into more understable format.

# In[8]:


titles=soup.find_all(['h1','h2','h3','h4','h5','h6'])


# In[13]:


print('all the headings are:',*titles,sep='\n\n\n')


# In[14]:


len(titles)


# In[15]:


import pandas as pd


# In[28]:


df=pd.DataFrame(titles,columns=['Headings'])


# In[29]:


df


# In[ ]:




