#!/usr/bin/env python
# coding: utf-8

# # FIBONACCI SERIES

# In[1]:


series = int(input("Enter the length to which you want to print Fibonacc Series : "))
no1=0
no2=1
result=0
print(no2)
for i in range(series-2):
    result = no1 + no2
    no1=no2
    no2=result
    print(result)

    


# # REVERSING A STRING METHOD 1

# In[17]:


text = input("Enter the string : ")
str1=""
for i in text:
    str1 = i + str1
print(str1)


# # REVERSING A STRING METHOD 2

# In[7]:


text = input("Enter the string : ")
text1 = text[::-1]
print(text1)


# # COUNTING NUMBER OF ODD AND EVEN IN A SERIES OF INTERGERS

# In[4]:


lst = []
no = int(input("Enter the number of values which user wants to input : "))
for i in range(no):
    items = int(input())
    lst.append(items)

even=0
odd=0

for j in lst:
    if j%2==0:
        even+=1
    else:
        odd+=1
print("Number of even numbers : ",even)
print("Number of odd numbers : ",odd)


# In[ ]:




