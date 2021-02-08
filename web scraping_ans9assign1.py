#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[2]:


page=requests.get('https://www.monsterindia.com/srp/results?query=Software%20Developer,software%20engineer&searchId=44df4faa-f946-45a2-8ae0-b54768f787b6')


# In[3]:


soup=BeautifulSoup(page.text,'html.parser')
print(soup.prettify())


# In[ ]:




