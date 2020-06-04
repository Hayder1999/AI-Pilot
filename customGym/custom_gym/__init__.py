from gym.envs.registration import register

register(
    id='Xplane-v0',
    entry_point='custom_gym.envs:XPL'
        )