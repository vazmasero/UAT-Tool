@echo off
echo Converting .ui files to .py files...

REM Activar el entorno virtual
call .venv\Scripts\activate.bat

REM Verificar que pyside6-uic esté disponible
where pyside6-uic >nul 2>&1
if %errorlevel% neq 0 (
    echo Error: pyside6-uic no encontrado. Asegurate de que PySide6 este instalado en el entorno virtual.
    pause
    exit /b 1
)

echo Convirtiendo archivos UI...

pyside6-uic ui/form_drone.ui -o ui/ui_form_drone.py
pyside6-uic ui/form_operator.ui -o ui/ui_form_operator.py
pyside6-uic ui/form_email.ui -o ui/ui_form_email.py
pyside6-uic ui/form_uas_zone.ui -o ui/ui_form_uas_zone.py
pyside6-uic ui/form_uhub_org.ui -o ui/ui_form_uhub_org.py
pyside6-uic ui/form_uhub_user.ui -o ui/ui_form_uhub_user.py
pyside6-uic ui/form_uspace.ui -o ui/ui_form_uspace.py
pyside6-uic ui/form_bug.ui -o ui/ui_form_bug.py
pyside6-uic ui/form_campaign.ui -o ui/ui_form_campaign.py
pyside6-uic ui/form_case.ui -o ui/ui_form_case.py
pyside6-uic ui/form_block.ui -o ui/ui_form_block.py
pyside6-uic ui/add_step.ui -o ui/ui_add_step.py
pyside6-uic ui/main.ui -o ui/ui_main.py
pyside6-uic ui/execution_campaign.ui -o ui/ui_execution_campaign.py
pyside6-uic ui/info_campaign.ui -o ui/ui_info_campaign.py
pyside6-uic ui/dialog_action.ui -o ui/ui_dialog_action.py

echo Conversion completed!
pause