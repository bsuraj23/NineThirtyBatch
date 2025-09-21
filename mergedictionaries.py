<<<<<<< HEAD
def merge_dicts(d1,d2):
    D=d1.copy()
    D.update(d2)
    return D
d1={'a':1,'b':2}
d2={'c':3,'d':4}
print(merge_dicts(d1,d2))