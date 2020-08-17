en = int(input('英文成績: '))
ma = int(input('數學成績: '))
if en >= 0 and ma<=100 and ma >= 0 and en<=100 :
    if en >= 90 and ma >= 90:
        print('有獎品')
        
    elif en < 60 and ma < 60:
        print('有處罰')
        
    elif en < 60 or ma < 60:
        print('再加油')
        
    else:
        print('沒事')
else:
    print('輸入錯誤')
