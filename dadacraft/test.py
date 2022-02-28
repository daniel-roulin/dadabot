from mcstatus import MinecraftServer

server_url = "dadarou.internet-box.ch"

def get_players():
    server = MinecraftServer.lookup(server_url)
    try:
        query = server.query()
        players = query.players.names
        print("The server has the following players online: {0}".format(", ".join(players)))
        return players
    except Exception as e:
        print('[MCStatus]: Error when querying the server:')
        print(str(e))
        return []

get_players()