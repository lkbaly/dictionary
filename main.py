word = input("Введите непонятное слово (большими буквами!): ")
meme_dict = {
            "КРИНЖ": "Что-то очень странное или стыдное",
            "ЛОЛ": "Что-то очень смешное"
            }
if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("Нету")
