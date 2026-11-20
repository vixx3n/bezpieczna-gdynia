@echo off
setlocal
pushd "%~dp0.." || exit /b 1

if not exist "data\raw\city_7_4_data.csv" (
    python scripts\download_data.py || goto :error
)

python scripts\prepare_data.py || goto :error

echo Otworz w przegladarce http://127.0.0.1:8000/
python -m http.server --bind 127.0.0.1 --directory src 8000
set "result=%errorlevel%"
popd
exit /b %result%

:error
echo Nie udalo sie przygotowac danych. Sprawdz komunikat powyzej.
popd
exit /b 1