import requests
import re


def headers_h3(text_html: str) -> list:
    result = list()
    h3_list = re.findall(r'<h3.*>.*</h3>', text_html)
    for i_h3 in h3_list:
        i_h3 = re.sub(r'<h3.*?>', '', i_h3)
        i_h3 = re.sub(r'</h3>', '', i_h3)
        result.append(i_h3)
    return result


if __name__ == '__main__':
    with open('examples.html', 'r') as f:
        print('Заголовки h3 в файле examples.html:', headers_h3(f.read()))

    # site_text = requests.get('https://www.columbia.edu/~fdc/sample.html').text
    # print(site_text)
    site_text = requests.get('http://csstemplatesmarket.com/freecsstemplates/alexx_c/').text
    print('Заголовки h3 на сайте csstemplatesmarket.com/freecsstemplates/alexx_c/:\n'
          + str(headers_h3(site_text)))
