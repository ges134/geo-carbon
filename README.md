# geo-carbon

A carbon footrpint calculator that print your carbon wherever you go

# purpose

The real purpose for this app is to get ready for CS Games 2020. But I might continue this readme as though it was a real project I was developping.

This app intends to measure your carbon footprint and then map it to your current position. That way, you would get a map of where you produce the most carbon.

An extended concept of this application would be to have a globalized system in which we could get the heatmap for every users on the platform. But we're not there yet.

# structure

The project is mainly focusing on the backend. So for now, it would only be a RESTful API connected to postGIS. More details to come!

# Get started

Follow this step-by-step!

1.  Clone the repo
1.  Configure virtual environment for python (`py 3 -m venv venv` on Windows)
1.  Install packages (`pip install -r requirements.txt`)
1.  Install PostGresSQL!
1.  Create a database named `geocarbon`
1.  Create a user named `Geocarbo` with the following password `pp@cc355`.
1.  Make user owner of the database.
1.  Run the migrations (`alembic upgrade head`)
1.  run the app (`uvicorn main:app --reload`)
