import pandas as pd

def ReadData(url: str) -> pd.DataFrame: 
    """    This function downloads the data from a GoogleTable sheet with the given link and transformes them into a csv and then reads them in into a pd.DataFrame

    Args:
        url (str): 

    Returns:
        pd.DataFrame: _description_
    """
    url_read = url.replace('/edit#gid=', '/export?format=csv&gid=')

    df = pd.read_csv(url_read, on_bad_lines='skip')

    return df

df = ReadData('https://docs.google.com/spreadsheets/d/1c5eXRyP4uLSDKJ_1PHlx48nZ8wQ06mUr1Ayrty-kfDg/edit#gid=0')
print(df.head(10))