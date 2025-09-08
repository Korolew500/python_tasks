import requests
import json
import pprint

if __name__ == '__main__':
    data_x_wing = json.loads(requests.get('https://www.swapi.tech/api/starships/?name=X-wing').text)
    result_x_wing = dict()
    result_x_wing['max_atmosphering_speed'] = data_x_wing['result'][0]['properties']['max_atmosphering_speed']
    result_x_wing['sheep_name'] = data_x_wing['result'][0]['properties']['name']
    result_x_wing['starship_class'] = data_x_wing['result'][0]['properties']['starship_class']
    result_x_wing['pilots'] = data_x_wing['result'][0]['properties']['pilots']

    for number, i_url in enumerate(result_x_wing['pilots']):
        data_pilot = json.loads(requests.get(i_url).text)
        result_x_wing['pilots'][number] = dict()
        result_x_wing['pilots'][number]['height'] = data_pilot['result']['properties']['height']
        result_x_wing['pilots'][number]['homeworld_url'] = data_pilot['result']['properties']['homeworld']
        data_homeworld = json.loads(requests.get(result_x_wing['pilots'][number]['homeworld_url']).text)
        result_x_wing['pilots'][number]['homeworld'] = data_homeworld['result']['properties']['name']
        result_x_wing['pilots'][number]['mass'] = data_pilot['result']['properties']['mass']
        result_x_wing['pilots'][number]['name'] = data_pilot['result']['properties']['name']

    pprint.PrettyPrinter().pprint(result_x_wing)

    with open('x-wing.json', 'w') as file:
        json.dump(result_x_wing, file, indent=4)
