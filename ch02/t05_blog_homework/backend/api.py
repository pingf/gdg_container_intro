from blog import query_all

def all():
    posts = query_all()
    return [
        {
            'id': post.id,
            'key': post.key,
            'title': post.title,
            'author': post.user,
            'content': post.content
        } for post in posts
    ]


