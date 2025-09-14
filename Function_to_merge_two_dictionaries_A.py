def merge_dicts(d1, d2):
    return { **d1, **d2 }
print(merge_dicts({'a1':1,'b1':2,'c1':3},{'e1':8,'b1':6,'c1':7,'d1':4}))