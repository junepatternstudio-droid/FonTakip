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



def get_tefas_page():

    try:

        url = "https://www.tefas.gov.tr"


        request = urllib.request.Request(
            url,
            headers={
                "User-Agent": "Mozilla/5.0"
            }
        )


        response = urllib.request.urlopen(
            request,
            timeout=20
        )


        html = response.read().decode(
            "utf-8",
            errors="ignore"
        )


        return html


    except Exception as e:

        return str(e)



def update_system():

    data = load_data()


    data["last_update"] = datetime.now().strftime(
        "%d.%m.%Y %H:%M"
    )


    page = get_tefas_page()


    data["tefas_debug"] = {

        "length": len(page),

        "sample": page[:2000]

    }


    save_data(data)


    print("TEFAS sayfa analizi tamamlandı")



if __name__ == "__main__":

    update_system()
