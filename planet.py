# first_planet_input = input('Enter the distance from the sun for the first planet in km')
# second_planet_input = input('Enter the distance from the sun for the second planet in km')
# first_planet = int(first_planet_input)
# second_planet = int(second_planet_input)
# distance_km = second_planet - first_planet
# print(abs(distance_km))

# distance_mi = distance_km // 1.609344
# print(distance_mi)

# print(round(1.4))
# print(round(1.5))
# print(round(2.5))
# print(round(2.6))


# from math import ceil, floor

# round_up = ceil(12.5)
# print(round_up)

# round_down = floor(12.5)
# print(round_down)

########################## list##################
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
print("The first planet is", planets[0])
print("The second planet is", planets[1])
print("The third planet is", planets[2])

number_of_planets = len(planets)
print("There are", number_of_planets, "planets in the solar system.")
planets.append("Pluto")
number_of_planets = len(planets)
print("There are actually", number_of_planets, "planets in the solar system.")
planets.pop()  # Goodbye, Pluto
number_of_planets = len(planets)
print("No, there are definitely", number_of_planets, "planets in the solar system.")
#####Indexes start at zero and increase. Negative indexes start at the end of the list and work backward.

print("The last planet is", planets[-1])
print("The penultimate planet is", planets[-2])
jupiter_index = planets.index("Jupiter")
print("Jupiter is the", jupiter_index + 1, "planet from the sun")

planets_after_earth = planets[3:]
print(planets_after_earth)


amalthea_group = ["Metis", "Adrastea", "Amalthea", "Thebe"]
galilean_moons = ["Io", "Europa", "Ganymede", "Callisto"]

regular_satellite_moons = amalthea_group + galilean_moons
regular_satellite_moons.sort(reverse=True)
print("The regular satellite moons of Jupiter are", regular_satellite_moons)

user_planet = input("Please enter the name of the planet (with a capital letter to start)")
planet_index = planets.index(user_planet)
print("Here are the planets closer than " + user_planet)
print(planets[0:planet_index])
print("Here are the planets further than " + user_planet)
print(planets[planet_index + 1:])



from time import sleep

countdown = [4, 3, 2, 1, 0]

for number in countdown:
    print(number)
    sleep(2)  # Wait 1 second
print("Blast off!! 🚀")