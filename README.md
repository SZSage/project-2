# UOCIS322 - Project 2 #

Simon Zhao: simonz@uoregon.edu

This project uses the concepts and tools we've learned in project 0 and project 1 to build and deploy a simple Flask page server using Docker.

The Flask page server handles requests to check if any files exist within the `web/pages/` directory. If so, the server will transmit `200/OK` header along with the file content. If the file does not exist, it will display `404 - File not found!`.

In addition, if any illegal characters such as `~` or `..` are contained in the request, it will display `403 File is forbidden!`
