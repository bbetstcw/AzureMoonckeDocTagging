from difflib import Differ, ndiff
import re
from removeTags import acn_tag_begin, acn_tag_end, acom_tag_begin, acom_tag_end
from removeTags import acn_tag_begin_no_escape, acn_tag_end_no_escape, acom_tag_begin_no_escape, acom_tag_end_no_escape
from math import floor


def addTags(mooncake, global_):
    mooncakeLines = mooncake.split("\n")
    globalLines = global_.split("\n")

    mooncakeLines_stripped = [line.strip() for line in mooncakeLines]
    globalLines_stripped = [line.strip() for line in globalLines]

    differ = Differ()

    diff = list(differ.compare(globalLines_stripped, mooncakeLines_stripped))

    mooncakeIndex = 0
    globalIndex = 0
    result = ""

    for line in diff:
        if line[0] == ' ':
            result+=mooncakeLines[mooncakeIndex]+"\n"
            mooncakeIndex+=1;
            globalIndex+=1;
        elif line[0] == '-':
            empty_spaces = ""
            empty_end = globalLines[globalIndex].find(line[2:])
            if "\t" in globalLines[globalIndex][:empty_end] or "    " in globalLines[globalIndex][:empty_end]:
                empty_spaces = globalLines[globalIndex][:empty_end]
            if len(re.findall("\|", line)) >= 1:
                result+=empty_spaces+"|"+acom_tag_begin_no_escape+"|\n"+globalLines[globalIndex]+"\n"+empty_spaces+"|"+acom_tag_end_no_escape+"|\n"
            elif re.match("\- \*\s.+", line):
                result+=empty_spaces+"* "+acom_tag_begin_no_escape+"\n"+globalLines[globalIndex]+"\n"+empty_spaces+"* "+acom_tag_end_no_escape+"\n"
            elif re.match("\- \-\s.+", line):
                result+=empty_spaces+"- "+acom_tag_begin_no_escape+"\n"+globalLines[globalIndex]+"\n"+empty_spaces+"- "+acom_tag_end_no_escape+"\n"
            elif re.match("\- \[0-9]+\.\s.+", line):
                result+=empty_spaces+"1. "+acom_tag_begin_no_escape+"\n"+globalLines[globalIndex]+"\n"+empty_spaces+"1. "+acom_tag_end_no_escape+"\n"
            else:
                result+=empty_spaces+acom_tag_begin_no_escape+"\n"+globalLines[globalIndex]+"\n"+empty_spaces+acom_tag_end_no_escape+"\n"
            globalIndex+=1;
        elif line[0] == '+':
            empty_spaces = ""
            empty_end = mooncakeLines[mooncakeIndex].find(line[2:])
            if "\t" in mooncakeLines[mooncakeIndex][:empty_end] or "    " in mooncakeLines[mooncakeIndex][:empty_end]:
                empty_spaces = mooncakeLines[mooncakeIndex][:empty_end]
            if len(re.findall("\|", line)) >= 1:
                result+=empty_spaces+"|"+acn_tag_begin_no_escape+"|\n"+mooncakeLines[mooncakeIndex]+"\n"+empty_spaces+"|"+acn_tag_end_no_escape+"|\n"
            elif re.match("\+ \*\s.+", line):
                result+=empty_spaces+"* "+acn_tag_begin_no_escape+"\n"+mooncakeLines[mooncakeIndex]+"\n"+empty_spaces+"* "+acn_tag_end_no_escape+"\n"
            elif re.match("\+ \-\s.+", line):
                result+=empty_spaces+"- "+acn_tag_begin_no_escape+"\n"+mooncakeLines[mooncakeIndex]+"\n"+empty_spaces+"- "+acn_tag_end_no_escape+"\n"
            elif re.match("\+ \[0-9]+\.\s.+", line):
                result+=empty_spaces+"1. "+acn_tag_begin_no_escape+"\n"+mooncakeLines[mooncakeIndex]+"\n"+empty_spaces+"1. "+acn_tag_end_no_escape+"\n"
            else:
                result+=empty_spaces+acn_tag_begin_no_escape+"\n"+mooncakeLines[mooncakeIndex]+"\n"+empty_spaces+acn_tag_end_no_escape+"\n"
            mooncakeIndex+=1
    content = "".join(result)
    content = re.sub("\n(1\. |\- |\* )?"+acom_tag_end+"\n(1\. |\- |\* )?"+acom_tag_begin+"\n", "\n", content)
    content = re.sub("\n(1\. |\- |\* )?"+acn_tag_end+"\n(1\. |\- |\* )?"+acn_tag_begin+"\n", "\n", content)
    content = re.sub("([\t ]+)"+acom_tag_end+"\n([\t ]+)"+acom_tag_begin+"\n", "", content)
    content = re.sub("([\t ]+)"+acn_tag_end+"\n([\t ]+)"+acn_tag_begin+"\n", "", content)
    content = re.sub("([^\n])\n("+acom_tag_end+"|"+acom_tag_begin+")",r"\1\n\n\2", content)
    content = re.sub("("+acom_tag_end+"|"+acom_tag_begin+")\n([^\n])",r"\1\n\n\2", content)
    content = re.sub("([^\n])\n("+acn_tag_end+"|"+acn_tag_begin+")",r"\1\n\n\2", content)
    content = re.sub("("+acn_tag_end+"|"+acn_tag_begin+")\n([^\n])",r"\1\n\n\2", content)
    content = re.sub(acn_tag_begin+"[\s\n]+"+acn_tag_end+"\n","", content)
    content = re.sub(acom_tag_begin+"[\s\n]+"+acom_tag_end+"\n","", content)
    content = re.sub("\n(1\. |\- |\* )?"+acom_tag_end+"\n+(1\. |\- |\* )?"+acom_tag_begin+"\n", "\n", content)
    content = re.sub("\n(1\. |\- |\* )?"+acn_tag_end+"\n+(1\. |\- |\* )?"+acn_tag_begin+"\n", "\n", content)
    content = re.sub("([\t ]+)"+acom_tag_end+"\n+([\t ]+)"+acom_tag_begin+"\n", "", content)
    content = re.sub("([\t ]+)"+acn_tag_end+"\n+([\t ]+)"+acn_tag_begin+"\n", "", content)
    content = tagsRefine(content, acom_tag_begin, acom_tag_end, acom_tag_end_no_escape)
    content = tagsRefine(content, acn_tag_begin, acn_tag_end, acn_tag_end_no_escape)
    content = re.sub("([^\n])\n([ \t]*)("+acom_tag_begin+"|"+acn_tag_begin+"|"+acom_tag_end+"|"+acn_tag_end+")", r"\1\n\n\2\3", mergeTags(content))
    content = re.sub("\n([ \t]*)("+acom_tag_begin+"|"+acn_tag_begin+"|"+acom_tag_end+"|"+acn_tag_end+")\n([^\n])", r"\n\1\2\n\n\3", content)
    content = re.sub("\n\n\n+", "\n\n", content)
    return content

def tagsRefine(content, begin, end, end_no_escape):
    begin_index = [m.start() for m in re.finditer(begin, content)]
    end_index = [m.end() for m in re.finditer(end, content)]
    if len(begin_index) != len(end_index):
        raise Exception("Begin tag and end tag numbers not match: '"+ re.escape(begin)+"', '"+re.escape(end)+"'.")

    next=0
    result = ""
    for i in range(len(begin_index)):
        if begin_index[i]>=end_index[i]:
            raise Exception("Tags nested: '"+ re.escape(begin)+"', '"+re.escape(end)+"'.")
        begin_new_line_index = content[:begin_index[i]].rfind("\n")
        begin_empty = content[begin_new_line_index:begin_index[i]]

        end_new_line_index = content[:end_index[i]].rfind("\n")
        result+=content[next:end_new_line_index]+begin_empty+end_no_escape
        next = end_index[i]
    result += content[next:]
    return result

def mergeTags(content):
    lines = content.split("\n")
    result = []
    i = 0
    while i < len(lines):
        if lines[i].strip() in [acom_tag_begin_no_escape, acn_tag_begin_no_escape]:
            j = getBlock(lines, i)
            mergelines = merge(lines, i, j)
            result += mergelines
            i = j+1
        else:
            result.append(lines[i])
            i+=1

    return "\n".join(result)

def merge(lines, i, j):
    if i == j:
        return lines[i:j+1]
    parts = level_split(lines, i, j)
    print(parts)
    result = []
    for part in parts:
        mooncake_result = []
        global_result = []
        index = lines[part[0]].find(lines[part[0]].strip())
        empty_string = lines[part[0]][:index]
        in_mooncake = False
        in_global = False
        k = part[0]
        while  k < part[1]:
            stripped = lines[k].strip()
            if stripped == acom_tag_begin_no_escape:
                in_mooncake = False
                in_global = True
                k+=1
                continue
            elif stripped == acn_tag_begin_no_escape:
                in_mooncake = True
                in_global = False
                k+=1
                continue
            elif stripped == acom_tag_end_no_escape:
                in_global = False
                k+=1
                continue
            elif stripped == acn_tag_end_no_escape:
                in_mooncake = False
                k+=1
                continue
            if in_global == True:
                global_result.append(lines[k])
            elif in_mooncake == True:
                mooncake_result.append(lines[k])
            k+=1
        if len(global_result)==0:
            result+=[empty_string+acn_tag_begin_no_escape]+mooncake_result+[empty_string+acn_tag_end_no_escape, ""]
        elif len(mooncake_result)==0:
            result+=[empty_string+acom_tag_begin_no_escape]+global_result+[empty_string+acom_tag_end_no_escape, ""]
        else:
            result+=[empty_string+acom_tag_begin_no_escape]+global_result+[empty_string+acom_tag_end_no_escape, "",empty_string+acn_tag_begin_no_escape]+mooncake_result+[empty_string+acn_tag_end_no_escape, ""]
    return result[:len(result)-1]

def level_split(lines, i, j):
    parts = []
    k = i+1
    m = i
    begin_level = get_level(lines[i])
    while k<j:
        if lines[k].strip() in [acom_tag_begin_no_escape, acn_tag_begin_no_escape]:
            level = get_level(lines[k])
            if level<begin_level:
                parts.append([m,k-1])
                m = k
                begin_level = level
        k+=1
    parts.append([m,j])
    return parts

def get_level(line):
    index = line.find(line.strip())
    empty_string = line[:index].replace("\t", "    ")
    return floor(len(empty_string)/4)

def getBlock(lines, i):
    mooncake_block_count = 0
    global_block_count = 0
    in_mooncake = False
    in_global = False
    j = i
    while j < len(lines):
        temp = lines[j].strip()
        if temp == acom_tag_begin_no_escape:
            global_block_count += 1
            in_global = True
            in_mooncake = False
        elif temp == acn_tag_begin_no_escape:
            mooncake_block_count += 1
            in_global = False
            in_mooncake = True
        elif temp == acom_tag_end_no_escape:
            in_global = False
        elif temp == acn_tag_end_no_escape:
            in_mooncake = False
        elif in_global == False and in_mooncake == False and temp != "":
            break;

        j += 1
    if j >= len(lines):
        return i
    while j> i:
        if lines[j].strip() in [acom_tag_end_no_escape, acn_tag_end_no_escape]:
            break;
        j-=1

    if mooncake_block_count > 1 or global_block_count > 1:
        return j
    return i
