from fasthtml.common import *

app,rt,todos,Todo = fast_app('data/todos.db', id=int, t_title=str, done=bool, pk='id')

def TodoRow(todo):
    return Li(
        A(todo.t_title, hx_get=f'/todos/{todo.id}'),
        (' (done)' if todo.done else ''),
        id=f'todo-{todo.id}'
    )

def home():
    add = Form(
            Group(
                Input(name="t_title", placeholder="New Todo"),
                Button("Add")
            ), hx_post="/",hx_target="closest Main"
        )
    card = Card(
                Ul(*map(TodoRow, todos()), id='todo-list'),
                header=add,
                footer=Div(id='current-todo')
            )
    return Main('Todo list', card)

@rt("/")
def get(): return home()

@rt("/")
def post(todo:Todo):
    todos.insert(todo)
    return home()

@rt("/todos/{id}")
def get(id:int):
    contents = Div(
        Div(todos[id].t_title),
        Button('Back', hx_get='/',hx_target="Main")
    )
    return Div('Todo details', contents)

serve()