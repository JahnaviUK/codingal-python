def hotel(nights):
    return 140 * nights
def plane(city):
    if "delhi" == city:
        return 183
    elif "chennai" == city:
        return 220
def car(days):
    if days>=7:
        return 40*days - 50
    else:
        return 40 * days
print("cost of hotel room",hotel(3))
print("cost of plane ride ",plane("chennai"))
print("cost of car ",car (4))