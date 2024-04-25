# def predict_employee_leave(user_input):
#     import pandas as pd
#     from sklearn.ensemble import RandomForestClassifier
#     from sklearn.preprocessing import LabelEncoder
#     from sklearn.impute import SimpleImputer

#     # Load datasets
#     satisfaction_df = pd.read_excel('employee_satisfaction_evaluation.xlsx', engine='openpyxl')
#     hr_df = pd.read_csv('hr_data.csv')

#     # Merge datasets
#     merged_df = pd.merge(hr_df, satisfaction_df, left_on='employee_id', right_on='EMPLOYEE #', how='inner')

#     # Identify target variable and features
#     target = 'left'
#     features = ['satisfaction_level', 'last_evaluation', 'number_project', 'average_montly_hours',
#                 'time_spend_company', 'Work_accident', 'promotion_last_5years', 'department', 'salary']

#     # Data preprocessing
#     le = LabelEncoder()
#     merged_df['department'] = le.fit_transform(merged_df['department'])
#     merged_df['salary'] = le.fit_transform(merged_df['salary'])

#     # Handle missing values
#     X = merged_df[features]
#     y = merged_df[target]

#     # Use SimpleImputer to fill NaN values with the mean
#     imputer = SimpleImputer(strategy='mean')
#     X = pd.DataFrame(imputer.fit_transform(X), columns=features)

#     # Train the model
#     model = RandomForestClassifier(random_state=42)
#     model.fit(X, y)

#     # Preprocess user input for department
#     user_department = user_input['department']
#     try:
#         encoded_department = le.transform([user_department])[0]
#     except ValueError:
#         # Assign a special label for unseen categories
#         encoded_department = len(le.classes_)  # Assign a label that is not used in the training data
#     user_input['department'] = encoded_department

#     # Preprocess user input for salary
#     user_salary = user_input['salary']
#     try:
#         encoded_salary = le.transform([user_salary])[0]
#     except ValueError:
#         # Assign a special label for unseen categories
#         encoded_salary = len(le.classes_)  # Assign a label that is not used in the training data
#     user_input['salary'] = encoded_salary

#     # Make prediction
#     prediction = model.predict(pd.DataFrame([user_input], columns=features))

#     if prediction[0] == 0:
#         return "The employee is not likely to leave."
#     elif prediction[0] == 1:
#         return "The employee is likely to leave."
#     else:
#         return "Unable to determine."


# # Example usage:
# user_input = {
#     'satisfaction_level': 0.2,
#     'last_evaluation': 0.5,
#     'number_project': 2,
#     'average_montly_hours': 150,
#     'time_spend_company': 3,
#     'Work_accident': 0,
#     'promotion_last_5years': 0,
#     'department': 'sales',
#     'salary': 'medium'
# }

# prediction = predict_employee_leave(user_input)
# print("Prediction:", prediction)



def predict_employee_leave(user_input):
    import pandas as pd
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.preprocessing import LabelEncoder
    from sklearn.impute import SimpleImputer

    # Load datasets
    satisfaction_df = pd.read_excel('employee_satisfaction_evaluation.xlsx', engine='openpyxl')
    hr_df = pd.read_csv('hr_data.csv')

    # Merge datasets
    merged_df = pd.merge(hr_df, satisfaction_df, left_on='employee_id', right_on='EMPLOYEE #', how='inner')

    # Identify target variable and features
    target = 'left'
    features = ['satisfaction_level', 'last_evaluation', 'number_project', 'average_montly_hours',
                'time_spend_company', 'Work_accident', 'promotion_last_5years', 'department', 'salary']

    # Data preprocessing
    le = LabelEncoder()
    merged_df['department'] = le.fit_transform(merged_df['department'])
    merged_df['salary'] = le.fit_transform(merged_df['salary'])

    # Handle missing values
    X = merged_df[features]
    y = merged_df[target]

    # Use SimpleImputer to fill NaN values with the mean
    imputer = SimpleImputer(strategy='mean')
    X = pd.DataFrame(imputer.fit_transform(X), columns=features)

    # Train the model
    model = RandomForestClassifier(random_state=42)
    model.fit(X, y)

    # Preprocess user input
    user_input_encoded = {
        'satisfaction_level': user_input['satisfaction_level'],
        'last_evaluation': user_input['last_evaluation'],
        'number_project': user_input['number_project'],
        'average_montly_hours': user_input['average_montly_hours'],
        'time_spend_company': user_input['time_spend_company'],
        'Work_accident': user_input['Work_accident'],
        'promotion_last_5years': user_input['promotion_last_5years']
    }
    
    # Encode department and salary
    user_department = user_input['department']
    try:
        encoded_department = le.transform([user_department])[0]
    except ValueError:
        # Assign a special label for unseen categories
        encoded_department = len(le.classes_)  # Assign a label that is not used in the training data
    user_input_encoded['department'] = encoded_department

    user_salary = user_input['salary']
    try:
        encoded_salary = le.transform([user_salary])[0]
    except ValueError:
        # Assign a special label for unseen categories
        encoded_salary = len(le.classes_)  # Assign a label that is not used in the training data
    user_input_encoded['salary'] = encoded_salary

    # Make prediction
    prediction = model.predict(pd.DataFrame([user_input_encoded], columns=features))

    if prediction[0] == 0:
        return "The employee is not likely to leave."
    elif prediction[0] == 1:
        return "The employee is likely to leave."
    else:
        return "Unable to determine."
    
# Example usage:
# user_input = {
#     'satisfaction_level': 0.1,
#     'last_evaluation': 0.8,
#     'number_project': 0,
#     'average_montly_hours': 360,
#     'time_spend_company': 3,
#     'Work_accident': 0,
#     'promotion_last_5years': 0,
#     'department': 'sales',
#     'salary': 'low'
# }

# prediction = predict_employee_leave(user_input)
# print("Prediction:", prediction)
