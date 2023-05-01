def calculate_showdown_result(mode, rank):
    if mode == "duoShowdown":
        if rank < 3:
            return "victory"
        else:
            return "defeat"
    else:
        if rank < 5:
            return "victory"
        else:
            return "defeat"