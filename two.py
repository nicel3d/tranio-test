import re
import sys

line = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalpPLNzRW' \
      + 'XfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewVzKTUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjE' \
      + 'GRJosUfuhRRDUuTQwLlJJJDdkVjfSAHqnLxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJ' \
      + 'sOvqppOfyIVjXapzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnWetekUTVu' \
      + 'PluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfCvzQWrMMsYpLtdqRltXPqcSMXJIv' \
      + 'lBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbRuXbJrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJM' \
      + 'BSShDqbjAuDGTTrSXZywYkmjCCEUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBH' \
      + 'QaOnLfBtQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGSeuTSkyjIGsiWLAL' \
      + 'HUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCfKCuUJmGYJZPpRBFNLkqigxFkrRAppYRXeS' \
      + 'CBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWHuXBqHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIhe' \
      + 'ApQGOXWeXoLWiDQNJFaXiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQoiQ' \
      + 'zTYwZAiRwycdlHfyHNGmkNqSwXUrxgc'

ls = "ssGWWasfassg1geegweAsfegwe"

def lowerText(line):
    l = 0
    text = ""
    reText = ""
    reFA = re.findall(r'([A-Z]([a-z]))|(([a-z])[A-Z])', line)
    print(reFA)
    #return reFA
    for reItem in reFA:
        if reItem[1] != "":
            reText += reItem[1]
        else:
            reText += reItem[3]
    print(reText)
    for x in line:
        y = 0
        if x.islower():
            if l >= 1:
                if line[l - 1].isupper():
                    y = 1
            if l + 1 < len(line) and y == 0:
                if line[l + 1].isupper():
                    y = 1
        if y == 1:
            text += str(x)
        l = l + 1
    return text

def lowerText2Simb(line):
    l = 0
    text = ""
    reFA = re.findall(r'[a-z]{2}([A-Z])[A-Z]{2}', line)
    for x in line:
        if l >= 2 and (l + 2) <= len(line):
            if line[l - 1].islower() and line[l + 1].isupper() and x.isupper():
                if line[l - 2].islower() and line[l + 2].isupper():
                    text += str(x)
        l = l + 1
    return [''.join(reFA), text]

def fileText(line):
    fileName = "file_"
    arr = [[]] * 6
    l = 1
    for x in line:
        if l >= 6:
            l = 1
        arr[l] = arr[l] + [x]
        #    fileName+str(l)
        l = l + 1
    l = 1
    while l <= 5:
        file = open(fileName+str(l), "w")
        file.write(str(''.join(arr[l])))
        file.close()
        l = l + 1
    return [len(line), arr]

textCode = ["FooBar", "Bar", "Foo"]
def devNumber(i = 100):
    num = 0
    num_summ = [] * i
    while num <= i:
        if num // 3 and num % 3 == 0 and num // 5 and num % 5 == 0:
            num_summ.insert(num, textCode[0])
        elif num // 5 and num % 5 == 0:
            num_summ.insert(num, textCode[1])
        elif num // 3 and num % 3 == 0:
            num_summ.insert(num, textCode[2])
        else:
            num_summ.insert(num, num)
        num = num + 1
    return num_summ

print("\n5. Вывести символы в нижнем регистре, которые окружают 1 "
      +"или более символа в верхнем регистре. \nРешить задачу двумя способами: с помощью re и без.")

print(lowerText(line))

print("\n6. Вывести символы в верхнем регистре, которые окружают ровно два символа в нижнем регистре слева "
      +"\nи два символа в верхнем регистре справа. "
      +"\nРешить задачу двумя способами: с помощью re и без.")

q6 = lowerText2Simb(line)

print(str("regex: \t\t" + q6[0]) + "\n" + "not regex: \t" + str(q6[1]))


print("\n7. Записать исходную строку в 5 разных файлов (1-й символ в первый, второй во второй и т.д.), "
      +"\nимеющих названия 'file_1', 'file_2' и т.д.")

q7 = fileText(line)

print("size text\t\t" + str(q7[0]))

for i,v in enumerate(q7[1]):
    print("size array " + str(i) + "\t" + str(len(v)))

print("\n8. Вывести числа от 1 до 100 включительно. "
      +"\nЕсли число делится на 3 то вместо него вывести Foo. "
      +"\nЕсли делится на 5 то вывести Bar. Если делится на 3 и на 5 то вывести FooBar.")

q8 = devNumber()


for key, val in enumerate(q8):
    print(str(key) + "\t:\t" + str(val))