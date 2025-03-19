text = 'Hello, World'

vowel_count = 0


for char in text: 
    if char in 'aeiouAEIOU': 
        vowel_count += 1
        print(vowel_count)