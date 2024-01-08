#!/usr/bin/env python
# coding: utf-8

# <h1><b>Data Extraction - Single Page</b></h1>

# In[1]:


get_ipython().system('pip install bs4')


# In[2]:


import urllib.request as urllib2
from bs4 import BeautifulSoup


# In[3]:


# Access the URL and retrieve its content

URLResponse = urllib2.urlopen('https://www.rottentomatoes.com/browse/movies_at_home/')
html_doc = URLResponse.read()


# In[4]:


# Parse the HTML content using BeautifulSoup

soup = BeautifulSoup(html_doc, 'html.parser')


# In[5]:


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


# In[6]:


# Print the first few movie entries as a sample

print(movie_info[:500])


# <h1><b>Data Transformation</b></h1>

# In[7]:


# We'll store it in a list of dictionaries, as shown above.
# 'movie_info' list now contains all the scraped data.

# We can access individual movie data like this:
movie_data = movie_info[0]
movie_name = movie_data['Movie Name']
tomatometer_rating = movie_data['Tomatometer Rating']
audience_score = movie_data['Audience Score']


# <h1><b> Data Presentation</b></h1>

# In[8]:


get_ipython().system('pip install tabulate')


# In[9]:


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



# 
# 
# <h2>------------------------------------------------------------------------------------------------<h4><b>Under this section, I have extracted and Display all the data that comes after clicking the "Load More" button.</b></h4></h2> 
# 
# <p> But there is an error while I am trying to build the solution. You can Try this as well!</p>
# <h2>-------------------------------------------------------------------------------------------------</h2>    

# <h1><b>Data Extraction - By clicking the "Load More" Button. </b></h1>

# !pip install selenium

# In[1]:


import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd

# Set up the Firefox WebDriver without headless mode
options = FirefoxOptions()

# Create the Firefox WebDriver without specifying executable_path
driver = webdriver.Firefox(options=options)

url = "https://www.rottentomatoes.com/browse/movies_at_home/"
driver.get(url)

# Initialize a WebDriverWait with a timeout
wait = WebDriverWait(driver, 10)

# Click the "Load More" button repeatedly until all content is loaded
while True:
    try:
        load_more_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-qa="dlp-load-more-button"]')))
        load_more_button.click()
       # time.sleep(3)  # Add a delay to allow the content to load
       # Wait for the new data to load dynamically
        wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, 'loadMoreResults')))
    except Exception as e:
        break
        
# Extract the page source after loading all content
page_source = driver.page_source

# Close the WebDriver
driver.quit()

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(page_source, 'html.parser')

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


# <h1><b>Data Presentation</b></h1>

# In[ ]:


import pandas as pd
from tabulate import tabulate

# Assuming you have already created the DataFrame 'df'

# Set Pandas options to display all columns and rows without truncation
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)  # Display full content of columns

# Use tabulate to display the DataFrame in a tabular form
print(tabulate(df, headers='keys', tablefmt='grid', showindex=False))


# In[28]:


df = pd.DataFrame(movie_info)


# In[35]:


df

