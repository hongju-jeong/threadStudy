i=0
while i<10 :
    with open(f'text{i}.txt','w') as f:
        f.write(f'{i}')
    i+=1
