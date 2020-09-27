#!/usr/bin/env python
# coding: utf-8

# In[26]:


from selenium.webdriver import Chrome
import pandas as pd

webdriver = "/Users/prastha/Downloads/chromedriver" # need to install chrome driver
                                                    # https://chromedriver.chromium.org/downloads

driver = Chrome(webdriver)

year_dict = {} # dictionary to save the dataset

for year in range(14,19):
    url = "https://www.bls.gov/lau/laucnty" + str(year) + ".xlsx"
    county_wise = pd.read_excel(url)
    year_dict[year] = county_wise # dictionary of dataframes

driver.close()


# In[27]:


unemployment_dataframe = pd.DataFrame(columns=['State','Year','Unemployment_Rate'])
states = ['AK','CA','FL','NY','PA']

for key,value in year_dict.items():
    
    year_dict[key] = value.loc[5:3223, ['Unnamed: 3','Unnamed: 4','Unnamed: 9']]
    year_dict[key].columns = ['State','Year','Unemployment_Rate']
    year_dict[key][['County','State']] = year_dict[key].State.str.split(",",expand = True)
    del year_dict[key]['County']

    year_dict[key] = year_dict[key].astype({'Year': 'int64', 'Unemployment_Rate': 'float64'})

    year_dict[key] = year_dict[key].apply(lambda x: x.str.strip() if x.dtype == "object" else x)
    
    unemployment_dataframe = unemployment_dataframe.append(year_dict[key])

unemployment_dataframe = unemployment_dataframe[unemployment_dataframe['State'].isin(states)]

unemployment_dataframe.reset_index(drop = True, inplace = True)  # resets the index

unemployment_dataframe = unemployment_dataframe.groupby(["State", "Year"]).mean().round(2) # takes the average of all counties
                                                                                            # group by state and year

unemployment_dataframe.reset_index(inplace=True)


# In[21]:





# In[13]:





# In[14]:


trial


# In[ ]:




