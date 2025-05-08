This is a simple python FastAPI project that logs user actions along with a timestamp. Users can send POST requests to record actions. They can also send GET requests to (a)get the latest 10 records (b)get specific
records based on action keyword (like assigned, uploaded, etc.). The logs are stored as dictionaries, and each entry includes the log number, the action performed and the exact time it was recorded. This project can
be extended with database for a more permanent storage and additional endpoints.
