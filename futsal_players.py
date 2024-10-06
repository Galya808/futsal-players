from fastapi import Body, FastAPI

app = FastAPI()

PLAYERS = [
    {'name': 'Higuita', 'position': 'gk', 'number': '2'},
    {'name': 'Douglas', 'position': 'cb', 'number': '14'},
    {'name': 'Leo', 'position': 'cm', 'number': '8'},
    {'name': 'Tursagulov', 'position': 'fw', 'number': '12'},
    {'name': 'Orazov', 'position': 'fw', 'number': '11'},
]


@app.get("/")
async def first_api():
    return {"message": "Hello Gala!"}


@app.get("/players")
async def get_all_players():
    return PLAYERS


@app.get("/players/{shirt_number}")
async def get_player(shirt_number: str):
    for player in PLAYERS:
        if player.get('number').casefold() == shirt_number.casefold():
            return {'player': player}


@app.get("/players/")
async def get_some_players(position:str):
    player_list = []

    for player in PLAYERS:
        if player.get('position').casefold() == position.casefold():
            player_list.append(player)

    return player_list


@app.post("/players/add_player")
async def add_player(new_player=Body()):
    for player in PLAYERS:
        if player.get("name").casefold() == new_player.get("name").casefold():
            return
    PLAYERS.append(new_player)


@app.put("/players/update_player")
async def update_player(updated_player=Body()):
    for i in range(len(PLAYERS)):
        if PLAYERS[i].get('name') == updated_player.get('name'):
            PLAYERS[i] = updated_player

@app.delete("/players/delete_player/{player_name}")
async def delete_player(player_name: str):
    for i in range(len(PLAYERS)):
        if PLAYERS[i].get("name").casefold() == player_name.casefold():
            PLAYERS.pop(i)
            break