def func(s):
    one = 0
    zero = 0
    
    for i in range(len(s)):
        if i > 0 and s[i] == s[i-1] : continue
        if s[i] == "1":
            one += 1
        else : 
            zero += 1
    
    return min(one,zero)


s = input()
print(func(s))
