## Python TODO API

This project is a simple API for a TODO application, written in Python3.

I am using FastAPI for my framework choice, as it is popular within the community and it has amazing documentation.

There is a Makefile included to interact with the application:

To start the application, run:

`make serve` - This will spin up the Docker containers for the server and the database, and then the application can be accessed locally on port 8000.

The paths for the application are:

`GET /task/{task_id}` - gets a single task

`GET /tasks/?{search_params}` - gets task by different search terms, the terms are matching the tasks schema in the DTO's, so to find different tasks, users can search by `title` , `description` , `completed` and any combination of these params

`POST /task/` - creates a new task from the request body, standard format for creating a new task is:

```
{
    "title": "my task title",
    "description": "very interesting description",
    "completed": true
}
```

Note: `description` can be omitted, as it is nullable, and if `completed` is not specified, tasks are created as uncompleted by default.

`PATCH /task/{task_id}` - updates a task, with the same body format as in the creating a new task route

`PATCH /task/complete/{task_id}` - marks a task as completed

`DELETE /task/{task_id}` - deletes a task


There is a Postman collection file included in this repo that already has these routes defined.

To stop the application from running:

`make stop`

And to run the e2e tests:

`make test`