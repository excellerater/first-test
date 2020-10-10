def numberOutput(string):
    numberList = sorted(string)
    for num in numberList:
        print(num, end='')
def main():
    numberStr = input("请输入一个字符串(仅含0-9的数字):")
    numberOutput(numberStr)
main()