## Бот для отслеживания текущей стоимости корзины в процессе покупок

### Бот создан в академических целях для закрепления навыков программирования на Python и работы с библиотекой Aiogram3.


#### Предпосылки для создания

В магазинах с кассами самообслуживания есть такая фишка, как ручные сканеры. Суть следующая:
1) сканируешь штрихкод товара
2) кладешь товар в корзину
3) повторить предыдущие 2 пункта в объеме приобретаемых товаров
4) на кассе сканируешь штрих-код на мониторе кассы и просто оплачиваешь весь перечень.

В процессе сканирования товаров их стоимость складывается и 
отображается на экране сканера. Нет необходимости складывать товар в корзину, потом выкладывать на кассе, сканировать 
все позиции, оплачивать и снова перекладывать в свою корзину/пакет.

Вещь удобная.
Но что делать, если такая фича в магазине не поддерживается, а отслеживать стоимость корзины нужно.

Можно использовать калькулятор телефона, но это не очень удобно. Во первых этот способ подвержен ошибкам 
(есть вероятность нажать неверную арифметическую операцию на экране), во вторых можно случайно нажать клавишу сброса С.

Для отслеживания стоимости вышеописанной корзины и был создан данный бот.

Несмотря на простоту, мне данный проект помог закрепить на практике:
- **написание Python кода**;
- **работу с базой данных через ORM (SQLAlchemy)**;
- **библиотеку Aiogram3**;
- **структурирование создаваемой программы.**

