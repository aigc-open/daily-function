import os
from yaml import load
from loguru import logger
try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader
from pydantic import BaseModel


class GlobalConfig(BaseModel):

    def parse_config(self, path=".conf/config.yaml"):
        if not os.path.exists(path):
            return None
        with open(path, "r") as f:
            return load(f, Loader=Loader)

    def init_config(self, path=".conf/config.yaml"):
        # parse the config.yaml
        CONFIG = self.parse_config(path)
        if CONFIG:
            for k, v in CONFIG.items():
                if hasattr(self, k):
                    logger.info(f"修改配置: {k}={v}, type={type(v)}")
                    setattr(self, k, v)
                else:
                    logger.warning(f"参数{k}={v}设置失败,因为没有这个属性")

    def init_env(self):
        env_ = {}
        for k, v in os.environ.items():
            if hasattr(self, k):
                if type(getattr(self, k)) == bool:
                    if v.lower() == "true":
                        setattr(self, k, True)
                    elif v.lower() == "false":
                        setattr(self, k, False)
                    else:
                        setattr(self, k, False)
                else:
                    setattr(self, k, type(getattr(self, k))(v))
            else:
                logger.warning(f"参数{k}={v}设置失败,因为没有这个属性")
        return env_
