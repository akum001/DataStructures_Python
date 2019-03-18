# input_string = input("Input numbers seperated by space: \n")
#
# my_list = input_string.split()
#
# print(my_list)

#+++++++++++++ALOG+++++++++++++++
#position <- 0
# found <- False
# while position < len(list) and not found:
#   if list[position] == item:
#        found = True
#   else:
#        position = position + 1



my_list = list(map(int, input("Enter numbers seperated by space\n").strip().split()))
item = int(input("Enter item to search: "))

print(my_list)

position = 0
found = False
n = len(my_list)
while position < n and not found:
    if my_list[position] == item:
        found = True
        print(f"Your item is available in the list at position {position}")
    else:
        position = position + 1
