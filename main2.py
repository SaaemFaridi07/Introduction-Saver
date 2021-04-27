name = input("Name Here: ")
nickname = input("NickName: ")
date = input("Date (eg. - 1/1/2017): ")
city = input("City: ")
country = input("Country: ")
hobbies = input("Hobbies(include a comma between for adding 1 or more hobbies.): ")



intro = (f"Hii ,My name Is {name} AKA {nickname}.\n I Was Born On {date}.\n I Live in {city},{country}.\n My Hobbies Are : {hobbies}.\n Thank You!!")
print(intro)

with open("output.txt",'w',encoding = 'utf-8') as f:
   f.write(str(intro))