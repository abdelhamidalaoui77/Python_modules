
def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    new_seed = seed_type.capitalize()

    if unit == "packets":
        print(new_seed, "seeds:", quantity, unit, "available")
    elif unit == "grams":
        print(new_seed, "seeds:", quantity, unit, "total")
    elif unit == "area":
        print(new_seed, "seeds: covers", quantity, "square meters")
    else:
        print("Unknown unit type")
