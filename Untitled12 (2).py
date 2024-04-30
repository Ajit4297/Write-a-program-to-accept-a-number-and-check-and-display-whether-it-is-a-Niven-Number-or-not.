#!/usr/bin/env python
# coding: utf-8

# In[4]:


n=int(input())
temp=n
s=0
while n!=0:
    d=n%10
    s=s+d
    n=n//10
print("Yes" if temp%s==0 else "No")


# In[ ]:




