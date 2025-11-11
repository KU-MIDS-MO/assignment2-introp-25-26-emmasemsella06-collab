#%%
def has_adjacent_duplicate(L):
    if len(L) < 2:
        return False 
    for i in range (len(L) - 1):
        if L[i] == L[i + 1]:
            return True 
    return False 
print(has_adjacent_duplicate([1, 2, 3, 4]))
print(has_adjacent_duplicate([5, 5, 2, 1]))   
print(has_adjacent_duplicate([1, 2, 2, 3, 4]))   
print(has_adjacent_duplicate([1]))
print(has_adjacent_duplicate([]))
print(has_adjacent_duplicate([1, 2, 3, 4, 2]))
print(has_adjacent_duplicate(['a','b','b','c']))
#%%