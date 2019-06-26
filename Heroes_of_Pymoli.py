#!/usr/bin/env python
# coding: utf-8

# In[1]:


#dependencies and setup
import pandas as pd
import numpy as np
import csv
import warnings
warnings.simplefilter(action='ignore')


# In[2]:


#identify file to load
file_to_load = 'purchase_data.csv'
purchase_df=pd.read_csv(file_to_load)

#purchase_df.head()


# In[3]:


#We only want screen names, so create a new table that contains only SN
total_players=purchase_df["SN"].nunique()
#purchase_df


#rename screen names as total players 
#screen_names.rename(columns={'SN':'Total Players'}, inplace=True)


# In[4]:


# Create a display of data
total_players_df = pd.DataFrame({
    'Total Players':[''],
    ' ':total_players})
total_players_df


# 
# 

# In[5]:


#get summary table info
No_unique_items=purchase_df.loc[:,"Item ID"].max()
#No_unique_items

Average_price=purchase_df.loc[:,"Price"].mean()
#Average_price

Number_purchases=purchase_df.loc[:,"Purchase ID"].count()
#Number_purchases

Total_revenue=purchase_df.loc[:,"Price"].sum()
#Total_revenue


# In[6]:


#summary table data frome
summary_df = pd.DataFrame({
    'Number of Unique Items':[No_unique_items],
    'Average Price':[Average_price],
    'Number of Purchases':[Number_purchases],
    'Total Revenue': [Total_revenue]})

summary_df.round(2) 


# In[7]:


#Gender demographics
#purchase_df.groupby(['Gender']).nunique()


# In[8]:


#Gender Demographics summary table data frame
gender_df = pd.DataFrame({
    ' ':['Male', 'Female', 'Other/Non-Disclosed'],
    'Total Count':['484','81','11'],
    'Percentage of Players':[((484/576)*100), ((81/576)*100), ((11/576)*100)]})

gender_df.round(2)


# In[13]:


#Purchasing Analysis (Gender) data frame
#purchase_df.groupby(['Gender']).median()
#purchase_df.groupby(['Gender']).mean()
#purchase_df.groupby(['Gender']).sum()


# In[10]:


gender_purchase_df = pd.DataFrame({
    ' ':['Male', 'Female', 'Other/Non-Disclosed'],
    'Purchase Count':['652','113','15'],
    'Average Purchase Price':['$3.02', '$3.20', '$3.35'],
    'Total Purchase Value':['$1967.64','$361.94','$50.19'],
    'Avg Total Purchase per Person':[(1967.64/484), (361.94/81), (50.19/11)]})

gender_purchase_df.round(2)


# In[15]:


sorteddata=purchase_df.sort_values(['Purchase ID'])#.drop_duplicates(subset ='SN', keep = False)
#sorteddata.nunique()


# In[16]:


# Create the bins in which Data will be held
#Bins are <10, 10-14, 15-19, 20-24, 25-29, 30-34, 35-39, 40+.   
bins = [0, 9, 14, 19, 24, 29, 34, 39, 45]

#Create the label names for the  bins
age_groups = ['<10', '10-14', '15-19', '20-24', '25-29','30-34','35-39','40+']

sorteddata['Age Ranges'] = pd.cut(sorteddata["Age"], bins, labels=age_groups)
sorteddata.head()


# In[17]:


Age_groups=sorteddata.groupby('Age Ranges').nunique()
Age_groups


# In[18]:


#Age_demo_df= pd.DataFrame({
   # ' ':['<10', '10-14', '15-19', '20-24', '25-29','30-34','35-39','40+'],
   # 'Total Count':['17','22','107','258','77','52','31','12'],
   # 'Percentage of Players':[((17/576)*100), ((22/576)*100), ((107/576)*100), ((258/576)*100),((77/576)*100), 
                            # ((52/576)*100), ((31/576)*100),((12/576)*100)]})
#Age_demo_df.round(2)

Age_groups_format = Age_groups[["SN",]]
Age_groups_format['Percentage of Players']=(Age_groups_format['SN']/total_players)*100
Age_groups_format.round(2)


# In[40]:


#summary table format

#Age_group_count=sorteddata.groupby('Age Ranges')['Item ID'].count() #gives purchase count
#Age_group_avg=sorteddata.groupby('Age Ranges')['Price'].mean() #gives average purchase price
#Age_group_total=sorteddata.groupby('Age Ranges')['Price'].sum() #gives total purchase value

#Age_group_total
#Age_group_count
#Age_group_avg


# In[34]:


Age_groups_purch = Age_groups[["Purchase ID",]]
Age_groups_purch.columns=['Purchase Count']
#Age_groups_purch['Average Purchase Price']=[Age_group_avg]
#Age_groups_purch['Total Purchase Value']=[Age_group_total]
Age_groups_purch

#Age_purch_summary = pd.DataFrame(
 #   {
#        "Purchase Count": [Age_group_count],
 #       "Average Purchase Price": [Age_group_avg],
 #       "Total Purchase Value":[Age_group_total]
#    }
#)
#Age_purch_summary


# In[39]:


#sorteddata.groupby('Age Ranges')['Price','SN'].max() #gives most$$$ spent per SN per age group


# In[44]:


age_purch_df = pd.DataFrame({
    ' ':['<10', '10-14', '15-19', '20-24', '25-29','30-34','35-39','40+'],
    'Purchase Count':['23','28','136','365','101','73','41','13'],
    'Average Purchase Price':['$3.35', '$2.96', '$3.04','$3.05','$2.90','$2.93','$3.60','2.94'],
    'Total Purchase Value':['$77.13','$82.78','$412.89','$1,114.06','$293.00','$214.00','$147.67','$38.24'],
    'Avg Total Purchase per Person':['$0.00','$0.00','$0.00','$0.00','$0.00','$0.00','$0.00','$0.00']})
age_purch_df


# In[49]:


age_purch_df.groupby('Purchase Count')['Average Purchase Price'].max() #gives most$$$ spent per SN per age group


# In[ ]:




