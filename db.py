import psycopg2
import db_credentials

def update_price(id: int, ts_price: int, sf_price: int):
    conn = psycopg2.connect(
        database="trade-scout",
        host="localhost",
        user=db_credentials.user,
        password=db_credentials.password,
        port="5432",
    )

    cursor = conn.cursor()

    cursor.execute(
        "update products set ts_price = %s, sf_price = %s where id = %s",
        (ts_price, sf_price, id),
    )

    conn.commit()
    conn.close()


def insert_new_product(
    name: str, ts_code: int, sf_code: int, qty: int, pack_size: str, description: str
):
    conn = psycopg2.connect(
    database="trade-scout", host="localhost", user=db_credentials.user, password=db_credentials.password, port="5432"
    )

    cursor = conn.cursor()

    cursor.execute(
        "insert into products (name, ts_code, ts_price, sf_code, sf_price, qty, pack_size, description) values (%s, %s, %s, %s, %s, %s, %s, %s)",
        (name, ts_code, 0, sf_code, 0, qty, pack_size, description),
    )

    conn.commit()
    conn.close()

def get_all_products() -> list:
    conn = psycopg2.connect(
        database="trade-scout",
        host="localhost",
        user=db_credentials.user,
        password=db_credentials.password,
        port="5432",
    )

    cursor = conn.cursor()

    cursor.execute("select * from products")
    rows = cursor.fetchall()

    conn.commit()
    conn.close()

    return rows


def create_products_table():
    conn = psycopg2.connect(
    database="trade-scout", host="localhost", user=db_credentials.user, password=db_credentials.password, port="5432"
    )

    cursor = conn.cursor()

    cursor.execute(
        "create table if not exists products(id serial, name varchar(255), ts_code int, ts_price int, sf_code int, sf_price int, qty int, pack_size varchar(20), description varchar(255));"
    )
    conn.commit()
    conn.close()

def main():
    get_all_products()
    update_price(1, 100, 100)
    get_all_products()


if __name__ == "__main__":
    main()
