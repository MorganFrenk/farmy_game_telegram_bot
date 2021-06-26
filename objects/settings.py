
# ------ POWER SETTINGS -------
power_setting = {
    'base_power': 10,  # Base power
}


# ------ FARM TIME SETTINGS -------
time_setting = {
    'base_time': 20,  # Base time for the location
    'step_time': 12,  # Step for the time upgrade from the power growth
}
# Farm time in minutes for the power
farm_time_from_power = {
    power_setting['base_power']: time_setting['base_time'],
    power_setting['base_power'] * 2: time_setting['base_time'] * time_setting['step_time'],
    power_setting['base_power'] * 3: time_setting['base_time'] * time_setting['step_time'] * 2,
    power_setting['base_power'] * 4: time_setting['base_time'] * time_setting['step_time'] * 3,
    power_setting['base_power'] * 5: time_setting['base_time'] * time_setting['step_time'] * 4,
}


# ------ GOLD REWARD SETTINGS -------
reward_setting = {
    'base_reward': 50,  # Base gold reward for the location
    'step_reward': 5,  # Step for the reward upgrade from the power growth
}
# Gold reward for the power
reward_from_power = {
    power_setting['base_power']: reward_setting['base_reward'],
    power_setting['base_power'] * 2: reward_setting['base_reward'] * reward_setting['step_reward'],
    power_setting['base_power'] * 3: reward_setting['base_reward'] * reward_setting['step_reward'] * 2,
    power_setting['base_power'] * 4: reward_setting['base_reward'] * reward_setting['step_reward'] * 3,
    power_setting['base_power'] * 5: reward_setting['base_reward'] * reward_setting['step_reward'] * 4,
}


# ------ CRITICAL WOUND SETTINGS -------
crit_settings = {
    'base_crit_chance': 1,  # Base chance of critical wound
    'step_crit_chance': 10,  # Step for the chance of critical wound if
                             # the power of the location is bigger than the power of the hero
    'base_crit_time': 1440,  # Time of a wound status of the hero in minutes
}
