import json
from datetime import datetime


file = "data.json"


with open(file, "r", encoding="utf-8") as f:
    data = json.load(f)


data["last_update"] = datetime.now().strftime("%d.%m.%Y %H:%M")


with open(file, "w", encoding="utf-8") as f:
    json.dump(
        data,
        f,
        ensure_ascii=False,
        indent=2
    )


print("Fon takip sistemi güncellendi")
