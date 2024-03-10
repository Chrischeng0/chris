import csv as c
student=[{'國文': 84, '英文': 55, '數學': 51},
         {'國文': 61, '英文': 97, '數學': 89},
         {'國文': 74, '英文': 64, '數學': 98},
         {'國文': 53, '英文': 59, '數學': 52}, 
         {'國文': 90, '英文': 90, '數學': 83},
         {'國文': 92, '英文': 57, '數學': 97},
         {'國文': 51, '英文': 99, '數學': 70},
         {'國文': 65, '英文': 55, '數學': 100}, 
         {'國文': 53, '英文': 71, '數學': 98},
         {'國文': 100, '英文': 100, '數學': 100}]


def save_csvfile(fn:str,data:list[dict[str,int]]):
    '''
    儲存為csv檔
    參數fn:str->檔案名稱
    參數data:list[dict]->dict內的key,必須是[國文,數學,英文]
    '''
    with open(fn,mode='w',encoding='utf-8',newline='') as  csvfile:
        writer=c.DictWriter(csvfile,fieldnames=['國文','數學','英文'])
        writer.writeheader()
        writer.writerows(data)

    print(f'{fn}存檔完成')
fileName = input('請輸入檔案名稱:')
csvName=f'{fileName}.csv'
save_csvfile(fn=csvName,data=student)