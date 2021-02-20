import numpy as np
# numpy data structures and functions are vectorised.

python_list = [1, 2, 3, 4, 5]
print(python_list * 5)

numpy_array = np.array([1, 2, 3, 4, 5])
print(numpy_array * 5)
print(np.sin(numpy_array))



# numpy data structure is the "array"
# pandas the main data structure is the "DataFrame"   (Minor data structure is the "Series")
print("\n\n  **  PANDAS  **")
import pandas as pd


example_data = pd.Series(np.random.random(5), index=["hello world", "b", "c", "d", "e"])
print(example_data)

print(example_data.mean())
print(example_data.b)
print(example_data["b"])

example_data["hello world"]
# example_data.hello world
print("\n\n")
d = [
[112536773,7,"2019-01-01 00:07:00","2019-01-01 00:14:00",3046,34.052872,-118.247490,3051,34.045422,-118.253517,"06468",1,"One Way","Walk-up","standard"],
[112536772,6,"2019-01-01 00:08:00","2019-01-01 00:14:00",3046,34.052872,-118.247490,3051,34.045422,-118.253517,12311,1,"One Way","Walk-up","standard"],
[112538689,32,"2019-01-01 00:18:00","2019-01-01 00:50:00",3030,34.051941,-118.243530,3075,34.042110,-118.256187,"05992",1,"One Way","Walk-up","standard"],
[112538688,30,"2019-01-01 00:20:00","2019-01-01 00:50:00",3030,34.051941,-118.243530,3075,34.042110,-118.256187,"05860",1,"One Way","Walk-up","standard"],
[112538687,28,"2019-01-01 00:22:00","2019-01-01 00:50:00",3030,34.051941,-118.243530,3075,34.042110,-118.256187,"06006",1,"One Way","Walk-up","standard"],
[112538686,28,"2019-01-01 00:23:00","2019-01-01 00:51:00",3030,34.051941,-118.243530,3075,34.042110,-118.256187,"06304",1,"One Way","Walk-up","standard"],
[112538685,27,"2019-01-01 00:24:00","2019-01-01 00:51:00",3030,34.051941,-118.243530,3075,34.042110,-118.256187,"05846",1,"One Way","Walk-up","standard"],
[112537730,7,"2019-01-01 00:27:00","2019-01-01 00:34:00",3029,34.048851,-118.246422,3038,34.046822,-118.248352,12364,1,"One Way","Walk-up","standard"],
[112538445,19,"2019-01-01 00:27:00","2019-01-01 00:46:00",3030,34.051941,-118.243530,3031,34.044701,-118.252441,"06394",1,"One Way","Walk-up","standard"],
[112537729,6,"2019-01-01 00:28:00","2019-01-01 00:34:00",3029,34.048851,-118.246422,3038,34.046822,-118.248352,12204,1,"One Way","Walk-up","standard"],
[112538443,18,"2019-01-01 00:28:00","2019-01-01 00:46:00",3030,34.051941,-118.243530,3031,34.044701,-118.252441,12225,1,"One Way","Walk-up","standard"],
[112537728,5,"2019-01-01 00:29:00","2019-01-01 00:34:00",3029,34.048851,-118.246422,3038,34.046822,-118.248352,"06718",1,"One Way","Walk-up","standard"],
[112538440,17,"2019-01-01 00:29:00","2019-01-01 00:46:00",3030,34.051941,-118.243530,3031,34.044701,-118.252441,"06704",1,"One Way","Walk-up","standard"]
]
c = ["trip_id","duration","start_time","end_time","start_station","start_lat","start_lon","end_station","end_lat","end_lon","bike_id","plan_duration","trip_route_category","passholder_type","bike_type"]

example_df = pd.DataFrame(d, columns=c)
print(example_df)

print(example_df.dtypes)
# print(example_df.describe())
# print(example_df.head())
# print(example_df.tail())

print(example_df.bike_id)
print(example_df[["bike_id", "duration"]])


# Filtering
filt_duration = example_df["duration"] > 25
filt_id = example_df.trip_id % 2 == 0
print(example_df[filt_duration | filt_id])

filename = "D:/TechTalents/Classes/Active/python-data-science-saturday/sf_metro_bikes/metro_bike_2019.csv"
data = pd.read_csv(filename)

print(data.describe())
