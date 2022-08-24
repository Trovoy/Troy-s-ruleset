import requests

rawnonip = requests.get("https://ruleset.skk.moe/List/non_ip/reject.conf").text
rawip = requests.get("https://ruleset.skk.moe/List/ip/reject.conf").text

result = rawnonip.split("\n") + rawip.split("\n")

with open("./Reject.conf", "w") as f:
    f.write("\n".join(result))
