finished: int = 0
successful: int = 0


def finish_test(success=True):
    global finished, successful
    finished += 1
    successful += 1 if success else 0


def run_util_tests():
    try:
        global finished, successful
        return (finished, successful)
    except Exception as e:
        print(e)
