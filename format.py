from xmltodict import parse
from yaml import safe_load

from json import dumps, loads
from csv import DictReader
from ast import literal_eval


class Parser:

    @staticmethod
    def __clean_json(row):
        row = row.replace('null', 'None').replace('true', 'True').replace('false', 'False')
        return literal_eval(row)

    @staticmethod
    def parseXML(row):
        return loads(dumps(parse(row)['dataset']['record']))

    @staticmethod
    def parseJSON(row):
        return Parser.__clean_json(row)

    @staticmethod
    def parseYAML(row):
        return safe_load(row)

    @staticmethod
    def parseCSV(row):
        global rows
        data = []
        line_count = 0
        csvReader = DictReader(row.splitlines())
        for rows in csvReader:
            if line_count == 0:
                line_count += 1
        data.append(rows)
        line_count += 1

        return data
