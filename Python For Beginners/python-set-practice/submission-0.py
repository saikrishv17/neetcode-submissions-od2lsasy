from typing import List

def contains_duplicate(words: List[str]) -> bool:
    og_count = len(words)
    new = set(words)
    new_count = len(new)

    if new_count < og_count:
        return True 
    else:
        return False

# do not modify code below this line
print(contains_duplicate(["hello", "world", "hello"]))
print(contains_duplicate(["hello", "world", "i", "am", "great"]))
print(contains_duplicate(["hello", "hello", "hello"]))
print(contains_duplicate(["Hello", "hellooo", "hello"]))
