# === Stage 2: Добавь модели данных и функции валидации пользовательского ввода ===
# Project: StudyTimer
class StudyTimerModel:
    def __init__(self):
        self.topics = []
        self.goals = []
        self.sessions = []
    
    def add_topic(self, name: str) -> bool:
        if not isinstance(name, str) or len(name.strip()) == 0:
            return False
        if any(t['name'].lower() == name.lower() for t in self.topics):
            return False
        self.topics.append({'id': len(self.topics) + 1, 'name': name})
        return True
    
    def add_goal(self, topic_id: int, description: str, duration_minutes: int) -> bool:
        if not isinstance(topic_id, int) or topic_id <= 0:
            return False
        if not isinstance(description, str) or len(description.strip()) == 0:
            return False
        if not isinstance(duration_minutes, int) or duration_minutes < 5:
            return False
        if topic_id > len(self.topics):
            return False
        self.goals.append({'id': len(self.goals) + 1, 'topic_id': topic_id, 
                           'description': description, 'duration_minutes': duration_minutes})
        return True
    
    def start_session(self, goal_id: int, break_duration: int = 5) -> dict | None:
        if not isinstance(goal_id, int) or goal_id <= 0:
            return {'error': 'Invalid goal ID'}
        if not isinstance(break_duration, int) or break_duration < 1:
            return {'error': 'Invalid break duration'}
        
        target_goal = next((g for g in self.goals if g['id'] == goal_id), None)
        if not target_goal:
            return {'error': 'Goal not found'}
        
        topic_name = next((t['name'] for t in self.topics if t['id'] == target_goal['topic_id']), 'Unknown')
        session_start = datetime.now()
        session_end = session_start + timedelta(minutes=target_goal['duration_minutes'])
        
        self.sessions.append({
            'goal_id': goal_id,
            'topic_name': topic_name,
            'start_time': session_start.isoformat(),
            'end_time': session_end.isoformat(),
            'break_duration': break_duration,
            'status': 'active'
        })
        
        return {'message': f'Session started for {topic_name}', 'session_id': len(self.sessions)}
    
    def end_session(self, session_id: int) -> dict | None:
        if not isinstance(session_id, int) or session_id <= 0:
            return {'error': 'Invalid session ID'}
        
        active_sessions = [s for s in self.sessions if s['status'] == 'active']
        target_session = next((s for s in active_sessions if s['id'] == session_id), None)
        
        if not target_session:
            return {'error': 'Session not found or already ended'}
        
        actual_duration = datetime.now() - datetime.fromisoformat(target_session['start_time'])
        target_session['actual_duration_minutes'] = int(actual_duration.total_seconds() / 60)
        target_session['status'] = 'completed'
        
        return {'message': f'Session completed', 'duration_minutes': actual_duration.total_seconds() / 60}

from datetime import datetime, timedelta
