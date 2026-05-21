distance_mi = 6
is_raining = True
has_bike = False
has_car = True
has_ride_share_app = False

if not distance_mi:
    print(False)
else:
    if distance_mi <= 1 and is_raining == False:
        print(True)
    elif distance_mi <= 1 and is_raining:
        print(False)
    elif 1 < distance_mi and distance_mi <= 6 and has_bike and is_raining:
        print(False)
    elif 1 < distance_mi and distance_mi <= 6 and has_bike == False and is_raining:
        print(False)
    elif 1 < distance_mi and distance_mi <= 6 and has_bike == False and is_raining == False:
        print(False)
    elif 1 < distance_mi and distance_mi <= 6 and has_bike and is_raining == False:
        print(True)
    elif distance_mi > 6 and has_car and has_ride_share_app:
        print(True)
    elif distance_mi > 6 and has_car == False and has_ride_share_app:
        print(True)
    elif distance_mi > 6 and has_car and has_ride_share_app == False:
        print(True)
    elif distance_mi > 6 and has_car == False and has_ride_share_app == False:
        print(False)
    else:
        print(False)