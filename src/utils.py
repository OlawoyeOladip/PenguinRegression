from sklearn.impute import SimpleImputer
import pandas as pd   
def take_care_of_nan(df: pd.DataFrame, column: str) ->pd.DataFrame:
    strategy = "most_frequent" if df[column].dtype == 'object' else "median"
    
    imputer = SimpleImputer(strategy=strategy)
    df[column] = imputer.fit_transform(df[[column]]).ravel()
    assert len(df.columns) == 7, "Problem, the number of columns has increased Unexpectedly"
    
    return df