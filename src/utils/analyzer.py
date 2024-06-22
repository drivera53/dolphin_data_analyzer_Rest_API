import statistics

def get_av_9_likes(user_posts):
    user_posts.sort(key = lambda x:x.timestamp)
    user_posts_count = len(user_posts)
    if user_posts_count > 8:
        user_posts_count = 9
    user_posts_likes = [likes.likes_count for likes in user_posts]
    user_posts_likes = user_posts_likes[:user_posts_count]
    return int(statistics.mean(user_posts_likes)), user_posts[0].timestamp

def process_Ig_Users_Posts(all_IgUsers, all_IgPosts):

    resp = []
    for ig_user in all_IgUsers:
        curr_user = {
                        "id": ig_user.id,
                        "username": ig_user.username,
                        "full_name": ig_user.full_name,
                        "last_updated": ig_user.last_updated
                    }
        resp.append(curr_user)
    
    for i, ig_user in enumerate(resp):
        user_posts = [post for post in all_IgPosts if post.user_id == ig_user["id"]]
        user_posts_count = len(user_posts)
        resp[i]["posts"] = user_posts_count
        if not user_posts_count:
            resp[i]["average_likes"] = 0
            resp[i]["most_recent_post"] = ig_user["last_updated"]
        else:
            resp[i]["average_likes"], resp[i]["most_recent_post"] = get_av_9_likes(user_posts) 
    
    return resp
