#dictionary creation with tuple
dTuple={'fruits':('apple','banana','grapes')}
print(dTuple)
#here tuple is immutable,so we are converting them into list or set and after convertion ...
# again we are convertion those to tuple.
#adding elements
fruits_list=list(dTuple['fruits'])
fruits_list.append('papaya')
dTuple['fruits']=tuple(fruits_list)
print(dTuple)
#removing elements
fruits_list=list(dTuple['fruits'])
fruits_list.remove('banana')
dTuple['fruits']=tuple(fruits_list)
print(dTuple)
#sorting elements
fruits_list=list(dTuple['fruits'])
fruits_list.sort()
dTuple['fruits']=tuple(fruits_list)
print(dTuple)
#reversing elements
fruits_list=list(dTuple['fruits'])
fruits_list.reverse()
dTuple['fruits']=tuple(fruits_list)
print(dTuple)
#methods
dTuple['fruits'].count('fruits')



