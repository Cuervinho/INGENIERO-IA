# services/query_builder.py

def apply_org_filter(query: str):
    if "WHERE" in query.upper():
        return query + " AND a.id_organizacion = ?"
    else:
        return query + " WHERE a.id_organizacion = ?"