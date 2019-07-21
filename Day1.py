#You are given two linked-lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

a,b=[2,4,3],[5,6,4]

r=sum([(x+y)*10**i for i,(x,y) in enumerate(zip(a,b))])
print(r)
