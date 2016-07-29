from removeTags import removeTags
from addTags import addTags
import json
from chardet import chardetect, detect

path = "E:/GitHub/AzureMoonckeDocTagging/merge/"
getCode = True

file = open("fileEncoding.json")
encodingJson = file.read()
file.close()
encodings = json.loads(encodingJson)

def process(name, getCode):
    filename = path + name
    print("processing: "+filename)
    if getCode:
        file = open(filename, "rb")
        contentBytes = file.read()
        file.close()
        try:
            encoding = encodings[filename]
        except:
            d = detect(contentBytes)
            print(d)
            encodings[filename] = d["encoding"]
            encoding = d["encoding"]
    else:
        encoding = "utf8"

    file = open(filename, "r", encoding=encoding)
    try:
        content = file.read()
    except:
        d = detect(contentBytes)
        print(d)
        encodings[filename] = d["encoding"]
        encoding = d["encoding"]
        content = contentBytes.decode(encoding)
    file.close()
    result = removeTags(content)
    temp = addTags(result[0], result[1])
    file = open("./mooncake2/"+name, "w", encoding=encoding)
    file.write(result[0])
    file.close()
    file = open("./global2/"+name, "w", encoding=encoding)
    file.write(result[1])
    file.close()

file = open("filelist.txt")
filenames = file.readlines()
for filename in filenames:
    process(filename.strip(), getCode)

a = json.dumps(encodings)
file = open("fileEncoding.json", "w", encoding="utf8")
file.write(a)
file.close()