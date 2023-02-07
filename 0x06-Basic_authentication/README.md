# 0x06. Basic authentication :snake:

Background Context

In this project, you will learn what the authentication process means and implement a Basic Authentication on a simple API.

In the industry, you should not implement your own Basic authentication system and use a module or framework that doing it for you (like in Python-Flask: [Flask-HTTPAuth](https://flask-httpauth.readthedocs.io/en/latest/)). Here, for the learning purpose, we will walk through each step of this mechanism to understand it by doing.

## Resources

**Read or watch:**

- [REST API Authentication Mechanisms](https://www.youtube.com/watch?v=501dpx2IjGY)
- [Base64 in Python](https://docs.python.org/3.7/library/base64.html)
- [HTTP header Authorization](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Authorization)
- [Flask](https://palletsprojects.com/p/flask/)
- [Base64 - concept](https://en.wikipedia.org/wiki/Base64)

## General

- What authentication means
- What Base64 is
- How to encode a string in Base64
- What Basic authentication means
- How to send the Authorization header

Download and start your project from this [archive.zip](https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/misc/2020/11/ec2f874b061bd3a2915949f081f4f5f055104f20.zip?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20230207%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20230207T014125Z&X-Amz-Expires=345600&X-Amz-SignedHeaders=host&X-Amz-Signature=f1bfab92390c3a45941cf3304bca4af2496a624305e36c1bf45d6dc96f660c36)

In this archive, you will find a simple API with one model: User. Storage of these users is done via a serialization/deserialization in files.

**Setup and start server**

    bob@dylan:~$ pip3 install -r requirements.txt
    ...
    bob@dylan:~$
    bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 python3 -m api.v1.app
    * Serving Flask app "app" (lazy loading)
    ...
    bob@dylan:~$

**Use the API (in another tab or in your browser)**

    bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/status" -vvv
    *   Trying 0.0.0.0...
    * TCP_NODELAY set
    * Connected to 0.0.0.0 (127.0.0.1) port 5000 (#0)
    > GET /api/v1/status HTTP/1.1
    > Host: 0.0.0.0:5000
    > User-Agent: curl/7.54.0
    > Accept: */*
    >
    * HTTP 1.0, assume close after body
    < HTTP/1.0 200 OK
    < Content-Type: application/json
    < Content-Length: 16
    < Access-Control-Allow-Origin: *
    < Server: Werkzeug/1.0.1 Python/3.7.5
    < Date: Mon, 18 May 2020 20:29:21 GMT
    <
    {"status":"OK"}
    * Closing connection 0
    bob@dylan:~$
