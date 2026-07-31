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



def get_tefas_data():

    """
    TEFAS veri bağlantısı için başlangıç bölümü.
    Veri alınamadığında boş liste döndürür.
    """

    try:

        url = "https://www.tefas.gov.tr"

        request = urllib.request.Request(
            url,
            headers={
                "User-Agent": "Mozilla/5.0"
            }
        )


        urllib.request.urlopen(
            request,
            timeout=10
        )


        # Gerçek veri ayrıştırma sonraki aşamada eklenecek.
        return []


    except Exception:

        return []



def update_system():

    data = load_data()


    data["last_update"] = datetime.now().strftime(
        "%d.%m.%Y %H:%M"
    )


    funds = get_tefas_data()


    data["tefas_status"] = {

        "connection": "OK" if funds else "Bekliyor",

        "fund_count": len(funds)

    }


    data["funds"] = funds


    save_data(data)


    print("TEFAS bağlantı testi tamamlandı")



if __name__ == "__main__":

    update_system()
