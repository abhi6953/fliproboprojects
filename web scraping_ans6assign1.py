#!/usr/bin/env python
# coding: utf-8

# # PART1 INCLUDES THE TOP10 TEAMS FOR ODI WOMENS.

# In[1]:


from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[2]:


page=requests.get('https://www.icc-cricket.com/rankings/womens/team-rankings/odi')


# In[3]:


soup=BeautifulSoup(page.text,'html.parser')
print(soup.prettify())


# In[4]:


TEAM_NAME=[]
MATCHES_AND_POINTS=[]
RATING=[]


# In[13]:


team=soup.find_all('span',class_="u-hide-phablet")
team[1:11]


# In[14]:


for n in team:
    TEAM_NAME.append(n.get_text())
TEAM_NAME[1:11]


# In[15]:


match=soup.find_all('td',class_='table-body__cell u-center-text')
match[0:20]


# In[16]:


for n in match:
    MATCHES_AND_POINTS.append(n.get_text())
no_of_matches=MATCHES_AND_POINTS[0::2]
no_of_matches[0:10]


# In[17]:


match_points=MATCHES_AND_POINTS[1::2]
match_points[0:10]


# In[18]:


rating=soup.find_all('td',class_="table-body__cell u-text-right rating")
rating[0:10]


# In[19]:


for n in rating:
    RATING.append(n.get_text())
RATING[0:10]


# In[21]:


ODI=pd.DataFrame({})
ODI['TEAM_NAME_TOP10']=TEAM_NAME[1:10]
ODI['NO.OF MATCHES']=no_of_matches[0:9]
ODI['MATCH POINTS']=match_points[0:9]
ODI['RATINGS_TOP20']=RATING[0:9]
ODI


# # PART2 INCLUDES THE TOP10 BAT WOMENS FOR ODI

# In[22]:


page2=requests.get('https://www.icc-cricket.com/rankings/womens/player-rankings/odi')


# In[23]:


soup2=BeautifulSoup(page2.text,'html.parser')
print(soup2.prettify())


# In[24]:


PLAYER_NAME=[]
NATIONALITY=[]
RATINGS=[]


# In[25]:


player=soup2.find_all('td', class_='table-body__cell name')
len(player)


# In[26]:


for n in player:
    PLAYER_NAME.append(n.get_text())
PLAYER_NAME[0:10]


# In[27]:


national=soup2.find_all('span', class_="table-body__logo-text")
len(national)


# In[28]:


for n in national:
    NATIONALITY.append(n.get_text())
NATIONALITY[0:10]


# In[29]:


rating=soup2.find_all('td', class_='table-body__cell u-text-right rating')
len(rating)


# In[30]:


for n in rating:
    RATINGS.append(n.get_text())
RATINGS[0:10]


# In[31]:


ODI_PLAYERS=pd.DataFrame({})
ODI_PLAYERS['PLAYER_NAME']=PLAYER_NAME[0:10]
ODI_PLAYERS['NATIONALITY']=NATIONALITY[0:10]
ODI_PLAYERS['RATINGS']=RATINGS[0:10]
ODI_PLAYERS


# # I AM NOT ABLE TO SOLVE THE PART 3 AS ATTRIBUTES ARE GETTING REPEAPTED AGAIN.

# In[ ]:




