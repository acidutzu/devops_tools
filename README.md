# devops_tools
http://localhost:8888 
will display pod ip and some other info:

172.17.0.2

  =-=-=-=-=-DEVOPS_TOOLS-=-=-=-=-  

Hi there, good to see you!
  Installed tools:
 python3 py3-pip iputils-ping net-tools netcat-openbsd git vim nano curl wget bind-tools jq bash  

********** 
To use the tools docker exec into the container/pod:

```docker exec -it deops_tools /bin/bash```
 or 
```kubectl exec -n namespace -it podname -- bash```
