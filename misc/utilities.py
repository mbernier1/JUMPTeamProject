def read_sql(name: str) -> str:
    with open(f"./queries/{name}.sql", 'r') as query:
        return query.read()

