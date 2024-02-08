def total_even_numbers(num):
    sum = 0
    for n in range(0,num+1,2):
        sum += n
    return sum

assert total_even_numbers(6) == 12, f"Reported {total_even_numbers(6)} for 'total_even_numbers(6)' instead of 12"
assert total_even_numbers(0) == 0, f"Reported {total_even_numbers(6)} for 'total_even_numbers(6)' instead of 0"
assert total_even_numbers(1) == 0, f"Reported {total_even_numbers(6)} for 'total_even_numbers(6)' instead of 0"
assert total_even_numbers(15) == 56, f"Reported {total_even_numbers(6)} for 'total_even_numbers(6)' instead of 56"

num = 9
print(total_even_numbers(num))