import requests

rawBiliBili = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/BiliBili/BiliBili.list").text
rawBiliBiliIntl = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/BiliBiliIntl/BiliBiliIntl.list").text

result = rawBiliBili.split("\n") + rawBiliBiliIntl.split("\n")

with open("./AsianMedia.conf", "w") as f:
    f.write("\n".join(result))
