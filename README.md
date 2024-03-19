# Beehive

A Data Federation Approach to Analyze Behavioral Health and Supplement Healthcare Practice with Community Health Metrics in Alaska

## Project description

This project aims to develop [Beehive](https://github.com/KathiraveluLab/Beehive/), a prototype implementation as an open-source data federation framework that can be used in research environments in Alaska and elsewhere.

To achieve the goals of Beehive, I have accomplished the following tasks using the Django framework:

1. Connected to a MySQL database for storing images and users' information.
2. Backend development for Beehive.
3. Frontend development for Beehive, designing a user-friendly web interface.

## Code framework

Describes some of the main files and their purposes in the project.

```
- Beehive
  - settings   * critical project configurations like database connections
  - urls       * mappings between URLs and backend functions
- app1
  - static     * store components required for frontend webpage like CSS, images
  - models     * design database tables
  - templates  
    - manager  * store HTML files for the admin frontend pages
    - user     * store HTML files for the user frontend pages
  - views.py   * defines backend functions for all web pages.
- media/images * store images in the database
```

## Demonstration
The webpages of Beehive are divided into the admin interface and user interface for different purposes.

Additionally, some demo videos have been created here to provide others with a better understanding of the Beehive webpages.

#### login interface
I have implemented a basic registration and login functionality. User registration information is stored in the "user" table in the database. 

Users or admins can log in to the system using their username and password. Upon logging in, admins will be directed to the admin interface, while regular users will be directed to the user interface.


https://github.com/yanhuojunjun/Beehive/assets/149027679/83a263a0-0a79-4587-9f81-551b8ee90c6f


#### admin interface
In the admin interface, users can perform CRUD operations on all tables in the database (currently, there are two tables: "image" and "user", more tables can be added in the future). The following video demonstrates how to perform CRUD operations on users.


https://github.com/yanhuojunjun/Beehive/assets/149027679/bc0d2fe6-baea-48c6-92d7-eb22daf2b9cd


CRUD operations on images:


https://github.com/yanhuojunjun/Beehive/assets/149027679/6f81853e-f00c-4d18-9341-ab52dae769ab


#### user interface
In the user interface, users can view all images on Beehive and query images based on specific features (such as "unhousing", "recovering alcoholic", "addiction" ect). 

Clicking on an image allows users to view detailed information about the image, including artist, time, location, description, type, etc. Additionally, I plan to add multiple features in the future, such as favorites, comments, and more.


https://github.com/yanhuojunjun/Beehive/assets/149027679/356dab65-2066-4e3c-9f36-a484b85fa21a


Similarly, users can publish their own works to Beehive. Additionally, each user has their own space where they can view the works they have published.


https://github.com/yanhuojunjun/Beehive/assets/149027679/0e6669f3-033c-4568-8d37-5464a058b759






