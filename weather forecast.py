#weather forecast

from pyowm import OWM
from pyowm.utils.config import get_default_config

place = input(" Введите город/страну: ")

config_dict = get_default_config()
config_dict['language'] = 'ru' 

owm = OWM( 'a00924790152d72d5575b27c2f767354', config_dict  )

mgr = owm.weather_manager()
observation = mgr.weather_at_place(place)
w = observation.weather


print(w)

temp = w.temperature()['temp']
temp=temp-273.15
print('{:.1f}'.format(temp))