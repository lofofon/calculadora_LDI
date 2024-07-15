
class Character:
    def __init__(self, race_multiplier, qi_control) -> None:
        self.race_multiplier = race_multiplier
        self.qi_control = qi_control

        self.base_meditation_points_per_hour = (1+(0.15*qi_control))*(0.1*race_multiplier)
