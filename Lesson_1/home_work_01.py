# task 01 == Виправте синтаксичні помилки
print("Hello", end = " ")
print("world!")

# task 02 == Виправте синтаксичні помилки
hello = "Hello"
world = "world"
if 3 > 2:
   print(f"{hello} {world}!")

# task 03  == Вcтавте пропущену змінну у ф-цію print
for letter in "Hello world!":
    print(letter)

# task 04 == Зробіть так, щоб кількість бананів була
# завжди в чотири рази більша, ніж яблук
apples = 2
banana = apples * 4
print ("have apples", apples , "have bananas", banana)

# task 05 == виправте назви змінних
storona_1 = 1
storona_2 = 2
storona_3 = 3
storona_4 = 4

# task 06 == Порахуйте периметр фігури з task 05
# та виведіть його для користувача
perimetery = storona_1 + storona_2 + storona_3 + storona_4
print("parametrs = ", perimetery)


# """
#     # Задачі 07 -10:
#     # Переведіть задачі з книги "Математика, 2 клас"
#     # на мову пітон і виведіть відповідь, так, щоб було
#     # зрозуміло дитині, що навчається в другому класі

# """

# task 07
"""
У саду посадили 4 яблуні. Груш на 5 більше яблунь, а слив - на 2 менше.
Скільки всього дерев посадили в саду?
"""
apples_tree = 4
pear_tree = apples_tree + 5 
plum_tree = apples_tree - 2
sum_tree = apples_tree + pear_tree + plum_tree
print ("sum will be", "\n", apples_tree, "+" ,pear_tree, "= 13" ",\n", apples_tree, "-", plum_tree, "= 2" ",\n", end = " ")
print ("13 + 2 = 15")



# task 08
"""
До обіда температура повітря була на 5 градусів вище нуля.
Після обіду температура опустилася на 10 градусів.
Надвечір потепліло на 4 градуси. Яка температура надвечір?
"""
temperature = 0
afternoon_temperature = temperature + 5
after_fternoon_temperature = afternoon_temperature - 10
af = 10
evning_temperature = after_fternoon_temperature + 4
ev = 4
print ("temperature:", " \n", afternoon_temperature, "+", temperature ,"=",afternoon_temperature, "\n", end = " ")
print (afternoon_temperature,"-",af, "=" ,after_fternoon_temperature, " \n", after_fternoon_temperature, "+", ev, "=", evning_temperature)


# # task 09
# """
# Взагалі у театральному гуртку - 24 хлопчики, а дівчаток - вдвічі менше.
# 1 хлопчик захворів та 2 дівчинки не прийшли сьогодні.
# Скількі сьогодні дітей у театральному гуртку?
# """

te_g_boys = 24
te_g_girl = te_g_boys / 2
te_g = te_g_boys + te_g_girl
te_g_out  = te_g - 3
print("chindrens_are","=", "\n",te_g_out)

# # task 10
# """
# Перша книжка коштує 8 грн., друга - на 2 грн. дороже,
# а третя - як половина вартості першої та другої разом.
# Скільки будуть коштувати усі книги, якщо купити по одному примірнику?
# """

F_B = 8
S_B = F_B + 2
R_B1 = F_B // 2 
R_B2 = S_B // 2
T_B = R_B1 + R_B2
ALL_B = F_B + S_B + T_B
print("second book is", "\n", F_B, "+", "2", "=" ,S_B, "\n", end = "")
print("Thears book is", "\n", ALL_B, "hrn" )