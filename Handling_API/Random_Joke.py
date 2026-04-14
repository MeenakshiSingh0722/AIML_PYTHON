import requests

def fetch_random_joke_freeapi():
    url="https://api.freeapi.app/api/v1/public/randomjokes/joke/random"
    response=requests.get(url)
    data=response.json()

    if data["success"] and "data" in data:
        joke_data=data["data"]
        id=joke_data.get("id")
        content=joke_data.get("content")
        page=joke_data.get("page")
        return id, content ,page
    else :
        raise Exception("Failed to fetch  user data")

def main():
    try:
        id, content , page =fetch_random_joke_freeapi()
        print(f" id:{id}\n content: {content} \n page: {page}")
    except Exception as e:
        print(str(e))

if __name__ =="__main__":
    main()