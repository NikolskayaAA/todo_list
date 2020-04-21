from django.template.defaulttags import register

# Минимальное число div на странице
DIV_COUNT = 6


@register.filter
def get_count(lists):
    """
    Возвращает список - количество, для генерации пустых блоков
    """
    return list(range(DIV_COUNT - len(lists)))
