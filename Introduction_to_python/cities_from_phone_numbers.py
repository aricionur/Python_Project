def find_cities(telephone_numbers):

    domain_code_list = set()
    for value in telephone_numbers:
        domain_code_list.add(value[0:3])

    return City.find_multi(domain_code_list)


print(find_cities([
    "2124442221",
    "2134442221",
    "2164442221",
    "2184442221",
    "2124442221"
]))
