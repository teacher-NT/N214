# list1 = [1,2,3,'olma', 'banan', 'gilos']
# print(list1)
# print(list1[2])
# list1[3] = 'Tarvuz'
# print(list1)  

# tuple1 = (1,2,3,42,3,56,78,5,34,2,5,2,3)
# print(tuple1.index(3))
# print(tuple1.count(2))


cars = ['GM', 'Lexus', 'BMW', 'Mersedes']
cars.append('BYD')
# print(cars)
cars.insert(2, "Porche")
# print(cars)
# books = ['Urush va tinchlik', 'Atom odatlar', 'Jimjitlik']
# cars.extend(books)
# cars.append(books)
# print(cars)

# cars.remove('GM')
# print(cars)

# a = cars.pop(4)
# print(cars)
# print(a)

# cars.clear()
# print(cars)

# sonlar = [4,6,1,10,18,3,5,2]
# sonlar.sort(reverse=True)
# print(sonlar)

sonlar = [1,2,3,4,5]
sonlar2 = sonlar.copy()
sonlar2[3] = 55
print(sonlar)
print(sonlar2)