import requests


def import_gists_to_database(db, username, commit=True):
    """
    Your import_gists_to_database function will take three parameters:
    db: The database object to connect to
    username: The GitHub user whose gists we are going to retrieve
    commit (Optional, defaults to True): If True, automatically commit changes to database
    You are going to use the GitHub gists API to retrieve the gists of a given user, insert
    those gists into a database (schema may be found in the schema.sql file), and if commit is True,
    commit those changes to the database.
    """

    query = "INSERT INTO gists('github_id', 'html_url', 'git_pull_url', 'git_push_url', 'commits_url', \
    'forks_url', 'public', 'created_at', 'updated_at', 'comments', 'comments_url') \
    VALUES (:github_id, :html_url, :git_pull_url, :git_push_url, :commits_url, :forks_url, \
    :public, :created_at, :updated_at, :comments, :comments_url)"

    r = requests.get('https://api.github.com/users/{}/gists'.format(username))
    r.raise_for_status()

    gists_data = r.json()

    for gist in gists_data:
        db.execute(query, 
        {
            'github_id': gist['id'],
            'html_url': gist['html_url'],
            'git_pull_url': gist['git_pull_url'],
            'git_push_url': gist['git_push_url'],
            'commits_url': gist['commits_url'],
            'forks_url': gist['forks_url'],
            'public': gist['public'],
            'created_at': gist['created_at'],
            'updated_at': gist['updated_at'],
            'comments': gist['comments'],
            'comments_url': gist['comments_url']
        })
        
        if commit:
            db.commit()