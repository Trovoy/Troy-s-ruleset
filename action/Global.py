import requests

rawGlobal = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Global/Global.list").text

result = list()
for rawresult in [rawGlobal]:
    result.extend([item for item in rawresult.split("\n") if not item.startswith('#')])
result_text = '\n'.join(result)

with open("./Global.conf", "w") as f:
    f.write("\n".join(result))
