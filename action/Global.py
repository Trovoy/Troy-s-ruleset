import requests

rawGlobal = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Global/Global.list").text
rawTelegram = requests.get("https://raw.githubusercontent.com/VirgilClyne/GetSomeFries/main/ruleset/ASN.Telegram.list").text
rawApple = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Apple/Apple.list").text

result = list()
for rawresult in [rawGlobal , rawTelegram , rawApple]:
    result.extend([item for item in rawresult.split("\n") if not item.startswith('#')])
result_text = '\n'.join(result)

with open("./Global.conf", "w") as f:
    f.write("\n".join(result))
