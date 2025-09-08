def main():
    products = []
    for i in range(int(input('Сколько сайтов: '))):
        product = input('Введите название продукта для нового сайта: ')
        products.append(product)
        sites(products.copy())


def sites(prod_list):
    for prod in prod_list:
        print(f'Сайт для {prod}:')
        print("site = {{\n"
              "\t\t'html': {{\n"
              "\t\t\t\t'head': {{\n"
              "\t\t\t\t\t\t'title': 'Куплю/продам {product} недорого'\n"
              "\t\t\t\t}},\n"
              "\t\t\t\t'body': {{\n"
              "\t\t\t\t\t\t'h2': 'У нас самая низкая цена на {product}',\n"
              "\t\t\t\t\t\t'div': 'Купить',\n"
              "\t\t\t\t\t\t'p': 'Продать'\n"
              "\t\t\t\t}}\n"
              "\t\t}}\n"
              "}}".format(product=prod))
        print()


main()
