import requests

baseUrl = "https://jsonplaceholder.typicode.com/"

def get_posts():
    url = baseUrl + "posts?_limit=5"
    response = requests.get(url)
    return response.json()

def get_users():
    url = baseUrl + "users?_limit=5"
    response = requests.get(url)
    return response.json()

def create_post(body = None, title = None):
    url = baseUrl + "posts"
    data = {
        "body": body,
        "title": title,
        "userId": 1
    }
    response = requests.post(url, data)
    return response.json()



def main():

    isValid = False

    while not isValid:
        # menu to choose what to do (getPost, getUsers, createPost)
        print("=====================================")
        print("1. Get Posts")
        print("2. Get Users")
        print("3. Create Post")
        print("=====================================")
        choice = input("Enter your choice: ")
        match choice:
            case "1":
                isValid = True
                posts = get_posts()
                print("Posts:")
                for post in posts:
                    print("Post N°"+str(post['id'])+": "+post['title'])
            case "2":
                isValid = True
                print("Users:")
                users = get_users()
                for user in users:
                    print("User N°"+str(user['id'])+": "+user['name'])
            case "3":
                isValid = True
                print("Create post:")
                body = input("Enter body:")
                title = input("Enter title:")
                post = create_post(body, title)
                print("Id du nouveau post: " + str(post['id']))
            case _:
                print("Invalid choice")

main()