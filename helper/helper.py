from os.path import dirname, abspath
import platform


def get_driver() -> str:
    """
    Get pyttsx3 driver according to the platform.
    :return:
    """
    op_sys = platform.platform()

    if "macOS" in op_sys:
        return "nsss"
    elif "Windows" in op_sys:
        return "sapi5"
    else:
        raise Exception("Not supported platform.")


def clear():
    """
    Clear screen.
    :return:
    """
    for i in range(100):
        print()


def get_project_path():
    return dirname(dirname(abspath(__file__)))
