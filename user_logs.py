from fastapi import FastAPI, Request
import datetime
from operator import itemgetter

app = FastAPI()

#sample user logs data
user_logs = [{"log_id":12,"user_action":"Started on Group project 2","log_time":"2025-05-08T19:12:19.155854"},
              {"log_id":11,"user_action":"Attended Celebratory meeting","log_time":"2025-05-08T19:10:55.187875"},
              {"log_id":10,"user_action":"Uploaded project report and presentation","log_time":"2025-05-08T19:03:05.174776"},
              {"log_id":9,"user_action":"Practiced the presentation for the project demo","log_time":"2025-05-08T19:02:39.686840"},
              {"log_id":8,"user_action":"Completed the project report","log_time":"2025-05-08T19:02:07.632504"},
              {"log_id":7,"user_action":"Prepared presentation notes","log_time":"2025-05-08T19:01:52.587355"},
              {"log_id":6,"user_action":"Assisted with creating the presentation","log_time":"2025-05-08T19:01:34.036911"},
              {"log_id":5,"user_action":"Attended group meeting to discuss project progress","log_time":"2025-05-08T19:01:09.754294"},
              {"log_id":4,"user_action":"Worked on individual task for project","log_time":"2025-05-08T19:00:37.529512"},
              {"log_id":3,"user_action":"Shared project document with team","log_time":"2025-05-08T19:00:19.469389"},
              {"log_id":2,"user_action":"Assigned project tasks to team members","log_time":"2025-05-08T18:59:50.743706"},
              {"log_id":1,"user_action":"Decided on project task deadlines","log_time":"2025-05-08T18:59:34.544833"}]

#returns the last 10 logs in descending order of log_time
@app.get("/logs")
async def read_root():
    sorted_logs = sorted(user_logs, key=itemgetter("log_time"), reverse=True)
    return sorted_logs[:10]

#returns the last 10 logs in descending order of log_time for a specific action
@app.get("/logs/{action}")
async def read_item(action: str):
    filtered_logs = []
    for log in user_logs:
        if action in log["user_action"]:
            filtered_logs.append(log)
    
    sorted_logs = sorted(filtered_logs, key=itemgetter("log_time"), reverse=True)
    return sorted_logs[:10]

#adds a new log entry to the user_logs list
@app.post("/log")
async def log_user_activity(request: Request):
    data = await request.json()
    print(data)
    user_action = data.get("user_action")
    log = {"log_id": len(user_logs) + 1,
           "user_action": user_action,
           "log_time": datetime.datetime.now().isoformat()
           }
    user_logs.append(log)
    return {"message": "Log added", "log": log}
