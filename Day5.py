data = "Tôi thích AI thích Toán"
corpus = ["Tôi thích môn Toán","Tôi thích AI", "Tôi thích âm nhạc"]
corpus = str(corpus).replace("[", "")
corpus = corpus.replace("]", "")
corpus = corpus.replace(",", "")
corpus = corpus.replace("'", "")

token = set(corpus.split(" "))
vocabulary = list(token)

data = data.split(" ")
dic = {}

for word in vocabulary:
    dic[word] = data.count(word)

for i in data:
    print(i,end=" ")
lst_word = list(dic.values())
print(":",lst_word)

lst_bow = list(dic.keys())
print("Bag-of-Words:",lst_bow)