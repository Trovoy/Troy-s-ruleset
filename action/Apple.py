import requests

rawApple = requests.get("https://ruleset.skk.moe/List/non_ip/apple_services.conf").text

result = rawApple.split("\n")

with open("./Apple.conf", "w") as f:
    f.write("\n".join(result))
