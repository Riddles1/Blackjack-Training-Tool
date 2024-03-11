def test_function1():
    print("test")


from Classes import Card

card = Card("A_H")

print(card.numeric_value)
card.numeric_value = 1
print(card.numeric_value)


list = [1, 2, 3]
list.append(1)
print(list)