print("📚 My Study Tracker")
print("-------------------")

subject = input("What subject did you study? ")
hours = float(input("How many hours did you study? "))

print("\nToday you studied", subject, "for", hours, "hours.")

if hours >= 3:
    print("Amazing! You worked really hard today. 🌟")
elif hours >= 1.5:
    print("Good job! Keep it up. 👍")
else:
    print("A little more practice tomorrow! 💪")