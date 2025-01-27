import DBScan as db
import pandas as pd
import numpy as np


data = pd.read_csv("color.csv")
data = data.drop(columns=["color"])
data_array = np.array(data)
data = []
for i in data_array:
    data.append(list(i))


def main():
    dbscan = db.DBSCAN(5, 25, data)
    cluster = dbscan.clustering()
    dbscan.draw(cluster)


if __name__ == "__main__":
    main()

