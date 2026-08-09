# Student Performance Prediction App

print("======================================")
print("     Student Performance Predictor")
print("======================================")

study_hours = float(input("Enter study hours per day: "))

if study_hours >= 8:
    score = 95
elif study_hours >= 6:
    score = 85
elif study_hours >= 4:
    score = 75
elif study_hours >= 2:
    score = 60
else:
    score = 45

print("\nPredicted Score:", score)

if score >= 90:
    print("Grade: A+")
elif score >= 80:
    print("Grade: A")
elif score >= 70:
    print("Grade: B")
elif score >= 60:
    print("Grade: C")
else:
    print("Grade: Needs Improvement")
