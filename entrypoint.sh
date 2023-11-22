#!/bin/bash

while true; do
  hostname=$(hostname)
  ip=$(hostname -i | awk '{print $1}')

  # Construct the HTML content
  html="<html><body>$ip<br/><br/>"

  # Add the commented lines to the HTML content
  html+="=-=-=-=-=-DEVOPS_TOOLS-=-=-=-=-<br/><br/>"
  html+="Hi there, good to see you!<br/><br/>"
  html+="Installed tools:<br/>$INSTALLED_TOOLS<br/><br/>"
  html+="**********<br/>To use the tools docker exec into the container/pod:<br/>docker exec -it deops_tools /bin/bash<br/>or<br/>kubectl exec -n namespace -it podname -- bash<br/>***********"
  html+="<br/>readme comming soon...<br/><br/>"
  html+="</body></html>"

  {

    echo -ne "HTTP/1.1 200 OK\r\nContent-Length: ${#html}\r\nContent-Type: text/html\r\n\r\n$html"

  } | nc -l -p 8888 -q 1 -N

  sleep 1
done
