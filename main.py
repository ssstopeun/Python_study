# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.



# Press the green button in the gutter to run the script.

def is_all_unique(list):
    return len(list) == len(set(list))

if __name__ == '__main__':
    print("================input===================")
    applicant_num = int(input())
    score_list = []
    if 0<applicant_num and applicant_num<=100000:
        for i in range(applicant_num):
            score1, score2 = map(int,input().split())
            score_list.append((score1,score2))

        score_list.sort(reverse=False)

        if is_all_unique(score_list):
            smallest = applicant_num
            representative_count = 0
            for x, y in score_list:
                if y < smallest:
                    smallest = y
                    representative_count +=1

                # is_representative = True
                # target_score1 = score_list1[i]
                # target_score2 = score_list2[i]
                # for j in range(applicant_num):
                #     if target_score1 > score_list1[j]:
                #         if target_score2 > score_list2[j]:
                #             is_representative = False
                #
                # if is_representative:
                #     representative_count = representative_count + 1

            print("================output===================")
            print(representative_count)

        else:
            print("입력에 같은 등수가 존재합니다. 다시 입력해주세요.")

    else:
        print("지원자의 수를 잘못입력하였습니다.(0<n<=100,000)")




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
