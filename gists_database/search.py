from .models import Gist
from datetime import datetime

def search_gists(db_connection, **kwargs):
    """
    Your search_gists method should take a db_connection parameter (the database connection), 
    as well as two optional arguments:
        github_id
        created_at
    If no parameter is provided, all the gists in the database should be returned. 
    If public_id or created_at parameters are provided, you should filter your SELECT query based on them.
    """
    
    query = "SELECT * FROM gists "
    
    if not kwargs:
        return db_connection.execute(query).fetchall()
    
    for key,val in kwargs.items():
        if key == 'github_id':
            query += "WHERE github_id = :github_id"
            # data with given specifics retrieved in a tuple
            tup = db_connection.execute(query, {'github_id': val})
        elif key == 'created_at':
            query += "WHERE datetime(created_at) = :created_at"
            tup = db_connection.execute(query, {'created_at': val})
    # before returning, convert tup into Gist models or list of gist objects
    result = []
    for eachitem in tup:
        result.append(Gist(eachitem))
    return result

    
    """
    This project contains optional tests that you can just uncomment if you want an extra challenge. 
    Your task will be to extend the search_gists function to accept the following optional parameters:

        created_at__gt
        created_at__gte
        created_at__lt
        created_at__lte
        updated_at__gt
        updated_at__gte
        updated_at__lt
        updated_at__lte

    These parameters will be operating against the created_at and updated_at fields using 
    the corresponding comparison: gt means greater than, gte greater than or equal to, 
    lt less than, lte less than or equal to.

    That is, created_at__gt=datetime(2018, 1, 1) are all the Gists that were created 
    AFTER January 1st 2018. If we use created_at__gt, that’d also include the corresponding day.
    """
