def calculate_course_duration(academical_hours):
    minutes_per_academic_hour = 45
    break_minutes_every_two_hours = 10

    teaching_minutes = academical_hours * minutes_per_academic_hour

    num_breaks = academical_hours // 2
    break_minutes = num_breaks * break_minutes_every_two_hours

    total_minutes = teaching_minutes + break_minutes

    total_hours = total_minutes / 60

    return total_hours

academical_hours = 64
total_duration = calculate_course_duration(academical_hours)
print(f"Total course duration: {total_duration:.2f} astronomical hours")
