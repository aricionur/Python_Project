import json


class City:
    # this class requires 2 parameters, 'city' and 'code'
    def __init__(self, code, name):
        self.name = name
        self.code = code
        self.population = 1000000

    def __repr__(self):
        return self.name

    @staticmethod
    def find(area_code):
        for city in cities:
            if city.code == area_code:
                return city

    @staticmethod
    def find_multi(area_codes):
        matching_cities = []
        for code in area_codes:
            matching_city = City.find(code)
            if matching_city:
                matching_cities.append(matching_city)
        # matching_cities = [city for city in [City.find(code) for code in area_codes] if city]
        return matching_cities

with open('area_codes.json') as json_file:
    city_data = json.load(json_file)    #  data is a list now
    # print("area_codes_list : ", city_data)

cities = [City(value['code'], value['name']) for value in city_data]


