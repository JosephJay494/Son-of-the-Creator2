# Son-of-the-creator


# PostgreSQL with Fastapi CRUD APPLICATION

This is a simple CRUD application built using PostgreSQL and FastAPI. 

## Running the server


Set your [URI connection string] as a parameter in `.env`. Make sure you replace the username and password placeholders with your own credentials.


Install the required dependencies:

```
python -m pip install -r requirements.txt
```

Start the server:
```
python -m uvicorn main:app --reload
```
In this section I've used ORM by putting a code that will look in the database and check if there is a certain table need for a specific model and there is no table it automatically creates the table, so will nolonger be creating the table in the pgAdmin the code will now be doing it for use.

I've also created the database.py , models.py models 
Intsall the required dependencies:

```
python -m pip install -r requirements.txt

```

Start the server:

```
python -m uvicorn main:app --reload

```
In this section l've changed the codes from SQL to traditonal python code by using ORM which l introduced in the previous task earlier which is a layer of abstraction that sits between the database and us.

l also introdued the schemas module or sometime called the pydantic model that is responsible for defining the structure of a request and response.

This model ensures that when a user wants to create a post the request will only go through if it has the 'title' , content and all other requiremnents in the body.

I also stored all my models in the folder Packages which changes the way to run the server now


Start the server:

```
python -m uvicorn Packages.main:app --reload

```
ln this section I modified the module models.py with adding the Users class that will automatically create a table for users in the database and also created the module utils.py that will handle the encryption of passwords in the database once a user account has been created.

In this section I created the module auth.py that will authenticated the uses when they Login their accountsand l've also creater the File routers which contains auth, post and user.py 

ln this section i created Jtw token that will help to increase security in our API for our users as they Login.

In this section l've created the user authenticator that will only allow user to create, read, update and delet once they have logged in.  

I established the relationship  between the tables in the database which are books and users in a way that i can assign a particular post to its user, 'showing who posted the post'.
Now in this section one can only delete a post if he/she is the ower of the post that they may want to delete.

In this section clean some of my cords mainly in the main.py module and i also edited the get_post router making it possible for users to be able to search for individual post and also skip some post if they do want them.

In this section i created the .env file that holds all the environment variables 

In this section i implemented the voting or likes system which enables the users to like the post.

In this section l have implemented the join and count function that will be reponsible for count the number of votes, the join function is joinig the Books and vote tables.

In this section I've database migrations using Alembic.I also set the CORS (CROSS ORIGIN RESOURCE SHARING)


Install the required dependencies:

```
python -m pip install -r requirements.txt

```
In this section i created a container and a build an image with the name son of the creator.
In this section I've created the docker-compose file which is responsibe for running the container


Start the server:

```
docker-compose up -d

```
Int this section I've modified the docker-compose file into two files one being the development and the other being the production one
To run the dev file we use the below running command. 

```
docker-compose -f docker-compose-dev.yml up -d

```
To run the prod filwe we use the following running command.

``` 
docker-compose -f docker-compose-prod.yml up -d

```

In this section i have creates the jps.py in the router module which contains so html code and also have created the templates module containing the files base.html, index.html.

I have also installed jinja2Tamplates package

Install the required dependencies:

```
python -m pip install -r requirements.txt

```

In this section i install aiofiles which works with the static file that also created in this section.

```
python -m pip install -r requirements.txt

```