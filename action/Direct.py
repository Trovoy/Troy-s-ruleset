import requests

rawWeChat = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/WeChat/WeChat.list").text
rawTesla = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Tesla/Tesla.list").text
rawXiaoHongShu = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/XiaoHongShu/XiaoHongShu.list").text
rawApple = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Apple/Apple.list").text
rawXianYu = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/XianYu/XianYu.list").text

result = list()
for rawresult in [rawWeChat , rawTesla , rawXiaoHongShu , rawApple ,rawXianYu]:
    result.extend([item for item in rawresult.split("\n") if not item.startswith('#')])
result_text = '\n'.join(result)

with open("./Direct.list", "w") as f:
    f.write("\n".join(result))
