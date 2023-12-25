# Copy Cat
Your favorite logging api 😺

## Resources
- https://blog.devgenius.io/token-authentication-in-django-rest-framework-9e6a7f97efa0

## TODO

- [x] make sure there are no repeats of project names per user
- [x] make sure there are no repeats of channel names per project per user
- [x] create /log/ endpoint for log entries
    - [x] if there is no channel when they send a POST, create that channel
    - [x] if there is no project when they send a POST, return err
- [x] create end points
    - [x] GET log/project
    - [x] GET log/project/channel
    - [x] GET log/project/channel/?start={date}&end={date}
- [x] change all HttpRequest objects to DRF Request objects. This is the correct type.
- [ ] change all error responses to be "error" instead of "message" in the json.
