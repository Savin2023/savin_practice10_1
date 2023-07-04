pets={}
pets_vn={}

print("Нуге-с, батенька, как зовут больного?")
name=input()
print("И кто у нас",name,"?")
vid=input()
print("Сколько годиков исполнилось?")
year=int(input())
print("Представьтесь, пожалуйста")
owner=input()

years=year-(year//10)*10
if year>=5 and year<=14:
    years_n="лет"
elif years==1:
    years_n="год"
elif years==2 or years==3 or years==4:
    years_n="года"
else:
    years_n="лет"

pets_vn={"vid_k":vid,"year_k":year,"owner_k":owner}
pets={"name":pets_vn}

print("Это",pets["name"]["vid_k"],"по кличке",name,". Возраст питомца",pets["name"]["year_k"],years_n,". Владелец:",pets["name"]["owner_k"])


# Не совсем понятно зачем в этом задании использовать методы keys() и values()
