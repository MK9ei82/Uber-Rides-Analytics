from graphviz import Digraph

# Create a new Graphviz Digraph
dot = Digraph('ERD', filename='erd_diagram', format='png')

# Set graph attributes to use HTML-like labels
dot.attr(rankdir='LR', size='12')

# Define nodes with table formatting
def add_table_node(dot, table_name, columns):
    label = f"""<
    <TABLE BORDER="1" CELLBORDER="1" CELLSPACING="0">
        <TR><TD BGCOLOR="lightblue"><B>{table_name}</B></TD></TR>
        {''.join([f'<TR><TD>{col}</TD></TR>' for col in columns])}
    </TABLE>
    >"""
    dot.node(table_name, label=label, shape="plaintext")

# Define tables
tables = {
    "fact_table": [
        "<B>PK</B> trip_id", 
        "<B>FK</B> datetime_id",
        "<B>FK</B> passenger_count_id",
        "<B>FK</B> trip_distance_id",
        "<B>FK</B> rate_code_id",
        "store_and_fwd_flag",
        "<B>FK</B> pickup_location_id",
        "<B>FK</B> dropoff_location_id",
        "<B>FK</B> payment_type_id",
        "fare_amount", "extra", "mta_tax",
        "tip_amount", "tolls_amount",
        "improvement_surcharge", "total_amount"
    ],
    "datetime_dim": [
        "<B>PK</B> datetime_id", 
        "tpep_pickup_datetime",
        "pick_hour", "pick_day", "pick_month", 
        "pick_year", "pick_weekday",
        "tpep_dropoff_datetime", "drop_hour", 
        "drop_day", "drop_month", 
        "drop_year", "drop_weekday"
    ],
    "passenger_count_dim": ["<B>PK</B> passenger_count_id", "passenger_count"],
    "trip_distance_dim": ["<B>PK</B> trip_distance_id", "trip_distance"],
    "rate_code_dim": ["<B>PK</B> rate_code_id", "RatecodeID", "rate_code_name"],
    "payment_type_dim": ["<B>PK</B> payment_type_id", "payment_type", "payment_type_name"],
    "pickup_location_dim": ["<B>PK</B> pickup_location_id", "pickup_latitude", "pickup_longitude"],
    "dropoff_location_dim": ["<B>PK</B> dropoff_location_id", "dropoff_latitude", "dropoff_longitude"]
}

# Add nodes
for table_name, columns in tables.items():
    add_table_node(dot, table_name, columns)

# Define relationships
relationships = [
    ("fact_table", "datetime_dim"),
    ("fact_table", "passenger_count_dim"),
    ("fact_table", "trip_distance_dim"),
    ("fact_table", "rate_code_dim"),
    ("fact_table", "pickup_location_dim"),
    ("fact_table", "dropoff_location_dim"),
    ("fact_table", "payment_type_dim")
]

# Add edges
for source, target in relationships:
    dot.edge(source, target)

# Render the graph
dot.render(view=True)
