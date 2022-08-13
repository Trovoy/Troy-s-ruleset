import requests

rawAppleDomain = requests.get("https://ruleset.skk.moe/List/domainset/apple_cdn.conf").text

result = rawAppleDomain.split("\n")

with open("./AppleDomain.conf", "w") as f:
    f.write("\n".join(result))
