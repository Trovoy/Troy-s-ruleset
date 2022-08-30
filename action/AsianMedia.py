import requests

rawBiliBili = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/BiliBili/BiliBili.list").text
rawBiliBiliIntl = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/BiliBiliIntl/BiliBiliIntl.list").text

result = list()
for rawresult in [rawBiliBili , rawBiliBiliIntl]:
    result.extend([item for item in rawresult.split("\n") if not item.startswith('#')])
result_text = '\n'.join(result)

with open("./AsianMedia.conf", "w") as f:
    f.write("\n".join(result))
