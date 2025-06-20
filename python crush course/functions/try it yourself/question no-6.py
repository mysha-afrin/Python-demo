def city_center (city, state):
    location = f"{city}, {state}"
    return location.title()
city = city_center('san francisco', 'california')
print(city)
