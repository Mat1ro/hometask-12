import json


def load_json() -> list[dict]:
    with open('posts.json', 'r', encoding='utf-8') as file:
        return json.load(file)


def get_by_word(word) -> list:
    result = []
    for post in load_json():
        if word.lower() in post['content'].lower():
            result.append(post)
    return result


def add_post(post: dict) -> dict:
    posts: list[dict] = load_json()
    posts.append(post)
    with open('posts.json', 'w', encoding='utf=8') as file:
        json.dump(posts, file)
    return post
