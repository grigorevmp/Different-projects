## Установка

Linux:
`sudo apt-get install git` 

Windows:
`Git for windows`

Mac OS:
`brew install git`

## Настройка
Ваша имя:
`$ git config --global user.name "My Name"`

Ваш mail:
`$ git config --global user.email myEmail@example.com`

## Созание папок
`$ mkdir Desktop/repo/`

`$ cd Desktop/repo/`

`$ git init`

__init__ - включает приложение в определённой папке и создаёт в ней скрытую директорию .git

## Состояние

__status__ — показывает информацию о текущем состоянии репозитория

`$ git status`

## Подготовка файлов

> "Холст, на который наносят изменения, которые нужны в коммите"

Добавление файла для коммита

`$ git add hello.txt`

Добавление всех файлов в директории для коммита:

`$ git add -A`

## Коммит

`$ git commit -m "Initial commit."`

## Подключение к удаленному репозиторию

`$ git remote add origin https://github.com/tutorialzine/awesome-project.git`

Обычно главный репозиторий называется origin.

## Отправка изменений на сервер

`$ git push origin master`

## Клонирование репозитория

`$ git clone https://github.com/tutorialzine/awesome-project.git`

## Запрос изменений с сервера

`$ git pull origin master`

## Создание новой ветки

`$ git branch notMaster`

## Переключение между ветками

`$ git checkout notMaster`

Если не создана:

`$ git checkout -m notMaster`

## Слияние веток

`$ git checkout master`

`$ git merge amazing_new_feature`

`$ git branch -d awesome_new_feature`

## Отслеживание изменений, сделанных в коммитах

`$ git log`

`<commit> - номер коммита`

Выбираем <commit>:

`$ git show <commit>`

Разница между коммитами:

`$ git diff <commit>..<commit>`

## Возвращение файла к предыдущему состоянию

`$ git checkout <commit> <file>`

## Исправление коммита

Последний:

`$ git revert HEAD`

Остальные:

`$ git revert <commit>`

## Перемещение всей ветки

`$ git rebase <branch>`

## Добавление изменений к предыдущему коммиту

`$ git commit -m 'initial commit'`

`$ git add forgotten_file`

`$ git commit --amend`

---

Адаптация статьи [proglib](https://proglib.io/p/git-for-half-an-hour) в виде интрукций