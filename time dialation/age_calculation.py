import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# =========================================================
# RELATIVITY TIME DILATION SIMULATOR
# =========================================================

print("\n" + "=" * 75)
print("          RELATIVITY TIME DILATION SIMULATOR")
print("=" * 75)

print("""
This simulator demonstrates Einstein's Special Relativity.

When a person travels close to the speed of light,
time moves slower for them compared to people on Earth.

This phenomenon is called TIME DILATION.
""")

# =========================================================
# USER INPUTS
# =========================================================

print("\nENTER DETAILS")
print("-" * 75)

traveler_name = input("Enter traveler name : ")

earth_name = input("Enter Earth observer name : ")

traveler_age = float(
    input(f"Enter {traveler_name}'s current age : ")
)

earth_age = float(
    input(f"Enter {earth_name}'s current age : ")
)

# =========================================================
# SPACE TRAVEL INPUTS
# =========================================================

print("\nSPACE TRAVEL DETAILS")
print("-" * 75)

space_days = float(
    input(f"How many days did {traveler_name} spend in space? : ")
)

velocity_percent = float(
    input("Enter spacecraft velocity (% of light speed) : ")
)

# Convert percentage into fraction
velocity_ratio = velocity_percent / 100

# =========================================================
# TIME CONVERSION
# =========================================================

space_years = space_days / 365

# =========================================================
# LORENTZ FACTOR
# =========================================================

gamma = 1 / np.sqrt(1 - velocity_ratio**2)

# =========================================================
# EARTH TIME CALCULATION
# =========================================================

earth_years = space_years * gamma

# =========================================================
# FINAL AGES
# =========================================================

traveler_final_age = traveler_age + space_years

earth_final_age = earth_age + earth_years

# =========================================================
# DATAFRAME
# =========================================================

data = {

    "Person": [
        traveler_name,
        earth_name
    ],

    "Initial Age": [
        traveler_age,
        earth_age
    ],

    "Time Experienced": [
        f"{space_days} days",
        f"{round(earth_years, 2)} years"
    ],

    "Final Age": [
        round(traveler_final_age, 2),
        round(earth_final_age, 2)
    ]
}

df = pd.DataFrame(data)

# =========================================================
# DISPLAY RESULTS
# =========================================================

print("\n" + "=" * 75)
print("SIMULATION RESULTS")
print("=" * 75)

print("\nTIME DILATION EXPLANATION")
print("-" * 75)

print(f"""
{traveler_name} traveled at extremely high speed.

Because of this, time moved slower inside
the spacecraft compared to Earth.

While {traveler_name} experienced only
{space_days} days,

Earth experienced approximately
{round(earth_years, 2)} years.

This effect is called TIME DILATION
in Einstein's Special Relativity.
""")

print("\nRELATIVITY CALCULATIONS")
print("-" * 75)

print(f"Lorentz Factor (γ) : {round(gamma, 2)}")

print(f"Velocity Fraction  : {round(velocity_ratio, 12)} c")

print(f"""
The spacecraft traveled at approximately
{round(velocity_percent, 10)}% of light speed.
""")

print("\nFINAL AGE COMPARISON")
print("-" * 75)

print(df)

print("\nAGE ANALYSIS")
print("-" * 75)

print(f"{traveler_name}'s final age : "
      f"{round(traveler_final_age, 2)} years")

print(f"{earth_name}'s final age : "
      f"{round(earth_final_age, 2)} years")

print("\nAGE DIFFERENCE")
print("-" * 75)

initial_difference = traveler_age - earth_age

final_difference = traveler_final_age - earth_final_age

print(f"Initial age difference : "
      f"{round(initial_difference, 2)} years")

print(f"Final age difference   : "
      f"{round(final_difference, 2)} years")

print("=" * 75)

# =========================================================
# VISUALIZATION
# =========================================================

people = [
    traveler_name,
    earth_name
]

final_ages = [
    traveler_final_age,
    earth_final_age
]

plt.figure(figsize=(8, 5))

bars = plt.bar(people, final_ages)

plt.title("RELATIVITY TIME DILATION")

plt.xlabel("Observer")

plt.ylabel("Final Age")

# Show values above bars
for bar in bars:

    y = bar.get_height()

    plt.text(
        bar.get_x() + bar.get_width() / 2,
        y + 1,
        round(y, 2),
        ha='center'
    )

plt.grid(True)

plt.tight_layout()

plt.show()