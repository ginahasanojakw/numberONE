# === Stage 40: Добавь CLI-параметры через argparse для основных операций ===
# Project: StudyTimer
import sys
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="StudyTimer CLI")
    parser.add_argument("--theme", type=str, help="Тема сессии")
    parser.add_argument("--goal", type=str, help="Цель сессии")
    parser.add_argument("--duration", type=int, default=25, help="Длительность в минутах")
    parser.add_argument("--break-min", type=int, default=5, help="Длительность перерыва в минутах")
    parser.add_argument("--focus", type=float, default=0.9, help="Коэффициент концентрации")
    return parser.parse_args()

args = parse_args()
if args.theme:
    print(f"Тема: {args.theme}")
if args.goal:
    print(f"Цель: {args.goal}")
print(f"Длительность: {args.duration} мин")
print(f"Перерыв: {args.break_min} мин")
print(f"Концентрация: {args.focus}")
