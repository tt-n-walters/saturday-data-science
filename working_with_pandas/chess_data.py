import pandas as pd

def handle_float_timestamp(as_float):
    return pd.Timestamp(float(as_float), unit="ms")

converters = {
    "created_at": handle_float_timestamp,
    "last_move_at": handle_float_timestamp
}
data = pd.read_csv("games.csv", converters=converters)

print(data.columns)
print(data.dtypes)
print(data.shape)


# winner_white = data[data.winner == "white"]
# winner_black = data[data.winner == "black"]
# winner_draw = data[data.winner == "draw"]

# print("white:", len(winner_white) / len(data))
# print("black:", len(winner_black) / len(data))
# print("draw:", len(winner_draw) / len(data))

example_id = "yellow_dragon"
filt_won_as_white = data.winner == "white"
filt_played_as_white = data.white_id == example_id
filt_won_as_black = data.winner == "black"
filt_played_as_black = data.black_id == example_id
games_found = data[(filt_played_as_white & filt_won_as_white) | (filt_played_as_black & filt_won_as_black)]
print(len(games_found))


all_names = pd.concat([data.white_id, data.black_id]).unique()
print(len(all_names))