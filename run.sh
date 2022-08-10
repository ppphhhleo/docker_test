docker build -t myimage .

docker run -d --name mycontainer -p 80:80 myimage

# docker stop mycontainer
# docker rm mycontainer
# docker container ls
# docker rmi myimage
# docker image l


