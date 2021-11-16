from collections import defaultdict
import re
import json
import pymorphy2


f = open('text.txt', encoding="utf8")
STOP_WORDS = f.readlines()
STOP_WORDS = [re.sub("\n", "", w) for w in STOP_WORDS]

morph = pymorphy2.MorphAnalyzer()

def extract_text(e):
    if isinstance(e, str):
        return e
    return "".join([x if isinstance(x, str) else x["text"] for x in e])


def process_export(fname):
    data = json.load(open(fname, encoding="utf8"))
    messages = " ".join([extract_text(e["text"]) for e in data["messages"]])
    messages = messages.replace("\n", " ")
    words = messages.lower().split(" ")
    words = [re.sub("[\\W_]", "", w) for w in words]
    #words = [morph.parse(w)[0].normal_form for w in words]
    words = [w for w in words if len(w) > 2]
    words = [w for w in words if not w in STOP_WORDS]
    return words


md = defaultdict(int)

for fname in ["result1.json"]:
    for w in process_export(fname):
        md[w] += 1



for w in sorted(md, key=md.get, reverse=False):
    # if w == 10:
    print("{} -> {}".format(w, md[w]))

# # data = json.load(open("result.json", encoding="utf8"))
# data = json.load(open("result1.json", encoding="utf8"))
# f = open('text.txt', encoding="utf8")
# file_contents = f.readlines()
# file_contents = [re.sub("\n", "", w) for w in file_contents]
#
#
# def extract_text(e):
#     if isinstance(e, str):
#         return e
#     return "".join([x if isinstance(x, str) else x["text"] for x in e])
#
#
# all_messages = " ".join([extract_text(e["text"]) for e in data["messages"]])
# all_messages = all_messages.replace("\n", " ")
# all_messages = all_messages.lower().split(" ")
# all_messages = [re.sub("[\W_]", "", w) for w in all_messages]
# all_messages = [w for w in all_messages if len(w) > 3 != ""]
# all_messages = [w for w in all_messages if not w in file_contents]
#  all_messages = [morph.parse(w).normal_form for w in all_messages]

# #
# # md = defaultdict(int)
# # for w in all_messages:
# #     md[w] += 1
#
# # for w in sorted(md, key=md.get, reverse=False):
# #     print("{} -> {}".format(w, md[w]))
