# Authentication Setup for Task Management API

This document explains the authentication mechanism used in the Task Management API and how to test it.

## Authentication Type
We use **JWT (JSON Web Token)** authentication to secure API endpoints.

### Endpoints
1. **Token Obtain**  
   - URL: `/api/token/`
   - Method: `POST`  
   - Description: Returns an access token and a refresh token for valid credentials.

2. **Token Refresh**  
   - URL: `/api/token/refresh/`
   - Method: `POST`  
   - Description: Generates a new access token using the refresh token.

### Testing Authentication
1. **Obtain Tokens**:
   - Send a `POST` request to `/api/token/` with:
     ```json
     {
       "username": "your_username",
       "password": "your_password"
     }
     ```
   - Example Response:
     ```json
     {
       "access": "jwt_access_token_here",
       "refresh": "jwt_refresh_token_here"
     }
     ```

2. **Access Secured Endpoints**:
   - Use the `access` token in the `Authorization` header:
     ```
     Authorization: Bearer jwt_access_token_here
     ```
   - Example: `GET /api/tasks/` will now return data for authenticated users only.

3. **Refresh Token**:
   - Send a `POST` request to `/api/token/refresh/` with:
     ```json
     {
       "refresh": "jwt_refresh_token_here"
     }
     ```
   - Example Response:
     ```json
     {
       "access": "new_jwt_access_token_here"
     }
     ```

---



