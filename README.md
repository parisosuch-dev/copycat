# Copy Cat
Your favorite logging api 😺

## Resources
- https://blog.devgenius.io/token-authentication-in-django-rest-framework-9e6a7f97efa0

## TODO

- [x] make sure there are no repeats of project names per user
- [x] make sure there are no repeats of channel names per project per user
- [ ] create /log/ endpoint for log entries
    - [ ] if there is no channel when they send a POST, create that channel
    - [ ] if there is no project when they send a POST, return err
