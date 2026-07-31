import json
from datetime import datetime


DATA_FILE = "data.json"


def load_data():

    with open(DATA_FILE, "r", encoding="utf-8") as file:
        return json.load(file)



def save_data(data):

    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(
            data,
            file,
            ensure_ascii=False,
            indent=2
        )



def update_system():

    data = load_data()


    data["last_update"] = datetime.now().strftime(
        "%d.%m.%Y %H:%M"
    )


    if "market_liquidity" not in data:

        data["market_liquidity"] = {

            "daily_inflow": 0,
            "daily_outflow": 0,
            "weekly_inflow": 0,
            "weekly_outflow": 0,
            "monthly_inflow": 0,
            "monthly_outflow": 0,
            "net_flow": 0,
            "liquidity_status": "Hazırlanıyor"

        }


    if "weekly_popular_funds" not in data:

        data["weekly_popular_funds"] = []


    if "monthly_best_funds" not in data:

        data["monthly_best_funds"] = []


    if "money_flow_leaders" not in data:

        data["money_flow_leaders"] = []


    save_data(data)


    print("Fon takip veri sistemi güncellendi")



if __name__ == "__main__":

    update_system()
