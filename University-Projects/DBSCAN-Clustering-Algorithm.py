# DBSCAN Clustering Algorithm
import pandas as pd
import numpy as np
import math

UNCLASSIFIED = False
NOISE = None

def _dist(p,q):
    print("\nDist p&q =\n ",p,q,"\n")
    # Uses Euclidean Distance as the measure
    #return math.sqrt(np.power(p-q, 2).sum())
    return np.abs(p-q).sum()

def _eps_neighborhood(p,q,eps):
	return _dist(p,q) < eps

def _region_query(m, point_id, eps):
    n_points = m.shape[1]
    seeds = []
    for i in range(0, n_points):
        if _eps_neighborhood(m[:,point_id], m[:,i], eps):
            seeds.append(i)
    return seeds

def _expand_cluster(m, classifications, point_id, cluster_id, eps, min_points):
    seeds = _region_query(m, point_id, eps)
    if len(seeds) < min_points:
        classifications[point_id] = NOISE
        return False
    else:
        classifications[point_id] = cluster_id
        for seed_id in seeds:
            classifications[seed_id] = cluster_id
            
        while len(seeds) > 0:
            current_point = seeds[0]
            results = _region_query(m, current_point, eps)
            if len(results) >= min_points:
                for i in range(0, len(results)):
                    result_point = results[i]
                    if classifications[result_point] == UNCLASSIFIED or \
                       classifications[result_point] == NOISE:
                        if classifications[result_point] == UNCLASSIFIED:
                            seeds.append(result_point)
                        classifications[result_point] = cluster_id
            seeds = seeds[1:]
        return True
        
def dbscan(m, eps, min_points):
    """Implementation of Density Based Spatial Clustering of Applications with Noise
    See https://en.wikipedia.org/wiki/DBSCAN
    
    scikit-learn probably has a better implementation
    
    Uses Euclidean Distance as the measure
    
    Inputs:
    m - A matrix whose columns are feature vectors
    eps - Maximum distance two points can be to be regionally related
    min_points - The minimum number of points to make a cluster
    
    Outputs:
    An array with either a cluster id number or dbscan.NOISE (None) for each
    column vector in m.
    """
    cluster_id = 1
    n_points = m.shape[1]
    classifications = [UNCLASSIFIED] * n_points
    for point_id in range(0, n_points):
        point = m[:,point_id]
        print (point)
        if classifications[point_id] == UNCLASSIFIED:
            if _expand_cluster(m, classifications, point_id, cluster_id, eps, min_points):
                cluster_id = cluster_id + 1
    return classifications

def test_dbscan():
    m = np.matrix('1 1.2 0.8 3.7 3.9 3.6 10; 1.1 0.8 1 4 3.9 4.1 10')
    print(m)
    eps = 0.5
    min_points = 2
    assert dbscan(m, eps, min_points) == [1, 1, 1, 2, 2, 2, None]


#m = np.matrix('3 4;6 7;4 4;5 7;6 6;2 2;1 2;3 8')
#m = np.matrix('3 6 4 5 6 2 1 3;4 7 4 7 6 2 2 8')
m = np.matrix('3 5 4 3 7 5 2 1 7;2 5 5 3 6 5 2 0 8;1 6 5 2 6 4 2 1 7')
eps = 3
min_points = 3
print(m)
print(dbscan(m, eps, min_points))

# test_dbscan()


data = pd.DataFrame([[3, 5, 6],
                     [2, 7, 5],
                     [2, 1, 1],
                     [1, 0, 1],
                     [5, 9, 7],
                     [6, 8, 8],
                     [1, 0, 2],
                     [4, 4, 4],
                     [2, 2, 2],
                     [9, 9, 9]],
                    columns=['F1', 'F2', 'F3'])


# Set Manual centroids
centroids = pd.DataFrame([[1, 0, 1],
                          [5, 9, 7],
                          [2, 7, 5]],
                         columns=['F1', 'F2', 'F3'])
