# === Stage 49: Добавь финальную самопроверку приложения и отчёт о готовности ===
# Project: StudyTimer
# StudyTimer v1.0 — Final Self-Check & Readiness Report

def self_check(study_session, goals, breaks, stats):
    """Run a final self-check on all StudyTimer components."""
    checks = []
    
    # Check 1: Study session has a topic and duration
    if study_session.get('topic') and study_session.get('duration', 0) > 0:
        checks.append("✓ Study session is properly configured")
    else:
        checks.append("✗ Study session needs topic and duration")
    
    # Check 2: Goals are set for the session
    if goals.get('goals', []) and len(goals['goals']) > 0:
        checks.append("✓ Goals are set for the session")
    else:
        checks.append("✗ No goals defined for the session")
    
    # Check 3: Break configuration exists
    if breaks.get('break_duration', 0) > 0:
        checks.append("✓ Break configuration is valid")
    else:
        checks.append("✗ Break duration not set")
    
    # Check 4: Study statistics are tracked
    if stats.get('total_study_time', 0) > 0 or stats.get('sessions_completed', 0) > 0:
        checks.append("✓ Study statistics are being tracked")
    else:
        checks.append("✗ Statistics not yet recorded")
    
    # Check 5: Focus score calculation
    if stats.get('focus_score', 0) > 0:
        checks.append("✓ Focus score is calculated")
    else:
        checks.append("✗ Focus score not yet computed")
    
    # Print readiness report
    print("=" * 50)
    print("STUDYTIMER FINAL SELF-CHECK REPORT")
    print("=" * 50)
    for check in checks:
        print(f"  {check}")
    print("=" * 50)
    
    all_passed = all("✓" in c for c in checks)
    if all_passed:
        print("🎉 ALL CHECKS PASSED - StudyTimer is ready to use!")
    else:
        print("⚠️ SOME CHECKS FAILED - Please review and fix the issues above.")
    
    print("=" * 50)
    return all_passed
