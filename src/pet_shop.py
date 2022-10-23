# WRITE YOUR FUNCTIONS HERE
from unicodedata import name


def get_pet_shop_name(pet_shop):
    return pet_shop["name"]


def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]


def add_or_remove_cash(pet_shop, amount):
    pet_shop["admin"]["total_cash"] += amount


def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]


def increase_pets_sold(pet_shop, num_pets):
    pet_shop["admin"]["pets_sold"] += num_pets


def get_stock_count(pet_shop):
    return len(pet_shop["pets"])


def get_pets_by_breed(pet_shop, breed):
    pets = []
    for pet_name in pet_shop["pets"]:
        if pet_name["breed"] == breed:
            pets.append(pet_name)
    return pets


def find_pet_by_name(pet_shop, name):
    for pet_name in pet_shop["pets"]:
        if pet_name["name"] == name:
            return pet_name


# def remove_pet_by_name(pet_shop, name):
#     for pet_name in pet_shop["pets"]:
#         if pet_name["name"] == name:
#             pet_shop["pets"].remove(pet_name)
            
def remove_pet_by_name(pet_shop, name):
    pet = find_pet_by_name(pet_shop, name)
    pet_shop["pets"].remove(pet)


def add_pet_to_stock(pet_shop, new_pet):
    pet_shop["pets"].append(new_pet)


def get_customer_cash(customers):
    return customers["cash"]


def remove_customer_cash(customer, amount):
    customer["cash"] -= amount


def get_customer_pet_count(customers):
    pet_count = []
    for customer in customers["pets"]:
        pet_count.append(customer)
    return len(pet_count)


def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet)