#!/usr/bin/env python
# Copyright 2020 Daisuke TONOSAKI

import sys
import os
import shutil
import argparse
import json
import csv


BUILD_DIR = 'build'
FIREBASE_JSON = 'firebase.json'
JSON_KEY_HOSTING = 'hosting'
JSON_KEY_REDIRECTS = 'redirects'
JSON_KEY_SOURCE = 'source'
JSON_KEY_DESTINATION = 'destination'
JSON_KEY_TYPE = 'type'


parser = argparse.ArgumentParser()
parser.add_argument('firebase_json_path', type=str)
parser.add_argument('redirects_csv_path', type=str)
parser.add_argument('--build_path', default=os.getcwd(), type=str)
args = parser.parse_args()


def main():
    json_data = None
    
    try:
        with open(args.firebase_json_path) as file:
            json_data = json.load(file)
            json_data[JSON_KEY_HOSTING][JSON_KEY_REDIRECTS] = []
    except Exception as e:
        print("Can't open file {0}".format(args.firebase_json_path))
        return


    try:
        with open(args.redirects_csv_path) as file:
            csv_reader = csv.reader(file)
            csv_header = next(csv_reader)

            for row in csv_reader:
                source = row[0]
                destination = row[1]
                type = row[2]

                json_data[JSON_KEY_HOSTING][JSON_KEY_REDIRECTS].append( {
                    JSON_KEY_SOURCE: source,
                    JSON_KEY_DESTINATION: destination, 
                    JSON_KEY_TYPE: int(type)
                })
    except Exception as e:
        print("Can't open file {0}".format(args.redirects_csv_path))
        return
    
    
    build_path = os.path.join(args.build_path, BUILD_DIR)

    if os.path.isdir(build_path):
        shutil.rmtree(build_path)

    os.makedirs(build_path)
    
    dest_firebase_json_path = os.path.join(build_path, FIREBASE_JSON)

    with open(dest_firebase_json_path, 'w') as dest_firebase_json:
        json.dump(json_data, dest_firebase_json, indent = 2)


if __name__ == '__main__':
    main()
