import json
from datetime import datetime
import urllib.request
import urllib.parse


DATA_FILE = "data.json"


def load_data():
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(
            data,
            f,
            ensure_ascii=False,
            indent=2
        )


def get_tefas_history():

    try:

        url = "https://www.tefas.gov.tr/api/DB/BindHistoryInfo"


        payload = urllib.parse.urlencode({

            "fontip": "YAT",
            "bastarih": "01.07.2026",
            "bittarih": "31.07.2026",
            "fonkod": ""

        }).encode("utf-8")


        request = urllib.request.Request(
            url,
            data=payload,
            headers={
                "User-Agent": "Mozilla/5.0",
                "Content-Type": "application/x-www-form-urlencoded"
            }
        )


        response = urllib.request.urlopen(
            request,
            timeout=20
        )


        return json.loads(
            response.read().decode("utf-8")
        )


    except Exception as e:

        print("TEFAS hata:", e)

        return None



def parse_funds(raw):

    funds = []


    if not raw:
        return funds


    try:

        items = raw.get("data", [])


        for item in items:

            funds.append({

                "code": item.get("FONKODU", ""),

                "name": item.get("FONUNVAN", ""),

                "price": item.get("FIYAT", 0),

                "date": item.get("TARIH", ""),

                "daily_return": 0,

                "weekly_return": 0,

                "monthly_return": 0,

                "daily_inflow": 0,

                "weekly_inflow": 0,

                "investor_change": 0

            })


    except Exception as e:

        print("Ayrıştırma hata:", e)


    return funds



def update_system():

    data = load_data()


    data["last_update"] = datetime.now().strftime(
        "%d.%m.%Y %H:%M"
    )


    raw = get_tefas_history()


    funds = parse_funds(raw)


    data["funds"] = funds


    data["tefas_status"] = {

        "connection": "OK" if funds else "NO DATA",

        "fund_count": len(funds)

    }


    save_data(data)


    print(
        "Fon sayısı:",
        len(funds)
    )



if __name__ == "__main__":

    update_system()
