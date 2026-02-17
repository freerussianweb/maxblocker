How to Disable the Preinstalled “Max” Messenger on Android (Properly)
Introduction

In 2025–2026, it is becoming increasingly difficult in Russia to purchase a smartphone without preinstalled system software — particularly the “Max” messenger.

Devices are now often sold with preinstalled applications that cannot be removed using standard Android tools. Additionally, discussions around IMEI registry initiatives may further complicate purchasing “gray market” devices without government-preinstalled software.

If an application cannot be removed through the Android interface, that does not mean it cannot be disabled.

I created a simple portable utility called:

maxblocker.exe


It allows you to:

Fully disable the application

Re-enable it if necessary

Remove it for the current user (even if it is a system app)

Everything can also be done manually via ADB. Instructions and commands are provided below.
If you prefer not to deal with ADB directly, you can use the ready-made tool.

Usage Instructions
1. Enable Developer Mode

Open Settings

Go to About Phone

Find Build Number

Tap it 7 times

You will see the message: “You are now a developer”

2. Enable USB Debugging

Go to Settings → Developer Options

Enable USB Debugging

Confirm the warning

3. Connect to PC

Connect the smartphone to your computer via USB

Unlock the device

Confirm the RSA fingerprint prompt (if shown)

4. Use the Utility

Run:

maxblocker.exe


Menu options:

1 — Disable Max
2 — Enable Max
3 — Remove Max (for current user)


All operations are performed automatically via ADB.

Why This Is More Effective Than “Freezing” the App
1. Freezing ≠ disable-user

Some Android shells allow you to “freeze” apps. However:

It often only restricts autostart

Services may remain active

System updates can re-enable it

Background processes may still exist

The command:

pm disable-user --user 0 ru.max.messenger


Performs a true system-level disable for the user.

This:

Removes the app from the launcher

Prevents services from starting

Blocks broadcast receivers

Stops background execution

2. Removing for User 0

Command:

pm uninstall -k --user 0 ru.max.messenger


This removes the app for the current user even if it is installed as a system app.

The APK remains in /system, but:

The app is inactive

It cannot run

It has no user data

It does not execute code

This is the cleanest non-root deactivation method available.

How the Utility Works

The utility is simply a wrapper around ADB.

It performs:

adb start-server
adb devices


Then checks if the package exists and executes one of:

Disable:
adb shell pm disable-user --user 0 ru.max.messenger

Enable:
adb shell pm enable ru.max.messenger

Remove:
adb shell pm uninstall -k --user 0 ru.max.messenger


No exploits.
No root.
No hidden tricks.
Only standard Android Package Manager commands.

How to Do Everything Manually (Without the Program)

If you prefer not to use the .exe file:

Download Android platform-tools from Google

Extract the archive

Open CMD in that folder

Check connection:
adb devices

Disable:
adb shell pm disable-user --user 0 ru.max.messenger

Remove for user:
adb shell pm uninstall -k --user 0 ru.max.messenger

Re-enable:
adb shell pm enable ru.max.messenger

About Security

The software is written in Python.

The .exe is built using PyInstaller

No hidden drivers

No external libraries

No network connections

Easily decompilable

Anyone can:

Extract the executable

Inspect the code

Verify that only ADB commands are executed

No telemetry.
No hidden behavior.

Important Limitations

USB debugging must be enabled

RSA fingerprint confirmation is required

May be blocked on corporate-managed devices

Must be repeated after factory reset

Conclusion

Android provides users with control tools.
ADB is one of them.

If a manufacturer or distributor preinstalls unwanted software, that does not mean the user must accept it.

maxblocker.exe simply makes a system command accessible in a few clicks.

If you prefer full manual control — use ADB directly.
