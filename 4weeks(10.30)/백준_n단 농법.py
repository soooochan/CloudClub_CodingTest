n = int(input())

# 딕셔너리 활용해서 -> 이게 있으면 ->를 타고 들어가고,,
dict = {}
for i in range(n):
    logic = input()
    logic = logic.split(" is ")
    first = logic[0]
    end = logic[1]
    if first not in dict.keys():
        dict[first] = end
    else:
        dict[first].append(end)

answer_n = int(input())

for i in range(answer_n):
    logic = input()
    logic = logic.split(" is ")
    first = logic[0]
    end = logic[1]
    if first in dict.keys():
        sec_first = dict[first]
        if sec_first in dict.keys():
            if dict[sec_first] == end:
                print("T")
                continue
            else:
                thir_first = dict[sec_first]
                if thir_first in dict.keys():
                    if dict[thir_first] == end:
                        print("T")
                        continue
                    else:
                        print("F")
                        continue

        if dict[first] == end:
            print("T")
            continue
        else:
            print("F")
            continue
    else:
        print("F")
