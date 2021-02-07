#!/usr/bin/env python
# coding: utf-8

# In[17]:


from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[18]:


page=requests.get('https://www.imdb.com/list/ls009997493/')


# In[19]:


page.text


# In[20]:


soup=BeautifulSoup(page.text,'html.parser')
print(soup.prettify())


# In[21]:


movie_name_indian=[]
IMDB_Rating=[]
year_of_release=[]


# In[22]:


movie=soup.find_all(['h3'])
movie[0:10]


# In[23]:


for m in movie:
    movie_name_indian.append(m.get_text())
movie_name_indian[0:10]


# In[25]:


rating=soup.find_all('span',class_="ipl-rating-star__rating")
rating[0:10]


# In[10]:


for r in rating:
    IMDB_Rating.append(r.get_text())
IMDB_Rating[0:10]


# In[11]:


release=soup.find_all('span',class_="lister-item-year text-muted unbold")
release[0:10]


# In[12]:


for r in release:
    year_of_release.append(r.get_text())
year_of_release[0:10]


# In[13]:


len(IMDB_Rating),len(year_of_release),len(movie_name_indian)


# In[15]:


movies=pd.DataFrame({})
movies['INDIAN MOVIE NAMES']=movie_name_indian[0:100]
movies['RATINGS OF A MOVIE']=IMDB_Rating[0:100]
movies['YEAR OF RELEASE']=year_of_release[0:100]
movies


# In[ ]:


in this problem statement i am unable to get the ratings for the movie as it is linked with other elements also.
kindly suggest me to do this.

