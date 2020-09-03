# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.
with open(r'C:\Users\Emi\Desktop\LambdaAssignMents\cs-module-project-hash-tables\applications\crack_caesar',"r") as f:
  words = f.read()

# Your code here
def crack_caesar(message):
  letter_frequency = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D','L', 'W', 'U', 'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']
  
  count = {}
  key = {}
  deciphered = ''
  
  for char in message:
    if char in letter_frequency:
      if count.get(char) is None:
        count[char] = 1
      else:
        count[char] = count[char] + 1
        
  sorted_count = sorted(count.items(), key=lambda x: x[1], reverse=True)
  
  for i in range(len(letter_frequency)):
    key[sorted_count[i][0]] = letter_frequency[i]
    
  for c in message:
    if c in letter_frequency:
      deciphered += key[c]
    else:
      deciphered += c
      
  return deciphered

print(crack_caesar(words))
