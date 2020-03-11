# geo-carbon

A carbon footrpint calculator that print your carbon wherever you go

# purpose

The real purpose for this app is to get ready for CS Games 2020. But I might continue this readme as though it was a real project I was developping.

This app intends to measure your carbon footprint and then map it to your current position. That way, you would get a map of where you produce the most carbon.

An extended concept of this application would be to have a globalized system in which we could get the heatmap for every users on the platform. But we're not there yet.

# structure

The project is mainly focusing on the backend. So for now, it would only be a RESTful API connected to postGIS. More details to come!

# Database connection

Database is runned on a docker container. Since I'm using windows, I'm using IP address 192.168.99.100 on port 5432.

In order to install the postGIS image

```sh
docker run -p 5432:5432 --name some-postgis -e POSTGRES_PASSWORD=yourpassword -d postgis/postgis
```

Afterwards, you're good to go with running the postgis image and accessing the psql shell with:

```sh
docker run -it --link some-postgis:postgres --rm postgres \
    sh -c 'exec psql -h "$POSTGRES_PORT_5432_TCP_ADDR" -p "$POSTGRES_PORT_5432_TCP_PORT" -U postgres'
```

You now have a fresh database!

# Get started

Follow this step-by-step!

_You need to have python, poetry and Docker installed on your machine. If you use windows, you should have docker tools installed._

1.  Clone the repo
1.  Install packages (`poetry install`) Poetry should create the virtual environment. If not, run this on Windows: py 3 -m venv .venv`
1.  Install postGis image: `docker run -p 5432:5432 --name some-postgis -e POSTGRES_PASSWORD=yourpassword -d postgis/postgis`
1.  Open postGis shell: `docker run -it --link some-postgis:postgres --rm postgres \ sh -c 'exec psql -h "$POSTGRES_PORT_5432_TCP_ADDR" -p "$POSTGRES_PORT_5432_TCP_PORT" -U postgres'`
1.  Create a user named `Geocarbon` with the following password `pp@cc355`. You can run this command in psql `CREATE USER "Geocarbon" WITH PASSWORD='@pp@cc355'`
1.  Create database geocarbon. You can run the following psql command: `CREATE DATABASE geocarbon WITH OWNER = "Geocarbon" ENCODING = 'UTF8' TABLESPACE = pg_default CONNECTION LIMIT = -1;`
1.  Run the migrations (`alembic upgrade head`)
1.  run the app (`uvicorn main:app --reload`)
