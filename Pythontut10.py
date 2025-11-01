'''
my_list = ["Recep", "JOhn", "Kelly", "PAnjeet"]
def second_letter(x):
    return x.lower()[1:]
        
y = sorted(my_list,key=second_letter)
print(y)
'''

'''
my_list = ["Recep", "JOhn", "Kelly", "PAnjeet"]
def length(x):
    return len(x)
y = sorted(my_list, key=length)
print(y)
'''

'''
inlist = [3,57,45,65,2.3,5.0,6.7]
def insertion_sort(x):
    output_list = []
    while len(x) != 0:
        output_list.append(min(x))
        x.pop(x.index(min(x)))
    print(output_list)
insertion_sort(inlist)
'''

'''
def insertion_sort(x):
    outlist = []
    for num in x:
        inserted = False
        for i in range(len(outlist)):
             if num < outlist[i]:
                 outlist.insert(i, num)
                 inserted = True
                 break
        if not inserted:
            outlist.append(num)
    print(outlist)

insertion_sort([5,36,7.2,14])
'''