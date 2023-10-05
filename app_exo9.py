from fastapi import FastAPI
from pydantic import BaseModel
import psycopg2
import uvicorn
app=FastAPI()



class Customer(BaseModel):
    email : str    
@app.post("/registration")

def register_user(customer:Customer):
    print(customer)
    try:
        conn=psycopg2.connect(host="localhost",database="cb00",user="postgres",password="mdp",port=5434)

        cur=conn.cursor()
        cur.execute(f"INSERT INTO customer (email) VALUES ('{customer.email}');")
        conn.commit()

    except Exception as e: 
        print("pbm dataconnection",e)
    return customer

if __name__=="__main__":
    import uvicorn
    #uvicorn.run(app,host="0.0.0.0",port=8000)
    register_user(Customer(email="toto@lala.com"))
