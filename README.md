# 1. What does this repo do?

this is not a useful project, I just do it for fun and learn what [pep503](https://peps.python.org/pep-0503/) and [pypi](https://pypi.org/simple/) do.

although name is like 'mypy' and 'pypi', but this repo is not related to mypy, just a implementation of pypi.

# 2. How to use?

first of all, this is a `uv` project, confirm that you have installed `uv`. if not, then:

```cmd
pip install uv
```

then, clone and this repo:

```cmd
# clone this repo
git clone https://github.com/HirasawaGen/MyPI.git
# enter the repo
cd MyPI
# sync the dependencies
uv sync
# run the server (ip and port can be changed)
uv run manage.py runserver 127.0.0.1:8000
```

then, open your browser and go to `http://127.0.0.1:8000/simple/`.

check did the server run successfully or not.

no index page is normal, because I didn't implement it. maybe I will implement it later.

If it is running successfully, then try to install demo *.whl files:

```cmd
# this two *.whl files are just for test
uv pip install helloworld --index-url http://127.0.0.1:8000/simple/
uv run -m helloworld
```

if everything is ok, you will see this output in terminal:

```cmd
Hello World!
```

and you can also try to install other packages:

```cmd
uv pip install fibonacci --index-url http://127.0.0.1:8000/simple/
uv run -m fibonacci 8
```

if everything is ok, you will see the fibonacci sequence of 8 numbers in terminal.

you can also download from your ip:

`http://127.0.0.1:8000/packages/fibonacci/fibonacci-0.1-py3-none-any.whl#sha256=58ee07eeb5a46dc15314ef78b7e891b514136759a0be199727854a60e0876ffd`
`http://127.0.0.1:8000/packages/helloworld/helloworld-0.1-py3-none-any.whl#sha256=0e86081497369eb0d1da3b232bf61f35406feee09ca8faa9605a95b2359b2413`


