import pandas as pd

def check_user_exist(email,cnxn):
    query = 'select from user cred where email is '
    df = pd.read_sql_query(query,cnxn)
    return df.shape[0]

def signupdata(firstname,lastname,email,password):
    query = str(firstname) + str(lastname) + str(email) + str(password)
    print(query)
    return query