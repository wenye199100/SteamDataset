import steam_reviews
import steam_products
import json
import pickle
import argparse
import os
# reviews = steam_reviews.get('5',True)
# print len(reviews)

# pro = steam_products.get(True)
#
# with open("./data/products.json",'r') as json_file:
# data = json.load(json_file)
#
# apps = data['applist']['apps']
#
# print len(apps)

# done_set = set()
#
# with open("./data/done",'r') as fin:
#     for line in fin:
#         done_set.add(line.strip())
#
# with open("./data/products.json",'r') as json_file:
#     data = json.load(json_file)
#
# apps = data['applist']['apps']
#
# start_num = 0
# end_num = 5
# count = 0
# for app in apps:
#     if count < start_num:
#         continue
#     if count > end_num:
#         break
#     appid = app['appid']
#     app_str = str(appid)
#     if app_str not in done_set:
#         reviews = steam_reviews.get(app_str, True)
#         if reviews:
#             with open('./review/{}'.format(int(appid)), 'wb') as fout:
#                 pickle.dump(reviews, fout)
#
#             with open("./data/useful", 'a+') as fout:
#                 fout.write(app_str + '\n')
#
#             with open("./data/done", 'a+') as fout:
#                 fout.write(app_str + '\n')
#
#
# print()


def get_review(app_str, done_set):
    if app_str not in done_set:
        reviews = steam_reviews.get(app_str, True)
        if reviews:
            with open('./review/{}'.format(int(appid)), 'wb') as fout:
                pickle.dump(reviews, fout)

            with open("./data/useful", 'a+') as fout:
                fout.write(app_str + '\n')

            with open("./data/done", 'a+') as fout:
                fout.write(app_str + '\n')

def get_reviews(start_num, end_num, done_set):
    apps = product_num()
    count = 0
    for app in apps:
        if count < start_num:
            continue
        if count > end_num:
            break
        appid = app['appid']
        app_str = str(appid)
        get_review(app_str, done_set)
        count += 1


def update_product():
    steam_products.get(True)
    with open("./data/products.json",'r') as json_file:
        data = json.load(json_file)
    apps = data['applist']['apps']

    count = 0
    with open("./data/product_list", 'wb') as fout:
        for app in apps:
            fout.write(str(count) + "," + str(app['appid']) + '\n')
            count += 1


def product_num(printable = False):
    with open("./data/products.json",'r') as json_file:
        data = json.load(json_file)
    apps = data['applist']['apps']
    if printable:
        print len(apps)
    return apps


if __name__ == '__main__':
    done_set = set()
    fp = open("./data/done", 'a+')
    fp.close()
    with open("./data/done", 'r') as fin:
        for line in fin:
            done_set.add(line.strip())
    parser = argparse.ArgumentParser()
    parser.add_argument("-r")
    parser.add_argument("-rs")
    parser.add_argument("-p", action='update product')
    parser.add_argument("-n", action='return product number')
    args = parser.parse_args()
    if args.r:
        get_review(args.r, done_set)
    if args.rs:
        tmp = args.l.split(",")
        start = int(tmp[0])
        end = int(tmp[1])
        get_reviews(int(start), int(end), done_set)
    if args.p:
        update_product()
    if args.n:
        product_num(True)

