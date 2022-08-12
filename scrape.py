import pandas as pd
import datetime

first_year = datetime.datetime.now().year - 3
last_year = datetime.datetime.now().year

combined_yearly_data = pd.DataFrame()

months_dict = {'JANUAR': '01', 'FEBRUAR': '02', 'MART': '03', 'APRIL': '04', 'MAJ': '05', 'JUN': '06', 'JUL': '07',
               'AVGUST': '08', 'SEPTEMBAR': '09', 'OKTOBAR': '10', 'NOVEMBAR': '11', 'DECEMBAR': '12'}

for i in range(first_year, last_year + 1):
    url = f'https://www.ipc.rs/statisticki_podaci/{i}/inflacija-merena-indeksom-potrosackih-cena-u-{i}-godini'
    dfs = pd.read_html(url)
    df = dfs[0]

    df_clean = df.droplevel(0, axis=1)
    df_clean = df_clean.iloc[:, :4]

    columns = [col for col in df_clean.columns]
    columns.remove('Mesec')
    df_clean[columns] = df_clean[columns] / 10

    new_cols = ['month', 'monthly_inflation', 'yearly_inflation', 'ytd_inflation']
    df_clean.columns = new_cols
    df_clean['month'] = str(i) + '.' + df_clean['month']
    combined_yearly_data = pd.concat([combined_yearly_data, df_clean])

combined_yearly_data['month'] = combined_yearly_data['month'].replace(months_dict, regex=True)
combined_yearly_data.reset_index(drop=True, inplace=True)
