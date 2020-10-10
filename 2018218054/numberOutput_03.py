def numberOutput(string):
    number_dict = {"0":0,"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0}
    for i in string:
        number_dict[i] += 1
    for num in sorted(number_dict.keys()):
        print(num*number_dict[num],end='')
def main():
    numberStr = input("请输入一个字符串(仅含0-9的数字):")
    numberOutput(numberStr)
main()