from django.db import connection

def dictfethall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

def dictfetchone(cursor):
    row = cursor.fetchone()
    if row is None:
        return False
    columns = [col[0] for col in cursor.description]
    return dict(zip(columns, row))


def get_products(**kwargs):
    with connection.cursor() as cursor:
        if kwargs.get("category_id"):
            where = f"""where pc.id = {kwargs.get("category_id")}"""
        else:
            where = ''
        cursor.execute(f"""
            select pp.*, pc."name" as category_name
            from product_product pp 
            inner join product_category pc on pc.id = pp.category_id 
            {where}
        """)

        return dictfethall(cursor)