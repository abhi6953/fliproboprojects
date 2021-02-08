#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[2]:


page=requests.get('https://forecast.weather.gov/MapClick.php?textField1=37.78&textField2=-122.42#.YB0oVOgzY2w')


# In[3]:


soup=BeautifulSoup(page.content,'html.parser')
print(soup.prettify())


# In[4]:


PERIOD=[]
SHORT_DESCRIPTION=[]
TEMPERATURE=[]
DESCRIPTION=[]


# In[5]:


period=soup.find_all('p',class_='period-name')
len(period)


# In[6]:


short_desc=soup.find_all('p',class_='short-desc')
len(short_desc)


# In[7]:


temp=soup.find_all('p',class_=['temp temp-low','temp temp-high'])
len(temp)


# In[8]:


desc=soup.find_all('div',class_='col-sm-10 forecast-text')
desc1=desc[0:9]


# In[9]:


for n in period:
    PERIOD.append(n.get_text())
for n in short_desc:
    SHORT_DESCRIPTION.append(n.get_text())
for n in temp:
    TEMPERATURE.append(n.get_text())
for n in desc1:
    DESCRIPTION.append(n.get_text())


# In[10]:


weather_report=pd.DataFrame({})
weather_report['PERIOD_REPORT']=PERIOD[0:9]
weather_report['SHORT_DESC_REPORT']=SHORT_DESCRIPTION[0:9]
weather_report['TEMERATURE_REPORT']=TEMPERATURE[0:9]
weather_report['DESC_REPORT']=DESCRIPTION[0:9]
weather_report


# In[ ]:




