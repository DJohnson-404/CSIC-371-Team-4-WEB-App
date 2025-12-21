from datetime import datetime
from sql_connection import get_sql_connection

def insert_order(connection, order):
    cursor = connection.cursor()

    # 1. Insert the main order record
    order_query = ("INSERT INTO orders "
                   "(customer_name, total, datetime)"
                   "VALUES (%s, %s, %s)")
    order_data = (order['customer_name'], order['grand_total'], datetime.now())

    cursor.execute(order_query, order_data)
    order_id = cursor.lastrowid # Get the ID of the order we just created

    # 2. Insert the order details (the specific items)
    order_details_query = ("INSERT INTO order_details "
                           "(order_id, item_id, quantity, total_price)"
                           "VALUES (%s, %s, %s, %s)")

    order_details_data = []
    for order_detail_record in order['order_details']:
        order_details_data.append([
            order_id,
            int(order_detail_record['item_id']), # Changed from product_id to item_id
            float(order_detail_record['quantity']),
            float(order_detail_record['total_price'])
        ])
    
    # Execute multiple inserts at once
    cursor.executemany(order_details_query, order_details_data)

    connection.commit()

    return order_id

def get_all_orders(connection):
    cursor = connection.cursor()
    # Simple query to get history
    query = ("SELECT * FROM orders")
    cursor.execute(query)
    response = []
    for (order_id, customer_name, total, dt) in cursor:
        response.append({
            'order_id': order_id,
            'customer_name': customer_name,
            'total': total,
            'datetime': dt,
        })
    cursor.close()
    return response