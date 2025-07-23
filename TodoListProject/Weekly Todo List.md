## Weekly Todo List Project

### Main Feature
- Add task by day
- History task
- Statistical Complete and do not complete in week 
  - statistic task completed
  - statistic task skip
  - percent completed by on Numbers of task in week

### Json Data Example
```json
{
  "monday": {
    "task": [
      {
        "task": "Todo 01",
        "estimate_time": "2 hours",  
        "start": "12:01 23-07-2025",
        "end": "14-01 23-07-2025",
        "status": "todo"
      }
    ]
  },
  "tuesday" : {
    "task": [
      {
        "task": "Todo 01",
        "estimate_time": "2 hours",  
        "start": "8:01 24-07-2025",
        "end": "14-01 24-07-2025",
        "status": "todo"
      },
      {
        "task": "Todo 02",
        "estimate_time": "2 hours",  
        "start": "12:01 23-07-2025",
        "end": "14-01 23-07-2025",
        "status": "todo"
      }
    ]
  },
  "wednesday" : {
    "tasks": [
      {
        "task": "Todo 01",
        "estimate_time": "",  
        "start": "",
        "end": "",
        "status": "todo"
      },
      {
        "task": "Todo 02",
        "estimate_time": "",  
        "start": "",
        "end": "",
        "status": "todo"
      }
    ]
  },
   "thursday" : {
    "task": []
  },
  "friday" : {
    "task": []
  },
  "saturday" : {
    "task": []
  },
  "sunday" : {
    "task": []
  }
}
```

- task (not null, not empty)
- estimate time: (can empty)
- start: (can empty)
- end: (can empty)
- status (not null, not empty)


### Status of Task
- todo (Just List)
- processing (is Doing)
- done (Really finished)
- skip (skip)