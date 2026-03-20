---
title: OpenClaw的win安装教程
cover: /Users/lzc/TNTprojectZ/CoolMessageInformationKnowledge/asset/openclaw教程.png
---
_**第一步**_ 点击键盘上的“win”，在搜索栏中搜索PowerShell

然后点击“以管理员身份运行”


如果PowerShell打不开，也可以用CMD（命令提示符）,同样也是用“以管理员身份运行” 然后输入

```Bash
wsl --install
```

这个命令的意思是安装WSL，安装好之后，它会让你重启电脑，那你就重启一下电脑。

  

_**第二步**_

重启完之后再次打开PowerShell/CMD的界面，再输入这个命令：

```Bash
wsl --install ubuntu-24.04
```

这个命令是安装Ubuntu Linux发行版。

  

下载完之后，需要你创建一个用户名和密码（自己设置即可）



  

设置好之后，能看到这个有颜色的一行，就说明成功进入了Linux的系统界面了。



  

接下来我们的所有操作就得在这里进行了，如果不小心退出了，可以再次点开PowerShell/CMD的界面，输入“wsl”，再回车，重新进入Linux的系统界面

_**第三步**_ 接下来在Linux的系统界面输入以下命令（下载OpenClaw）

```Bash
curl -fsSL https://openclaw.ai/install.sh | bash
```

这是官方推荐的一键安装脚本，它的好处是可以直接帮你处理环境依赖关系，比如它检测到你没有安装node.js，它会自动帮你安装它。



  

需要注意两点：

1.记得在这里输入你刚刚设置的密码



2.当你发现电脑半天没反应，没有输出的时候，看看是不是有这个单词“Installing”，它的意思是正在安装，期间没有任何输出，是正常情况，请稍等。



  

当出现这个欢迎界面的时候，就说明已经安装好了



  

```Bash
openclaw dashboard
```

  

会跳出控制台。如果没跳出，可以复制这个网址，用浏览器打开。



  

然后依次选择 Setting（设置）＞Config（配置） > Authentication，点击菜单下方的 Raw。



  

复制以下配置信息，替换原"agents": {...},部分，并将baseUrl及 apikey 替换为你自己的。

```Bash
{
  "models": {
    "mode": "merge",
    "providers": {
      "bailian": {
        "baseUrl": "https://coding.dashscope.aliyuncs.com/v1",
        "apiKey": "YOUR_API_KEY",
        "api": "openai-completions",
        "models": [
          {
            "id": "MiniMax-M2.5",
            "name": "MiniMax-M2.5",
            "reasoning": false,
            "input": ["text"],
            "cost": {
              "input": 0,
              "output": 0,
              "cacheRead": 0,
              "cacheWrite": 0
            },
            "contextWindow": 196608,
            "maxTokens": 32768
          }
        ]
      }
    }
  },
  "agents": {
    "defaults": {
      "model": {
        "primary": "bailian/MiniMax-M2.5"
      }
    }
  },
  "gateway": {
    "mode": "local"
  }
}
```

配置完成后，单击右上角 **Save** 保存配置，再单击 **Update**。