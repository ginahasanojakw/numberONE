# === Stage 22: Добавь проверку просроченных напоминаний ===
# Project: StudyTimer
def check_expired_reminders():
    now = datetime.datetime.now()
    expired = [r for r in reminders if r["time"] < now and not r["delivered"]]
    if expired:
        print(f"⚠️  Просрочено {len(expired)} напоминание(й):")
        for r in expired:
            print(f"   - {r['title']} (было в {r['time'].strftime('%H:%M')})")

check_expired_reminders()
