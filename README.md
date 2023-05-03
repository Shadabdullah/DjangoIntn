To use the API, you will need to have a server running with the backend structure and endpoints implemented. Here are the steps you can follow to use the API:

    Clone the repository to your local machine.

    Install the required dependencies by running pip install -r requirements.txt.

    Run the server by running python manage.py runserver.

    You can now make requests to the API endpoints using a tool like Postman or cURL.

    a. To get all works, make a GET request to /api/works. You will receive a response containing all the works with their respective links and types.

    b. To get works by artist name, make a GET request to /api/works?artist=[Artist Name]. Replace [Artist Name] with the name of the artist you want to search for. You will receive a response containing all the works by that artist.

    c. To get works of a specific type, make a GET request to /api/works?work_type=[Work Type]. Replace [Work Type] with the type of work you want to search for, e.g., "YouTube", "Instagram", or "Other". You will receive a response containing all the works of that type.

    d. To register a new user, make a POST request to /api/register with the username and password in the request body. For example:

    arduino

    POST /api/register
    {
      "username": "testuser",
      "password": "123123"
    }

    You will receive a response containing the user ID, username, and a masked password for security reasons.

That's it! You can now use the API to retrieve works and register new users.