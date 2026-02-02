def planner_prompt(user_prompt):
    planner_prompt = f"""
    You are the PLANNER agent. your task is to convert the user prompt into a COMPLETE engineering project plan
    user request: {user_prompt}
    """
    return planner_prompt