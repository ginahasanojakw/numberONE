# === Stage 5: Добавь удаление записей и аккуратную обработку отсутствующих идентификаторов ===
# Project: StudyTimer
def delete_session(session_id: int) -> bool:
    if not session_id or not isinstance(session_id, int):
        print("Ошибка: идентификатор сессии должен быть целым числом.")
        return False
    
    try:
        with open('study_timer_data.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        if session_id not in data['sessions']:
            print(f"Сессия с ID {session_id} не найдена.")
            return False
        
        del data['sessions'][session_id]
        
        with open('study_timer_data.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
            
        print(f"Сессия {session_id} успешно удалена.")
        return True
        
    except FileNotFoundError:
        print("Файл данных не найден. Убедитесь, что вы запустили приложение ранее.")
        return False
    except json.JSONDecodeError as e:
        print(f"Ошибка чтения JSON файла: {e}")
        return False
