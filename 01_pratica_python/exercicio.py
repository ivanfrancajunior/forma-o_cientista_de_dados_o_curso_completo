#%%
#1
def amplitude(vetor: list) -> None:

    max_value = max(vetor)
    min_value = min(vetor)
    result = max_value - min_value
    print(result)


vet = [12, 13, 14, 15, 16, 17]
amplitude(vet)

#2
def print_vertical_string(value: str) -> None:
    for letter in value:
        print(letter)

print_vertical_string('python')

#3
def calc_total_price(weigth: float|int) -> str:

    total_price = 0

    if int(weigth) <= 10:
        total_price = 50
    elif int(weigth) > 10 and int(weigth) <=20 :
        total_price = 80
    else:
        return 'Transport not allowed'

    return f'Total price: {total_price}'


print(calc_total_price(12.5))
print(calc_total_price(7.5))
print(calc_total_price(35.5))

# %%
