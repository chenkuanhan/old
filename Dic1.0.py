input1 = ['a', 'b', 'c', 'a', 'c', 'a', 'x']

dic1 = {}

for i in range(len(input1)):
  ddic = {input1[i]:input1.count(input1[i])}
  #print(dic1)
  dic1.update(ddic)
print(dic1)