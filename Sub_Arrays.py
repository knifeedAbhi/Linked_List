def SubArray(arr):
    final_list = []

    for i in range(0,len(arr)):
        end = len(arr)
        while end!=i:
            list2 = list()
            for count in range(i,end):
                list2.append(arr[count])
                count+=1
            final_list.append(list2)
            end-=1

    print(final_list)


demo_list = [2, 7, 5]
SubArray(demo_list)