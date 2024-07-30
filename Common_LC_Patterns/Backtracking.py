def backtrack(curr, other_args):
    if base_case(curr, other_args):
        # Modify the answer
        return base_case_result
    
    ans = 0
    for item in iterable_input:
        # modify the current state
        modify_current_state(curr, item)
        # recursively call backtrack
        ans += backtrack(curr, other_args)
        # undo the modification of the current state
        undo_modification(curr, item)
    
    return ans