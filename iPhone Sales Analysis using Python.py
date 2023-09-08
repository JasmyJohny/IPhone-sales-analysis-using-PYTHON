#!/usr/bin/env python
# coding: utf-8

# In[45]:


import pandas as pd

import plotly.express as px
import plotly.graph_objects as go


# In[46]:


df = pd.read_csv(r'/Users/jasmylenson/Documents/Pandas/ReadingFile/apple_products.csv')
df


# In[4]:


pd.set_option('display.max_rows', 63)


# In[8]:


pd.set_option('display.max_columns', 12)


# In[7]:


df.shape


# In[10]:


df.info()


# In[11]:


# dataset contains any null values or not:

df.drop_duplicates()


# In[47]:


df.isnull().sum()


# In[48]:


# check the descriptive statistics of the data

df.describe()


# In[49]:


# lets find out the highest rated iphones in india

top_rated = df.sort_values(by='Star Rating', ascending = False).head(10)
top_rated


# In[50]:


print(top_rated['Product Name'])


# In[53]:


#iphones = top_rated['Product Name'].value_counts()
#iphones


# In[54]:


#label = iphones.index
#label

#count = top_rated['Number Of Ratings']
#count


# In[ ]:


#Now let’s have a look at the number of ratings of the highest-rated iPhones on Flipkart:


# In[51]:


figure = px.bar(top_rated, x='Product Name', 
                y = 'Number Of Ratings', 
            title="Number of Ratings of Highest Rated iPhones")
figure.show()


# In[ ]:


#According to the above bar graph, APPLE iPhone 8 Plus (Gold, 64 GB) has the most ratings on Flipkart


# In[ ]:


#Now let’s have a look at the number of reviews of the highest-rated iPhones on Flipkart:


# In[52]:


figure = px.bar(top_rated, x='Product Name', 
                y = 'Number Of Reviews', 
            title="Number of Ratings of Highest Rated iPhones")
figure.show()


# In[ ]:


#APPLE iPhone 8 Plus (Gold, 64 GB) is also leading in the highest number of reviews on Flipkart among the highest-rated iPhones in India.


# In[58]:


#Now let’s have a look at the relationship between the sale price of iPhones and their ratings on Flipkart:

figure = px.scatter(data_frame = df, x="Number Of Ratings",
                    y="Sale Price", size="Discount Percentage", 
                    trendline="ols", 
                    title="Relationship between Sale Price and Number of Ratings of iPhones")
figure.show()


# In[ ]:


#There is a negative linear relationship between the sale price of iPhones and the number of ratings. 
#It means iPhones with lower sale prices are sold more in India. 

#Now let’s have a look at the relationship between the discount percentage on iPhones on Flipkart and the number of ratings:


# In[ ]:





# In[60]:


figure = px.scatter(data_frame = df, x="Number Of Ratings",
                    y="Discount Percentage", size="Sale Price", 
                    trendline="ols", 
                    title="Relationship between Discount Percentage and Number of Ratings of iPhones")
figure.show()


# In[ ]:


#There is a linear relationship between the discount percentage on iPhones on Flipkart and the number of ratings.
#It means iPhones with high discounts are sold more in India.


# # Summary

# In[ ]:


APPLE iPhone 8 Plus (Gold, 64 GB) was the most appreciated iPhone in India
iPhones with lower sale prices are sold more in India
iPhones with high discounts are sold more in India

