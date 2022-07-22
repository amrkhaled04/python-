#!/usr/bin/env python
# coding: utf-8

# In[86]:


#question 1

x = open("C:/Users/amrkh/Desktop/python.txt")
x.read()


# In[85]:


#question 2

x = open("C:/Users/amrkh/Desktop/python.txt")
y = eval(input())
c = 0
for line in x:
    if(c<y):     
        print(line, end = '')
    c+=1


# In[81]:


# question 3

x = open("C:/Users/amrkh/Desktop/python.txt")
y = eval(input())
c = 0
i = 0
for k in x:
    c+=1
f = c-y-1
x = open("C:/Users/amrkh/Desktop/python.txt")
for line in x:
    if (i > f):
        print(line, end='')
    i+=1


# In[96]:


#question 4 

x = open("C:/Users/amrkh/Desktop/python.txt")
y = x.read().split()
print(len(y))


# In[ ]:




