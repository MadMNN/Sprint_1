timeString = '1h 45m,360s,25m,30m 120s,2h 60s'
minAll =0
str1 = timeString.split(",")

print(str1)

for timeStringOne in str1:
    stringH = 0
    stringM = 0
    stringS = 0
    h = timeStringOne.find('h')
    m = timeStringOne.find('m')
    s = timeStringOne.find('s')
    print(timeStringOne)

    timeStringCut = timeStringOne
    if h != -1:
        stringH = timeStringCut[0:timeStringCut.find('h')]
        cutH = timeStringCut[0:timeStringCut.find('h')+1]
        timeStringCut = timeStringCut.replace(cutH,'')
        timeStringCut = timeStringCut.strip()

    if m != -1:
        stringM = timeStringCut[0:timeStringCut.find('m')]
        cutM = timeStringCut[0:timeStringCut.find('m')+1]
        timeStringCut = timeStringCut.replace(cutM,'')
        timeStringCut = timeStringCut.strip()

    if s != -1:
        stringS = timeStringCut[0:timeStringCut.find('s')]
        cutS = timeStringCut[0:timeStringCut.find('s')+1]
        timeStringCut = timeStringCut.replace(cutS,'')
        timeStringCut = timeStringCut.strip()

    minOne = (int(stringH)*60 + int(stringM) + int(stringS)/60)
    print('всего по единице ', minOne)

    minAll += minOne

print('Итого:',minAll)




