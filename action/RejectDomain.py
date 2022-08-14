import requests

rawREJECTDomain = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Advertising/Advertising_Domain.list").text

result = rawREJECTDomain.split("\n")

with open("./REJECTDomain.conf", "w") as f:
    f.write("\n".join(result))
   
