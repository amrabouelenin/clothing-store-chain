# Clothing Store Chain

This simple project using distributed and scalable web application and database to transfer load from one central server
and pass it to branch offices with separate database for each.

Below are 3 diagrams showing the following:

* High-level architecture view of the system composed of one headquarter and several branches
* Communication between Headquarter and branches through API server in headquarter using RESTful webservice.
* Simple Entity Relationship Diagram (ERD) for both headquarter and branch offices.

The system can be deployed in containerized environment using Containers application like [Docker](https://docker.org)
and can be deployed with [Kubernetes](https://Kubernetes.io) also can be used without containers either in one server or distributed across multiple servers.

This application contains basic design elements for clothing chain shop; however, it can be scaled to contain many features and many branches.

![System Architecture](https://github.com/amrabouelenin/clothing-store-chain/blob/master/clothes-shope-disributed-scalable-architecture.png)

Figure 1. shows the basic components for both headquarter and branch offices. in the same time, it shows that every branch shall has its own database instance in order to transfer the load from the central server.

![Communications Headquarter and Branch offices](https://github.com/amrabouelenin/clothing-store-chain/blob/master/clothes-shop-headquarter-branches-communications.png)

Figure 2. shows 3 main and basic tables required to setup the headquarter office system. Headquarter employee shall be able to access through web application or even mobile application that can be integrated later. 
The system contains Django main web application utilized with authentication components to access required reports from web.

It contains as well, RESTFUL webservice using Flask to allow separate teams to work on this service without being involved in any other features developed by Django main web app. This component act as the API server to allow requests from branch offices.

Headquarter database has branches table that act as tenant information table for every branch. this information is required to be validated by service calls for the API server from branch office web system.

![Entity Relationship Diagram ERD](https://github.com/amrabouelenin/clothing-store-chain/blob/master/clothes-shop-erd-headquarter-branches.png)

Figure 3. shows basic main tables for headquarter and branches office. Headquarter branches table to store branch office required information like, name of branch, location, and URL(DNS name) of the branch office. daily_revnue table is table accessed by internal API service call, initiated from the branch office to save important information for headquarter office like revenue total of the transaction of today and loss in dollar.

As for ERD branch office. it has 4 tables, Products table that contains information about the product like price and name (we can add more fields later), transactions table to record the daily transactions made by the operator in the branch. service calls table and this is required and accessed by the internal function (send_revenue_loss) that send two parameters total invoices of the day and total losses in case there is any.

The auth table is a common table required for both headquarter and branch office and it is separated in purpose to avoid centralized authentication from the same server.

### How to setup the system.

[to be added later]

### Tasks required

* implement similar api server in the branch office
* create tables/modles for the branch office.
* user restframework for authentication user
* implement client to use the restfult webservice from the headquarter (Headquarter client) Required models[Branch]
* implement client to use the restfult webservice from the branch (Headquarter client) required models [DailyRevenue]
* implement cron job that just call the send revenue webservice from headquarter

* Create the required reports for the project:
   1 . Feasibility study of communication between systems
        preparation of a working Web Service (or Web Services) in selected technologies
        basic working client of Web Service (console, graphical, mobile, or web application)
        include in the report the most important parts of the code
        include pointers to the source materials (such as URLs)
        
   2 . Establish the business context, sketch the system architecture, select technology
        project description
        determine the scope of the project
        selection of technologies planned for the construction of the system
        documentation of the main business process - UML activity diagram
        documentation of system architecture - UML deployment diagram

   3 . Implementation of data exchange and synchronization (headquarters / offices)
        background service (in headquarter and/or branch server) that performs periodic data synchronization
        fault tolerance when connection between HQ and branches is not available (try to synchronize next time)
        Also:
        completion of service layer, and user interface in client applications
        presentation of running applications
        presentation of data exchange or data synchronization between headquarters and branches

   4 . Performance analysis, summary and conclusions of the project [Amro, Onur]
        description of methodology of testing the presentation layer, or other parts of your system (what and how has been tested)
        include the results of measurements (not screenshots!)
        analysis of results
        Summary and Conclusions about the experience of work during the project from each team member
        (it's an open subject - just a couple of paragraphs. Please use this opportunity!)
   
    5. Final presentation
        Final presentation
        Effective communication in a variety of professional contexts
        Here is a place to upload your presentation describing your project and results of your work during whole semester.

        think about showing off best aspects of your project to potential investors, employers or other specialits in the field,
        presentation should be rather short yet informative (which is hard, but it's a noble goal to pursue),
        you may describe for eample:
        your project and its goals, team members
        scope of your project,
        user requirements (if any)
        architecture of your solution
        technologies used
        important aspects of your code
        your workflow used for the project
        ... and so on
        you may also include summary and conclusions of the project from each team member
        if you want to, you may use Inception Desk from "Agile Samurai" book as a baseline for your presentation



