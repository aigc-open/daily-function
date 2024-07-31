# daily-function

日常开发封装装饰器等

## 输出执行时间

```python
from daily_function.basic import logger_execute_time

@logger_execute_time(doc="xxx")
def test():
    pass
```

## 文件安全目录

```python
from daily_function.basic import safe_dir
def test():
    with safe_dir() as _dir:
        pass
```

## generate_sorted_uuid

## pretty_print_dict

## GlobalConfig(全局配置，可文件可环境变量)

```python
from daily_function.global_config import GlobalConfig
class GlobalConfig_(GlobalConfig):
    name:str="xxx"


global_config = GlobalConfig_()
global_config.init_config(path=".conf/config.yaml")
global_config.init_env()
```

## gpt_cut_messages

```python
def test_cut_messages():
    from daily_function.gpt_cut_messages import cut_messages,cut_string,messages_token_count
    question = "hi你是谁呢"*100
    messages=[{"role": "user", "content": question}]*100
    token_limit = 200
    print(messages_token_count(messages,token_limit=200000))
    cut_messages(messages=messages, token_limit=token_limit)
    print(messages)
    print(len(messages))
    print(messages_token_count(messages,token_limit=200000))
```
