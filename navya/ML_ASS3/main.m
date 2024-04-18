% how to run: run main.m

% Load the training dataset
trainData = csvread('MNIST_training_HW2.csv', 1, 0);

% Extract the features and labels
X_train = trainData(:, 2:end);
y_train = trainData(:, 1);

% Load the test dataset
testData = csvread('MNIST_test_HW2.csv', 1, 0);

% Extract the features and labels
X_test = testData(:, 2:end);
y_test = testData(:, 1);

% Set the value of K (number of neighbors)
K = 3;

% Initialize variables to count correctly and incorrectly classified test data
correctCount = 0;
incorrectCount = 0;

% Iterate over each test data point
for i = 1:size(X_test, 1)
    % Compute Euclidean distances from the current test data point to every training data point
    distances = sqrt(sum((X_train - X_test(i, :)).^2, 2));
    
    % Find the K nearest neighbors and get their labels
    [~, indices] = mink(distances, K);
    nearestLabels = y_train(indices);
    
    % Find the majority class (label) among the nearest neighbors
    predictedLabel = mode(nearestLabels);
    
    % Compare the predicted label with the ground truth label
    if predictedLabel == y_test(i)
        % Correctly classified
        correctCount = correctCount + 1;
    else
        % Incorrectly classified
        incorrectCount = incorrectCount + 1;
    end
end

% Compute the accuracy
accuracy = correctCount / size(X_test, 1) * 100;
fprintf('Accuracy: %.2f%%\n', accuracy);
