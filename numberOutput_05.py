from collections import Counter
def numberOutput(string):
    numcount = Counter(string)
    print(''.join(sorted(numcount.elements())))
def main():
    numberStr = input("请输入一个字符串(仅含0-9的数字):")
    numberOutput(numberStr)
main()