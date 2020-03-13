menu = []
for i in range(5):
    menu.append(int(input()))

buger = menu[:3]
beverage = menu[3:]

print(min(buger)+min(beverage)-50)
