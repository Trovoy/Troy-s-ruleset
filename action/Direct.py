import requests

rawApple = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Apple/Apple.list").text
rawWeChat = requests.get("https://raw.githubusercontent.com/NobyDa/Script/master/Surge/WeChat.list").text

result = list()
for rawresult in [rawApple , rawWeChat]:
    result.extend([item for item in rawresult.split("\n") if not item.startswith('#')])
result_text = '\n'.join(result)

with open("./Direct.conf", "w") as f:
    f.write("\n".join(result))
