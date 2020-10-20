# Вычисляет расстояние между двумя городами и позволяет пользователю выбрать размерность расстояния.
# Эта программа может потребовать информацию о городах, такую как долготу и широту.

# Use latitude and longitude of two cities to calculate a distance between them

import numpy as np
from geopy.geocoders import Nominatim

locator = Nominatim(user_agent="cityDistance")


def get_distance(locA, locB):
    # use haversine formula
    earth_rad = 6371.0
    dlat = np.deg2rad(locB[0] - locA[0])
    dlon = np.deg2rad(locB[1] - locA[1])
    a = np.sin(dlat / 2) * np.sin(dlat / 2) + \
        np.cos(np.deg2rad(locA[0])) * np.cos(np.deg2rad(locB[0])) * \
        np.sin(dlon / 2) * np.sin(dlon / 2)
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))
    return earth_rad * c


def get_latlongs(location):
    loc = locator.geocode(location)
    return [loc.latitude, loc.longitude]


def convert_km_to_miles(km):
    miles_per_km = 0.621371192
    return km * miles_per_km


def main():
    """
    Main function
    - Get user's number
    - Calculate result
    - Print result
    """

    print("-- City distance --\n")

    shouldContinue = True

    while shouldContinue:

        cityA = input('Type the first City: ')
        print(get_latlongs(cityA))

        # get second city
        cityB = input('Type the second city: ')
        print(get_latlongs(cityB))

        # get units
        units = ''
        while (units != 'km') & (units != 'm'):
            units = str.lower(input('Type distance units (miles or kilometers): '))
            if units in ['clicks', 'km', 'kilometers', 'kilometer']:
                units = 'km'
            elif units in ['m', 'mile', 'miles']:
                units = 'm'
            else:
                print('units not recognised, please try again')

            # find the distance in km
        try:
            a = get_latlongs(cityA)
            b = get_latlongs(cityB)
            distance = get_distance(a, b)
            # display the distance
            if units == 'km':
                print(str(distance), ' km')
            else:
                distance = convert_km_to_miles(distance)
                print(str(distance), ' miles')
        except Exception:
            print('Error raised.  Are the input cities correct?')

        should = input("\nContinue (Y/[N]): ")
        if should.upper() != 'Y':
            shouldContinue = False
        else:
            shouldContinue = True


if __name__ == '__main__':
    main()
