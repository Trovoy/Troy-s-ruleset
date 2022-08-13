import requests

rawBiliBili = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/BiliBili/BiliBili.list").text
rawBiliBili_Resolve = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/BiliBili/BiliBili.list").text

result = rawBiliBili.split("\n") + result = rawBiliBili_Resolve.split("\n")

with open("./AsianMedia.conf", "w") as f:
    f.write("\n".join(result))
