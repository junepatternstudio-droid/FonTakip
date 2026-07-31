import json
from datetime import datetime


with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)


data["last_update"] = datetime.now().strftime("%d.%m.%Y %H:%M")


with open("data.json", "w", encoding="utf-8") as f:
    json.dump(
        data,
        f,
        ensure_ascii=False,
        indent=2
    )


print("Fon takip güncellendi")
