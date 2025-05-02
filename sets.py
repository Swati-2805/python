myset={12,78,34,78}
print(myset)
myset2={76,34,22}
print(myset2)
print(type(myset))
res=myset|myset2
print("The union of both the set",res)
res2=myset.union(myset2)
print("The union of both the sets are",res2)
res=myset & myset2
print(res)
