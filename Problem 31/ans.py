cnt=0
for i in range(2):
    for j in range(3):
        if i*200+j*100>200:
            break
        for k in range(5):
            if i*200+j*100+k*50>200:
                break
            for l in range(11):
                if i*200+j*100+k*50+l*20>200:
                    break
                for m in range(21):
                    if i*200+j*100+k*50+l*20+m*10>200:
                        break
                    for n in range(41):
                        if i*200+j*100+k*50+l*20+m*10+n*5>200:
                            break
                        for o in range(101):
                            if i*200+j*100+k*50+l*20+m*10+n*5+o*2>200:
                                break
                            for p in range(201):
                                if i*200+j*100+k*50+l*20+m*10+n*5+o*2+p*1>200:
                                    break
                                if i*200+j*100+k*50+l*20+m*10+n*5+o*2+p*1==200:
                                    cnt+=1
print("%d different ways to make $2"%cnt)