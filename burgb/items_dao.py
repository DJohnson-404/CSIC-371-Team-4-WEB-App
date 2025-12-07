from sql_connection import get_sql_connection

def get_all_items(connection):

    cursor = connection.cursor()

    query = ("select items.item_id, items.name, items.unit_id, items.price_per_item, unit.unit_name "
    "from items inner join unit on items.unit_id = unit.unit_id")

    cursor.execute(query)

    response = []

    for (item_id, name, unit_id, price_per_item, unit_name) in cursor:
        response.append(
            {
                'item_id': item_id,
                'name': name,
                'unit_id': unit_id,
                'price_per_item': price_per_item,
                'unit_name': unit_name
            }
        )

    return response

def insert_new_item(connection, item):
    cursor = connection.cursor()
    query = ("Insert INTO items "
             "(name, unit_id, price_per_item)"
             "VALUES (%s, %s, %s)")
    
    data = (item['item_name'], item['unit_id'], item['price_per_item'])

    cursor.execute(query, data)
    connection.commit()

    return cursor.lastrowid


def delete_item(connection, item_id):
    cursor = connection.cursor()
    query = ("DELETE FROM items where item_id=" + str(item_id))
    cursor.execute(query)
    connection.commit()

    return cursor.lastrowid


if __name__ == '__main__':
    connection = get_sql_connection()
    # print(get_all_items(connection))
    #used to add and delete items from the sql database directly in the python code; example
    #shows an addition of baked potato, to remove an item from the database call the delete_item function followed by its item_id
    print(insert_new_item(connection, {
        'item_name': 'Baked Potato',
        'unit_id': '1',
        'price_per_item': 5.99
    }))
