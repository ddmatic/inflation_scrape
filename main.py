from scrape import combined_yearly_data
from oracle import *

rows = [tuple(row) for row in combined_yearly_data.values]

c = conn.cursor()

c.execute(oracle.delete_statement)
conn.commit()

c.executemany(oracle.insert_statement, rows)
conn.commit()

conn.close()
