'''
author: Mr.Chen
function: sequence sort
version:1.0
date:2020/10/6
'''
from collections import Counter

def digit_sort1(sequence):
    # use the list method
    l = list(sequence)
    l.sort()
    # use join method
    s = ''.join(l)
    print('     Sorted sequence:', s)

def digit_sort2(sequence):
    # create a counter
    counter = [0] * 10
    # get the counts
    for s in sequence:
        counter[int(s)] += 1

    # display the sorted sequence
    print('     Sorted sequence: ', end='')
    for i, count in enumerate(counter):
        print(str(i) * count, end='')
    # use the tab to beautify the output
    print()

def digit_sort3(sequence):
    # create a hashable / dict
    counter = {}
    for s in sequence:
        counter[s] = counter.get(s, 0) + 1
    items = list(counter.items())
    # ascending sort
    items.sort(key=lambda x: x[0])
    # display the sorted sequence
    print('     Sorted sequence: ', end='')
    for s in items:
        print(s[0] * s[1], end='')
    print()

def digit_sort4(sequence):
    counter = Counter(sequence)
    items = list(counter.items())
    # ascending sort
    items.sort(key=lambda x: x[0])
    # display the sorted sequence
    print('     Sorted sequence: ', end='')
    for s in items:
        print(s[0] * s[1], end='')
    print()


def main():
    # enter digit sequence
    sequence = input('Enter digit sequence: ')
    digit_sort1(sequence)
    digit_sort2(sequence)
    digit_sort3(sequence)
    digit_sort4(sequence)


if __name__ == '__main__':
    main()

# 有兴趣可以查看 https://leetcode-cn.com/problems/sort-colors/ 颜色分类