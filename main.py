from traverse import Traverse
from save import SaveData
from format import Parser


def main():
    results = Traverse('http://127.0.0.1:5000').register()
    save = SaveData()

    for element in results:
        data = element['data']
        if 'file_type' in element:
            fileType = element['file_type']

            if fileType == 'application/xml':
                save.adds(Parser.parseXML(data))
            elif fileType == 'text/csv':
                save.adds(Parser.parseCSV(data))
            elif fileType == 'application/x-yaml':
                save.adds(Parser.parseYAML(data))

        else:
            save.adds(Parser.parseJSON(data))

    print(save.selectColumns(['first_name', 'last_name', 'email']))


if __name__ == "__main__":
    main()
