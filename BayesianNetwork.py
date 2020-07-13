import pandas as pd
import csv

def read_data(filename=''):
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        headers = []
        rows = []
        for row in csv_reader:
            if line_count == 0:
                headers += row
                line_count += 1
            else:
                rows.append(row)
                line_count += 1

    data = pd.DataFrame(rows, columns = headers)

    return data


def init_conditional_features(data, table, features = []):
    if len(features) == 1:
        ftr = features[0]
        table[ftr] = data[ftr].unique()

    elif len(features) == 2:
        ftr0 = features[0]
        ftr1 = features[1]
        col0_data = []
        col1_data = []
        for val0 in data[ftr0].unique():
            for val1 in data[ftr1].unique():
                col0_data.append(val0)
                col1_data.append(val1)
        #conditional features
        table[ftr0] = col0_data
        table[ftr1] = col1_data
    
    return table

def prob(data, feature, value):
    freq = 0
    for index, row in data.iterrows():
        if row[feature] == value:
            freq += 1
    return freq / len(data)

def conditional_prob(data, conditions = [], con_vals = [], feature = '', value = ''):
    con_freq = 0
    freq = 0
    for index, row in data.iterrows():
        find = True
        for i in range(len(conditions)):
            if row[conditions[i]] != con_vals[i]:
                find = False
        if find:
            freq += 1
        if find and row[feature] == value:
            con_freq +=1

    return con_freq / freq

def create_table(data, feature, conditional_features = []):
    table = pd.DataFrame()
    #find diff values in conditional columns
    table = init_conditional_features(data, table, conditional_features)
    #find feature cols
    feature_uniques = data[feature].unique()
    for val in feature_uniques:
        table[val] = 0.0
    
    #calc probs
    for val in feature_uniques:
        if len(conditional_features) == 0:
            pr = prob(data,feature,val)
            table[val] = [pr]
        else:
            for index, row in table.iterrows():
                con_vals = [row[ftr] for ftr in conditional_features]
                table.at[index, val] = conditional_prob(data, conditional_features, con_vals, feature, val)

    print(feature,'table')
    print(table)
    print()
    
    return table

def main():
    data = read_data('Train.txt')
    table_class = create_table(data, 'class')
    table_property_magnitude = create_table(data, 'property_magnitude', ['class'])
    table_own_telephone = create_table(data, 'own_telephone', ['class','job'])
    table_housing = create_table(data, 'housing',['class','property_magnitude'])
    table_job = create_table(data, 'job',['class','property_magnitude'])
    table_personal_status = create_table(data, 'personal_status',['class','housing'])
    table_purpose = create_table(data, 'purpose', ['class','housing'])
    table_credit_history = create_table(data, 'credit_history', ['class', 'own_telephone'])
    table_employment = create_table(data, 'employment', ['class', 'job'])

    test_data = read_data('Test.txt')

    true_positive = 0
    true_negative = 0
    false_positive = 0
    false_negative = 0
    
    print('test started... ')
    for index,test in test_data.iterrows():
        
        own_telephone = test['own_telephone']
        credit_history = test['credit_history']
        housing = test['housing']
        purpose = test['purpose']
        job = test['job']
        employment = test['employment']
        personal_status = test['personal_status']
        property_magnitude = test['property_magnitude']
        _class = test['class']

        result = {}
        for col in table_class.columns: 
            p_test = 1.0
            p_test *= table_class[col].values[0]
            p_test *= table_own_telephone.loc[(table_own_telephone['class'] == col) 
                                    & (table_own_telephone['job'] == job),own_telephone].values[0]
            p_test *= table_credit_history.loc[(table_credit_history['class'] == col) 
                                    & (table_credit_history['own_telephone'] == own_telephone),credit_history].values[0]
            p_test *= table_housing.loc[(table_housing['class'] == col) 
                                    & (table_housing['property_magnitude'] == property_magnitude),housing].values[0]
            p_test *= table_purpose.loc[(table_purpose['class'] == col) 
                                    & (table_purpose['housing'] == housing),purpose].values[0]
            p_test *= table_job.loc[(table_job['class'] == col) 
                                    & (table_job['property_magnitude'] == property_magnitude),job].values[0]
            p_test *= table_employment.loc[(table_employment['class'] == col) 
                                    & (table_employment['job'] == job),employment].values[0]
            p_test *= table_personal_status.loc[(table_personal_status['class'] == col) 
                                    & (table_personal_status['housing'] == housing),personal_status].values[0]
            p_test *= table_property_magnitude.loc[(table_property_magnitude['class'] == col),property_magnitude].values[0]
            result[col] = p_test
        
        value = -1
        if result['bad'] != 0 and result['good'] != 0:
            value = result['bad']/(result['bad']+result['good'])

        if value >= 0.5:
            if _class == 'bad':
                true_positive += 1
            else:
                false_positive += 1
        else:
            if _class == 'good':
                true_negative += 1
            else:
                false_negative += 1

    accuracy = (true_positive+true_negative)/test_data.shape[0]
    tp_rate = true_positive/(true_positive+false_negative)
    tn_rate = true_negative/(false_positive+true_negative)

    print('results ', true_positive, true_negative, false_positive, false_negative, tp_rate, tn_rate, accuracy)

main()
