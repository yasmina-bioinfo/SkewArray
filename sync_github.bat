@echo off
echo ===================================================
echo 🔄 Synchronisation automatique avec GitHub...
echo ===================================================

git add -A
git commit -m "Auto-update %date% %time%"
git push

echo ✅ Synchronisation terminee.
pause
