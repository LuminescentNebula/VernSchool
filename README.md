# Программирование
Материалы для школьников

.ipynb - файлы Jupyter Notebook ([Подробнее](https://jupyter.org/install#jupyter-notebook))  
.py - файлы Python  
.drawio - файлы с схемами draw.io ([Подробнее](https://www.drawio.com/))


[JN.bat](JN.bat) - исполняемый файл для запуск Jupyter Notebook на Windows  
[JN.sh](JN.sh) - исполняемый файл для запуск Jupyter Notebook на Linux

```mermaid
---
title: Схема сборки релизов
---
flowchart LR
    subgraph "Исходные материалы"
        subgraph "Теория"
            T1[.ipynb]
            H1[.html]
            PP1[Презентации]
            P1[.py]
            D1[.drawio]
        end
        subgraph "Задания"
            Z1[Задания с ранжированием оценки<br> .html+.css]
            M1[Схемы .mmd]
            MD1[.md]
            W1[Задания по web<br> .html, .css, .js]
            W3[< !--png-- ><br>html]
        end
    end

    subgraph "VernSchool.zip"
        T1 -- nbconvert --> T2[.pdf]
        H1 -- pandoc --> H2[.pdf + .html]
        PP1 --> PP2[Презентации]
        P1 -- сменить <br>расширение --> P2[.txt]
        D1 -- drawpyo --> D2[.png <br> с белым фоном]
        Z1 -- pandoc --> Z2[.pdf]
        M1 -- mermaid --> M2[.png]
        MD1 --pandoc--> MD2[.png] 
        W1 --сменить <br>расширение--> W2[.html.txt, .css.txt, .js.txt]
        W3 -- pandoc --> W4[Скриншот страницы<br>.png]

    end
```

При сборке расширение меняется на .txt, потому что MЭШ не дает загружать другие файлы

