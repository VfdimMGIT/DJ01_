from django.http import HttpResponse

def home_page(request):
    return HttpResponse("""
        <h1>Главная страница</h1>
        <ul>
            <li><a href="/data/">Страница данных</a></li>
            <li><a href="/test/">Тестовая страница</a></li>
        </ul>
    """)

def data_page(request):
    return HttpResponse("""
        <h1>Страница данных</h1>
        <p>Здесь будут важные данные проекта</p>
        <a href="/">На главную</a>
    """)

def test_page(request):
    return HttpResponse("""
        <h1>Тестовая страница</h1>
        <p>Это страница для тестирования</p>
        <a href="/">На главную</a>
    """)