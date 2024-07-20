list1=list(map(int,input().split()))
sec_max=0
new_list=[]
for i in list1:
    if i>sec_max:
        sec_max=i
new_ele=sec_max
sec2_max=0
for i in list1:
    if i>sec2_max and i!=new_ele:
            new_ee=i
print(new_ele)