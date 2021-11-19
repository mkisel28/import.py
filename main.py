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
    words = [morph.parse(w)[0].normal_form for w in words]
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
