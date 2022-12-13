import requests

rawWeChat = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/WeChat/WeChat.list").text

result = list()
for rawresult in [rawWeChat]:
    result.extend([item for item in rawresult.split("\n") if not item.startswith('#')])
result_text = '\n'.join(result)

with open("./Direct.conf", "w") as f:
    f.write("\n".join(result))
