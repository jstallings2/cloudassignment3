
#
#
# Author: Aniruddha Gokhale
# CS4287-5287: Principles of Cloud Computing, Vanderbilt University
#
# Created: Sept 6, 2020
#
# Purpose:
#
#    Demonstrate the use of Kafka Python streaming APIs.
#    In this example, demonstrate Kafka streaming API to build a consumer.
#

import os   # need this for popen
import time # for sleep
import json
from kafka import KafkaConsumer  # consumer of events
import sys, getopt
import pycouchdb

def main(argv):

    try:
        opts, args = getopt.getopt(argv,"b:h:")
    except getopt.GetoptError:
        print('Invalid option for consumer.py')
        sys.exit(2)

    # Set up server/db
    host = 'localhost:5984'
    boostrap_server= "129.114.25.52:9092"
    
    for opt, arg in opts:
        if opt == '-b':
            boostrap_server = arg
        if opt == '-h':
            host = arg

    print("Bootstrap server: ",boostrap_server)
    print("Host IP: ", host)

    base_url = 'http://admin:password1@' + host
    print("Base url: ", base_url)
    
    couch = pycouchdb.Server(base_url)

    db = couch.create('assignment3')

    # We can make this more sophisticated/elegant but for now it is just
    # hardcoded to the setup I have on my local VMs

    # acquire the consumer
    # (you will need to change this to your bootstrap server's IP addr)
    consumer = KafkaConsumer (bootstrap_servers=boostrap_server)

    # subscribe to topic
    consumer.subscribe (topics=["utilization1", "utilization2"])

    # we keep reading and printing
    for msg in consumer:
        # what we get is a record. From this record, we are interested in printing
        # the contents of the value field. We are sure that we get only the
        # utilizations topic because that is the only topic we subscribed to.
        # Otherwise we will need to demultiplex the incoming data according to the
        # topic coming in.
        #
        # convert the value field into string (ASCII)

        message = str(msg.value, 'ascii')

        # deserialize
        doc = json.loads(message)

        # dump doc into db
        db.save(doc)

        

    # we are done. As such, we are not going to get here as the above loop
    # is a forever loop.
    consumer.close ()
    

if __name__ == "__main__":
    main(sys.argv[1:])
