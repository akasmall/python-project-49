<a id = "anchor"></a>
# Игры разума - Brain Games

### Hexlet tests and linter status:
[![Actions Status](https://github.com/akasmall/python-project-49/workflows/hexlet-check/badge.svg)](https://github.com/akasmall/python-project-49/actions) <a href="https://codeclimate.com/github/akasmall/python-project-49/maintainability"><img src="https://api.codeclimate.com/v1/badges/a83c753bdcdabd8080cb/maintainability" /></a> <a href="https://codeclimate.com/github/akasmall/python-project-49/test_coverage"><img src="https://api.codeclimate.com/v1/badges/a83c753bdcdabd8080cb/test_coverage" /></a>

## Обзор
Проект создан в целях получения практического опыта разработки на языке Python на курсе компании __Хекслет__.
В проект вошли пять игр:
* «Проверка на чётность» ( Brain even )
* «Калькулятор» ( Brain calc )
* «Наибольший общий делитель (НОД)» ( Brain gcd )
* «Арифметическая прогрессия» ( Brain progression )
* «Простое ли число?» ( Brain prime )

[Посмотреть видео проекта](#brain_games)

---
## Требования
###### Для установки и запуска проекта, необходимы:
~~~sh
1. python версии 3.10 и выше
2. pip 23.2.1 и выше
3. poetry версии 1.6.1 и выше
4. prompt версии 0.4.1 и выше
~~~
## Как установить
##### 1. [установить **python**](https://github.com/Hexlet/ru-instructions/blob/main/python.md)
###### 2. установить **pip**, с версии python 3.4 идет в пакете и/или обновить **pip**
~~~
$ # проверка pip
python3 -m pip --version
$ # если требуется обновление, то так:
python3 -m pip install --upgrade --user pip
~~~
###### 3. [установить менеджер пакетов **poetry**](https://python-poetry.org/docs/)
после установки 
~~~
$ # проверить что работает и версию
poetry --version
~~~

###### 4. создание виртуального окружения в директории проекта
~~~
$ # выполните команду
poetry config virtualenvs.in-project true
~~~
###### 5. склонируйте [репозиторий проекта](https://github.com/akasmall/python-project-49) с GitHub
~~~
git clone git@github.com:akasmall/python-project-49.git
~~~
###### 6. Подключите в зависимости библиотеку **prompt** командой
```
poetry add prompt
```
###### 7. собирите проект
```
make build
```

###### 8. установите проект
```
make package-install
```

## Как запускать игры
* Brain_even
* Brain_calc
* Brain_gcd
* Brain_progression
* Brain_prime

## Видео игры
<a id = "brain_games"></a>
[![asciicast](https://asciinema.org/a/Nr8zJPzvdooByxeWYKVZnsf0Q.svg)](https://asciinema.org/a/Nr8zJPzvdooByxeWYKVZnsf0Q)


[Вверх](#anchor)