# Data serving setup on AWS

1. open port 10000 and 8330 for communication
2. install hiveserver2, and make sure Hive is running properly
3. install pyhs2 library: pip install pyhs2
4. create a directory cgi-bin under the home of root: mkdir cgi-bin
5. copy HQL_SELECT.py to ~/cgi-bin folder (cp HQL*.py ~/cgi-bin/), and make it executable: chmod +x HQL_SELECT.py
6. as root, start hiveserver2: hive --service hiveserver2
7. as root, under the home directory (~), start Python CGI service: python -m CGIHTTPServer 8330
8. insert your AWS IP into line: var host = '<the AWS host ip>' of main.html;
9. query server is ready to accept request, and note:
  - hiveserver2 can only handle one query at time, sending a new one before the previous complete will cause issue
  - javascript runs asynchronously, thus please be cautious when sending AJAX query and make sure multiple queries (if necessary) are sent sequentially.
