MikeBot
=====

MikeBot - это бот для Telegram, созданный с целью обучения.

Установка
----
Создайте виртуальное окружение и активируйте его. В виртуальном окружении выполните:
.. code-block:: text
    pip install -r requirement.txt

Наполните папку /cats_images картинками с котиками. Название файлов должно содержать "cat" и иметь разрешение .jpg / .jpeg.
Например, cat123.jpg.

Настройка
-----
Создайте файл settings.py и добавьте в него следующие настройки:
.. code-block:: python
    PROXY = {"proxy_url" : "socks5://ВАШ_SOCKS5_ПРОКСИ:1080", "urllib3_proxy_kwargs" : {"username" : "ЛОГИН", "password" : "ПАРОЛЬ"}}

    TG_API_KEY = "API ключ, который вы получили у BotFather"

    USER_EMOJI = [':smiley_cat:', ':smiling_imp:', ':panda_face:', ':dog:']

Запуск
-----
В активированном виртуальном окружении выполните:
..code-block:: text
    python3.py

