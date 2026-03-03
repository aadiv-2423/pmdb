import requests as reqs                                                                                             # Importing the reqs to make requests.get() easier

url = "https://api.themoviedb.org/3/search/movie?include_adult=false&language=en-US&page=1"

def search_movie(title): 
    response = reqs.get(url, params={"api_key": "", "query": title})                # Laying out the request by inputting URL, API Key (for access to TMDB) and test search query
    response_dict = response.json()                                                                         # Converts JSON response into a py dict so we can use it like regular py data
    results = response_dict ["results"]                                                                     # Accessing the results key from the dict (which contains the movies)
    return results [:2]                                                                                     # Line to request the top two results to the query, which would most likely be the relevant ones
