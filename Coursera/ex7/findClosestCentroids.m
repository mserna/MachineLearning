function idx = findClosestCentroids(X, centroids)
%FINDCLOSESTCENTROIDS computes the centroid memberships for every example
%   idx = FINDCLOSESTCENTROIDS (X, centroids) returns the closest centroids
%   in idx for a dataset X where each row is a single example. idx = m x 1 
%   vector of centroid assignments (i.e. each entry in range [1..K])
%

% Set K
K = size(centroids, 1);
unsorted_list = [];

% You need to return the following variables correctly.
idx = zeros(size(X,1), 1);
% closest_centroid = inf;
% next_closest_centroid = inf;
for row = 1:size(X,1),
    difference = [];
    for iter = 1:K,
        % Using distance formula find closer centroid
        difference(iter) = sqrt(sum((X(row,:) - centroids(iter, :)) .^ 2, 2));
        %disp(difference(iter));
    endfor
    % Check for minimal difference
    [min_diff, min_idx] = min(difference);
    idx(row) = min_idx;
endfor

end

