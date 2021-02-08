#!/usr/bin/env python
# coding: utf-8

# In[2]:


from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[3]:


page=requests.get('https://www.amazon.in/s?k=mobile+under+20000&crid=36239E8IK8PB2&sprefix=mobile%2Caps%2C317&ref=nb_sb_noss_2')


# In[4]:


soup=BeautifulSoup(page.content,'html.parser')
print(soup.prettify())


# In[5]:


name=soup.find_all(['h2'])
len(name)


# In[6]:


NAME=[]
for n in name:
    NAME.append(n.get_text())
NAME[0:16]


# In[7]:


price=soup.find_all('span',class_="a-price-whole")
len(price)


# In[9]:


PRICE_MOBILE=[]
for n in price:
    PRICE_MOBILE.append(n.get_text())
PRICE_MOBILE[0:17]


# In[43]:


image=soup.find_all('img')
for n in image:
    link=(n['src'])
    print(link)


# In[10]:


rating=soup.find_all('span',class_="a-size-base")
len(rating)


# In[11]:


RATING=[]
for n in rating:
    RATING.append(n.get_text())
RATING[0:16]


# I AM NOT ABLE TO GET THE RATINGS AS IT HAS BEEN DESINGED BY THE CUSTOMER REVIEWS
# SECOND: NOT ABLE TO APPEND THE IMAGE TAG FOR THE FURTHER ANALYSIS.

# In[ ]:




