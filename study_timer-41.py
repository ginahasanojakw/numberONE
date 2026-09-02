# === Stage 41: Добавь режим dry-run для операций изменения данных ===
# Project: StudyTimer
import copy

def dry_run(func, *args, **kwargs):
    """
    Выполняет func в сухом режиме: если func возвращает None,
    выводит описание предполагаемого действия, иначе возвращает результат.
    """
    if args or kwargs:
        desc = f"{func.__name__}({', '.join(repr(a) for a in args)})"
        if kwargs:
            desc += f", {', '.join(f'{k}={v!r}' for k, v in kwargs.items())}"
    else:
        desc = func.__name__

    result = func(*args, **kwargs)
    if result is None:
        print(f"[DRY-RUN] {desc} — действие не выполнено.")
        return None
    return result
