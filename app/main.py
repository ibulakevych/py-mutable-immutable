lucky_number = 777
pi = 3.14
one_is_a_prime_number = False
name = "Richard"
my_favourite_films = [
    "The Shawshank Redemption",
    "The Lord of the Rings: The Return of the King",
    "Pulp Fiction",
    "The Good, the Bad and the Ugly",
    "The Matrix",
]
profile_info = ("michel", "michel@gmail.com", "12345678")
marks = {
    "John": 4,
    "Sergio": 3,
}
collection_of_coins = {1, 2, 25}


def sort_variables(*args) -> dict:
    mutable_list = []
    immutable_list = []
    sorted_variables = {
        "mutable": mutable_list,
        "immutable": immutable_list
    }

    for variable in args:
        if type(variable) is list or set or dict:
            mutable_list.append(variable)
        else:
            immutable_list.append(variable)

    return sorted_variables


sort_variables(lucky_number, pi, one_is_a_prime_number, name, my_favourite_films, profile_info, marks,
               collection_of_coins)
