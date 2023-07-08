#!/usr/bin/env python
# coding: utf-8

# # DataFrame Basics Exercise

# ## Part 1
# 

# In[16]:


import pandas as pd 
bestsallers = pd.read_csv("data/bestsellers.csv")
bestsallers.shape


# In[10]:


bestsallers.head()


# In[12]:


bestsallers.head(19)


# In[11]:


bestsallers.tail()


# In[13]:


bestsallers.tail(2)


# In[14]:


bestsallers.info()
#no mising values 
#user rating has float type 
#3 intger columens 


# ## Part 2
# 
# 

# In[23]:


depth = pd.read_csv("data/mount_everest_deaths.csv", index_col=0 )
depth


# In[24]:


depth.info()
#name , data columns have zero null values
#age column has the most null value 


# ## Part 3
# 

# In[30]:


pd.read_csv("data/movie_titles.tsv", sep="\t")
 


# In[36]:


names = ["id", "title", "year", "imdb_rating", "imdb_id","genres"]
movie = pd.read_csv("data/movie_titles.tsv", sep="\t", names=names)
movie 


# In[37]:


movie.tail(7)


# In[ ]:




