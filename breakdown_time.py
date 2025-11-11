def breakdown_time(seconds):
    if type(seconds) != int or seconds < 0:
        return -1
    if seconds == 0:
        return {}
    
    h = seconds // 3600
    m = (seconds % 3600) // 60
    s = (seconds % 3600) % 60
    
    result = {}
    if h != 0:
        result[3600] = h
    if m != 0:
        result[60] = m
    if s != 0:
        result[1] = s
    
    return result
print(breakdown_time(7200))
print(breakdown_time(3675))
print(breakdown_time(0))
print(breakdown_time("3600"))
print(breakdown_time(-3600))
#%%
