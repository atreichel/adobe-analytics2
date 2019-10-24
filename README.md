# Python wrapper for Adobe Analytics 2.0 API
Create requests for retrieving reports from the Adobe Analytics 2.0 API. Writing operations are not supported.

# Supported features
* User authenthication with the Adobe IMS
* JWT token generation
* Proxy support
* Create and download (multi-breakdown) reports

# Supported Endpoints
| Name              | Type   | Endpoint                   | Description                                                  |
|-------------------|--------|----------------------------|--------------------------------------------------------------|
| dimensions        | GET    | /dimensions                | Returns a list of dimension for a given report suite         |
| metrics           | GET    | /metrics                   | Returns a list of metrics for the given report suite         |
| reports           | POST   | /reports                   | Runs a report for the request in the post body               |
| segments          | GET    | /segments                  | Retrieve all segments                                        |
|                   | GET    | /segments/{id}             | Get a single segment                                         |
| users             | GET    | /users                     | Returns a list of users for the current user's login company |
|                   | GET    | /users/me                  | Get the current user                                         |


# Installation
1. Clone this repository
2. Create an Adobe [service account](https://console.adobe.io/home) with Developer or Admin rights
3. Create a private key
4. Add your account credentials and paths to `credentials/config`
5. `cd` into the repository folder
6. Run `pip install -e .`

# Useful links:
* [Analytics API Reports User Guide](https://www.adobe.io/apis/experiencecloud/analytics/docs.html#!AdobeDocs/analytics-2.0-apis/master/reporting-guide.md)
* [Swagger UI](https://adobedocs.github.io/analytics-2.0-apis/)
* [adobeio-auth](https://github.com/AdobeDocs/adobeio-auth/tree/master)
* [analytics-2.0-apis](https://github.com/AdobeDocs/analytics-2.0-apis)
