from fasthtml.common import *

app,rt,todos,Todo = fast_app('data/todos.db', id=int, t_title=str, done=bool, pk='id')

@rt("/")
def get():
    todo_list = [
        Li(
            A(todo.t_title, hx_get=f'/todos/{todo.id}'),
            (' (done)' if todo.done else ''),
            id=f'todo-{todo.id}'
        ) for todo in todos()
    ]
    card = Card(
                Ul(*todo_list, id='todo-list'),
                header=add,
                footer=Div(id='current-todo')
            )
    return Main('Todo list', card)

@rt("/todos/{id}")
def get(id:int):
    contents = Div(
        Div(todos[id].t_title),
        Button('Back', hx_get='/',hx_target="Main")
    )
    return Div('Todo details', contents)
serve()