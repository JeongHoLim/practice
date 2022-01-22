# https://programmers.co.kr/learn/courses/30/lessons/42577

from collections import defaultdict
    
def solution(phone_book):
    
    my_dict = defaultdict(bool)  
    phone_book.sort(key=len,reverse=True)
    
    for phone in phone_book:
        temp = ""
        for i in range(len(phone)-1):
            temp += phone[i]
            my_dict[temp] = True
            
        if my_dict[phone]:
            return False
        my_dict[phone] = True
    return True