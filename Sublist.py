# def contains_sublist(lst, sublst):
#     len_lst = len(lst)
#     len_sublst = len(sublst)
#     for i in range(len_lst - len_sublst + 1):
#         if lst[i:i + len_sublst] == sublst:
#             return True
#     return False
# main_list = [1, 2, 3, 4, 5]
# sub_list = [3, 4]
# print(contains_sublist(main_list, sub_list))





















def check(list,sublist):
    listlen=len(list)
    sublen=len(sublist)
    for i in range(listlen-sublen+1):
        if list[i:i+sublen]==sublist:
            return True
    return False
mainlist=[1,2,3,4,5,6,7,8,9,10]
sub=[5,6]
print(check(mainlist,sub))