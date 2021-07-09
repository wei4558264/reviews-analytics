data = []
with open('reviews.txt','r') as f:
	for line in f:
		data.append(line)
x = 0 #
for d in data:
	x = x + len(d)	
print(x/len(data))

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '筆清單長度小於100字')
print(new[0])
print(new[1])

good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('留言中有出現 good 共有',len(good), '筆')
print(good[0])
print(good[1])
