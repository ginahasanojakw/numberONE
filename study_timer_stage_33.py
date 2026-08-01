# === Stage 33: Добавь откат последнего действия там, где это разумно ===
# Project: StudyTimer
def undo(self):
            if not self._undo_stack:
                return
            action = self._undo_stack.pop()
            if isinstance(action, UndoableAction):
                action.undo()
                self._last_action = None
            elif isinstance(action, (TimerEvent, TimerStateUpdate)):
                # Revert state to last known snapshot
                for key in list(self._state_snapshot.keys()):
                    val = self._state_snapshot[key]
                    if hasattr(val, 'undo'):
                        val.undo()
            elif action == "start":
                self.stop_timer()
            elif action == "pause":
                self.resume_timer()
            elif action == "reset":
                self.reset_timer()
