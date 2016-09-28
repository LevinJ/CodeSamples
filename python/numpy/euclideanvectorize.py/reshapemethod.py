import numpy as np


A_orign = np.array([[1,1,1,1],[2,2,2,2]])
B_orgin = np.array([[1,2,3,4],[1,1,1,1],[1,2,1,9]])

A = A_orign.reshape((2,1,4))
B = B_orgin.reshape((1,3,4))

distance = np.sum((A_orign[:,np.newaxis,:] - B) ** 2, axis = 2)
print distance


sum1 =  np.sum(A **2, axis = 2) 
sum2 = - 2 * A_orign.dot(B_orgin.T)
sum3 = np.sum(B **2, axis = 2)
distance_2 = sum1 + sum2 + sum3
print distance_2

def compute_distances_no_loops(self, X):
        """
        Compute the distance between each test point in X and each training point
        in self.X_train using no explicit loops.

        Input / Output: Same as compute_distances_two_loops
        """
        num_test = X.shape[0]
        num_train = self.X_train.shape[0]
        dists = np.zeros((num_test, num_train)) 
        #########################################################################
        # TODO:                                                                                                                                 #
        # Compute the l2 distance between all test points and all training            #
        # points without using any explicit loops, and store the result in            #
        # dists.                                                                                                                                #
        #                                                                                                                                             #
        # You should implement this function using only basic array operations; #
        # in particular you should not use functions from scipy.                                #
        #                                                                                                                                             #
        # HINT: Try to formulate the l2 distance using matrix multiplication        #
        #             and two broadcast sums.                                                                                 #
        #########################################################################
        test_matrix = X
        train_matrix = self.X_train
        dists = np.sum(test_matrix[:,np.newaxis,:] ** 2, axis = 2) -2 * test_matrix.dot(train_matrix.T) + np.sum(train_matrix[np.newaxis,:,:] **2, axis = 2)
        
        #########################################################################
        #                                                 END OF YOUR CODE                                                            #
        #########################################################################
        return dists