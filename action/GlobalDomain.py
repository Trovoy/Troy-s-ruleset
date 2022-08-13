import requests

rawGlobalDomian = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Global/Global_Domain.list").text

result = rawGlobalDomian.split("\n")

with open("./GlobalDomain.conf", "w") as f:
    f.write("\n".join(result))
