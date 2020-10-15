from traverse import Traverse
from save import SaveData
from format import Parser


def main():
    results = Traverse('http://127.0.0.1:5000').register()
    save = SaveData()


    for element in results:
        data = element['data']
        if 'mime_type' in element:
            fileType = element['mime_type']

            if fileType == '/xml':
                save.adds(Parser.parseXML(data))
            elif fileType == '/csv':
                save.adds(Parser.parseCSV(data))
            elif fileType == '/x-yaml':
                save.adds(Parser.parseYAML(data))

        else:
            save.adds(Parser.parseJSON(data))

    print(save.selectColumns(['first_name', 'last_name', 'email']))


if __name__ == "__main__":
    main()
