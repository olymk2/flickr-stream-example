# flickr-stream-example
Example django application that pulls photos from flickr

To get started checkout the project to your machine.

    git clone https://github.com/olymk2/flickr-stream-example.git


The simplest way to setup this site locally is to use docker and run the commands below.

    sudo docker build -t flickr-example .
    sudo docker run -p 8000:8000 -i -t flickr-example /bin/bash

Once running you can run docker ps and check the port forwarding shows something like this 0.0.0.0:8000->8000/tcp
then connect through you browser to 127.0.0.1:8000.

Alternatively you can setup a virtualenv and use pip, this is untested but these should be the required dependencies.

    pip install django==1.7.6
    pip install cjson==1.1.0

Notes
* This infinite scroll plugin is a disaster, it seems quite buggy. https://github.com/fredwu/jquery-endless-scroll.
* I do not have IE or safari availble to test with so can not confirm they look and work correctly.
* I have put in a screenshot just incase.

The main files are in these folders.
    flickr_stream/templates
    flickr_stream/static
    flickr_stream/fps
The rest is django boilerplate setup.
