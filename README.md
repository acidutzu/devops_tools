# devops_tools
http://localhost:5000 or 8888 
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


### to build the project
```docker build -t devops_tools:1.7 .```

### to deploy de project
```docker run -d -p 5000:5000 -p 8888:8888 --name devops_tools devops_tools:1.7```

### to access the project

http://localhost:5000

and or

http://localhost:8888
