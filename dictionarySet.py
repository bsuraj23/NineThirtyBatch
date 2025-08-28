dSet1={'boquet':{'flowers':{'roses','lilly','jasmine'}},
       'color':{'red','blue','pink'}}
dSet2={'boquets':{'flowers':{'mariegold','lilly','roses'}}}
#union operatior
union=dSet1['boquet']['flowers']|dSet2['boquets']['flowers']
print(union)
#intresection operator
inter=dSet1['boquet']['flowers'] and dSet2['boquets']['flowers']
print(inter)
#difference operator
diff=dSet1['boquet']['flowers']- dSet2['boquets']['flowers']
print(diff)
#adding elements
dSet1['boquet']['flowers'].add('hibiscus')
dSet1['color'].add('green')
print(dSet1)
#removing elements
dSet1['boquet']['flowers'].remove('lilly')
dSet2['boquets']['flowers'].remove('mariegold')
print(dSet1)
print(dSet2)
