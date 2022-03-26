instr = input()
pattern = input()
count = i = 0
while i <= len(instr)-len(pattern):
    if instr[i:i+len(pattern)] == pattern: 
        count+=1
        i += len(pattern)
    else : i += 1
print(count)