#Task 1:


def log_activities(activities, durations):
    if len(activities) != len(durations):
        print("Error: Number of activities does not match number of durations.")
        return None
    log = {}
    for i in range(len(activities)):
        log[activities[i]] = durations[i]
    return log




#Task 2: 


def calculate_calories_burned(activity, duration):
    return duration * 3.5




#Task 3: 


def generate_summary(activity_log):
    total_calories = 0
    print("Fitness Activity Log:")
    for activity, duration in activity_log.items():
        calories_burned = calculate_calories_burned(activity, duration)
        total_calories += calories_burned
        print(f"{activity}: {duration} minutes, Calories Burned: {calories_burned}")
    print("Total Calories Burned for the day:", total_calories)

activities = ['Dancing', 'Swimming', 'Biking']
durations = [10, 20, 15]
activity_log = log_activities(activities, durations)
generate_summary(activity_log)
