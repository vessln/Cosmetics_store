import time


def generate_unique_number():
    order_id = f"{str(int(time.time()))[::-1][:10]}"

    return order_id

