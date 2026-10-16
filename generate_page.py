#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Программа-генератор HTML-страницы об организации прохождения практики
с демонстрацией официального корпоративного шрифта и 5 альтернативных вариантов.
"""

from pathlib import Path

ORGANIZATION_NAME = "САО «ВСК» (Страховой Дом ВСК)"

HTML_TEMPLATE = f"""<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{ORGANIZATION_NAME}</title>
    <!-- Подключение официального шрифта (Montserrat) и 5 альтернативных вариантов из Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Fira+Sans:wght@400;600&family=Inter:wght@400;600&family=Montserrat:wght@400;600;700&family=Open+Sans:wght@400;600&family=PT+Serif:wght@400;700&family=Roboto:wght@400;500;700&display=swap" rel="stylesheet">
    <style>
        :root {{
            --primary-color: #004b93;
            --accent-color: #e30613;
            --bg-color: #f4f7fb;
            --card-bg: #ffffff;
            --text-color: #1f2937;
            /* Официальный корпоративный шрифт веб-платформ компании */
            --font-official: 'Montserrat', sans-serif;
            /* 5 дополнительных вариантов шрифтов */
            --font-variant-1: 'Roboto', sans-serif;
            --font-variant-2: 'Open Sans', sans-serif;
            --font-variant-3: 'Inter', sans-serif;
            --font-variant-4: 'PT Serif', serif;
            --font-variant-5: 'Fira Sans', sans-serif;
        }}

        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }}

        body {{
            font-family: var(--font-official);
            background-color: var(--bg-color);
            color: var(--text-color);
            line-height: 1.6;
            padding: 30px 20px;
            transition: font-family 0.2s ease;
        }}

        .container {{
            max-width: 1000px;
            margin: 0 auto;
        }}

        header {{
            background: linear-gradient(135deg, var(--primary-color), #002d5a);
            color: #ffffff;
            padding: 35px 40px;
            border-radius: 12px;
            margin-bottom: 30px;
            box-shadow: 0 8px 20px rgba(0, 75, 147, 0.15);
            border-bottom: 4px solid var(--accent-color);
        }}

        header h1 {{
            font-size: 28px;
            margin-bottom: 10px;
        }}

        header p {{
            opacity: 0.9;
            font-size: 16px;
        }}

        .info-card {{
            background: var(--card-bg);
            padding: 30px;
            border-radius: 12px;
            margin-bottom: 30px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
        }}

        .info-card h2 {{
            color: var(--primary-color);
            margin-bottom: 15px;
            font-size: 22px;
        }}

        .info-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 15px;
            margin-top: 20px;
        }}

        .info-item {{
            background: #f8fafc;
            padding: 15px;
            border-left: 4px solid var(--primary-color);
            border-radius: 6px;
        }}

        .info-item strong {{
            display: block;
            color: var(--primary-color);
            margin-bottom: 5px;
        }}

        .fonts-section h2 {{
            color: var(--primary-color);
            margin-bottom: 20px;
            font-size: 22px;
        }}

        .font-sample {{
            background: var(--card-bg);
            padding: 22px 25px;
            border-radius: 10px;
            margin-bottom: 16px;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
            border: 1px solid #e5e7eb;
        }}

        .font-sample.official {{
            border: 2px solid var(--primary-color);
            background: #f0f7ff;
        }}

        .font-badge {{
            display: inline-block;
            padding: 4px 12px;
            font-size: 12px;
            font-weight: 600;
            border-radius: 20px;
            background: var(--primary-color);
            color: #fff;
            margin-bottom: 10px;
        }}

        .font-official {{ font-family: var(--font-official); }}
        .font-v1 {{ font-family: var(--font-variant-1); }}
        .font-v2 {{ font-family: var(--font-variant-2); }}
        .font-v3 {{ font-family: var(--font-variant-3); }}
        .font-v4 {{ font-family: var(--font-variant-4); }}
        .font-v5 {{ font-family: var(--font-variant-5); }}
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>{ORGANIZATION_NAME}</h1>
            <p>Организация прохождения производственной (проектно-технологической) практики</p>
        </header>

        <section class="info-card">
            <h2>Сведения об организации</h2>
            <p>
                <strong>Страховой Дом ВСК (САО «ВСК»)</strong> — одна из крупнейших универсальных
                страховых компаний России, реализующая передовые цифровые и ИТ-решения в сфере
                InsurTech, автоматизированного тестирования, микросервисной архитектуры и DevOps.
            </p>
            <div class="info-grid">
                <div class="info-item">
                    <strong>Организационно-правовая форма</strong>
                    Непубличное акционерное общество (САО «ВСК»)
                </div>
                <div class="info-item">
                    <strong>Центральный офис</strong>
                    г. Москва, ул. Островная, д. 4 (более 75 филиалов по РФ)
                </div>
                <div class="info-item">
                    <strong>Ключевые направления ИТ</strong>
                    Разработка ПО, QA и автотестирование, DevOps (CI/CD, Kubernetes), СУБД и телеком
                </div>
            </div>
        </section>

        <section class="fonts-section">
            <h2>Демонстрация официального шрифта и 5 дополнительных вариантов</h2>

            <div class="font-sample official font-official">
                <span class="font-badge">Официальный шрифт компании: Montserrat</span>
                <h3>{ORGANIZATION_NAME}</h3>
                <p>Страховое акционерное общество «ВСК» — цифровая экосистема страховых и ИТ-сервисов. 0123456789</p>
            </div>

            <div class="font-sample font-v1">
                <span class="font-badge">Вариант 1: Roboto (Sans-Serif)</span>
                <h3>{ORGANIZATION_NAME}</h3>
                <p>Страховое акционерное общество «ВСК» — цифровая экосистема страховых и ИТ-сервисов. 0123456789</p>
            </div>

            <div class="font-sample font-v2">
                <span class="font-badge">Вариант 2: Open Sans (Humanist Sans-Serif)</span>
                <h3>{ORGANIZATION_NAME}</h3>
                <p>Страховое акционерное общество «ВСК» — цифровая экосистема страховых и ИТ-сервисов. 0123456789</p>
            </div>

            <div class="font-sample font-v3">
                <span class="font-badge">Вариант 3: Inter (UI Neo-Grotesque)</span>
                <h3>{ORGANIZATION_NAME}</h3>
                <p>Страховое акционерное общество «ВСК» — цифровая экосистема страховых и ИТ-сервисов. 0123456789</p>
            </div>

            <div class="font-sample font-v4">
                <span class="font-badge">Вариант 4: PT Serif (Классическая антиква с засечками)</span>
                <h3>{ORGANIZATION_NAME}</h3>
                <p>Страховое акционерное общество «ВСК» — цифровая экосистема страховых и ИТ-сервисов. 0123456789</p>
            </div>

            <div class="font-sample font-v5">
                <span class="font-badge">Вариант 5: Fira Sans (Гуманистический гротеск)</span>
                <h3>{ORGANIZATION_NAME}</h3>
                <p>Страховое акционерное общество «ВСК» — цифровая экосистема страховых и ИТ-сервисов. 0123456789</p>
            </div>
        </section>
    </div>
</body>
</html>
"""

def main():
    output_path = Path("index.html")
    output_path.write_text(HTML_TEMPLATE, encoding="utf-8")
    print(f"HTML-страница успешно сгенерирована: {output_path.resolve()}")

if __name__ == "__main__":
    main()
