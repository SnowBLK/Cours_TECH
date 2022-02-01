from i_temperature_observer import ITemperatureObserver
from event import Event

class WeatherStation(ITemperatureObserver):
    station_counter = 0 
    
    def __init__(self):
        WeatherStation.station_counter += 1
        self.__number = WeatherStation.station_counter

    def displayTemperatures(self, sensorName, temperature):
        print("Station : ", self.__number, " + ",
        sensorName, " : ", temperature)
    
    @property
    def number(self):
        return self.__number
    
    def updateObs(self, event : Event ):
        self.displayTemperatures(event.name, event.temperature)

# if __name__ == "__main__":
#     w = WeatherStation()
#     w.displayTemperatures("Sensor 1", 21)
#     print(w.number)
    