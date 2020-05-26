import json
import os
import hashlib
blockchain_dir = os.curdir + '/blockchain/'


def get_hash(filename):
    file = open( blockchain_dir + filename, 'rb').read()        # open file (by path)
    return hashlib.md5(file).hexdigest()                        # hach of filename

def get_files():                                                # func of getting list of files
    files = os.listdir(blockchain_dir)                          # all files
    return sorted([int(x) for x in files])                      # sorted

def check_integrity():
    fileslist = get_files()                                     # getting list of files from func - get_files()
    results = []                                                # for saving results after checking
    for file in fileslist[1:]:
        h = json.load(open(blockchain_dir + str(file)))['hash'] # reading hash from current file
        prev_file = str(file - 1)
        actual_hash = get_hash(prev_file)                       # calculating hash prev block

        if h == actual_hash:                                    #  comparison hashs between culculating hashs prev block and hash (pulled out) from current block
            res = 'Ok'
        else:
            res = 'Error!'
        results.append({'block': prev_file, 'result': res})
    return results

def write_block(name, amount, to_whom, prev_hash=''):
    fileslist = get_files()                                     # getting list of files from func - get_files()
    prev_file = fileslist[-1]                                   # find last file
    filename = str(prev_file + 1)                               # creating name of new file by plusing 1
    prev_hash = get_hash(str(prev_file))                        # culculating hash of previous file

    data = {'name':name,                                        # format of data
            'amount': amount,
            'to_whom': to_whom,
            'hash': prev_hash}

    with open(blockchain_dir + filename, 'w') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)     #saving data into json file, data - saving data \
                                                                # file - place for data, indent=4, ensure_ascii=False - Cyrillic

def main():
    write_block(name = 'ivav', amount=12, to_whom= 'igor' )     # run scripts
    print(check_integrity())

if __name__=='__main__':
    main()