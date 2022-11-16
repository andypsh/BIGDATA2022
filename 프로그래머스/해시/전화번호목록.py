phoneBook = ["119", "97674223", "1195524421"]
def solution(phoneBook):
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True

solution(phoneBook)


for p1, p2 in zip(phoneBook, phoneBook[1:]):
    print("p1 : {}".format(p1))
    print("p2 : {}".format(p2))

print(list(zip(phoneBook, phoneBook[1:])))
#119 , 97674223 ---- 97674223 , 1195524421 ==> 2가지 ==> zip 함수는 조합을 해준다.
print(list(zip(phoneBook, phoneBook[-1:])))
print("dfagd".startswith("abcd"))
#startswith 함수는 abcd가 dfagd로 시작하는지의 여부를 확인해준다.
print("abcde".startswith("abcd"))
print("abcde".endswith("cde"))
#endswith 함수는 cde가 abcde의 마지막에 있는지 여부를 확인해준다.
#%%
