##猜數字遊戲##
import random as rm
min=1
max=100
guess=rm.randint(min,max)
count = 0

print("==============猜數字遊戲==============\n\n")
#print(f'要猜的數字是{guess}')
while(True):
    try:
        keyin=int(input(f'猜數字遊戲{min}-{max}'))
        count+=1

        if(max>=keyin>=min):
            if keyin==guess:
                print(f'賓果!猜對了,答案是:{guess}')
                print(f'您已經猜了{count}次')
                break
            elif keyin>guess:
                print('在小一點')
                max=keyin-1
            else:
                print('在大一點')
                min=keyin+1
                
        else:
            print('超出範圍')
            count+=1
  
    except:
        print('輸入格式錯誤')
        count+=1
    
    print(f'您已經猜了{count}次')
print('遊戲結束')