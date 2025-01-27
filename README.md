Musiclang
=========

![MusicLang logo](https://github.com/MusicLang/musiclang/blob/main/documentation/images/MusicLang.png?raw=true "MusicLang")


[![Documentation Status](https://readthedocs.org/projects/musiclang/badge/?version=latest)](https://musiclang.readthedocs.io/en/latest/?badge=latest)

The Python framework to write, analyze, transform and predict music.


What is MusicLang ?
--------------------

MusicLang which simply stands for "music language" is a Python framework
implementing a new language for tonal music.
This language allows composers to load, write, transform and predict symbolic music in a simple,
condensed and high level manner.

MusicLang internally uses a [LLM (Large Language Model)](https://huggingface.co/floriangardin/musiclang)  to predict what could happen next in a musical score.
/!\ Please note that : we decoupled AI from the language itself in a new package called musiclang_predict. If you want to use AI capabilities of musiclang please install [musiclang_predict](https://github.com/MusicLang/musiclang_predict) package.

This framework is well suited to :
- Generate musical ideas quickly.
- Do symbolic music prediction or inpainting.
- Create an interpretable and rich text representation of a midi file


[Read our documentation](https://musiclang.readthedocs.io/en/latest).


How to install
--------------

MusicLang is available on Pypi :

```
pip install musiclang
```

- Render In:     
- https://huggingface.co/spaces/asigalov61/Advanced-MIDI-Renderer

Examples
---------

1. A hello world example to create a C-major chord in musiclang and save it to midi :

```python
from musiclang.library import *

# Write a C major chord (First degree of C major scale)
score = (I % I.M)(piano=[s0, s2, s4])

# Store it to midi
score.to_midi('c_major.mid')
```

2. Create, transform and harmonize a theme quickly : 

```python
from musiclang.library import *

# Create a cool melody (the beginning of happy birthday, independant of any harmonic context)
melody = s4.ed + s4.s + s5 + s4 + s0.o(1) + s6.h

# Create a simple accompaniment with a cello and a oboe
acc_melody = r + s0.o(-1).q * 3 + s0.o(-1).h
accomp = {'cello__0': acc_melody, 'oboe__0': acc_melody.o(1)}

# Play it in F-major
score = (I % IV.M)(violin__0=melody, **accomp)

# Repeat the score a second time in F-minor and forte
score += (score % I.m).f

# Just to create an anachrusis at the first bar
score = (I % I.M)(violin__0=r.h) + score

# Transform a bit the accompaniment by applying counterpoint rules automatically
score = score.get_counterpoint(fixed_parts=['violin__0'])

score.to_midi('happy_birthday.mid')

# Save it to musicxml
score.to_musicxml('happy_birthday.musicxml', signature=(3, 4), title='Happy birthday !')

# Et voilà !
```
![Happy birthday score](https://github.com/MusicLang/musiclang/blob/main/documentation/images/happy_birthday.png?raw=true "Happy Birthday")


3. Predict a score using a deep learning model trained on musiclang language :

See [MusicLang Predict](https://github.com/MusicLang/musiclang_predict) for more information.


- Infer Demp
```python
以下是将代码整理为单个 `.py` 文件的版本：

```python
# -*- coding: utf-8 -*-

# 安装所需的库
!pip install openai

# 下载 musiclang 的 library.py 文件
!wget https://raw.githubusercontent.com/svjack/musiclang/refs/heads/main/musiclang/write/library.py -O library.py

from openai import OpenAI

# 设置 API 密钥
api_key = ""

# 初始化 OpenAI 客户端
client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com")

# 读取 library.py 文件内容
with open("library.py", "r") as f:
    library_str = f.read()

# 使用 deepseek-chat 模型生成音乐相关的知识
model_name = "deepseek-chat"
response = client.chat.completions.create(
    model=model_name,
    messages=[
        {"role": "system", "content": "你是一个AI音乐创作作家。"},
        {"role": "user", "content": "下面是一些音乐相关的python代码定义，你想到了什么？" + "\n" + library_str},
    ],
    stream=False
)

# 打印生成的音乐知识
print(response.choices[0].message.content)

# 将生成的音乐知识保存到文件中
with open("library_knowledge.txt", "w") as f:
    f.write(response.choices[0].message.content)

# 读取保存的音乐知识
with open("library_knowledge.txt", "r") as f:
    library_knowledge = f.read()

# 定义生成《生日快乐》MIDI 文件的 Python 代码
produce_midi_py = '''
下面是根据上面的知识生成 happy_birthday mid 的python代码
```python
from musiclang.library import *

# Create a cool melody (the beginning of happy birthday, independant of any harmonic context)
melody = s4.ed + s4.s + s5 + s4 + s0.o(1) + s6.h

# Create a simple accompaniment with a cello and a oboe
acc_melody = r + s0.o(-1).q * 3 + s0.o(-1).h
accomp = {'cello__0': acc_melody, 'oboe__0': acc_melody.o(1)}

# Play it in F-major
score = (I % IV.M)(violin__0=melody, **accomp)

# Repeat the score a second time in F-minor and forte
score += (score % I.m).f

# Just to create an anachrusis at the first bar
score = (I % I.M)(violin__0=r.h) + score

# Transform a bit the accompaniment by applying counterpoint rules automatically
score = score.get_counterpoint(fixed_parts=['violin__0'])

score.to_midi('happy_birthday.mid')
```
'''

# 定义用户提示，要求生成《一闪一闪亮晶晶》的 Python 代码
user_prompt = produce_midi_py + "\n" + "现在要求你给出《一闪一闪亮晶晶》的python生成代码。注意格式相同"

# 使用 deepseek-chat 模型生成《一闪一闪亮晶晶》的 Python 代码
model_name = "deepseek-chat"
response = client.chat.completions.create(
    model=model_name,
    messages=[
        {"role": "system", "content": "你是一个AI音乐创作作家。"},
        {"role": "user", "content": "下面是一些音乐相关的python代码定义，你想到了什么？" + "\n" + library_str},
        {"role": "assistant", "content": library_knowledge},
        {"role": "user", "content": user_prompt}
    ],
    stream=False  # 启用流式输出
)

# 打印生成的《一闪一闪亮晶晶》的 Python 代码
print(response.choices[0].message.content)
```


Contact us
----------

If you want to help shape the future of open source music generation / language modeling,
please contact [us](mailto:fgardin.pro@gmail.com)

License
-------

The MusicLang base language (this package) is licensed under the BSD 3-Clause License.
The MusicLang predict package and its associated models is licensed under the GPL-3.0 License.


