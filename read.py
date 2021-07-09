data = []
with open('reviews.txt','r') as f:
	for line in f:
		data.append(line)
i = 0
x = 0
while i < 1000000:
	x = x + len(data[i])
	i = i+1
print(x/1000000)
