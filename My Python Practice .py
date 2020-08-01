#!/usr/bin/env python
# coding: utf-8

# <h3 1d="download"> Objects & Classes:</h3>

# In[77]:


class employee:
    
  def __init__ (self, first, last, pay):
    self.first=first
    self.last=last
    self.pay=pay
               
emp_1=employee("Hani", "Nazmi", 48000)
empy_2=employee("Mariam", "Hani", 80000)

print(emp_1.first)


# In[75]:


class employee:                                         

 def __init__(self, first, last, pay):
   self.first = first                                      
   self.last = last                                           
   self.pay = pay                                    

e1 = employee("Hani", "Namzi", 80000)
e2 = employee("Yassin", "Nour", 50000)

print("Employee Name:", e1.first, e1.last, "Salary:", e1.pay) 
print("Employee Name:", e2.first, e2.last, "Salary:", e2.pay)


# <h3 1d="download"> Pandas:</h3>

# In[19]:


import pandas as pd


# In[18]:


GPD = "C:\Users\hanyn\Desktop\GDP.xlsx"
df = pd.read_excel(GPD)
df.head()


# In[ ]:




