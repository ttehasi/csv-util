import csv

from tabulate import tabulate


def make_table(data: list[list]):
    data = sorted(data, key=lambda x: x[1], reverse=True)
    for i in range(len(data)):
        data[i].insert(0, i + 1)
    
    headers = ['', 'brand', 'rating']
    return tabulate(data, headers=headers, floatfmt=".2f", tablefmt="grid")
    
# dt = [
#     ['samsung', '4.8888'],
#     ['xiaomi', '4.6'],
#     ['apple', '4.9'],
# ]

# print(make_table(dt))
    

def processing(brand_and_rating_list: list[list]):
    dict_res = {}
    res = []
    list_of_brand = [i[0] for i in brand_and_rating_list]
    brand_without_replic = []
    for i in range(len(list_of_brand)):
        if list_of_brand[i] not in brand_and_rating_list:
            brand_without_replic.append(list_of_brand[i])
    for i in range(len(brand_without_replic)):
        ratings = [float(x[1]) for x in brand_and_rating_list
            if x[0] == brand_without_replic[i]]
        dict_res[brand_without_replic[i]] = sum(ratings) / len(ratings)
    for brand, rating in dict_res.items():
        res.append([brand, rating])
    data = sorted(res, key=lambda x: x[1], reverse=True)
    return data


def unite(filenamelist: list):
    res_data = []
    for i in range(len(filenamelist)):
        with open(filenamelist[i], 'r') as file:
            spamreader = csv.reader(file)
            idx_brand = None
            idx_rating = None
            for row in spamreader:   # определение на каких местах находятся рейтинг и бренд, это дает гибкость # noqa
                for i in range(len(row)):
                    match row[i]:
                        case 'brand':
                            idx_brand = i
                        case 'rating':
                            idx_rating = i
                break
            for row in spamreader:
                if row[idx_brand] == 'brand':
                    continue
                brand = row[idx_brand]
                rating = row[idx_rating]
                res_data.append([brand, rating])
    return res_data
