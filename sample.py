from fastapi import FastAPI
import sqlite3

app = FastAPI()

@app.get("/user/{user_id}")
def get_user(user_id: str):
    # db connect
    conn = sqlite3.connect("users.db")
    
    query = f"SELECT * FROM users WHERE id = '{user_id}'"
    
    result = conn.execute(query)
    
    return result.fetchone()
