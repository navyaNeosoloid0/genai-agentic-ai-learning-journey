# Day 1 - Python Basics Practice

# Variables
name = "Navya"
learning_path = "Generative AI and Agentic AI"

# Numbers
age = 21
hours_studied = 2.5

# Boolean
is_learning_ai = True

# Print variables
print("Name:", name)
print("Learning Path:", learning_path)
print("Age:", age)
print("Hours Studied:", hours_studied)
print("Learning AI:", is_learning_ai)


# List
skills = [
    "Python",
    "Java",
    "SQL",
    "ServiceNow"
]

print("\nCurrent Skills:")

for skill in skills:
    print("-", skill)


# Dictionary
profile = {
    "name": "Navya",
    "degree": "B.Tech CSE (IoT)",
    "goal": "Generative AI Engineer"
}

print("\nProfile Information:")

for key, value in profile.items():
    print(key, ":", value)


# String formatting
print(f"\nHello, I am {name}.")
print(f"I am currently learning {learning_path}.")
