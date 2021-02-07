#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[2]:


page1=requests.get('https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,desc')


# In[3]:


page1.content


# In[4]:


soup1=BeautifulSoup(page1.content,'html.parser')
print(soup1.prettify())


# In[5]:


movie_name=[]
IMDB_Rating=[]
year_of_release=[]


# In[6]:


movie=soup1.find_all(['h3'])
movie[0:10]


# In[ ]:





# In[9]:


for m in movie:
    movie_name.append(m.get_text())
movie_name[0:10]


# In[11]:


rating=soup1.find_all('strong')
rating[2:10]


# In[12]:


for r in rating:
    IMDB_Rating.append(r.get_text())
IMDB_Rating[2:10]


# In[13]:


release=soup1.find_all('span',class_="lister-item-year text-muted unbold")
release[0:10]


# In[14]:


for r in release:
    year_of_release.append(r.get_text())
year_of_release[0:10]


# In[18]:


len(IMDB_Rating),len(year_of_release),len(movie_name)


# In[17]:


movies=pd.DataFrame({})
movies['MOVIE NAMES']=movie_name[0:50]
movies['RATINGS OF A MOVIE']=IMDB_Rating[2:52]
movies['YEAR OF RELEASE']=year_of_release[0:50]
movies


# In[ ]:




