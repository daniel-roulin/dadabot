import requests

def get_uuid(player):
    uuid_url = "https://api.mojang.com/users/profiles/minecraft/"
    return requests.get(uuid_url + player).json()["id"]

def get_skin_url(uuid):
    skin_url = "https://crafatar.com/renders/body/{}?overlay"
    return skin_url.format(uuid)

print(get_skin_url("Superbloc100"))