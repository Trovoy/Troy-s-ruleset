import requests

rawChinaASN = requests.get("https://raw.githubusercontent.com/VirgilClyne/VirgilClyne/main/modules/ASN/ASN.list").text

result = list()
for rawresult in [rawChinaASN]:
    result.extend([item for item in rawresult.split("\n") if not item.startswith('#')])
result_text = '\n'.join(result)

with open("./ChinaASN.conf", "w") as f:
    f.write("\n".join(result))
