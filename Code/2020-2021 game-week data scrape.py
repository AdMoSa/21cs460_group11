#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


player_id = pd.read_csv("20-21_player_idlist.csv")


# In[3]:


player_id.head()


# In[4]:


player_id['Name'] = player_id['first_name'] + ' ' + player_id['second_name']
print(player_id)


# In[7]:


list(player_id.columns.values)


# In[8]:


player_id = player_id[['Name', 'id', 'first_name', 'second_name']]
print(player_id)


# In[12]:


player_id = player_id.drop(['first_name', 'second_name'], axis=1)
print(player_id)


# In[17]:


gw1= pd.read_csv("20-21_gws\gw1.csv")


# In[18]:


gw1.head()


# In[15]:


list(gw1.columns.values)


# In[19]:


gw1 = gw1.drop(['position', 'team', 'xP', 'assists', 'bonus', 'bps', 'clean_sheets', 'creativity', 'element',
                'fixture', 'goals_conceded', 'goals_scored', 'ict_index', 'influence', 'kickoff_time', 'minutes',
                'opponent_team', 'own_goals', 'penalties_missed', 'penalties_saved', 'red_cards', 'round', 'saves',
                'selected', 'team_a_score', 'team_h_score', 'threat', 'transfers_balance', 'transfers_in',
                'transfers_out', 'value', 'was_home', 'yellow_cards'], axis=1)
print(gw1)


# In[22]:


gw1 = gw1.rename({'name':'Name','total_points':'gw1'}, axis=1)


# In[36]:


gw1_data = pd.merge(player_id, gw1, on=['Name'], how='left') 


# In[37]:


print(gw1_data)


# In[76]:


gw = []
for i in range(1,39):
    gw.append(pd.read_csv("20-21_gws\gw"+str(i)+".csv"))


# In[77]:


all_gw = player_id
for i in range(0,38):
    gw[i] = gw[i].drop(['position', 'team', 'xP', 'assists', 'bonus', 'bps', 'clean_sheets', 'creativity', 'element',
                'fixture', 'goals_conceded', 'goals_scored', 'ict_index', 'influence', 'kickoff_time', 'minutes',
                'opponent_team', 'own_goals', 'penalties_missed', 'penalties_saved', 'red_cards', 'round', 'saves',
                'selected', 'team_a_score', 'team_h_score', 'threat', 'transfers_balance', 'transfers_in',
                'transfers_out', 'value', 'was_home', 'yellow_cards'], axis=1)
    d = {'total_points': 'sum', 'name': 'first'}
    gw[i] = gw[i].groupby('name', as_index=True).aggregate(d).reindex(columns=gw[i].columns)
    gw[i] = gw[i].rename({'name':'Name','total_points':'gw'+str(i+1)}, axis=1)
    
    


# In[82]:


all_gw = player_id
for i in range(0,38):
    all_gw = pd.merge(all_gw, gw[i], on=['Name'], how='left')
all_gw=all_gw.fillna(0)
print(all_gw)


# In[83]:


all_gw.to_csv('20-21_all_gw.csv', encoding='utf-8')

