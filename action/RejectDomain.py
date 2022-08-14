import requests

rawRejectDomain = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Advertising/Advertising_Domain.list").text

result = rawRejectDomain.split("\n")

with open("./RejectDomain.conf", "w") as f:
    f.write("\n".join(result))
   
