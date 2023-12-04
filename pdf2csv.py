#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tabula
import os
import csv
import pandas as pd


# In[7]:


with open('d:/output/pathpdf.txt') as pdf:
    pdfpath= pdf.read()


# In[8]:


print("Converting start....")
print("Converting Progress....")


# In[9]:


with open('d:/output/pathcsv.txt') as csv:
    csvpath= csv.read()


# In[10]:


df=tabula.convert_into('d:/output/1.pdf', 'd:/output/1.csv', output_format="csv", pages='all')
print("file converted....")

# In[ ]:


os.remove('d:/output/1.pdf')
print("Converting deleting file....")
print("Converting Complete!")

