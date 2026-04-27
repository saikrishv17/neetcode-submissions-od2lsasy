from typing import List

def count_unique_words(words: List[str]) -> int:
    count = 0 
    words = set(words)
    words = list(words)
    for element in words:
        count += 1 
    return count 

# do not modify code below this line
print(count_unique_words(["hello", "world", "hello", "goodbye"]))
print(count_unique_words(["hello", "world", "i", "am", "world"]))
print(count_unique_words(["hello", "hello", "hello"]))
print(count_unique_words([]))
