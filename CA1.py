#!/usr/bin/env python
# coding: utf-8

# In[1]:


1+1


# In[2]:


1*3


# In[3]:


1/2


# In[4]:


2**4


# In[5]:


4%2


# In[6]:


5%2


# In[7]:


(2+3)*(5+5)


# In[8]:


#Can not start with number or special characters
name_of_var = 2


# In[9]:


x= 0
y = 3


# In[10]:


z = x + y


# In[11]:


z


# In[12]:


'single quotes'


# In[13]:


example = 'single quotes'
print(example)


# In[14]:


"double quotes"


# In[15]:


'wrap lot"s of other quotes'


# In[16]:


x = 'hello'


# In[17]:


x


# In[18]:


print(x)


# In[19]:


num = 12


# In[20]:


name = 'Sam'


# In[21]:


print('My number is:{one}, and my name is: {two}'.format(one=num,two=name))


# In[22]:


print('My number is:{one}, and my name is: {two}'.format(one=num,two=name))


# In[23]:


print('My number is:{}, and my name is: {}'.format(num,name))


# In[24]:


[1,2,3]


# In[25]:


['hi',1,[1,2]]


# In[26]:


my_list = ['a','b','c']


# In[27]:


type(my_list)


# In[28]:


my_list.append('d')


# In[29]:


my_list.append(3)


# In[30]:


my_list


# In[31]:


my_list[0]


# In[32]:


my_list[1]


# In[33]:


my_list[:3]


# In[34]:


#the End index is not included
my_list[:2]


# In[35]:


my_list


# In[36]:


my_list[5] = 'New'


# In[37]:


my_list.append(3)


# In[38]:


my_list


# In[40]:


my_list[5] = 'NEW'


# In[41]:


my_list


# In[42]:


list1 = ['target']
list2 = [4,5,list1]
list3 = [1,2,3,list2]
list3


# In[43]:


nest = [1,2,3,[4,5,['target']]]


# In[44]:


nest[3]


# In[45]:


nest[3][2]


# In[46]:


nest[3][2][0]


# In[47]:


type(nest[3][2])


# In[48]:


type(nest[3][2][0])


# In[49]:


d = {'key1':'item1','key2':'item2','key3':'item3'}


# In[50]:


d


# In[51]:


d_value = d['key1']
print(d_value)


# In[52]:


d['key1']


# In[53]:


d.keys()


# In[54]:


d.values()


# In[55]:


d_keys=d.keys()
type(d_keys)


# In[56]:


True


# In[57]:


False


# In[58]:


t = (1,2,3,2,'aaa',[1,1,3])


# In[59]:


t[0]


# In[60]:


t[0]='NEW'


# In[61]:


t.count[3]


# In[62]:


t.count(3)


# In[63]:


t.index(2,2)


# In[64]:


{1,2,3}


# In[65]:


set_example=set([0,0,5,6])
set_example1 = set([5,1])


# In[66]:


set_example


# In[67]:


{1,2,3,1,2,1,2,3,3,3,3,2,2,2,1,1,2}


# In[68]:


set.example.intersection(set_example1)


# In[69]:


set_example.intersection(set_example1)


# In[70]:


1>2


# In[71]:


1<2


# In[72]:


1>=1


# In[73]:


1<=4


# In[74]:


1==1


# In[75]:


'hi'='bye'


# In[76]:


'hi'=='bye'


# In[77]:


'HI' != 'hi'


# In[78]:


(1>2)and(2<3)


# In[79]:


(1>2)or(2<3)


# In[80]:


(1==2)or(2==3)or(4==4)


# In[81]:


not(1==2)


# In[82]:


if 1<2:
    print('Yelp!')
    print('Yelp2!')


# In[83]:


if 1<2:
    print('yep!')


# In[84]:


if 3<2:
    print('first')
else:
    print('last')


# In[85]:


if 1>2:
    print('first')
else:
    print('last')


# In[86]:


if 1==2:
    print('first')
elif 3==3:
    print('middle')
else:
    print('Last')


# In[87]:


seq = [1,2,3,4,5]


# In[88]:


for i in seq:
    print(i+30)


# In[89]:


for item in seq:
    print('Yep')


# In[90]:


for jelly in seq:
    print(jelly+jelly)


# In[91]:


i = 1
while i<5:
    print('i is:{}'.format(i))
    i = i+1
    


# In[92]:


#Upper limit, i.e:the stop;is not included
x=range(5)
print(x)


# In[93]:


for i in rnage(5):
    print(i)


# In[94]:


for i in range(5):
    print(i)


# In[95]:


for i in range(-2,7,2):
    print(i)


# In[96]:


L=list(range(5))
print(L)


# In[97]:


LL = [list(range(5))]
print(LL)


# In[98]:


print(LL[0])


# In[99]:


print(LL[1][2])


# In[100]:


x = list(range(10000))


# In[101]:


get_ipython().run_cell_magic('timeit', '', 'out[]\nfor item in x:\n    out.append(item*2)')


# In[102]:


get_ipython().run_cell_magic('timeit', '', 'out[]\nfor item in x:\n    out.append(item*2)\n#print(out)')


# In[103]:


get_ipython().run_cell_magic('timeit', '', 'out[]\nfor item in x:\n    out.append(item**2)\n#print(out)')


# In[104]:


get_ipython().run_line_magic('timeit', '')
out[]
for item in x:
    out.append(item**2)
#print(out)


# In[117]:


def my_func(param2,param1='Amr'):
    """
    Docstring goes here.
    Template: https://www.python.org/dev/peps/pep-0008/
    """
    print(paraml)
    return


# In[109]:


my_fun(param2='new param')


# In[118]:


my_func(param2='new param')


# In[119]:


my_func


# In[120]:


my_func('new param')


# In[121]:


def square(x):
    return x**2


# In[122]:


out = square(3)


# In[123]:


print(out)


# In[124]:


def times2(var):
    return var*2


# In[125]:


times2(2)


# In[126]:


lambda var: var*2


# In[127]:


seq = [1,2,3,4,5]


# In[128]:


map(times2,seq)


# In[129]:


list(map(times2,seq))


# In[130]:


list(map(lambda var: var*2,seq))


# In[131]:


filter(lambda item: item%2 ==0,seq)


# In[132]:


filtered_list = list(filter(lambda x: x%2 == 0,seq))


# In[133]:


filtered_list


# In[ ]:




