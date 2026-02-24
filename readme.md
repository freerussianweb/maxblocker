# 🚫 MaxBlocker — Disable Preinstalled "Max" Messenger on Android

> **A lightweight ADB-based tool to disable, remove, or re-enable the "Max" messenger on Android devices in Russia — no root required.**

---

## 📖 Background

In 2025–2026, it has become increasingly common in Russia to purchase smartphones with preinstalled system software — particularly the **"Max" messenger** — that cannot be removed through standard Android tools.

If an application cannot be removed through the Android interface, that does **not** mean it cannot be disabled.

This project gives you two ways to take back control:
- **`maxblocker.exe`** — a portable GUI-like utility (Windows)
- **`maxblocker.bat`** — a simple batch script using ADB directly
- **Manual ADB commands** — full control, no executable needed

---

## ⚙️ Prerequisites

Before using any method, complete the following steps on your Android device:

### 1. Enable Developer Mode
1. Open **Settings**
2. Go to **About Phone**
3. Find **Build Number**
4. Tap it **7 times**
5. You'll see: _"You are now a developer"_

### 2. Enable USB Debugging
1. Go to **Settings → Developer Options**
2. Enable **USB Debugging**
3. Confirm the warning

### 3. Connect to PC
1. Connect your smartphone via **USB**
2. Unlock the device
3. Confirm the **RSA fingerprint** prompt if shown

---

## 🖥️ Method 1 — maxblocker.bat (Batch Script)

A ready-made Windows batch script that guides you through the process with a simple interactive menu.

### Requirements
- [Android Platform Tools (ADB)](https://developer.android.com/studio/releases/platform-tools) downloaded and added to your system **PATH**
- USB Debugging enabled (see Prerequisites above)
- Phone connected and screen unlocked

### Usage

1. Download **`maxblocker.bat`**
2. Double-click to run _(or run from CMD)_
3. Read the on-screen checklist and press any key to continue
4. Choose an action from the menu:

```
[1] Disable Max      — pm disable-user --user 0
[2] Remove Max       — pm uninstall -k --user 0
[3] Re-enable Max    — pm enable
[4] Exit
```

The script will:
- Start the ADB server
- Detect your connected device
- Execute the selected command automatically
- Confirm the result

> ℹ️ The `.bat` file is plain text — open it in any text editor to inspect every command before running.

---

## 💻 Method 2 — maxblocker.exe (Portable Utility)

A portable Windows executable that wraps ADB commands in a simple interface.

### Menu Options
| Option | Action |
|--------|--------|
| `1` | Disable Max |
| `2` | Enable Max |
| `3` | Remove Max (current user) |

All operations are performed automatically via ADB.

---

## 🔧 Method 3 — Manual ADB Commands

Prefer full manual control? Use these commands directly:

**1. Download Platform Tools**
```
https://developer.android.com/studio/releases/platform-tools
```

**2. Check device connection**
```bash
adb devices
```

**3. Disable Max**
```bash
adb shell pm disable-user --user 0 ru.max.messenger
```

**4. Remove for current user**
```bash
adb shell pm uninstall -k --user 0 ru.max.messenger
```

**5. Re-enable Max**
```bash
adb shell pm enable ru.max.messenger
```

---

## 🧠 Why ADB Disable Is More Effective Than "Freezing"

Some Android shells allow you to "freeze" apps — but this is not the same as a true system-level disable.

| Method | Freezing | `pm disable-user` |
|--------|----------|-------------------|
| Removes from launcher | ⚠️ Sometimes | ✅ Yes |
| Prevents services | ❌ No | ✅ Yes |
| Blocks broadcast receivers | ❌ No | ✅ Yes |
| Stops background execution | ❌ No | ✅ Yes |
| Survives system updates | ❌ No | ✅ More reliable |

### What `pm uninstall -k --user 0` Does

This removes the app **for the current user** even if it's installed as a system app.

- The APK remains in `/system` — so the partition is untouched
- The app **cannot run**, has no user data, and executes **no code**
- This is the **cleanest non-root deactivation method** available

---

## 🔒 Security & Transparency

Both `maxblocker.exe` and `maxblocker.bat` are transparent by design:

| Property | Details |
|----------|---------|
| Language | Python (exe) / Batch (bat) |
| Build tool | PyInstaller |
| Network access | ❌ None |
| Hidden drivers | ❌ None |
| External libraries | ❌ None |
| Telemetry | ❌ None |
| Inspectable | ✅ Yes — decompile or read source |

The `.exe` can be extracted and inspected. The `.bat` is plain text. Only standard Android Package Manager commands are executed.

---

## ⚠️ Known Limitations

- USB Debugging **must** be enabled
- RSA fingerprint confirmation is required on first connection
- May be blocked on **corporate-managed devices**
- Settings must be **repeated after a factory reset**

---

## 📜 Conclusion

Android provides users with built-in control tools. ADB is one of them.

If a manufacturer or distributor preinstalls unwanted software, that does not mean the user must accept it.

**`maxblocker`** makes standard system commands accessible in a few clicks — nothing more, nothing less.

---

<div align="center">

_No root. No exploits. No tricks. Just ADB._

</div>
