
def is_post_liked(like_set, current_user):
    for like in like_set:
        if like.owner == current_user:
            return like
    return False
