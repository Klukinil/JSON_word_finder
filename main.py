import json
def word_finder(json_file, word_length, top):
  with open(json_file) as f:
    json_data = json.load(f)
  news_list = json_data["rss"]["channel"]["items"]
  news_text = []
  for item in news_list:
    news_text.append(item['description'])
  words_list = []
  for news in news_text:
    words_list.append(news.split())
  words = words_list[0]
  for i in range(1, len(words_list)):
    words += words_list[i]
    i +=1
  long_words = []
  for word in words:
    if len(word) >= word_length:
      long_words.append(word)
  long_words.sort()
  words_count = dict()
  for  long_word in long_words:
    words_count[long_word] = long_words.count(long_word)
  value_count = []
  for value in words_count.values():
    value_count.append(value)
  value_count.sort(reverse=True)
  top_value = value_count[0:top]
  top_word = dict()
  for key,value in words_count.items():
    if value in top_value:
      top_word[key] = value
  print(top_word)

word_finder("newsafr.json", 6, 10)