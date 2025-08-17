from fastapi import HTTPException
from app.utils.core import get_language

def get_credit_items():
    items = CreditItems.get(get_language(), [])
    if not items:
        raise HTTPException(status_code=404)
    return items

CreditItems = {
    "cn":[
        {
            "id": 0,
            "name": "2000积分",
            "code": "credit_items_0",
            "price": 10,
            "addonType": "credit_items",
            "isFirstRecharge": True,
            "addonValue": 2000
        },
        {
            "id": 1,
            "name": "1000积分",
            "code": "credit_items_1",
            "price": 10,
            "addonType": "credit_items",
            "isFirstRecharge": False,
            "addonValue": 1000
        },
        {
            "id": 2,
            "name": "5000积分",
            "code": "credit_items_2",
            "price": 50,
            "addonType": "credit_items",
            "isFirstRecharge": False,
            "addonValue": 5000
        },
        {
            "id": 3,
            "name": "10000积分",
            "code": "credit_items_3",
            "price": 100,
            "addonType": "credit_items",
            "isFirstRecharge": False,
            "addonValue": 10000
        },
        {
            "id": 4,
            "name": "50000积分",
            "code": "credit_items_4",
            "price": 500,
            "addonType": "credit_items",
            "isFirstRecharge": False,
            "addonValue": 50000
        }
    ],
    "en":[
        {
            "id": 0,
            "name": "2000 Credits",
            "code": "credit_items_0",
            "price": 10,
            "addonType": "credit_items",
            "isFirstRecharge": True,
            "addonValue": 2000
        },
        {
            "id": 1,
            "name": "1000 Credits",
            "code": "credit_items_1",
            "price": 10,
            "addonType": "credit_items",
            "isFirstRecharge": False,
            "addonValue": 1000
        },
        {
            "id": 2,
            "name": "5000 Credits",
            "code": "credit_items_2",
            "price": 50,
            "addonType": "credit_items",
            "isFirstRecharge": False,
            "addonValue": 5000
        },
        {
            "id": 3,
            "name": "10000 Credits",
            "code": "credit_items_3",
            "price": 100,
            "addonType": "credit_items",
            "isFirstRecharge": False,
            "addonValue": 10000
        },
        {
            "id": 4,
            "name": "50000 Credits",
            "code": "credit_items_4",
            "price": 500,
            "addonType": "credit_items",
            "isFirstRecharge": False,
            "addonValue": 50000
        }
    ],
    "tw":[
        {
            "id": 0,
            "name": "2000積分",
            "code": "credit_items_0",
            "price": 10,
            "addonType": "credit_items",
            "isFirstRecharge": True,
            "addonValue": 2000
        },
        {
            "id": 1,
            "name": "1000積分",
            "code": "credit_items_1",
            "price": 10,
            "addonType": "credit_items",
            "isFirstRecharge": False,
            "addonValue": 1000
        },
        {
            "id": 2,
            "name": "5000積分",
            "code": "credit_items_2",
            "price": 50,
            "addonType": "credit_items",
            "isFirstRecharge": False,
            "addonValue": 5000
        },
        {
            "id": 3,
            "name": "10000積分",
            "code": "credit_items_3",
            "price": 100,
            "addonType": "credit_items",
            "isFirstRecharge": False,
            "addonValue": 10000
        },
        {
            "id": 4,
            "name": "50000積分",
            "code": "credit_items_4",
            "price": 500,
            "addonType": "credit_items",
            "isFirstRecharge": False,
            "addonValue": 50000
        }
    ],
    "ja":[
        {
            "id": 0,
            "name": "2000ポイント",
            "code": "credit_items_0",
            "price": 10,
            "addonType": "credit_items",
            "isFirstRecharge": True,
            "addonValue": 2000
        },
        {
            "id": 1,
            "name": "1000ポイント",
            "code": "credit_items_1",
            "price": 10,
            "addonType": "credit_items",
            "isFirstRecharge": False,
            "addonValue": 1000
        },
        {
            "id": 2,
            "name": "5000ポイント",
            "code": "credit_items_2",
            "price": 50,
            "addonType": "credit_items",
            "isFirstRecharge": False,
            "addonValue": 5000
        },
        {
            "id": 3,
            "name": "10000ポイント",
            "code": "credit_items_3",
            "price": 100,
            "addonType": "credit_items",
            "isFirstRecharge": False,
            "addonValue": 10000
        },
        {
            "id": 4,
            "name": "50000ポイント",
            "code": "credit_items_4",
            "price": 500,
            "addonType": "credit_items",
            "isFirstRecharge": False,
            "addonValue": 50000
        }
    ],
}
