new_list = [1, 4, 23, 2, 53, 34]
print("new_list:", new_list)
# to sort the list in ascending order
sorted_list = new_list.sort()
print("sorted list:", sorted_list)  # None -> return value of sort() method is None
print("new list:", new_list)

# to sort the list in descending order
new_list.sort(reverse=True)
# do not assign to a variable, because sort() method returns None, only sorts the original list (so changes the original list)
print("new_list:", new_list)

# sorted() method returns a new sorted list, does not change the original list
new_list2 = [3, 4, 1, 2, 5, 9, 13, 8, 7, 6]
print("new list 2:", new_list2)

sorted_list2 = sorted(new_list2)
print("sorted list ascending:", sorted_list2)
print("new list 2:", new_list2)  # original list is not changed

# descending sorted() method
sorted_list3 = sorted(new_list2, reverse=True)
print("sorted list descending:", sorted_list3)

# list append method
new_list3 = [1, 2, 3, 4, 5]
print("new list 3:", new_list3)
new_list3.append(6)
print("new list 3:", new_list3)

# list insert method
new_list4 = [1, 2, 3, 4, 5]
print("new list 4:", new_list4)
new_list4.insert(3, 43)
print("new list 4:", new_list4)

# list extend method
new_list5 = [1, 2, 3, 4, 5]
print("new list 5:", new_list5)
new_list5.extend(
    [6, 7, 8, 9, 10]
)  # or (6, 7, 8, 9, 10) or {6, 7, 8, 9, 10} does not matter
print("new list 5:", new_list5)

# extend method with string
new_list5.extend(
    "hello"
)  # "hello" is a string, so it is treated as a list of characters
print("new list 5:", new_list5)
new_list5.extend(
    ("world",)
)  # ("world",) is a tuple, so it is treated as a single element
print("new list 5:", new_list5)
new_list5.extend(
    ["world"]
)  # it is treated as a single element but ("world") is a string, so it is treated as a list of characters
print("new list 5:", new_list5)


# list remove method
new_list6 = [1, 2, 3, 4, 5]
print("new list 6:", new_list6)
new_list6.remove(3)  # 3 is the value, not the index
print("new list 6:", new_list6)

# list pop method
new_list7 = [1, 2, 3, 4, 5]
print("new list 7:", new_list7)
new_list7.pop()
print("new list 7:", new_list7)
new_list7.pop(0)  # 0 is the index, not the value
print("new list 7:", new_list7)

# list clear method
new_list8 = [1, 2, 3, 4, 5]
print("new list 8:", new_list8)
new_list8.clear()
print("new list 8:", new_list8)

# list index method
new_list9 = [1, 2, 3, 4, 5]
print("new list 9:", new_list9)
print("index of 3:", new_list9.index(3))

# list count method
new_list10 = [1, 2, 3, 4, 5, 3, 3, 3, 3]
print("new list 10:", new_list10)
print("count of 3:", new_list10.count(3))

# list concatenation
new_list11 = [1, 2, 3, 4, 5]
new_list12 = [6, 7, 8, 9, 10]
print("new list 11:", new_list11)
print("new list 12:", new_list12)
new_list13 = new_list11 + new_list12
print("new list 13:", new_list13)

# list repetition
new_list14 = [1, 2, 3, 4, 5]
print("new list 14:", new_list14)
new_list15 = new_list14 * 3
print("new list 15:", new_list15)

# list membership
new_list16 = [1, 2, 3, 4, 5]
print("new list 16:", new_list16)
print("is 3 in new list 16:", 3 in new_list16)
print("is 6 in new list 16:", 6 in new_list16)

# list iteration
new_list17 = [1, 2, 3, 4, 5]
print("new list 17:", new_list17)
for i in new_list17:
    print(i)

# list comprehension
new_list18 = [1, 2, 3, 4, 5]
print("new list 18:", new_list18)
new_list19 = [i for i in new_list18]
print("new list 19:", new_list19)

# list comprehension with if condition
new_list20 = [1, 2, 3, 4, 5]
print("new list 20:", new_list20)
new_list21 = [i for i in new_list20 if i % 2 == 0]
print("new list 21:", new_list21)

# list comprehension with if else condition
new_list22 = [1, 2, 3, 4, 5]
print("new list 22:", new_list22)
new_list23 = [i if i % 2 == 0 else "odd" for i in new_list22]
print("new list 23:", new_list23)

# list comprehension with nested for loop
new_list24 = [1, 2, 3, 4, 5]
print("new list 24:", new_list24)
new_list25 = [[i, j] for i in new_list24 for j in new_list24]
print("new list 25:", new_list25)

# list comprehension with nested for loop and if condition
new_list26 = [1, 2, 3, 4, 5]
print("new list 26:", new_list26)
new_list27 = [[i, j] for i in new_list26 for j in new_list26 if i != j]
print("new list 27:", new_list27)

# list comprehension with nested for loop and if else condition
new_list28 = [1, 2, 3, 4, 5]
print("new list 28:", new_list28)
new_list29 = [[i, j] if i != j else "same" for i in new_list28 for j in new_list28]
print("new list 29:", new_list29)

# list comprehension with nested for loop and if else condition
new_list30 = [1, 2, 3, 4, 5]
print("new list 30:", new_list30)
new_list31 = [
    [i, j] if i != j else "same" for i in new_list30 for j in new_list30 if i != j
]
print("new list 31:", new_list31)


# list slicing
new_list32 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# list[start:end:step] -> "start" is inclusive, "end" is exclusive, "step" is optional, default is 1
print("new list 32:", new_list32)
print("new_list32[1:9:3]:", new_list32[1:9:3])
# step - 1 -> skip items -> new_list32[1:9:3] -> 3 - 1 = 2 -> skip 2 items -> 2, 5, 8
print("new list 32[1:3]:", new_list32[1:3])
print("new list 32[1:]:", new_list32[1:])  # from index 1 to end
print(
    "new list 32[:3]:", new_list32[:3]
)  # from start to index 3 (not including index 3)
print(
    "new list 32[::2]:", new_list32[::2]
)  # from start to end with step 2 (skip 1 element)

# negative slicing
print("new list 32[::-1]:", new_list32[::-1])  # reverse the list
print("new list 32[-1:]:", new_list32[-1:])  # last element
print("new list 32[-3:]:", new_list32[-3:])  # last 3 elements
print("new list 32[:-3]:", new_list32[:-3])  # all elements except last 3 elements
print("new list 32[-3:-1]:", new_list32[-3:-1])  # last 3 elements except last element
print(
    "new list 32[-3:-1:2]:", new_list32[-3:-1:2]
)  # last 3 elements except last element with step 2
print(
    "new list 32[-1:-4:-1]:", new_list32[-1:-4:-1]
)  # last 3 elements in reverse order -> negative "step" (-1) means reverse order

# with using slice method
new_list33 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("new list 33:", new_list33)
sliced_list = slice(1, 9, 3)  # slice(start, end, step)
print(
    "sliced list:", new_list33[sliced_list]
)  # new_list33[1:9:3] is same as new_list33[sliced_list]
