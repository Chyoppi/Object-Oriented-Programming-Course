class WeatherStation:
    def __init__(self, name):
        self.name = name
        self.weather = []

    def add_observation(self, observation: str):
        self.weather.append(observation)

    def latest_observation(self):
        return self.weather[-1]
    
    def number_of_observations(self):
        return len(self.weather)
    
    def __str__(self):
        return f"{self.name}, {len(self.weather)} observations"
    
station = WeatherStation("Texas")
station.add_observation("Sunny")
station.add_observation("Rainy")

print(station.latest_observation())

print(station.number_of_observations())
print(station)  
    
