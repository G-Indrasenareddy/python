import random
coin_result=["Head","Tail"]
head_count=0
Tail_count=0
for x in range(100):
    result=random.choice(coin_result)
    if(result=="Head"):
        head_count+=1
    elif(result=="Tail"):
        Tail_count+=1
    print(result)

print("Head count: ",head_count)
print("Tail count: ",Tail_count)
