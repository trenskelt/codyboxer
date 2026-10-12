earth_weight = float(input("What is your weight on Earth? "))

planets = {
    "Mercury": 0.90,
    "Venus": 0.91,
    "Mars": 0.38,
    "Jupiter": 2.34,
    "Saturn": 1.06,
    "Uranus": 0.92,
    "Neptune": 1.19,
    "Pluto": 0.063,
}

for planet, gravity in planets.items():
    planet_weight = earth_weight * gravity
    print(f"Your weight on {planet} is {planet_weight:.2f}.")
