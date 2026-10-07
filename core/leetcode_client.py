import httpx

URL = "https://leetcode.com/graphql"
queryString = """
query updateSubmissions($username: String!, $limit: Int!) {
    recentSubmissionList(username: $username, limit: $limit) {
        title
        titleSlug
        timestamp
    }
}
"""
def getRecentSubmissions(username: str, limit: int = 5):
    #{Key, Value} = {"query": queryString, "variables": {"username": username, "limit": limit}}
    #queryString = String defined above
    #variables = Nested dictionary passing function arguments :
    #{"username": username, "limit: limit}
    payLoad = {
            "query": queryString,
            "variables": {
                "username": username,
                "limit": limit
                }
            }

    #Metadata sent with HTTP request, tells Leetcode & Cloudflare how to interpret request and who is making the request.
    headers = {
            "Content-Type": "application/json", #Tells LeetCode server that the incoming format is JSON
            "Origin" : "https://leetcode.com", #
            "Referer": "https://leetcode.com", #Tells GraphQL that requests are originating from leetcode.com
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" #Tells leetcode request is originating from a web browser.
            }

    try:
        #Parameters : httpx.post() 
        #queryString
        #json=payLoad : Automatically converts dictionary to JSON formatted byte string
        #headers=headers : Passes headers, functionality specified at dict definition^^
        #timeout=10.0 : Prevents post call from hanging indefinitely in the event of service failure
        response = httpx.post(URL, json=payLoad, headers=headers, timeout=25.0)
    
        response.raise_for_status() #Handles 404, 403, and 500 errors

        data = response.json()

        if "errors" in data:
            return None
        
        output = data["data"]["recentSubmissionList"]
        return output
        ##
        #print("HTTP Status:", response.status_code) #Testing
        ##

    except httpx.HTTPError as exc:
        print(f"Network error: {exc}") #Logs errors not handled above; FIXME: Reroute these errors to a log
        return None

##
for submission in getRecentSubmissions("ramosnick"): #Testing
    print(submission)
##

