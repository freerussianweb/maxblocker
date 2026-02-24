@echo off
chcp 1251 >nul
color 0A

echo.
echo  === MAXBLOCKER - Otklyuchenie messendzhera Max ===
echo.
echo  VNIMANIE! Pered zapuskom ubedites chto:
echo.
echo  [1] ADB skachan s sayta Google i dobavlen v PATH:
echo      https://developer.android.com/studio/releases/platform-tools
echo.
echo  [2] Smartfon podklyuchen k kompyuteru cherez USB
echo.
echo  [3] Ekran smartfona razblokirovan
echo.
echo  [4] Rezhim razrabotchika aktivirovan:
echo      Nastroyki - O telefone - nazhat "Nomer sborki" 7 raz
echo.
echo  [5] Otladka po USB vklyuchena:
echo      Nastroyki - Dlya razrabotchikov - Otladka po USB
echo.
echo  [6] Na smartfone podtverdite RSA-otpechatok esli poyavitsya zapros
echo.
echo  ------------------------------------------------------------------
echo.
pause

echo.
echo  Proveryaem podklyuchenie ustroystva...
echo.
adb start-server >nul 2>&1
adb devices

echo.
echo  ------------------------------------------------------------------
echo  Vyberite deystvie:
echo.
echo  [1] Otklyuchit Max (disable-user)
echo  [2] Udalit Max dlya tekushchego polzovatelya (uninstall --user 0)
echo  [3] Vklyuchit Max obratno (enable)
echo  [4] Vyhod
echo.
set /p choice=Vvedite nomer i nazhmite Enter: 

if "%choice%"=="1" goto disable
if "%choice%"=="2" goto uninstall
if "%choice%"=="3" goto enable
if "%choice%"=="4" goto finish

echo  Neverniy vybor. Zapustite skript zanovo.
goto finish

:disable
echo.
echo  Otklyuchaem messenger Max...
adb shell pm disable-user --user 0 ru.max.messenger
echo.
echo  Gotovo! Max otklyuchen. Prilozhenie ne budet zapuskatsya.
goto end

:uninstall
echo.
echo  Udalyaem Max dlya tekushchego polzovatelya...
adb shell pm uninstall -k --user 0 ru.max.messenger
echo.
echo  Gotovo! Max udalen dlya polzovatelya 0.
echo  APK ostaetsya v /system, no prilozhenie polnostyu neaktivno.
goto end

:enable
echo.
echo  Vklyuchaem Max obratno...
adb shell pm enable ru.max.messenger
echo.
echo  Gotovo! Max vklyuchen.
goto end

:end
echo.
echo  ------------------------------------------------------------------
echo  Operatsiya zavershena. Mozhno otklyuchit telefon.
echo  ------------------------------------------------------------------
echo.

:finish
pause
