import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


class DBSCAN:
    def __init__(self, minpts: int, eps: float, x: list):
        self.minpts = minpts              # min neighbour for condition
        self.eps = eps                    # min evclidian distance for condition
        self.x = x                        # data
        self.clusters = {
            'noise': [],
        }
        self.visited = []

    def distance(self, point1: list[float], point2: list[float]):           #evclid distation
        return np.sqrt(np.sum(((np.array(point1) - np.array(point2)) ** 2)))

    
    def neighbour(self, p: list[float]):        #neigbours root point
        result = []
        for i in self.x:
            if self.distance(i, p) < self.eps:
                result.append(i)
        return result

    
    def clustering(self) -> int:
        c_cluster = 0               #count clusters
        for cl in range(len(self.x)):
            root_point = self.x[np.random.randint(0, len(self.x))]
            if root_point not in self.visited:
                if len(self.neighbour(root_point)) <= self.minpts:
                    self.clusters['noise'].append(root_point)
                    self.visited.append(root_point)
                    continue
                need_visit = self.neighbour(root_point)
                c_cluster += 1
                self.clusters[c_cluster] = [root_point]
                while len(need_visit) > 0:
                    for i in need_visit:
                        need_visit.remove(i)
                        if i not in self.visited:
                            new_neightbour = self.neighbour(i)
                            self.clusters[c_cluster] += new_neightbour
                            need_visit += new_neightbour
                            self.visited.append(i)

        print(c_cluster)
        return c_cluster

    
    def draw(self, count_cluster: int) -> None:
        random_color = []
        for i in range(0, count_cluster):
            r = np.random.randint(1, 255) / 224
            g = np.random.randint(1, 255) / 224
            b = np.random.randint(1, 255) / 224
            random_color.append((r, g, b))

        for cluster in self.clusters:
            for point in self.clusters[cluster]:
                if cluster == 'noise':
                    color = '#000000'
                    plt.scatter(point[0], point[1], c=color, marker='x')
                else:
                    color = random_color[cluster - 1]
                    plt.scatter(point[0], point[1], c=color)
        
        plt.title('DBSCAN Clustering')
        plt.show()
