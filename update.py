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



def get_tefas_funds():

    """
    TEFAS fon sorgusu için temel bağlantı.
    """

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
            timeout=15
        )


        result = response.read().decode(
            "utf-8"
        )


        return result


    except Exception as e:

        print(e)

        return None



def update_system():

    data = load_data()


    data["last_update"] = datetime.now().strftime(
        "%d.%m.%Y %H:%M"
    )


    tefas_result = get_tefas_funds()


    if tefas_result:

        data["tefas_status"] = {
            "connection": "OK",
            "raw_data_received": True
        }


    else:

        data["tefas_status"] = {
            "connection": "FAILED",
            "raw_data_received": False
        }



    save_data(data)


    print("TEFAS veri testi tamamlandı")



if __name__ == "__main__":

    update_system()
