HQML
=========
HQML starts as a fork of PureQML that bring QML technology into web. PureQML is a QML to HTML/javscript translator. Almost everything should be done in QML. This approach is very good until project start to scale. HQML makes more steps further, providing interoperability to other frontend codebases and improve developers UX. With HQML, you are able to cleanly separate UI and backend stuff. UI developers can create their fancy widgets in QML, while backend developers can still choose their favorite languages and tools to implement complex logic.


## Motivation

For a long time there's no good solution to implement fancy GUI, until everybody start using HTML/CSS and we were one of them. Due to the evolution of CSS, we are allowed to achieve plenty of cool effects. However, for creating UI, HTML uses wrong abstraction, it was originally designed to create documents. We started to think if there's better way for creating fancy UI? The answer is QML.

## QML

QML is a declarative language for designing user interface–centric applications. Inline JavaScript code handles imperative aspects. It should be treated as a new language rather than a hack on javascript.


## Install
```bash
git clone --recursive https://github.com/tim37021/HQML
```

## Usage
hqml <create|build|channel|config>

#### Create
Create new project in sepecified path
```bash
hqml create .
```

#### build
Build project in current working directory
```
hqml build
```

#### config
Configure "project" setting
```bash
hqml config --hot-reload=true
```