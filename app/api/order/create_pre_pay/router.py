from fastapi import APIRouter

create_pre_pay_router = APIRouter(
    prefix='/create_pre_pay',
    tags=['order-prepay']
)

from .wx.router import wx_router
create_pre_pay_router.include_router(wx_router)