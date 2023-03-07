# 0x0B. Redis basic

## Resources

### **Read or watch:**

- [Redis commands](https://redis.io/commands/)
- [Redis python client](https://redis-py.readthedocs.io/en/stable/)
- [How to Use Redis With Python](https://realpython.com/python-redis/)
- [Redis Crash Course Tutorial](https://www.youtube.com/watch?v=Hbt56gFj998)

## Learning Objectives

- Learn how to use redis for basic operations
- Learn how to use redis as a simple cache

## **Install Redis on Ubuntu 18.04**

    $ sudo apt-get -y install redis-server
    $ pip3 install redis
    $ sed -i "s/bind .*/bind 127.0.0.1/g" /etc/redis/redis.conf

## **Use Redis in a container**

        $ docker run -p 6379:6379 -d redis:latest
        $ docker exec -it <container_id> bash
        $ redis-cli

Redis server is stopped by default - when you are starting a container, you should start it with: service redis-server start

[functools.wraps](https://docs.python.org/3.7/library/functools.html#functools.wraps)
