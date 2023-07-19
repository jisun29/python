from collections import UserDict
from urllib import response


a = {'A': 90, 'B': 80, 'C': 70, 'D': 60}
print(a["B"])
print(a.get("B"))
if ('B' in a):
    print(a['B'])


my_list = [1, 2, 3, 4, "A"]
my_list.append("B")
print(my_list)
#print(set(my_list))
#my_set = set()
my_set = {1, 2, 3}
my_set.add(4)
print(my_set)

set1 = {1, 2, 3, 4, 5}

set2 = {4, 5, 6, 7}
set2.add(8)

print(set1 & set2)
print(set1 | set2)
print(set1 - set2)


s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])
s3 = s1 & s2
s3 = s1.intersection(s2)
s4 = s1 - s2
s4 = s1.difference(s2)

my_list = [1, 2, 3, 4, 9, 11, 11, 11, 14]
my_list = set(my_list)
print(my_list)

print(5 == "5")
print(5 !=3)
print(3 <=2 )


print(5> 3 and 10 >1)
print(5 > 3 or 1 > 10)
print(not False)
print(not True)
#if UserDict.authenticated:
 #   return response("message": "로그인을 먼저 해주세요")


# a = "teacher"
    # if True:
   #    print('~~~~~')
  #     print('-----')
#elif ( 3> 5 and 2 < 4 ):
 #  print('hello')
#else:
#   print('aaa')

score = input("점수가 몇점인가요?")
score = int(score)
if score >= 90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
else:
    print('D')