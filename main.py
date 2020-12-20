# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import csv
import random
import time
import numpy as np
from builtins import print
centroids_number = 2

class Pair:
    elements = []
    meanVector = []

def readScvFile(fileName):
    # Use a breakpoint in the code line below to debug your script.
    with open(fileName) as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        rows = list(reader)  # rows then have all CVS file rows in form of list of list[[] ,[], [] , ...]
        return rows
        print(rows)

def get_random_centroids(rows):
    random_centroids = []
    lsitTemp=random.sample(range(1, len(rows)), centroids_number)
    #lsitTemp = [1, 4]
    for randomIndex in lsitTemp:
        random_centroids.append(rows[randomIndex])
    return random_centroids

def getManhattanDistance(firstPoint, secondPoint):
    result = 0
    for i in range(len(firstPoint)):
        result = result + abs(float(firstPoint[i]) - float(secondPoint[i]))
    return result

def get_initial_cluster_mean(centroid):
    Group_item = Pair()
    Group_item.elements = centroid[:1]
    Group_item.meanVector = [centroid[1:]]
    return Group_item

def generate_new_clusters():
    clusters = []
    for i in range(centroids_number):
        Group_item = Pair()
        Group_item.elements=[]
        Group_item.meanVector=[]
        clusters.append(Group_item)
    return clusters

def calculate_new_mean_vector(list):
    a = []
    for element in list:
        temp = []
        for number in element:
            temp.append(float(number))
        a.append(temp)
    return np.mean(a, axis=0).tolist()

def calculate_new_cluster(oldCluster, rows, newCluster):
    for item in oldCluster:
        distances = []
        for row in rows:
            for cluster in oldCluster:
                distances.append(getManhattanDistance(cluster.meanVector[0], row[1:]))
            newCluster[distances.index(min(distances))].elements.append(row[0])
            newCluster[distances.index(min(distances))].meanVector.append(row[1:])
            distances.clear()
        for cluster in newCluster:
             cluster.meanVector=[calculate_new_mean_vector(cluster.meanVector)]
        return newCluster

def isDifferencesDetected(oldCluster,newCluseter):
    for i in range (len(oldCluster)):
        if (oldCluster[i].elements!=newCluseter[i].elements):
            return True
    return False

if __name__ == '__main__':
    rows = readScvFile('test.csv')
    initial_Clusters = []
    for item in get_random_centroids(rows):
        initial_Clusters.append(get_initial_cluster_mean(item))
    while True:
        print('Old Cluster is')
        for cluster in initial_Clusters:
            print(cluster.elements, ' -- ', cluster.meanVector)
        print('newer Cluster is')
        new_cluster = calculate_new_cluster(initial_Clusters, rows[1:], generate_new_clusters())
        for item in new_cluster:
            print(item.elements, ' ', item.meanVector)
        time.sleep(0.5)
        if  not  (isDifferencesDetected(initial_Clusters,new_cluster)):
            break
        initial_Clusters=new_cluster
    generate_new_clusters()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
