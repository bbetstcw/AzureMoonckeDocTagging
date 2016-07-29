import re

acn_tag_begin = "\[AZURE\.ACN\]\{"

acn_tag_end = "\[AZURE\.ACN\]\}"

acom_tag_begin = "\[AZURE\.ACOM\]\{"

acom_tag_end = "\[AZURE\.ACOM\]\}"

acn_tag_begin_no_escape = "[AZURE.ACN]{"

acn_tag_end_no_escape = "[AZURE.ACN]}"

acom_tag_begin_no_escape = "[AZURE.ACOM]{"

acom_tag_end_no_escape = "[AZURE.ACOM]}"

def removeTags(article):
    mooncake = _removeTag(article, "\r?\n\s*"+acom_tag_begin+"\s*\r?\n", "\r?\n\s*"+acom_tag_end)
    mooncake = _removeTag(mooncake, "\r?\n\s*\|\s*"+acom_tag_begin+"\s*\|\s*\r?\n", "\r?\n\s*\|\s*"+acom_tag_end+"\s*\|")
    mooncake = _removeTag(mooncake, "\r?\n\s*1\.\s*"+acom_tag_begin+"\s*\r?\n", "\r?\n\s*1\.\s*"+acom_tag_end)
    mooncake = _removeTag(mooncake, "\r?\n\s*\-\s*"+acom_tag_begin+"\s*\r?\n", "\r?\n\s*\-\s*"+acom_tag_end)
    mooncake = _removeTag(mooncake, "\r?\n\s*\*\s*"+acom_tag_begin+"\s*\r?\n", "\r?\n\s*\*\s*"+acom_tag_end)
    mooncake = re.sub("\r?\n\s*"+acn_tag_begin,"", mooncake)
    mooncake = re.sub("\r?\n\s*\|\s*"+acn_tag_begin+"\s*\|","", mooncake)
    mooncake = re.sub("\r?\n\s*1\.\s*"+acn_tag_begin+"\s*\r?\n","\n", mooncake)
    mooncake = re.sub("\r?\n\s*\-\s*"+acn_tag_begin+"\s*\r?\n","\n", mooncake)
    mooncake = re.sub("\r?\n\s*\*\s*"+acn_tag_begin+"\s*\r?\n","\n", mooncake)
    mooncake = re.sub("\r?\n\s*"+acn_tag_end,"", mooncake)
    mooncake = re.sub("\r?\n\s*\|\s*"+acn_tag_end+"\s*\|","", mooncake)
    mooncake = re.sub("\r?\n\s*1\.\s*"+acn_tag_end+"\s*\r?\n","\n", mooncake)
    mooncake = re.sub("\r?\n\s*\-\s*"+acn_tag_end+"\s*\r?\n","\n", mooncake)
    mooncake = re.sub("\r?\n\s*\*\s*"+acn_tag_end+"\s*\r?\n","\n", mooncake)

    global_ = _removeTag(article, "\r?\n\s*"+acn_tag_begin+"\s*\r?\n", "\r?\n\s*"+acn_tag_end)
    global_ = _removeTag(global_, "\r?\n\s*\|\s*"+acn_tag_begin+"\s*\|\s*\r?\n", "\r?\n\s*\|\s*"+acn_tag_end+"\s*\|")
    global_ = _removeTag(global_, "\r?\n\s*1\.\s*"+acn_tag_begin+"\s*\r?\n", "\r?\n\s*1\.\s*"+acn_tag_end)
    global_ = _removeTag(global_, "\r?\n\s*\-\s*"+acn_tag_begin+"\s*\r?\n", "\r?\n\s*\-\s*"+acn_tag_end)
    global_ = _removeTag(global_, "\r?\n\s*\*\s*"+acn_tag_begin+"\s*\r?\n", "\r?\n\s*\*\s*"+acn_tag_end)
    global_ = re.sub("\r?\n\s*"+acom_tag_begin,"", global_)
    global_ = re.sub("\r?\n\s*\|\s*"+acom_tag_begin+"\s*\|","", global_)
    global_ = re.sub("\r?\n\s*1\.\s*"+acom_tag_begin+"\s*\r?\n","\n", global_)
    global_ = re.sub("\r?\n\s*\-\s*"+acom_tag_begin+"\s*\r?\n","\n", global_)
    global_ = re.sub("\r?\n\s*\*\s*"+acom_tag_begin+"\s*\r?\n","\n", global_)
    global_= re.sub("\r?\n\s*"+acom_tag_end,"", global_)
    global_ = re.sub("\r?\n\s*\|\s*"+acom_tag_end+"\s*\|","", global_)
    global_ = re.sub("\r?\n\s*1\.\s*"+acom_tag_end+"\s*\r?\n","\n", global_)
    global_ = re.sub("\r?\n\s*\-\s*"+acom_tag_end+"\s*\r?\n","\n", global_)
    global_ = re.sub("\r?\n\s*\*\s*"+acom_tag_end+"\s*\r?\n","\n", global_)
    return mooncake, global_

def _removeTag(article, begin, end):
    begin_index = [m.start() for m in re.finditer(begin, article)]
    end_index = [m.end() for m in re.finditer(end, article)]

    if len(begin_index) != len(end_index):
        raise Exception("Begin tag and end tag numbers not match: '"+ re.escape(begin)+"', '"+re.escape(end)+"'.")

    next=0
    result = ""
    for i in range(len(begin_index)):
        if begin_index[i]>=end_index[i]:
            raise Exception("Tags nested: '"+ re.escape(begin)+"', '"+re.escape(end)+"'.")
        result+= article[next:begin_index[i]]
        next = end_index[i]

    result += article[next:]

    return result