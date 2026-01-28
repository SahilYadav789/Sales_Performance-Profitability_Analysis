from io import StringIO
import pandas as pd

data = '''Order_ID,Date,Product,Category,Quantity,Price
1001,2024-01-05,Laptop,Electronics,1,55000
1002,2024-01-07,Mobile,Electronics,2,20000
1003,2024-01-10,Headphones,Accessories,3,2000
1004,2024-02-03,Laptop,Electronics,1,55000
1005,2024-02-10,Mobile,Electronics,1,20000
1006,2024-02-15,Keyboard,Accessories,2,1500
1007,2024-03-01,Mobile,Electronics,3,20000
1008,2024-03-05,Laptop,Electronics,2,55000
1009,2024-03-10,Mouse,Accessories,4,800
1010,2024-03-15,Headphones,Accessories,1,2000'''

def get_data():
    df = pd.read_csv(StringIO(data))
    return df

get_data()

product_data = {
    "Product": ["Laptop", "Mobile", "Headphones", "Keyboard", "Mouse"],
    "Brand": ["Dell", "Samsung", "Boat", "Logitech", "HP"],
    "Cost_Price": [42000, 15000, 1200, 900, 400]
}

def get_product_df():
    product_df = pd.DataFrame(product_data)
    return product_df

get_product_df()
