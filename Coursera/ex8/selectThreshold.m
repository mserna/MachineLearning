function [bestEpsilon bestF1] = selectThreshold(yval, pval)
%SELECTTHRESHOLD Find the best threshold (epsilon) to use for selecting
%outliers
%   [bestEpsilon bestF1] = SELECTTHRESHOLD(yval, pval) finds the best
%   threshold to use for selecting outliers based on the results from a
%   validation set (pval) and the ground truth (yval).

bestEpsilon = 0;
bestF1 = 0;
F1 = 0;
cvPredictions = 1;

stepsize = (max(pval) - min(pval)) / 1000;
for epsilon = min(pval):stepsize:max(pval),

    % To get binary vector
    cvPredictions = (pval < epsilon);

    fp = sum((cvPredictions == 1) & (yval == 0)); % False positive
    % disp(fp);
    tp = sum((cvPredictions == 1) & (yval == 1)); % True positive
    % disp(tp);
    fn = sum((cvPredictions == 0) & (yval == 1)); % False negative
    % disp(fn);
    precision = tp / (tp + fp);
    % disp(precision);
    recall = tp / (tp + fn);
    % disp(recall);

    F1 = (2*precision*recall) / (precision + recall);

    if F1 > bestF1
       bestF1 = F1;
       bestEpsilon = epsilon;
    endif
endfor

end
