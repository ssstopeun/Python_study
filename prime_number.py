from itertools import permutations


def check_primeNumber(number):
    if number<2:
        return False
    for i in range(2,number):
        if number % i == 0:
            return False
    return True

if __name__ == "__main__":
    print("==============Input================")
    input = (input())
    target_list = []
    for i in str(input):
        target_list.append(i)


    if len(target_list) <= 20:
        primeNumber_list = []
        for i in range(1, len(target_list) + 1):
            permutations_list = list(map(''.join, permutations(list(target_list),i)))
            for j in list(set(permutations_list)):
                if check_primeNumber(int(j)):
                    primeNumber_list.append(int(j))

        print("==============Output================")
        print(len(primeNumber_list))

    else :
        print("문자열의 길이는 20이하 입니다.")




