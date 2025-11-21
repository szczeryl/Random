% Pearson's Coefficient (r) Computation with Econometrics Package 
% The package costs USD6 and I am not willing to pay when it can be done in this manner

%change data accordingly
training = [
    3.3459    1.0893    3.2103    1.7440    1.6762; 
    2.7435    2.9113    1.4706    1.2895    2.1366; 
   -1.7253   -0.7804   -0.9944    0.5307   -1.0502; 
    2.9972    1.1399    2.2280    0.3387    2.5042
];

% row1, 2,3...
x1 = training(1, :);
x2 = training(2, :);
x3 = training(3, :);
y = training(4, :);

%Where the computation is
corr_x1_y = sum(((x1 - mean(x1)) .* (y - mean(y))) / (sqrt(sum((x1 - mean(x1)).^2)) * sqrt(sum((y - mean(y)).^2))));
corr_x2_y = sum(((x2 - mean(x2)) .* (y - mean(y))) / (sqrt(sum((x2 - mean(x2)).^2)) * sqrt(sum((y - mean(y)).^2))));
corr_x3_y = sum(((x3 - mean(x3)) .* (y - mean(y))) / (sqrt(sum((x3 - mean(x3)).^2)) * sqrt(sum((y - mean(y)).^2))));

% r-value will be displayed here
disp(['Correlation between x1 and y: ' num2str(corr_x1_y)]);
disp(['Correlation between x2 and y: ' num2str(corr_x2_y)]);
disp(['Correlation between x3 and y: ' num2str(corr_x3_y)]);
