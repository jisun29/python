

#print("*" * 100)
#happy_face = '^^'
#print(happy_face)
#print("*")
#a = "3"
#b = 5

#print(type(a))
#print(type(b))
#print(type(3.5))
#print(type(True))
#a = "256"
#print(int(a), type(int(a)))
#print(float(a), type(float(a)))

#print("hello", "world")



a = [9, 3, 6, 1, 2, 33, 12] #sorted와 sort가 있다
#print(sorted(a))
#print(a)
#a.sort()
#print(a)

#a = ["a", "b", "c", "A", "B"]

#a.reverse()
#print(a)


#a.append(10)
#print(a)
#a.insert(2, "0")
#print(a)

#print(a)
#a = [1, 2, 3, 1, 2, 3]
#a.remove(3)
#print(a) #[1, 2, 3, 1, 2, 3]
#a.pop() #마지막에 나오는 애 삭제
#print(a)

#b = [2, 3, 4, 1, 2, 4]
#b.remove(4)
#print(b)
#b.pop()


#a = ["A", "B", "C", "d", "e"]
#print(a.pop(1))
#print(a)
# pop은 pop() 하면 마지막 요소가 튀어나오지만 인덱스를 지정할 수 있다.

#a = "lalalalalaa"
#print("Count of a is:", a.count("a"))
#a = ["A","c", "b", "E", "B"]
#print(a.count("A"))
#print(sorted(a))



#a = ["red", "pink", "orange", "yellow", "green", "blue", "purple", "black", "white"]


#a.remove("green")
#print(a)

#color_list = ["red", "pink", "orange", "yellow", "green", "blue", "purple", "black", "white"]
#color_list.remove("green")
#print(color_list)

#color_list.insert(1,"pink")
#print(color_list)


#my_list = [0] * 10
#my_tuple = (0,0)*5
#print(my_list)
#print(my_tuple)

#my_list = [1, 2, 3, ["a", "b", "c"]]
#print(my_list[3][2])
#print(len(my_list))#4
#print(len(my_list[3]))#3

my_dictionary = dict()
print(my_dictionary)
my_dictionary = {"name": "Jisun", "location": "Korea"}
my_dictionary["age"] = 21
my_dictionary["name"]= "Kristen"
my_dictionary["favorite_color"] = [{"name": "blue",
                                   "is_cool": True}]

                                  
print(my_dictionary["name"])
print(my_dictionary.get("office_location", "Unknown"))

print(my_dictionary.keys())
print(my_dictionary.values())
print(my_dictionary.items())
for key, value in my_dictionary.items():
    print("key:", key)
    print("value:", value)

print(5 > 3) #boolean 값으로 바뀐다
print(5 < 10)
print("age" in my_dictionary) #"age"라는 키값이 my_dictionary에 있다

if "age" in my_dictionary:
    pass
else:
    my_dictionary["age"] = 50