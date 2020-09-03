# Your code here
with open(r'C:\Users\Emi\Desktop\LambdaAssignMents\cs-module-project-hash-tables\applications\histo\robin.txt',"r") as f:
  words = f.read()
  
def histo(words):
  filtered_chars = '":;,.-+=/\|[]{}()*^&'
  
  filtered_string = ''.join(filter(lambda x : x not in filtered_chars, words))
  
  word_list = filtered_string.split()
  
  largest_word = max(word_list, key=lambda s: (len(s), s))
  
  count = {}
  
  for w in word_list:
    word = w.lower()
    if count.get(word) is None:
      count[word] = 1
    else:
      count[word] = count[word] + 1
      
  count_sorted = sorted(count.items(), key=lambda x: x[1], reverse=True)
  
  for word, count in count_sorted:
    white_space = len(largest_word) - len(word) + 2
    print(word + ' ' * white_space + count * '#')
    
print(histo(words))

