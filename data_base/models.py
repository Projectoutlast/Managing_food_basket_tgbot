from sqlalchemy import Column, Enum, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from data_base.base import Base
from logic.enums import BotMode


class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True)
    first_name = Column(String(60), nullable=True)
    user_name = Column(String(60), nullable=True)

    customer_setting = relationship("CustomerSetting", uselist=False, back_populates="customer")
    customer_FSM = relationship("CustomerFSM", uselist=False, back_populates="customer_fsm")
    customer_basket = relationship("CustomerBasketSetting", uselist=False, back_populates="customer_basket")


class CustomerSetting(Base):
    __tablename__ = "customers_setting"

    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey("customers.id"))
    basket_limit = Column(Float, nullable=True)
    bot_mode = Column(Enum, default=BotMode.normal)
    language = Column(Enum)

    customer = relationship("Customer", back_populates="customer_setting")


class CustomerFSM(Base):
    __tablename__ = "customers_FSM"

    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey("customers.id"))
    current_state = Column(Enum)

    customer = relationship("Customer", back_populates="customer_state_fsm")


class CustomerBasketSetting(Base):
    __tablename__ = "customers_basket_settings"

    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey("customers.id"))
    current_sum = Column(Float, default=0.00)

    customer = relationship("Customer", back_populates="customer_basket_settings")
