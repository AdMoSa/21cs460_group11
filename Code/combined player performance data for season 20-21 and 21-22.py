#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[17]:


player_id_20 = pd.read_csv("20-21_player_idlist.csv")
player_id_20['Name'] = player_id_20['first_name'] + ' ' + player_id_20['second_name']
player_id_20 = player_id_20[['Name', 'id', 'first_name', 'second_name']]
player_id_20 = player_id_20.drop(['first_name', 'second_name'], axis=1)

player_id_21 = pd.read_csv("21-22_player_idlist.csv")
player_id_21['Name'] = player_id_21['first_name'] + ' ' + player_id_21['second_name']
player_id_21 = player_id_21[['Name', 'id', 'first_name', 'second_name']]
player_id_21 = player_id_21.drop(['first_name', 'second_name'], axis=1)


# In[18]:


player_id_combine = pd.concat([player_id_20, player_id_21], ignore_index=True, sort=True, join="inner")


# In[21]:


player_id_combine = player_id_combine.drop_duplicates(subset='Name', keep="first")


# In[22]:


print(player_id_combine)


# In[24]:


player_id_combine.to_csv('player_id_combine.csv', encoding='utf-8')


# In[28]:


gw = []
for i in range(1,39):
    gw.append(pd.read_csv("20-21_gws\gw"+str(i)+".csv"))
for i in range(1,12):
    gw.append(pd.read_csv("21-22_gws\gw"+str(i)+".csv"))
for i in range(0,49):
    gw[i] = gw[i].drop(['position', 'team', 'xP', 'assists', 'bonus', 'bps', 'clean_sheets', 'creativity', 'element',
                'fixture', 'goals_conceded', 'goals_scored', 'ict_index', 'influence', 'kickoff_time', 'minutes',
                'opponent_team', 'own_goals', 'penalties_missed', 'penalties_saved', 'red_cards', 'round', 'saves',
                'selected', 'team_a_score', 'team_h_score', 'threat', 'transfers_balance', 'transfers_in',
                'transfers_out', 'value', 'was_home', 'yellow_cards'], axis=1)
    d = {'total_points': 'sum', 'name': 'first'}
    gw[i] = gw[i].groupby('name', as_index=True).aggregate(d).reindex(columns=gw[i].columns)
    gw[i] = gw[i].rename({'name':'Name','total_points':'gw'+str(i+1)}, axis=1)
all_gw = player_id_combine
for i in range(0,49):
    all_gw = pd.merge(all_gw, gw[i], on=['Name'], how='left')
all_gw=all_gw.fillna(0)
print(all_gw)


# In[29]:


all_gw.to_csv('20-22_all_gw.csv', encoding='utf-8')

