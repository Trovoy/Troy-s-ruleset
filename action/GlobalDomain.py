import requests

rawGlobalDomian = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Global/Global_Domain.list").text

result = list()
for rawresult in [rawGlobalDomian]:
    result.extend([item for item in rawresult.split("\n") if not item.startswith('#')])
result_text = '\n'.join(result)

with open("./GlobalDomain.list", "w") as f:
    f.write("\n".join(result))
