data = []
with open ('reviews.txt','r') as f:
	data = [a for a in f]
print(data[0])
badset = []
badset = [d for d in data if 'bad' in d]
print(badset[0])



