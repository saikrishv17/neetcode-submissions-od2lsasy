from typing import List

def read_integers() -> List[int]:
    nums = input()
    my_list = []
    for char in nums.split(","):
        my_list.append(int(char))
    return my_list 
    
# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
