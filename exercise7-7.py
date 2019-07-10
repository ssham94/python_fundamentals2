def distance_and_time(person):
    print("How far did person {} run? (in meters)".format(person))
    dist = float(input())
    print("How long did person {} take to run {} metres?".format(person, dist))
    mins = float(input())
    return dist, mins

def calc_speed(distance, total_min):
    seconds = int(total_min) * 60
    speed = int(distance)/seconds
    return speed

def find_fastest(speed_one, speed_two, speed_three):
    if speed_one == speed_two and speed_two == speed_three:
        return "Everyone tied at {:.2f} m/s".format(speed_one)
    speed_array = [speed_one, speed_two, speed_three]
    if len(speed_array) != len(set(speed_array)):
        return "Well done everyone!"
    fastest = max(speed_array)
    fastest_person = speed_array.index(fastest)
    return "Person {} was the fastest at {:.2f} m/s".format(fastest_person+1, fastest)


distance1, minutes1 = distance_and_time(1)
distance2, minutes2 = distance_and_time(2)
distance3, minutes3 = distance_and_time(3)

speed1 = calc_speed(distance1, minutes1)
speed2 = calc_speed(distance2, minutes2)
speed3 = calc_speed(distance3, minutes3)

print(find_fastest(speed1, speed2, speed3))