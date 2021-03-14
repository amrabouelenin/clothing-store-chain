# Clothing Store Chain

This simple project using distributed and scalable web application and database to transfer load from one centeral server
and pass it to branch offices with separate database for each.

Below 3 diagram shows the following

* Highlevel archticuture view of the system composed of one headquarter and several branches
* Communication between Headquarter and branches through api server in headquarter using RESTful webservice.
* Simple Entity Relationship Diagram (ERD) for both headquarter and branch offices.

The system can be deployed in containarized environment using Containers application like [Docker](https://docker.org)
and can be deployed with [Kubernetes](https://Kubernetes.io) also can be used without containers either in one server or distributed accross multiple servers.

This application contains basic design elements for clothing chain shop, However it can be scalled to contain many features and many branches.

[System Architecture](https://raw.githubusercontent.com/amrabouelenin/clothing-store-chain/master/clothes-shope-disributed-scalable-architecture.png)
Figure 1. shows the basic components for both headquarter and branch offices. in the same time it shows that every branch shall has it's own database instance in order to transfer the load from the centeral server.

[Communications Headquarter and Branch offices](https://github.com/amrabouelenin/clothing-store-chain/blob/master/clothes-shop-headquarter-branches-communications.png)
Figure 2. shows 3 main and basic tables required to setup the headquarter office system. Headquarter employee shall be able to access through web application or even mobile application that can be integrated later. 
The system contains Django main web application utilized with authentication componentes to access repuired reports from web.

It contains as well, RESTFUL webservice using Flask to allow separate teams to work on this service withough being involved in any other features developed by Django main web app. This component act as the Api server to allow requests from branch offices.

Headquarter database has branches table that act as tenant information table for every branch. this information is required to be validated by service call for the api server from branch office web system.

[Entity Replationship Diagram ERD](https://github.com/amrabouelenin/clothing-store-chain/blob/master/clothes-shop-erd-headquarter-branches.png).
Figure 3. shows basic main tables for headquarter and branaches office. Headquarter branches table to store branch office required informatino like, name of branch, location, and url(dns name) of the branch office. daily_revnue table is table accessed by internal api service call, initiated from the branch office to save important information for headquarter office like revnu total of the transcation of today and loss in dollar.

As for ERD branch office. it has 4 tables, Products table that contains information about the product like price and name(we can add more fields later), transcations table to record the daily transactions made by the operator in the branch. service calls table and this is required and accessed by the internal function (send_revenu_loss) that send two parameters total invoices of the day and total losses in case there is any.

The auth table is a common table required for both headquarter and branch office and it is separated in purpose to avoid centeralized authentication from the same server.

How to setup the system
[to be added later]



