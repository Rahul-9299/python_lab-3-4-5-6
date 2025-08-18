def student_profile(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Call with at least three named arguments
student_profile(name="Rahul", age=20, grade="A")
