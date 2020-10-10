def numberOutput(string):
    counts = [0,0,0,0,0,0,0,0,0,0]
    for i in string:
        counts[int(i)] = counts[int(i)] + 1
    for j in range(len(counts)):
        print(str(j) * counts[j], end='')
def main():
    numberStr = input("请输入一个字符串(仅含0-9的数字):")
    numberOutput(numberStr)
main()