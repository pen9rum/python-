import random
life=10
count=0
player=int(input('輸入遊玩人數，1代表單人模式，2代表雙人模式!'))  
print('最多只能玩1000次')
for i in range(1000):
  
  while player==1:
    a = random.randint(1,99)
    b = int(input('輸入 1～99 的數字：'))  
    while a!=b and life>0: 
        if a>b:    
          b = int(input('數字太小囉！再試一次吧：'))           
        elif b > a:
           b = int(input('數字太大囉！再試一次吧：'))   
        life-=1
 
    if life>0:
      print('答對囉！ 你還有',life,'條命')
      life=10
      player=int(input('輸入遊玩人數，1代表單人模式，2代表雙人模式'))
      break
    elif life==0:
      print('你太爛囉！死掉了!')
      life=10
      player=int(input('輸入遊玩人數，1代表單人模式，2代表雙人模式'))
      break
  
  while player==2:
        a = random.randint(1,99)
        b = int(input('輸入 1～99 的數字：'))
        while a!=b:
          if a>b:    
            b = int(input('數字太小囉！再試一次吧：'))           
          elif b > a:
           b = int(input('數字太大囉！再試一次吧：')) 
          count+=1

          if count%2==0 and a==b:
            print('玩家二勝利')
            player=int(input('輸入遊玩人數，1代表單人模式，2代表雙人模式'))
            break
          elif count%2==1 and a==b:
            print('玩家一勝利')
            player=int(input('輸入遊玩人數，1代表單人模式，2代表雙人模式'))
            break
  
  while player==3 or player>3:
    a = random.randint(1,99)
    print('不要鬧了 只能輸入1跟2')
    player=int(input('輸入遊玩人數，1代表單人模式，2代表雙人模式')) 
#我想聽 體面 
 
