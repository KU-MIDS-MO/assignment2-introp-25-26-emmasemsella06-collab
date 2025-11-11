def swap_ends(L, k):
    if k <= 0 or len(L) == 0 or k > len(L) // 2:
        return(L.copy(), 0)
    
    first_part = L[:k]
    middle_part = L[k:-k]
    last_part = L[-k:]
    
    new_list = last_part + middle_part + first_part
    num_swaps = k
    return(new_list, num_swaps)

print(swap_ends([1, 2, 3, 4, 5, 6], 2))
print(swap_ends(['a', 'b', 'c', 'd', 'e'], 2))
print(swap_ends([10, 20, 30, 40, 50], 3))
print(swap_ends([], 2))
print(swap_ends([1, 2, 3], 0))
#%%























