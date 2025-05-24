from django.urls import path

from apps.todo.template_view import TodoListView, TodoDeleteView, TodoUpdateView, TodoDetailView, SubtaskCompleteView, \
    SubtaskUpdateView, SubtaskDeleteView
from apps.todo.views import ExampleGETView, ExampleQueryParamView,ExamplePOSTHeaderView,\
ExamplePATCHPathParamView, ExamplePUTBodyView

app_name = "todo"

urlpatterns = [
    path("example-get", ExampleGETView.as_view()),
    path("example-query-param", ExampleQueryParamView.as_view()),
    path("example-header", ExamplePOSTHeaderView.as_view()),
    path('example-path-param/<int:id>/<str:name>', ExamplePATCHPathParamView.as_view()),
    path('body', ExamplePUTBodyView.as_view())
]

template_url_patterns = [
    path("", TodoListView.as_view(), name="todo_list"),
    path("<int:pk>", TodoDetailView.as_view(), name="todo_detail"),
    path("<int:pk>/update", TodoUpdateView.as_view(), name='todo_update'),
    path("<int:pk>/delete", TodoDeleteView.as_view(), name="todo_delete"),

    path("<int:todo_id>/<int:subtask_id>/complete", SubtaskCompleteView.as_view(), name="subtask_complete"),
    path("subtask/<int:todo_id>/<int:subtask_id>/update", SubtaskUpdateView.as_view(), name="subtask_update"),
    path("subtask/<int:todo_id>/<int:subtask_id>/delete",SubtaskDeleteView.as_view(), name="subtask_delete"),

]

urlpatterns += template_url_patterns