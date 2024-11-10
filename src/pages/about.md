---
layout: ../layouts/Layout.astro
---

## 关于此站

用来发布`notebook`。

## 编程语言

- 🐍python
- 🫘javascript

## 技术流程

- `jupyter notebook`：用来编写包括大量数据分析和图表的笔记。
- `jupyter nbconvert`：将ipynb格式笔记转换为html格式。
- `astro`框架：用来发布html格式的笔记。
    - html文件保存在`src/components`目录下。
    - 使用python脚本在`src/pages`目录下创建对应的astro文件。
    - 使用框架提供的glob函数创建导航页面。

