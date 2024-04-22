import numpy as np
import math

points = np.array([[2, 10], [2, 6], [11, 11], [6, 9], [6, 4], [1, 2], [5, 10], [4, 9], [10, 12], [7, 5], [9, 11], [4, 6], [3, 10], [3, 8], [6, 11]])
k = 3  

centroids = points[np.random.choice(points.shape[0], k, replace=False)]
centroid_dict = {i: centroid for i, centroid in enumerate(centroids)}

num_iterations = 10 

for iteration in range(num_iterations):
    cluster_assignments = {key: [] for key in range(k)}

    for point in points:
        dist_arr = [math.sqrt((point[0] - centroid_dict[j][0])**2 + (point[1] - centroid_dict[j][1])**2) for j in range(k)]

        min_index = np.argmin(dist_arr)

        cluster_assignments[min_index].append(point)

    for j in range(k):
        if len(cluster_assignments[j]) > 0:
            new_centroid = np.mean(cluster_assignments[j], axis=0)
            centroid_dict[j] = new_centroid

    # print(f"Iteration {iteration + 1}")
    # for idx in cluster_assignments:
    #     print(f"Cluster {idx}: {np.array(cluster_assignments[idx])}")
    # print("Centroids:", {idx: list(centroid) for idx, centroid in centroid_dict.items()})

print("Final Cluster assignments:")
for idx in cluster_assignments:
    print(f"Cluster {idx+1}, {centroid_dict[idx]}: {np.array(cluster_assignments[idx])}")