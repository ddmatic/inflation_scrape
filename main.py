from scrape import combined_yearly_data
from oracle import *

rows = [tuple(row) for row in combined_yearly_data.values]

c = conn.cursor()

c.execute(delete_statement)
conn.commit()

c.executemany(insert_statement, rows)
conn.commit()

conn.close()