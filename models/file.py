counter = 0 

with open('map.txt', 'r') as f:
    for l in f:
        
        for i in l:
            if i == '1':
                counter += 1

with open('map.txt', 'r') as file:
    l = file.readlines()
    res = l[13].split(' ')
count = 0    
with open('map.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        numbers = line.split(' ')
        for n in numbers:
            count = count + int(n)
    
with open('map.txt', 'r') as f:
    
