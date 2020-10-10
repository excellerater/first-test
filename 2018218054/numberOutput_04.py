def numberOutput(string):
    for i in range(10):
        print(str(i) * string.count(str(i)),end='')
def main():
    numberStr = input("请输入一个字符串(仅含0-9的数字):")
    numberOutput(numberStr)
main()