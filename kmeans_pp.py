# pip pandas, numpy
#DONE

# import pandas, numpy, sys, inf

import pandas as pd
import numpy as np

import sys
from math import inf

# main

def main():

#  check the validity of the arguments

    k = int(sys.argv[1])
    max_iter = 300
    firstT = 2
    seceondT = 3
    if len(sys.argv) > 3:
        max_iter = int(sys.argv[2])
        firstT = 3
        seceondT = 4

# txt1 into panda
# txt2 into panda

    df1 = pd.read_csv(sys.argv[firstT],sep = ",", header = None)
    df2 = pd.read_csv(sys.argv[seceondT],sep = ",", header = None)

    df1 = df1.sort_values(by=0,ascending=True)



# join both of them by the first column (5 numbers in a row)

    df = pd.merge(df1, df2, on = 0, sort = True)

# turn into numpy without the first column ( 4 numbers in a row)

    df = df.iloc[:,1:] # cut the first column
    arr = df.to_numpy()

# construct array of clusters - the first cluster is randomly selected

    num_rows, num_cols = arr.shape # num_cols = dimension
    np.random.seed(0)
    first_cluster_idx = np.random.choice(num_rows) # choose randomly one of the points
    print(first_cluster_idx)
    # does 'clusters' in np or array. remember that clusters is dependent with arr
    # turn np to array?
    clusters = np.zeros((k,num_cols)) # create an array of all zeros for the k clusters to come
    clusters[0] = arr[first_cluster_idx] # update the first cluster
                                        # clusters = [arr[first_cluster_idx].tolist()] # set the first cluster to be the randomly selected point


# set array of probabilites called prob
    probability = [float(inf) for i in range(num_rows)]

# loop over and update k initial clusters

    z = 1
    while (z < k):
        #loop over all the data points (1-n)
            # loop over all the current clusters

        for i in range(num_rows): # Find Di for each point
            for j in range(z): # loop over the current clusters updated
                cur_norm = np.linalg.norm(arr[i] - clusters[j]) # Di for the j cluster
                if cur_norm < probability[i]:                          # set Di to be the min
                    probability[i] = cur_norm

        sumOfProbs = sum(probability) # sum of probabilities
        for i in range(len(probability)):
            probability[i] = probability[i] / sumOfProbs

    # use 'probability' to randomly choose point to be cluster

        next_cluster_idx = np.random.choice(num_rows, p = probability)
        clusters[z] = arr[next_cluster_idx] # initialize another cluster
        print(next_cluster_idx)
      #  print(probability[73])
       # print(probability[75])

        probability = [float(inf) for i in range(num_rows)] #initialize the probability array
        z += 1

    print(clusters)


# c  ?

if __name__ == "__main__":
    main()