Dic1 ={1:10, 2:20}
Dic2 ={3:30, 4:40}
Dic3 ={5:50,6:60}
Final = {}
for items in (Dic1, Dic2, Dic3): Final.update(items)
print(Final)
