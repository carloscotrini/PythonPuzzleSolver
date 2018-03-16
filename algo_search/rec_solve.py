

def rec_search(state):

    for act in state.next_actions():
        new_state = state.apply(act)
        if new_state.solved():
            return new_state
        elif new_state.consistent():
            result_state = rec_search(new_state)
            if result_state is not None and result_state.solved():
                return result_state

    return None
