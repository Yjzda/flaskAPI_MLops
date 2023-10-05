from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uuid
import sqlite3  

app = FastAPI()

# Database setup (SQLite in this example)
conn = sqlite3.connect("user_db.sqlite")
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT UNIQUE NOT NULL,
        token TEXT UNIQUE NOT NULL
    )
""")
conn.commit()

class UserRegistration(BaseModel):
    email: str

@app.post("/register")
async def register_user(user: UserRegistration):
    # Generate a unique token for the user
    user_token = str(uuid.uuid4())

    try:
        # Insert the user's email and token into the database
        cursor.execute("INSERT INTO users (email, token) VALUES (?, ?)", (user.email, user_token))
        conn.commit()
    except sqlite3.IntegrityError:
        # Handle the case where the email is not unique (already registered)
        raise HTTPException(status_code=400, detail="Email already registered")

    return {"token": user_token}
