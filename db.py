import psycopg2


def insert_new_product(
    name: str, ts_code: int, sf_code: int, qty: int, pack_size: str, description: str
):
    cursor.execute(
        "insert into products (name, ts_code, ts_price, sf_code, sf_price, qty, pack_size, description) values (%s, %s, %s, %s, %s, %s, %s, %s)",
        (name, ts_code, 0, sf_code, 0, qty, pack_size, description),
    )


conn = psycopg2.connect(
    database="trade-scout", host="localhost", user="dan", password="Leinad", port="5432"
)

cursor = conn.cursor()

cursor.execute(
    "create table if not exists products(id serial, name varchar(255), ts_code int, ts_price int, sf_code int, sf_price int, description varchar(255));"
)

insert_new_product("ptfe", 63859, 35444, 1, "10", "Plumbers tape")

conn.commit()

cursor.execute("select * from products")
print(cursor.fetchall())

conn.close()
