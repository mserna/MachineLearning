function centroids = computeCentroids(X, idx, K)
%COMPUTECENTROIDS returns the new centroids by computing the means of the 
%data points assigned to each centroid.
%   centroids = COMPUTECENTROIDS(X, idx, K) returns the new centroids by 
%   computing the means of the data points assigned to each centroid. It is
%   given a dataset X where each row is a single data point, a vector
%   idx of centroid assignments (i.e. each entry in range [1..K]) for each
%   example, and K, the number of centroids. You should return a matrix
%   centroids, where each row of centroids is the mean of the data points
%   assigned to it.
%

% Useful variables
[m n] = size(X);

% You need to return the following variables correctly.
centroids = zeros(K, n);

for iter = 1:K,
    % Set idx to iterator
    idx_iter = find(idx == iter);

    % Set centroid K
    C_k = numel(idx_iter);
    %disp(C_k);

    % Compute centroid
    centroids(iter,:) = (1/C_k) * (sum(X(idx_iter,:)));
endfor

end

