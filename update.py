import json
from datetime import datetime
import urllib.request


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



def get_market_status():

    return {

        "daily_inflow": 0,
        "daily_outflow": 0,
        "weekly_inflow": 0,
        "weekly_outflow": 0,
        "monthly_inflow": 0,
        "monthly_outflow": 0,
        "net_flow": 0,
        "liquidity_status": "Veri bağlantısı hazırlanıyor"

    }



def update_system():

    data = load_data()


    data["last_update"] = datetime.now().strftime(
        "%d.%m.%Y %H:%M"
    )


    data["market_liquidity"] = get_market_status()


    save_data(data)


    print("Fon takip sistemi güncellendi")



if __name__ == "__main__":

    update_system()
