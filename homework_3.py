"""
# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та екрануйте всі символи одинарної дужки у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк
"""


alice_in_wonderland = '"Would you tell me, please, which way I ought to go from here? "\n'\
'"That depends a good deal on where you want to get to, said the Cat."\n'\
'"I don\'t much care where "\n'\
'"—— said Alice .""Then it doesn\'t matter which way you go, said the Cat."\n'\
'"—— so long as I get somewhere, Alice added as an explanation."\n'\
"Oh, you're sure to do that, said the Cat, if you only walk long enough."
print(alice_in_wonderland)


"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
black_sea_area_km2 = 436_402
azov_sea_area_km2 = 37_800
total_sea_area_km2 = black_sea_area_km2 + azov_sea_area_km2

print("Total area of the Black Sea and Azov Sea:")
print(f"{black_sea_area_km2} + {azov_sea_area_km2} = {total_sea_area_km2} km2")




# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""

total_items = 375_291
items_1_and_2 = 250_449
items_2_and_3 = 222_950

items_3 = total_items - items_1_and_2
items_1 = total_items - items_2_and_3
items_2 = total_items - (items_1 + items_3)

print(f"1) Third warehouse: {total_items} - {items_1_and_2} = {items_3}")
print(f"2) First warehouse: {total_items} - {items_2_and_3} = {items_1}")
print(f"3) Second warehouse: {total_items} - ({items_1} + {items_3}) = {items_2}")
print()
print(f"First warehouse = {items_1}")
print(f"Second warehouse = {items_2}")
print(f"Third warehouse = {items_3}")



# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
months_to_pay = 18
monthly_payment_uah = 1179

total_price_uah = months_to_pay * monthly_payment_uah

print("Computer Purchase Summary:\n")
print(f"Monthly payment: {monthly_payment_uah} UAH")
print(f"Payment period:  {months_to_pay} months")
print(f"Total price:     {total_price_uah} UAH")


# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""

a = 8019 % 8    
b = 9907 % 9 
c = 2789 % 5     
d = 7248 % 6
e = 7128 % 5
f = 19224 % 9

print("Remainders:")
print(f"a) 8019 % 8  = {a}")
print(f"b) 9907 % 9  = {b}")
print(f"c) 2789 % 5  = {c}")
print(f"d) 7248 % 6  = {d}")
print(f"e) 7128 % 5  = {e}")
print(f"f) 19224 % 9 = {f}")



# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""

pizza_large_qty = 4
pizza_large_price = 274
cost_pizza_large = pizza_large_qty * pizza_large_price
pizza_medium_qty = 2
pizza_medium_price = 218
cost_pizza_medium = pizza_medium_qty * pizza_medium_price
juice_qty = 4
juice_price = 35
cost_juice = juice_qty * juice_price
cake_qty = 1
cake_price = 350
cost_cake = cake_qty * cake_price
water_qty = 3
water_price = 21
cost_water = water_qty * water_price
total_cost = cost_pizza_large + cost_pizza_medium + cost_juice + cost_cake + cost_water
print("Birthday Order Summary:\n")
print(f"1) {pizza_large_qty} × {pizza_large_price} = {cost_pizza_large} UAH (large pizza)")
print(f"2) {pizza_medium_qty} × {pizza_medium_price} = {cost_pizza_medium} UAH (medium pizza)")
print(f"3) {juice_qty} × {juice_price} = {cost_juice} UAH (juice)")
print(f"4) {cake_qty} × {cake_price} = {cost_cake} UAH (cake)")
print(f"5) {water_qty} × {water_price} = {cost_water} UAH (water)")
print(f"6) {cost_pizza_large} + {cost_pizza_medium} + {cost_cake} + {cost_juice} + {cost_water} UAH (All products)")
print(f"\nTotal cost: {total_cost} UAH \n")

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
photos_igors = 232
max_photos_per_page = 8
page_photo = 232 / 8
print(f"1){photos_igors} : {max_photos_on_page} = {page_photo} (pages we nead ) \n"
      f"we nead {page_photo} for all photo")

# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""


distance_kharkiv_budapest = 1600
fuel_per_100km = 9
tank_capacity = 48
vid = 100
total_fuel_needed = (distance_kharkiv_budapest / vid) * fuel_per_100km
refuel_count = total_fuel_needed // tank_capacity

print(f"Total fuel needed: {total_fuel_needed} liters")
print(f"Minimum number of full refuels: {refuel_count}")

