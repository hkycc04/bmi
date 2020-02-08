wei = input('請輸入體重: ')
hight = input('請輸入身高(公分): ')
wei = int(wei)
hight = int(hight) /100
bmi = int(wei / hight / hight)
if bmi < 18.5:
    print('體重過輕')
elif bmi >= 18.5 and bmi < 24:
    print('您的bmi值為:', bmi, '正常')
elif bmi >= 24 and bmi < 27:
    print('您的bmi值為:', bmi, '過重')
elif bmi >= 27 and bmi < 30:
    print('您的bmi值為:', bmi, '輕度肥胖')
elif bmi >= 30 and bmi < 35:
    print('您的bmi值為:', bmi, '中度肥胖')
else:
    print('您的bmi值為:', bmi, '重度肥胖')
