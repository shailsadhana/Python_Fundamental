#!/usr/bin/env python
# coding: utf-8

# In[19]:


class dog:
    """creating a dog class and describing its instructions"""
    def __init__(self, name, age):
        self.name=name
        self.age=age
        print('This print automatically')
        
        def sit(self):
            print(f"(self.name) is now sitting.")
        
        def roll_over(self):
            print(f"(self.name) is now rolling over")
        
        def jump(self): 
            print(f"(self.name) is now jumping")    


# In[25]:


a=dog('rex',4)
a.sit


# In[26]:


a.jump


# In[ ]:





# In[22]:


def describe_pet(pet_name,animal_type='Dog'):
    """ Creating a function to describe about details of pet"""
    print(f"I have a Pet {animal_type}")
    print(f"my animal type name is {pet_name}")
    
describe_pet('Jery')


# In[23]:


describe_pet('cat','snowball')


# In[24]:


describe_pet('rex','dog')


# In[ ]:




