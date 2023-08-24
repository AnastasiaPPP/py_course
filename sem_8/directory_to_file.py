import os
import csv, json, pickle


def directory_to_pickle(path_dir):
    with open ('directory.pickle', 'wb') as file:
        pickle.dump(path_pars(path_dir), file)


def directory_to_json(path_dir):
    with open ('directory.json', 'w', encoding='utf-8') as file:
        json.dump(path_pars(path_dir), file)


def directory_to_csv(path_dir):
    directories = path_pars(path_dir)
    with open ('directory.csv', 'w', newline='', encoding='utf-8') as f:
        csv_write = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
        csv_write.writerow(['Directory Name', 'Parent Directory', 'Type', 'Size'])
        for key, value in directories.items():
            sb = ''
            for value2 in value.values():
                sb += str(value2) + ' '
            sb = sb.split()
            csv_write.writerow([key, sb[0], sb[1], sb[2]])


def path_pars(path):
    dictionary = {}
    for i in range(0, 3):
        for elem in os.walk(path):
            if type(elem[i]) == list:
                for j in range(len(elem[i])):
                    directory = elem[0] + '\\' + elem[i][j]
                    type_of_elem = 'directory' if i == 1 else 'file'
                    if i == 2:
                        size = os.path.getsize(directory)
                    else:
                        size = get_dir_size(directory)
                    dictionary[elem[i][j]] = {'parent_directory': elem[0][elem[0].rindex('\\') + 1:],
                                              'type': type_of_elem, 'size': size}
    return dictionary


def get_dir_size(path):
    total = 0
    with os.scandir(path) as it:
        for entry in it:
            if entry.is_file():
                total += entry.stat().st_size
            elif entry.is_dir():
                total += get_dir_size(entry.path)
    return total
