from pathlib import Path
HTML = """<!DOCTYPE html>
<html lang="ru">
<head><meta charset="UTF-8"><title>АНО ВО «Университет «Синергия»</title>
<link href="https://fonts.googleapis.com/css2?family=Fira+Sans&family=Inter&family=Montserrat:wght@400;700&family=Open+Sans&family=PT+Serif&family=Roboto&display=swap" rel="stylesheet">
<style>
    body { font-family: 'Montserrat', sans-serif; background: #f4f7fb; padding: 30px; }
    header { background: #18224b; color: #fff; padding: 30px; border-radius: 12px; }
    .card { background: #fff; padding: 22px; border-radius: 10px; margin-top: 16px; }
    .f-v1 { font-family: 'Roboto', sans-serif; }
    .f-v2 { font-family: 'Open Sans', sans-serif; }
    .f-v3 { font-family: 'Inter', sans-serif; }
    .f-v4 { font-family: 'PT Serif', serif; }
    .f-v5 { font-family: 'Fira Sans', sans-serif; }
</style></head>
<body>
    <header><h1>АНО ВО «Университет «Синергия»</h1></header>
    <div class="card">Официальный шрифт (Montserrat): Платформа дистанционного обучения</div>
    <div class="card f-v1">Вариант 1 (Roboto): Платформа дистанционного обучения</div>
    <div class="card f-v2">Вариант 2 (Open Sans): Платформа дистанционного обучения</div>
    <div class="card f-v3">Вариант 3 (Inter): Платформа дистанционного обучения</div>
    <div class="card f-v4">Вариант 4 (PT Serif): Платформа дистанционного обучения</div>
    <div class="card f-v5">Вариант 5 (Fira Sans): Платформа дистанционного обучения</div>
</body></html>"""
Path("index.html").write_text(HTML, encoding="utf-8")
print("HTML-страница создана.")
