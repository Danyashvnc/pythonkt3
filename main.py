import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import User, Order, Product

sys.stdout.reconfigure(encoding="utf-8")
engine = create_engine("sqlite:///kt3.db")

with Session(engine) as session:
    user = User(email="example@example.com")
    keyboard = Product(name="Клавиатура", price=1200.0)
    mouse = Product(name="Мышь", price=300.0)
    pad = Product(name="Коврик", price=500.0)
    user.orders = [
        Order(total_price=1500.0, products=[keyboard, mouse]),
        Order(total_price=800.0, products=[mouse, pad]),
    ]
    session.add(user)
    session.commit()

    user = session.get(User, 1)
    print("User -> Orders:", [o.id for o in user.orders])
    print("Order -> User:", session.get(Order, 1).user.email)
    for o in user.orders:
        print(f"Order {o.id} -> Products:", [p.name for p in o.products])
    for pid in (1, 2, 3):
        p = session.get(Product, pid)
        print(f"Product '{p.name}' -> Orders:", [o.id for o in p.orders])
