# django_intern_assignment

1. Registet API endpoint : http://127.0.0.1:8000/api/register/

This endpoint is for registering the user, it accepts user's username, password and the clients name. The client is related to the User model using Foreign key relation.

2. http://127.0.0.1:8000/api/artists/

This endpoint accepts the artists name link of their work and the platformm of their work such as Youtube, Instagram or Others from a dropdown list of choices. The artist can be searched by their name using the filter search bar. This is implemented using SearchFilter from rest_frameworks.filters. 

3. http://127.0.0.1:8000/api/works/

This API endpoint displays list of all the works and their links.
