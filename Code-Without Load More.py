#!/usr/bin/env python
# coding: utf-8

# <h3><b>194044D - Assignment 01</b></h3>

# <h1><b>Data Extraction</b></h1>

# In[80]:


get_ipython().system('pip install bs4')


# In[81]:


import urllib.request as urllib2
from bs4 import BeautifulSoup


# In[82]:


# Access the URL and retrieve its content

URLResponse = urllib2.urlopen('https://www.rottentomatoes.com/browse/movies_at_home/')
html_doc = URLResponse.read()


# In[83]:


# Parse the HTML content using BeautifulSoup

soup = BeautifulSoup(html_doc, 'html.parser')


# In[84]:


# Find and extract the relevant information for each movie
movie_elements = soup.find_all(['a','div'], attrs={'data-track': 'scores', 'data-qa': 'discovery-media-list-item-caption'})

movie_info = []

for movie_element in movie_elements:
    # Extract movie name
    movie_name = movie_element.find('span', attrs={'data-qa': 'discovery-media-list-item-title'}).text.strip()

    # Extract tomatometer value and audience score
    score_pairs = movie_element.find('score-pairs')
    tomatometer = score_pairs['criticsscore']
    audience_score = score_pairs['audiencescore']
    
    movie_info.append({'Movie Name':  movie_name, 'Tomatometer Rating': tomatometer, 'Audience Score': audience_score})


# In[85]:


# Print the first few movie entries as a sample

print(movie_info[:500])


# <h1><b>Data Transformation</b></h1>

# In[86]:


# We'll store it in a list of dictionaries, as shown above.
# 'movie_info' list now contains all the scraped data.

# We can access individual movie data like this:
movie_data = movie_info[0]
movie_name = movie_data['Movie Name']
tomatometer_rating = movie_data['Tomatometer Rating']
audience_score = movie_data['Audience Score']


# <h1><b> Data Presentation</b></h1>

# In[87]:


get_ipython().system('pip install tabulate')


# In[88]:


import pandas as pd
from tabulate import tabulate

# Convert the list of dictionaries into a DataFrame
df = pd.DataFrame(movie_info)

# Set Pandas options to display all columns and rows without truncation
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)

# Use tabulate to display the DataFrame in a tabular form
print(tabulate(df, headers='keys', tablefmt='grid', showindex=False))



# In[ ]:




