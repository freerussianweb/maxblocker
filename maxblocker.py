import subprocess
import os
import sys
import time

PACKAGE_NAME = "ru.oneme.app"


# Корректный путь для PyInstaller onefile
if hasattr(sys, "_MEIPASS"):
    BASE_PATH = sys._MEIPASS
else:
    BASE_PATH = os.path.dirname(__file__)

ADB_PATH = os.path.join(BASE_PATH, "adb.exe")


def run_adb(args):
    try:
        result = subprocess.run(
            [ADB_PATH] + args,
            capture_output=True,
            text=True
        )
        return result.returncode, result.stdout.strip(), result.stderr.strip()
    except Exception as e:
        return -1, "", str(e)


def start_server():
    run_adb(["start-server"])
    time.sleep(1)


def get_device_status():
    code, out, err = run_adb(["devices"])

    if code != 0:
        return "adb_error"

    lines = out.splitlines()[1:]  # пропускаем "List of devices attached"

    if not lines:
        return "no_device"

    for line in lines:
        if "unauthorized" in line:
            return "unauthorized"
        if "offline" in line:
            return "offline"
        if "\tdevice" in line:
            return "device"

    return "unknown"


def is_package_installed():
    code, out, _ = run_adb(["shell", "pm", "list", "packages", PACKAGE_NAME])
    return PACKAGE_NAME in out


def disable_app():
    return run_adb(["shell", "pm", "disable-user", "--user", "0", PACKAGE_NAME])


def enable_app():
    return run_adb(["shell", "pm", "enable", PACKAGE_NAME])


def uninstall_app():
    return run_adb(["shell", "pm", "uninstall", "-k", "--user", "0", PACKAGE_NAME])


def print_device_error(status):
    if status == "no_device":
        print("Устройство не обнаружено.")
    elif status == "unauthorized":
        print("Телефон не авторизован.")
        print("Разблокируйте экран и подтвердите RSA-ключ.")
    elif status == "offline":
        print("Устройство offline. Переподключите кабель.")
    elif status == "adb_error":
        print("Ошибка запуска adb.")
    else:
        print("Неизвестная ошибка подключения.")


def main():
    print("=== Блокировка мессенджера Макс ===\n")

    print("Перед запуском убедитесь что:")
    print("- Включен режим разработчика")
    print("- Включена отладка по USB")
    print("- Телефон подключен к ПК\n")

    print("1) Отключить Макс")
    print("2) Включить Макс")
    print("3) Полностью удалить Макс\n")

    choice = input("Введите цифру: ").strip()

    print("\nЗапуск adb...")
    start_server()

    status = get_device_status()

    if status != "device":
        print_device_error(status)
        input("\nНажмите Enter для выхода...")
        return

    print("Устройство подключено.\n")

    if not is_package_installed():
        print("Пакет ru.max.messenger не найден на устройстве.")
        input("\nНажмите Enter для выхода...")
        return

    if choice == "1":
        code, out, err = disable_app()
    elif choice == "2":
        code, out, err = enable_app()
    elif choice == "3":
        code, out, err = uninstall_app()
    else:
        print("Неверный выбор.")
        return

    print("\nРезультат:")

    if code == 0:
        print(out if out else "Операция выполнена.")
    else:
        print("Ошибка:")
        print(err)

    input("\nНажмите Enter для выхода...")


if __name__ == "__main__":
    main()
