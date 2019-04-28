# Personal Blog flask App
#### This is a Python web application using Flask framework and Postgresql, 2019
#### By **[Collins kipkemoi](https://github.com/kipkemoimayor)**
## Description
This is a Personal blog web application developed using flask framework and python core, Its a platform where a write can post anything or any topic, The topic are saved on a Database where any user who accesses the application can read the blogs and either comment on them or make an email subscription to get a notification everytime a blog is posted.
## Setup/Installation Requirements
* A PC mainly with an Operating system.
* Python3.6 or later is installed in your PC.
* Postgresql installed
* clone the directory into your local machine
* navigate to the cloned folder by `cd Blog_App`
* run `source virtual/bin/activate`
* pip install `requirements.txt`
* run this command on terminal `chmod +x start.sh`
* run `./start.py`
* The application should work
## Known Bugs
NO known bugs as at the moment please reach to us if you see any.
## Behavior Driven Development

| __Behavior__  | __Input example__ | __Output example__ |
| ------------- | ----------------- | ------------------ |
| The user should be able to view all Blogs  | "https://www.com"   | Blogs  |
| The user should read the full article of a blog  | command | all blog view |
| The User should be able to either view or leave a comment | blogs | comments |
| The user should be able to get emails notification once they comment | /comment | email notification |
| The application should restrict deletes of blogs to blog writers | view | hidden to normal users |
| The  writers should be able to delete a blog when necessary  | delete | true/false |
| The writers should be able to register and login into the application  | register/login | true |
| The application should restrict any unauthorized user access to the application | login | not a member |
| The application should logout the writers when prompted | logout | True |


## Technologies Used
## main languages used are
* Python
* Material design
* flask
* JavaScript/jquery
* CSS
* PostgreSQL Database

## Support and contact details
get me at collinskipkemoi24@gmail.com
### License
*License is under MIT 2019*
Copyright (c) 2019 **collins kipkemoi**
This software is free to use and distribute, Therefore all rights and given to any user to modify and either use for Commercial purpose or local purpose.
