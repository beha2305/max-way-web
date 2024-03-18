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


def get_products():
    with connection.cursor() as cursor:
        cursor.execute(f"""
            select pp.*, pc."name" as category_name
            from product_product pp 
            inner join product_category pc on pc.id = pp.category_id 
        """)
        return dictfethall(cursor)
