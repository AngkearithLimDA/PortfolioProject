#!/usr/bin/env python
# coding: utf-8

# In[8]:


# First let's import the packages we will use in this project
# You can do this all now or as you need them
import pandas as pd
import numpy as np
import seaborn as sns

import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import matplotlib
plt.style.use('ggplot')
from matplotlib.pyplot import figure

get_ipython().run_line_magic('matplotlib', 'inline')
matplotlib.rcParams['figure.figsize'] = (12,8)

pd.options.mode.chained_assignment = None



# Now we need to read in the data
df = pd.read_csv(r'C:\Main Documents\Portfolio Projects\Python-Documents\movies.csv')


# In[10]:


# Now let's take a look at the data

df


# In[11]:


# Check for any missing data

for col in df.columns:
    pct_missing = np.mean(df[col].isnull())
    print('{} - {}%'.format(col, pct_missing))


# In[12]:


# Data types for our colums
df.dtypes


# In[14]:


print(df.dtypes)


# In[15]:


# Any Outliers?

df.boxplot(column = ['gross'])


# In[16]:


df.drop_duplicates()


# In[17]:


# Order Data a bit to see

df.sort_values(by = ['gross'], inplace=False, ascending=False)


# In[18]:


sns.regplot(x="gross", y="budget", data=df)


# In[19]:


sns.regplot(x="score", y="gross", data=df)


# In[20]:


#  Correlation Matrix between all numeric columns

df.corr(method ='pearson')


# In[21]:


df.corr(method ='kendall')


# In[22]:


df.corr(method ='spearman')


# In[23]:


correlation_matrix = df.corr()

sns.heatmap(correlation_matrix, annot = True)

plt.title("Correlation matrix for Numeric Features")

plt.xlabel("Movie features")

plt.ylabel("Movie features")

plt.show()


# In[24]:


# Using factorize - this assigns a random numeric value for each unique categorical value

df.apply(lambda x: x.factorize()[0]).corr(method='pearson')


# In[48]:


correlation_matrix = df.apply(lambda x: x.factorize()[0]).corr(method='pearson')

sns.heatmap(correlation_matrix, annot = True)

plt.title("Correlation matrix for Numveric Features")

plt.xlabel("Movie features")

plt.ylabel("Movie features")

plt.show()


# In[49]:


correlation_mat = df.apply(lambda x: x.factorize()[0]).corr()

corr_pairs = correlation_mat.unstack()

print(corr_pairs)


# In[27]:


sorted_pairs = corr_pairs.sort_values(kind = "quicksort")

print(sorted_pairs)


# In[28]:


# High correlation (> 0.5)

High_corr = sorted_pairs[abs(sorted_pairs) > 0.5]

print(High_corr)


# In[29]:


# Top 15 compaies by gross revenue

CompanyGrossSum = df.groupby('company')[["gross"]].sum()

CompanyGrossSumSorted = CompanyGrossSum.sort_values('gross', ascending = False)[:15]

CompanyGrossSumSorted = CompanyGrossSumSorted['gross'].astype('int64') 

CompanyGrossSumSorted


# In[30]:


df['Year'] = df['released'].astype(str).str[:4]
df


# In[31]:


df.groupby(['company', 'year'])[["gross"]].sum()


# In[32]:


CompanyGrossSum = df.groupby (['company', 'year']) [["gross"]].sum()

CompanyGrossSumSorted = CompanyGrossSum.sort_values(['gross','company','year'], ascending = False)[:15]

CompanyGrossSumSorted = CompanyGrossSumSorted['gross'].astype('int64') 

CompanyGrossSumSorted


# In[33]:


CompanyGrossSum = df.groupby(['company'])[["gross"]].sum()

CompanyGrossSumSorted = CompanyGrossSum.sort_values(['gross','company'], ascending = False)[:15]

CompanyGrossSumSorted = CompanyGrossSumSorted['gross'].astype('int64') 

CompanyGrossSumSorted


# In[34]:


plt.scatter (x=df['budget'], y=df['gross'], alpha=0.5)
plt.title ('Budget vs Gross Earnings')
plt.xlabel ('Gross Earnings')
plt.ylabel ('Budget for Film')
plt.show()


# In[35]:


df.head()


# In[36]:


df_numerized = df


for col_name in df_numerized.columns:
    if(df_numerized[col_name].dtype == 'object'):
        df_numerized[col_name]= df_numerized[col_name].astype('category')
        df_numerized[col_name] = df_numerized[col_name].cat.codes
        
df_numerized


# In[37]:


df_numerized.corr(method='pearson')


# In[38]:


correlation_matrix = df_numerized.corr (method='pearson')

sns.heatmap (correlation_matrix, annot = True)

plt.title ("Correlation matrix for Movies")

plt.xlabel ("Movie features")

plt.ylabel ("Movie features")

plt.show()


# In[46]:


# Plot budget vs gross using seaborn
sns.regplot(x='budget',y='gross',data=df, scatter_kws={"color": "Red"}, line_kws={"color":"purple"})


# In[47]:


# Correlation
df.corr()


# In[ ]:




