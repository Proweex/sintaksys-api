# SintakSys (Cloud Computing path)
## Overview

We create API server to communicate with mobile app using managed instance groups and cloud load balancer to help with the autoscale and auto balancing traffic when needed.

## Architecture

![SintakSys Architecture](https://cdn.discordapp.com/attachments/512833723255750676/851625189859131422/Design_Arsitektur.jpg)

- We decided to use VM instance and call the trained machine learning model directly inside the VM instance and serve it to the Internet with flask and gunicorn server
- For saving budget purpose, we just using one managed instance group in us-central1 and will add more later if needed
