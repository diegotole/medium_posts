import csv
from collections import defaultdict
import pandas as pd
from matplotlib import pyplot as plt

RAIL_ROAD_ENTRANCE_ID = "0BF5D5A0A713B6B6A081"
MINNIES_HOUSE_ID = "0D8D702F9D13A7C3A0D4"
RAIL_ROAD_TOMORROWLAND_ID = "005DCC8A8413B6B56EFF"


def load_df(f_attractions, f_edges):
    df = pd.read_csv(f_attractions)

    df[['lat', 'long']] = (df[['lat', 'long']] - df[['lat', 'long']].min()) / (
            df[['lat', 'long']].max() - df[['lat', 'long']].min())

    df_edges = pd.read_csv(f_edges)

    return df, df_edges


def load_maps(f_attractions, f_edges):
    attractions_map = {}
    attractions_edges = defaultdict(set)

    with open(f_attractions) as fin:

        csvr = csv.reader(fin)
        next(csvr)
        for line in csvr:
            attractions_map[line[0]] = {"name": line[1], "lat": float(line[2]), "long": float(line[3])}

    with open(f_edges) as fin:

        csvr = csv.reader(fin)
        next(csvr)

        for line in csvr:
            attractions_edges[line[0]].add(line[1])

    return attractions_map,attractions_edges


def display_dictionary(mymap):
    ##ROTATE coordinates
    # df['tmp'] = df['rot_x']
    # df['rot_x'] = df['rot_y']
    # df['rot_y'] = df['tmp']

    tmp = [mymap[x]['lat'] for x in mymap]
    map(  lambda x:  tmp[x] , mymap )


    plt.figure(figsize=(10, 10))

    plt.scatter([mymap[x]['lat'] for x in mymap], [mymap[x]['long'] for x in mymap])

    plt.scatter([mymap[RAIL_ROAD_ENTRANCE_ID]['lat'], ], [mymap[RAIL_ROAD_ENTRANCE_ID]['long'], ], color="red")
    plt.scatter([mymap[MINNIES_HOUSE_ID]['lat'], ], [mymap[MINNIES_HOUSE_ID]['long'], ], color="black")
    plt.scatter([mymap[RAIL_ROAD_TOMORROWLAND_ID]['lat'], ], [mymap[RAIL_ROAD_TOMORROWLAND_ID]['long'], ],
                color="yellow")

    plt.show()




if __name__ == "__main__":
    f_maps = "disneyland_attractions.csv"
    f_edges = "attractions_edges.csv"

    mmap, medges = load_maps(f_maps, f_edges)

    display_dictionary(mmap)

# def display_df(x,y ):
#     plt.figure(figsize=(10,10))
#
#     plt.scatter( x, y)
#
#     plt.scatter( (RAIL_ROAD_ENTRANCE_ROW['rot_x'].values[0] ,), (RAIL_ROAD_ENTRANCE_ROW['rot_y'].values[0] ,) , color="red" )
#     plt.scatter( (MINNIES_HOUSE_ROW['rot_x'].values[0] ,), (MINNIES_HOUSE_ROW['rot_y'].values[0] ,) , color="black" )
#     plt.scatter( (RAIL_ROAD_TOMORROWLAND_ROW['rot_x'].values[0] ,), (RAIL_ROAD_TOMORROWLAND_ROW['rot_y'].values[0] ,) , color="yellow" )
#
#
#     plt.show()
