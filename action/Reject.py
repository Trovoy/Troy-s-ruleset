import requests

rawnonip = requests.get("https://ruleset.skk.moe/List/non_ip/reject.conf").text
rawip = requests.get("https://ruleset.skk.moe/List/ip/reject.conf").text

result = list()
for rawresult in [rawnonip , rawip]:
    result.extend([item for item in rawresult.split("\n") if not item.startswith('#')])
result_text = '\n'.join(result)

with open("./Reject.conf", "w") as f:
    f.write("\n".join(result))
