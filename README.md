# Flask API

## Start

If you don't have the venv directory, then create it

    python -m venv venv

To continue on your work on a Windows machine

    source venv/Scripts/activate
    pip install -r requirements.txt
    python main.py

Then open browser at

    http://localhost:8080

## User API

To create a user, we send to  http://localhost:8080/create

    POST /create

with the format

    {
        "name": "Musse Pigg",
        "user_id": "user123",
        "dob": "1901-12-24"
        "weight": 40,
        "height": 1.50
    }

To read a user

    GET /{user_id}

it returns user in the format

    {
        "name": "Musse Pigg",
        "user_id": "user123",
        "dob": "1901-12-24"
        "weight": 40,
        "height": 1.50
    }



To update a user

    PATCH /{user_id}

with the body

    {
        "weight": 45,
        "height": 1.60
    }

To remove a user

    DELETE /{user_id}



