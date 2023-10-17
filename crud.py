
#create

attendees = ["sujitha", "anusha", "madhuha"]
attendees.append("delip")
attendees.append("anusha")
print(attendees)
attendees.insert(3 ,"ramya")
#read
print(attendees.index("ramya"))
print(attendees.count("anusha"))
print(attendees.count("durga"))
if(attendees.count("durga")>0):
    print(attendees.index("durga"))
#update
attendees1 = [".3" "sri", "raji", "kusuma"]
print(attendees1)
lst = []
lst.append('aa')
print(lst)
attendees.extend(lst)
print(attendees)
#delete
attendees.remove('sujitha')
print(attendees)
attendees.pop()
attendees.pop()
print(attendees)
attendees.pop(3)
print(attendees)
#clear
fruits = ["mango", "watermelon", "orange"]
print(fruits.clear())
print(type(fruits))
print(attendees)
#delete
fruits = ["mango", "watermelon", "orange"]
del fruits[2]
print(fruits)

#sort
l = [2, 9, 8, 0 ,4, 88,3]
l.sort()
print(l)
#reverse
l1 = [0,77,90,87,32]
l1.reverse()
print(l1)

#tuple
#implicit
fruits = ("mango", "banana", "kivi")
print(fruits)
#explicit
fruits = tuple(("mango", "apple", "berry"))
print(fruits)
#variable annotation
fruits:tuple =("mango", "watermelon", "orange")
print(fruits)


#count
tpl = tuple((1,2, 3,9,1))
print(tpl.count(1))
#index
print(tpl.index(3))
#convert tuple to list
lst = list(tpl)
print(lst)
print(type(lst))
#convert list to tuple
l = tuple(lst)
print(l)
print(type(l))
#sort the list without using sort function
l1 = [56, 65, 67,45, 8,50,0]

for i in range(0, len(l1)):
    for j in range(i+1, len(l1)):
        if l1[i] >= l1[j]:
            temp = l1[i]
            l1[i] = l1[j]
            l1[j] = temp
    print(l1)




