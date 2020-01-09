def reward_function(params):
    # Read input parameters
    all_wheels_on_track = params['all_wheels_on_track']
    distance_from_center = params['distance_from_center']
    track_width = params['track_width']
    steering = abs(params['steering_angle'])  # Only need the absolute steering angle

    # Calculate 4 markers that are at varying distances away from the center line
    marker_1 = 0.2 * track_width
    marker_2 = 0.3 * track_width
    marker_3 = 0.4 * track_width
    marker_4 = 0.45 * track_width
    marker_5 = 0.5 * track_width + 0.05

    # Give a high reward if no wheels go off the track and
    # the agent is somewhere in between the track borders
    if all_wheels_on_track:

        if distance_from_center <= marker_1:
            reward = 1
        elif distance_from_center <= marker_2:
            reward = 0.95
        elif distance_from_center <= marker_3:
            reward = 0.7
        elif distance_from_center <= marker_4:
            reward = 0.3
        elif distance_from_center <= marker_5:
            reward = 0.1
        else:
            reward = 1e-3  # likely crashed/ close to off track
    else:
        # Give a very low reward by default
        reward = 1e-3

    # Steering penality threshold, change the number based on your action space setting
    abs_steering_threshold = 20

    # Penalize reward if the agent is steering too much
    if steering > abs_steering_threshold:
        reward *= 0.8

    # Always return a float value
    return float(reward)
