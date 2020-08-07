
#Pre-Requisites
#Install docker and start the docker service

#Command to build the docker image from the source
docker build . --tag=enerman:django

#Start the container
#Make sure 8000 port is available on the host, else available tcp port 
docker run --name django_app --publish 8000:8000 enerman:django

#On your browser navigate to the url http://<host-ip>:8000/devices


#Stop the container
docker stop django_app
docker rm django_app 
