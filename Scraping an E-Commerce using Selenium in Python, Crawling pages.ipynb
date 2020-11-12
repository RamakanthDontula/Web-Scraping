#!/usr/bin/env python
# coding: utf-8

# ### Importing the libraries required

# In[1]:


import time
import selenium
from selenium import webdriver as wb
webD = wb.Chrome('chromedriver.exe')
webD.get('https://webscraper.io/test-sites/e-commerce/static')


# ### Clicking on menu item

# In[2]:


clicking_category = webD.find_element_by_xpath('//*[@id="side-menu"]/li[2]/a').click()


# ### Clicking on sub-menu item

# In[3]:


clicking_sub_category = webD.find_element_by_xpath('//*[@id="side-menu"]/li[2]/ul/li[1]/a').click()


# ### Finding item on the page

# In[4]:


lapsLinks = webD.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[2]/div/div[1]')


# #### Checking if page item caught

# In[5]:


print(lapsLinks.text)


# ### Finding all the items on the page

# In[6]:


lapsOnPage = webD.find_elements_by_class_name('thumbnail')


# #### Checking if all page items caught

# In[7]:


for lp in lapsOnPage:
    print(lp.text)


# In[8]:


len(lapsOnPage)


# In[9]:


kk= webD.find_elements_by_class_name('page-link')[-1]


# In[10]:


kk.text


# In[11]:


kk.get_attribute('aria-label')


# In[12]:


listOflinks=[]
condition=True
while condition:
    productInfoList=webD.find_elements_by_class_name('thumbnail')
    for elm in productInfoList:
        pp1=elm.find_elements_by_tag_name('h4')[-1]
        pp2=pp1.find_element_by_tag_name('a')
        listOflinks.append(pp2.get_property('href'))
        time.sleep(3)
    try:

        kk= webD.find_elements_by_class_name('page-link')[-1]
        print (kk.get_attribute('aria-label'))
        if kk.get_attribute('aria-label')== 'Next »':
            kk.click()
        else:
            condition=False            
    except:
        condition=False


# In[13]:


len(listOflinks)


# In[14]:


listOflinks[0]


# In[15]:


listOflinks[-1]


# In[16]:


int(str(listOflinks[-1])[-3:])-int(str(listOflinks[0])[-3:])


# In[17]:


from tqdm import tqdm


# In[18]:


alldetails=[]
for i in tqdm(listOflinks):
    webD.get(i)
    nameoftheproduct=webD.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[2]/div/div/div[2]/div[1]/h4[2]').text
    descriptionOfProduct=webD.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[2]/div/div/div[2]/div[1]/p').text
    priceProduct=webD.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[2]/div/div/div[2]/div[1]/h4[1]').text
    reviewOftheProduct=webD.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[2]/div/div/div[2]/div[3]/p').text
    tempJ={'nameoftheproduct':nameoftheproduct,
      'priceProduct':priceProduct,
      'reviewOftheProduct':reviewOftheProduct,
      'descriptionOfProduct':descriptionOfProduct,
      'linkofProduct':i}
    alldetails.append(tempJ)


# In[19]:


import pandas as pd


# In[23]:


prods = pd.DataFrame(alldetails)
prods


# In[24]:


prods.to_csv('laptops_data.csv', index=False)

