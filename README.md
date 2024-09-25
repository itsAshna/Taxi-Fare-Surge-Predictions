# Taxi-Fare-Surge-Predictions
Reading and cleaning a dataset, building a Decision Tree model, making predictions, and manually processing CSV data for cleaning purposes.


Steps:

Reading the Data: Read the CSV file into a DataFrame (rides) and extract the first three columns as features (X) and the fourth column as the target variable (Y).

Manual Data Cleanup: Remove newline characters (\n), and then appending the cleaned values to an output list.

Training the Decision Tree Regressor: Build a Decision Tree Regressor model using the extracted data (X and Y) and testing it by predicting the target value for a specific input ([0, 0, 0]).

Closing the File: After the file has been processed, close it and display the output list containing the prediction.

