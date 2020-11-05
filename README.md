# Assignment 3 - Data Pipeline with Docker & Kubernetes
## Team 14: Jacob Stallings & Quinton Chudik  

This README contains the steps needed to run the data pipeline with the Assignment 3 configuration.
1. Run Vagraant Up to start everything up, from there ansible will take over.
2. Once the vms have started up, you must ssh into VM2 and create the private registry then build and tag and push all the neccessary docker images (besides consumer)
3. Once the images are ready you can start up Kubernetes on VM2 and then connect VM3 with the command given
4. Then using the provided yaml files you start up the zookeeper then the brokers (the brokers yaml's must be edited to add the zookeeper's cluster IP)
5. Then start up CouchDB using its yaml file
6. Then run the bootstrap command from a seperate VM to create the topics bin/kafka-topics.sh --create --topic utilization1 --bootstrap-server 129.114.25.96:30000 (we did this and then the same command but with utilization2 from where we ran one of the producers)
7. Finally, build, tag, and push the consumer docker image then start the consumer job using the yaml and run producers from seperate VMs (the consumer code must have the proper IP for the CouchDB cluster IP)
8. We can then check to see if it worked by running curl -X GET http://admin:password1@129.114.25.96:30005/assignment3/_all_docs?include_docs=true
