import requests

rawREJECT = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Advertising/Advertising.list").text

result = rawREJECT.split("\n")

with open("./Reject.conf", "w") as f:
    f.write("\n".join(result))
