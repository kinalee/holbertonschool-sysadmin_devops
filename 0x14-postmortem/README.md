## Postmortem for Apache2 disconnection

#### Issue Summary
The outage broke out approximately at 5:00am(PST) On Feb., 20th, 2017 for 1 hours. While trying to `curl` port 8080 mapped to Docker container port 80, two errors `curl: (56) Recv failure: Connection reset by peer` and `curl: (52) Empty reply from server` were returned instead of the root page. The issue was caused because Apache2 was not running properly, and 37% of users experienced inconvenience due to the outage. The team found the issue about 40 mintues after the problem occured, and fixed the issue by starting(restarting) Apache2.

#### Timeline
- 5:02am(PST) - outage detected and reported by user complaint
- 5:08am(PST) - team jumped in to investigate cause, started with checking everything is running properly on the website
- 5:40am(PST) - while inspecting the configuration files, spotted that Apache2 was not running on the server
- 5:43am(PST) - created a bash script that restarts Apache and ran it on the server
- 5:50am(PST) - ran the script on Docker container to test and made sure everything is ready to be reset
- 5:53am(PST) - server started running properly again

#### Root cause and Resolution
The root cause was that server was trying to `curl` a page that was run by Apache2, while Apache2 was not properly running on the server. There was a test that required Nginx to be run earlier the day, and Apache2 was temporarily stopped since the test needed to use the same port but it was never restarted afterwards. The problem was solved after running the bash script that restart the service.


#### Corrective and Preventative Measures
The team created a bash script that restarts Apache2 service so it can be used when same issue occurs in the future. We could prevent the same kind of problem by running test on a seperate server or on a Docker container.
