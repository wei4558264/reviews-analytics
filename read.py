data = []
with open('reviews.txt','r') as f:
	for line in f:
		data.append(line)
x = 0 #
for d in data:
	x = x + len(d)	
print(x/len(data))
