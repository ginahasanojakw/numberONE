# === Stage 18: Добавь поддержку тегов и операции добавления/удаления тегов ===
# Project: StudyTimer
def add_tag(topic_id, tag):
    """Добавить тег к теме."""
    if topic_id not in STUDY_TIMER:
        print(f"Ошибка: тема {topic_id} не найдена")
        return False
    topic = STUDY_TIMER[topic_id]
    if tag not in topic["tags"]:
        topic["tags"].append(tag)
        save_timer()
        print(f"Тег '{tag}' добавлен к теме {topic['title']}")
        return True
    else:
        print(f"Тег '{tag}' уже существует для этой темы")
        return False

def remove_tag(topic_id, tag):
    """Удалить тег из темы."""
    if topic_id not in STUDY_TIMER:
        print(f"Ошибка: тема {topic_id} не найдена")
        return False
    topic = STUDY_TIMER[topic_id]
    if tag in topic["tags"]:
        topic["tags"].remove(tag)
        save_timer()
        print(f"Тег '{tag}' удален из темы {topic['title']}")
        return True
    else:
        print(f"Тег '{tag}' не найден для этой темы")
        return False

def list_tags(topic_id=None):
    """Показать все теги. Если topic_id указан, только теги одной темы."""
    if topic_id is not None:
        if topic_id in STUDY_TIMER:
            print(f"Теги для '{STUDY_TIMER[topic_id]['title']}': {', '.join(STUDY_TIMER[topic_id].get('tags', []))}")
        else:
            print(f"Ошибка: тема {topic_id} не найдена")
    else:
        all_tags = set()
        for topic in STUDY_TIMER.values():
            all_tags.update(topic.get("tags", []))
        if all_tags:
            print("Все теги:", ", ".join(sorted(all_tags)))
        else:
            print("Теги не найдены")
