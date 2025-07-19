import requests

url = "https://cricbuzz-cricket.p.rapidapi.com/matches/v1/recent"

headers = {
	"x-rapidapi-key": "ff678dde7cmsh5f7ba20e7acca27p1a9ef3jsnde5ef7ca8b21",
	"x-rapidapi-host": "cricbuzz-cricket.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

print(response.json())