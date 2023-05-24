def reward_function(params):
    '''
    Example of penalize steering, which helps mitigate zig-zag behaviors
    '''
    
    # Read input parameters
    speed = params['speed']
    steering = abs(params['steering_angle']) # Only need the absolute steering angle
    is_offtrack = params['is_offtrack']
    progress = params['progress']

    # encourage higher speeds # did it work?
    speedReward = speed * speed

    # Steering penality threshold, change the number based on your action space setting
    ABS_STEERING_THRESHOLD = 20

    # Penalize reward if the car is steering too much
    steeringPenalty = 1
    if steering > ABS_STEERING_THRESHOLD:
        steeringPenalty = 1e-1000
    
    # encourage more progress
    progressReward = progress * 100

    # off track penalty
    offtrackPenalty = 1
    if is_offtrack:
        offtrackPenalty = 1e-100000000000000000000000

    # calculate overall reward
    reward = speedReward * progressReward * steeringPenalty * offtrackPenalty

    return float(reward)
