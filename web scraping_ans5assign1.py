#!/usr/bin/env python
# coding: utf-8

# # PART 1 INCLUDES THE TOP 10 TEAMS FOR ODI

# In[2]:


from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[3]:


page=requests.get('https://www.icc-cricket.com/rankings/mens/team-rankings/odi')


# In[4]:


page.content


# In[5]:


soup=BeautifulSoup(page.text,'html.parser')
print(soup.prettify())


# In[6]:


TEAM_NAME=[]
MATCHES_AND_POINTS=[]
RATING=[]


# In[7]:


team=soup.find_all('span',class_="u-hide-phablet")
team[1:11]


# In[8]:


for n in team:
    TEAM_NAME.append(n.get_text())
TEAM_NAME[1:11]


# In[9]:


match=soup.find_all('td',class_='table-body__cell u-center-text')
match[0:20]


# In[24]:


for n in match:
    MATCHES_AND_POINTS.append(n.get_text())
no_of_matches=MATCHES_AND_POINTS[0::2]
no_of_matches[0:10]


# In[29]:


match_points=MATCHES_AND_POINTS[1::2]
match_points[0:10]


# In[30]:


rating=soup.find_all('td',class_="table-body__cell u-text-right rating")
rating[0:10]


# In[31]:


for n in rating:
    RATING.append(n.get_text())
RATING[0:10]


# In[33]:


ODI=pd.DataFrame({})
ODI['TEAM_NAME_TOP10']=TEAM_NAME[1:11]
ODI['NO.OF MATCHES']=no_of_matches[0:10]
ODI['MATCH POINTS']=match_points[0:10]
ODI['RATINGS_TOP20']=RATING[0:10]
ODI


# # PART2 INCLUDES THE TOP10 BATMENS FOR ODI

# In[35]:


page2=requests.get('https://www.icc-cricket.com/rankings/mens/player-rankings/odi')


# In[36]:


soup2=BeautifulSoup(page2.text,'html.parser')
print(soup2.prettify())


# In[37]:


PLAYER_NAME=[]
NATIONALITY=[]
RATINGS=[]


# In[47]:


player=soup2.find_all('td', class_='table-body__cell name')
len(player)


# In[57]:


for n in player:
    PLAYER_NAME.append(n.get_text())
PLAYER_NAME[0:10]


# In[49]:


national=soup2.find_all('span', class_="table-body__logo-text")
len(national)


# In[51]:


for n in national:
    NATIONALITY.append(n.get_text())
NATIONALITY[0:10]


# In[52]:


rating=soup2.find_all('td', class_='table-body__cell u-text-right rating')
len(rating)


# In[53]:


for n in rating:
    RATINGS.append(n.get_text())
RATINGS[0:10]


# In[55]:


ODI_PLAYERS=pd.DataFrame({})
ODI_PLAYERS['PLAYER_NAME']=PLAYER_NAME[0:10]
ODI_PLAYERS['NATIONALITY']=NATIONALITY[0:10]
ODI_PLAYERS['RATINGS']=RATINGS[0:10]
ODI_PLAYERS


# # PART3 INCLUDES THE TOP10 BOWLERS FOR ODI

# In[58]:


page3=requests.get('https://www.icc-cricket.com/rankings/mens/player-rankings/odi')


# In[59]:


soup3=BeautifulSoup(page3.text,'html.parser')
print(soup2.prettify())


# In[60]:


I AM NOT ABLE TO SOLVE THE PART 3 AS ATTRIBUTES ARE GETTING REPEAPTED AGAIN.


# In[ ]:




