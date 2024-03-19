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

<iframe height=498 width=510 src="demo video/login">


#### admin interface



#### user interface
