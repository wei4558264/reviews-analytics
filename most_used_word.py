#開啟檔案
data = []
count_reviews = 0
with open ('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count_reviews += 1
print("共有", count_reviews, "個留言")

# 計算最常出現的單字
worddict = {}
for line in data:
	line2 = line.split()
	for word in line2:
		if word in worddict:
			worddict[word]+=1
		else:
			worddict[word] = 1
	
#列出超過出現200次以上的單字
#for wd in worddict:
	#if worddict[wd] >= 200:
		#print(wd, ":", worddict[wd])

#互動式單字次數查詢
while True:
	ask_word = input("請問你想查哪個單字出現次數:")
	if ask_word == "q":
		break
	elif ask_word in worddict:
		print(ask_word, "出現了", worddict[ask_word], "次")
	else:
		print(ask_word, "沒有出現喔!")