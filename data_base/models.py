from sqlalchemy import Column, Enum, Float, ForeignKey, Integer, String
from sqlalchemy.orm import DeclarativeBase, relationship

from logic.enums import BotMode, FSMCustomerEnum


class Base(DeclarativeBase):
    pass


class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True)
    user_id_telegram = Column(Integer, nullable=False)
    first_name = Column(String(60), nullable=True)
    user_name = Column(String(60), nullable=True)

    customer_setting = relationship("CustomerSetting", uselist=False, back_populates="customer")
    customer_state_fsm = relationship("CustomerFSM", uselist=False, back_populates="customer_fsm")
    customer_basket_settings = relationship("CustomerBasketSetting", uselist=False, back_populates="customer_basket")


class CustomerSetting(Base):
    __tablename__ = "customers_setting"

    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey("customers.user_id_telegram"))
    basket_limit = Column(Float, default=0.00)
    bot_mode = Column(Enum(BotMode), default=BotMode.NORMAL)
    bot_language = Column(String, nullable=True)

    customer = relationship("Customer", back_populates="customer_setting")


class CustomerFSM(Base):
    __tablename__ = "customers_FSM"

    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey("customers.user_id_telegram"))
    current_state = Column(Enum(FSMCustomerEnum), default=FSMCustomerEnum.DEFAULT_STATE)

    customer_fsm = relationship("Customer", back_populates="customer_state_fsm")


class CustomerBasketSetting(Base):
    __tablename__ = "customers_basket_settings"

    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey("customers.user_id_telegram"))
    current_sum = Column(Float, default=0.00)

    customer_basket = relationship("Customer", back_populates="customer_basket_settings")
