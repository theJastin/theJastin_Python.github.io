veggies = ["carrot", "zuccini", "potato", "cucumber"]

def i_love(things):
    for thing in things:
        if len(thing) > 5:
            print(f"I love {thing}s!")


i_love(veggies)