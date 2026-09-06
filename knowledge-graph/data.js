window.KB_DATA = {
 "generatedAt": "2026-09-06 14:40:04",
 "nodes": [
  {
   "id": "s:0",
   "type": "stage",
   "name": "0. Python 基础",
   "code": "0",
   "progress": 100
  },
  {
   "id": "s:1",
   "type": "stage",
   "name": "1. LLM 基础",
   "code": "1",
   "progress": 98
  },
  {
   "id": "s:2",
   "type": "stage",
   "name": "2. Agent 核心",
   "code": "2",
   "progress": 100
  },
  {
   "id": "m:0.1",
   "type": "module",
   "name": "0.1 语法与数据结构",
   "code": "0.1",
   "stage": "0"
  },
  {
   "id": "m:0.2",
   "type": "module",
   "name": "0.2 文件读写",
   "code": "0.2",
   "stage": "0"
  },
  {
   "id": "m:0.3",
   "type": "module",
   "name": "0.3 面向对象",
   "code": "0.3",
   "stage": "0"
  },
  {
   "id": "m:0.4",
   "type": "module",
   "name": "0.4 Git 与工具",
   "code": "0.4",
   "stage": "0"
  },
  {
   "id": "m:1.1",
   "type": "module",
   "name": "1.1 概念",
   "code": "1.1",
   "stage": "1"
  },
  {
   "id": "m:1.2",
   "type": "module",
   "name": "1.2 模型全景",
   "code": "1.2",
   "stage": "1"
  },
  {
   "id": "m:1.3",
   "type": "module",
   "name": "1.3 API 调用",
   "code": "1.3",
   "stage": "1"
  },
  {
   "id": "m:1.4",
   "type": "module",
   "name": "1.4 流式输出",
   "code": "1.4",
   "stage": "1"
  },
  {
   "id": "m:1.5",
   "type": "module",
   "name": "1.5 Prompt Engineering",
   "code": "1.5",
   "stage": "1"
  },
  {
   "id": "m:1.6",
   "type": "module",
   "name": "1.6 结构化输出",
   "code": "1.6",
   "stage": "1"
  },
  {
   "id": "m:2.1",
   "type": "module",
   "name": "2.1 Tool Calling",
   "code": "2.1",
   "stage": "2"
  },
  {
   "id": "m:2.2",
   "type": "module",
   "name": "2.2 Agent 循环手写（ReAct）",
   "code": "2.2",
   "stage": "2"
  },
  {
   "id": "m:2.3",
   "type": "module",
   "name": "2.3 记忆系统",
   "code": "2.3",
   "stage": "2"
  },
  {
   "id": "m:2.4",
   "type": "module",
   "name": "2.4 任务规划与分解",
   "code": "2.4",
   "stage": "2"
  },
  {
   "id": "m:2.5",
   "type": "module",
   "name": "2.5 Reflection 反思机制",
   "code": "2.5",
   "stage": "2"
  },
  {
   "id": "m:7.1",
   "type": "module",
   "name": "7.1 论文阅读（元能力）",
   "code": "7.1",
   "stage": "2"
  },
  {
   "id": "m:2.6",
   "type": "module",
   "name": "2.6 安全与护栏",
   "code": "2.6",
   "stage": "2"
  },
  {
   "id": "k:0.1:变量与数据类型",
   "type": "knowledge",
   "name": "变量与数据类型",
   "desc": "int/float/str/bool，类型由值决定",
   "module": "0.1",
   "stage": "0",
   "pitfalls": [
    {
     "num": 42,
     "err": "`int(msg[\"role\"])` ValueError",
     "fix": "求字符数用 `len()`"
    }
   ],
   "learned": true,
   "days": [
    3,
    1,
    7
   ]
  },
  {
   "id": "k:0.1:条件判断",
   "type": "knowledge",
   "name": "条件判断",
   "desc": "if/elif/else 分支，elif 可多个",
   "module": "0.1",
   "stage": "0",
   "pitfalls": [],
   "learned": true,
   "days": [
    1
   ]
  },
  {
   "id": "k:0.1:循环",
   "type": "knowledge",
   "name": "循环",
   "desc": "while（条件循环）/ for（遍历循环）+ break/continue",
   "module": "0.1",
   "stage": "0",
   "pitfalls": [],
   "learned": true,
   "days": [
    1,
    5
   ]
  },
  {
   "id": "k:0.1:四种数据结构",
   "type": "knowledge",
   "name": "四种数据结构",
   "desc": "list（有序可变）/ tuple（有序不可变）/ dict（键值对）/ set（去重）",
   "module": "0.1",
   "stage": "0",
   "pitfalls": [
    {
     "num": 39,
     "err": "`merged + recent_messages[1:]` 报错",
     "fix": "用 `[merged] + recent_messages[1:]` 包成列表再拼接"
    },
    {
     "num": 50,
     "err": "`id in list[dict]` 永远 False 不报错",
     "fix": "in 之前核对两边类型一致；查 id 集合用 set"
    }
   ],
   "learned": true,
   "days": [
    4,
    7,
    5
   ]
  },
  {
   "id": "k:0.1:内置函数",
   "type": "knowledge",
   "name": "内置函数",
   "desc": "sum/max/min/len/round/float 等",
   "module": "0.1",
   "stage": "0",
   "pitfalls": [
    {
     "num": 23,
     "err": "变量名 max/min 行为诡异",
     "fix": "别用内置函数名做变量名"
    }
   ],
   "learned": true,
   "days": [
    1
   ]
  },
  {
   "id": "k:0.1:字符串操作",
   "type": "knowledge",
   "name": "字符串操作",
   "desc": "split() 切分、strip() 去空格、f-string 格式化",
   "module": "0.1",
   "stage": "0",
   "pitfalls": [
    {
     "num": 5,
     "err": "f-string 内 `{'c': 42}` 格式冲突",
     "fix": "先存变量再放进 f-string"
    },
    {
     "num": 7,
     "err": "f-string 输出 `{student_level}` 字面量",
     "fix": "检查字符串前有 f"
    }
   ],
   "learned": true,
   "days": [
    1,
    3,
    2
   ]
  },
  {
   "id": "k:0.1:卫语句",
   "type": "knowledge",
   "name": "卫语句",
   "desc": "空值/非法输入提前 return，减少嵌套",
   "module": "0.1",
   "stage": "0",
   "pitfalls": [],
   "learned": true,
   "days": []
  },
  {
   "id": "k:0.1:异常处理",
   "type": "knowledge",
   "name": "异常处理",
   "desc": "try/except + 具体异常类型（ValueError/FileNotFoundError）",
   "module": "0.1",
   "stage": "0",
   "pitfalls": [],
   "learned": true,
   "days": [
    1,
    2,
    5
   ]
  },
  {
   "id": "k:0.2:with open()",
   "type": "knowledge",
   "name": "with open()",
   "desc": "自动管理资源，不用手动 close",
   "module": "0.2",
   "stage": "0",
   "pitfalls": [
    {
     "num": 52,
     "err": "落盘 FileNotFoundError",
     "fix": "写文件三件套：open(path, \"w\", encoding=\"utf-8\")"
    }
   ],
   "learned": true,
   "days": [
    2
   ]
  },
  {
   "id": "k:0.2:读取模式",
   "type": "knowledge",
   "name": "读取模式",
   "desc": "read() 全读 / readlines() 按行列表 / 逐行 for 遍历",
   "module": "0.2",
   "stage": "0",
   "pitfalls": [],
   "learned": true,
   "days": []
  },
  {
   "id": "k:0.2:CSV 解析套路",
   "type": "knowledge",
   "name": "CSV 解析套路",
   "desc": "读行 → strip → split → 类型转换 → 收集",
   "module": "0.2",
   "stage": "0",
   "pitfalls": [],
   "learned": true,
   "days": [
    2,
    1
   ]
  },
  {
   "id": "k:0.2:跳过表头",
   "type": "knowledge",
   "name": "跳过表头",
   "desc": "`lines[1:]` 切片",
   "module": "0.2",
   "stage": "0",
   "pitfalls": [
    {
     "num": 9,
     "err": "列名被当数据处理",
     "fix": "`for line in lines[1:]`"
    }
   ],
   "learned": true,
   "days": [
    2
   ]
  },
  {
   "id": "k:0.2:脏数据跳过",
   "type": "knowledge",
   "name": "脏数据跳过",
   "desc": "try/except 包裹类型转换，失败 continue",
   "module": "0.2",
   "stage": "0",
   "pitfalls": [],
   "learned": true,
   "days": [
    1,
    5,
    2
   ]
  },
  {
   "id": "k:0.3:class + __init__",
   "type": "knowledge",
   "name": "class + __init__",
   "desc": "类定义与构造方法，self 指实例本身",
   "module": "0.3",
   "stage": "0",
   "pitfalls": [],
   "learned": true,
   "days": [
    2,
    3
   ]
  },
  {
   "id": "k:0.3:实例属性 vs 方法",
   "type": "knowledge",
   "name": "实例属性 vs 方法",
   "desc": "属性不加括号，方法要加括号调用",
   "module": "0.3",
   "stage": "0",
   "pitfalls": [
    {
     "num": 18,
     "err": "把属性当方法调（b.title()）",
     "fix": "属性不加括号"
    }
   ],
   "learned": true,
   "days": [
    2
   ]
  },
  {
   "id": "k:0.3:__repr__",
   "type": "knowledge",
   "name": "__repr__",
   "desc": "魔法方法，控制 print(obj) 的输出",
   "module": "0.3",
   "stage": "0",
   "pitfalls": [],
   "learned": true,
   "days": [
    2,
    3
   ]
  },
  {
   "id": "k:0.3:布尔状态管理",
   "type": "knowledge",
   "name": "布尔状态管理",
   "desc": "用 available 等布尔属性控制状态（借/还）",
   "module": "0.3",
   "stage": "0",
   "pitfalls": [],
   "learned": true,
   "days": [
    2
   ]
  },
  {
   "id": "k:0.3:继承",
   "type": "knowledge",
   "name": "继承",
   "desc": "`class A(B):`，子类复用父类接口",
   "module": "0.3",
   "stage": "0",
   "pitfalls": [],
   "learned": true,
   "days": [
    3
   ]
  },
  {
   "id": "k:0.3:super().__init__()",
   "type": "knowledge",
   "name": "super().__init__()",
   "desc": "调父类构造，不传 self",
   "module": "0.3",
   "stage": "0",
   "pitfalls": [],
   "learned": true,
   "days": [
    3,
    2
   ]
  },
  {
   "id": "k:0.3:方法覆盖",
   "type": "knowledge",
   "name": "方法覆盖",
   "desc": "子类重写父类方法，各自实现",
   "module": "0.3",
   "stage": "0",
   "pitfalls": [],
   "learned": true,
   "days": [
    3
   ]
  },
  {
   "id": "k:0.3:isinstance()",
   "type": "knowledge",
   "name": "isinstance()",
   "desc": "验证继承关系",
   "module": "0.3",
   "stage": "0",
   "pitfalls": [],
   "learned": true,
   "days": [
    3,
    5
   ]
  },
  {
   "id": "k:0.3:@dataclass",
   "type": "knowledge",
   "name": "@dataclass",
   "desc": "自动生成 __init__/__repr__/__eq__，省 80% 样板代码",
   "module": "0.3",
   "stage": "0",
   "pitfalls": [],
   "learned": true,
   "days": [
    3,
    2
   ]
  },
  {
   "id": "k:0.3:field(default_factory=list)",
   "type": "knowledge",
   "name": "field(default_factory=list)",
   "desc": "可变默认值的正确写法",
   "module": "0.3",
   "stage": "0",
   "pitfalls": [
    {
     "num": 2,
     "err": "`self.tags = list[str] = []` 语法错误",
     "fix": "`self.tags: list[str] = []`"
    },
    {
     "num": 3,
     "err": "`self.tags : list[str] = []` 报错",
     "fix": "冒号紧跟变量名"
    },
    {
     "num": 4,
     "err": "f-string 输出带引号 `'a', 'b'`",
     "fix": "`', '.join(list)` 手动拼"
    }
   ],
   "learned": true,
   "days": [
    3
   ]
  },
  {
   "id": "k:0.3:Literal[1,2,3]",
   "type": "knowledge",
   "name": "Literal[1,2,3]",
   "desc": "限制取值只能是字面量集合",
   "module": "0.3",
   "stage": "0",
   "pitfalls": [],
   "learned": true,
   "days": [
    3
   ]
  },
  {
   "id": "k:0.3:类型注解 vs 赋值",
   "type": "knowledge",
   "name": "类型注解 vs 赋值",
   "desc": "`变量: 类型 = 值`，冒号管类型、等号管值",
   "module": "0.3",
   "stage": "0",
   "pitfalls": [],
   "learned": true,
   "days": [
    3
   ]
  },
  {
   "id": "k:0.4:Git 三区模型",
   "type": "knowledge",
   "name": "Git 三区模型",
   "desc": "工作区(add)→暂存区(commit)→本地仓库(push)→远程",
   "module": "0.4",
   "stage": "0",
   "pitfalls": [
    {
     "num": 36,
     "err": "git push 慢/超时",
     "fix": "正常现象，小项目可接受；必要时走代理"
    }
   ],
   "learned": true,
   "days": [
    1
   ]
  },
  {
   "id": "k:0.4:.gitignore",
   "type": "knowledge",
   "name": ".gitignore",
   "desc": "排除缓存/虚拟环境/IDE 配置",
   "module": "0.4",
   "stage": "0",
   "pitfalls": [],
   "learned": true,
   "days": [
    1
   ]
  },
  {
   "id": "k:0.4:conda + pip",
   "type": "knowledge",
   "name": "conda + pip",
   "desc": "环境管理；pip 用清华镜像加速",
   "module": "0.4",
   "stage": "0",
   "pitfalls": [
    {
     "num": 35,
     "err": "conda 环境混乱",
     "fix": "只用一个源"
    }
   ],
   "learned": true,
   "days": [
    1
   ]
  },
  {
   "id": "k:0.4:PYTHONUTF8=1",
   "type": "knowledge",
   "name": "PYTHONUTF8=1",
   "desc": "环境变量根治 Windows GBK 终端编码问题",
   "module": "0.4",
   "stage": "0",
   "pitfalls": [
    {
     "num": 31,
     "err": "终端输出 emoji 崩溃",
     "fix": "`setx PYTHONUTF8 1` 根治"
    }
   ],
   "learned": true,
   "days": [
    4,
    2
   ]
  },
  {
   "id": "k:1.1:AI→ML→DL→LLM→Agent",
   "type": "knowledge",
   "name": "AI→ML→DL→LLM→Agent",
   "desc": "俄罗斯套娃层级关系",
   "module": "1.1",
   "stage": "1",
   "pitfalls": [],
   "learned": true,
   "days": [
    4,
    5,
    7
   ]
  },
  {
   "id": "k:1.1:Token",
   "type": "knowledge",
   "name": "Token",
   "desc": "LLM 最小计数单位，1 token ≈ 1 英文词 ≈ 0.6 中文字",
   "module": "1.1",
   "stage": "1",
   "pitfalls": [],
   "learned": true,
   "days": [
    4,
    7
   ]
  },
  {
   "id": "k:1.1:参数（7B/70B）",
   "type": "knowledge",
   "name": "参数（7B/70B）",
   "desc": "模型\"脑容量\"，越大越强越贵",
   "module": "1.1",
   "stage": "1",
   "pitfalls": [],
   "learned": true,
   "days": [
    4
   ]
  },
  {
   "id": "k:1.1:训练 vs 推理",
   "type": "knowledge",
   "name": "训练 vs 推理",
   "desc": "训练=大厂烧钱造模型；推理=你用 API 答题",
   "module": "1.1",
   "stage": "1",
   "pitfalls": [],
   "learned": true,
   "days": [
    4
   ]
  },
  {
   "id": "k:1.1:幻觉",
   "type": "knowledge",
   "name": "幻觉",
   "desc": "LLM 本质是\"预测下一个词\"，不是查数据库",
   "module": "1.1",
   "stage": "1",
   "pitfalls": [],
   "learned": true,
   "days": [
    4,
    8
   ]
  },
  {
   "id": "k:1.1:上下文窗口",
   "type": "knowledge",
   "name": "上下文窗口",
   "desc": "一次能处理的 token 上限",
   "module": "1.1",
   "stage": "1",
   "pitfalls": [],
   "learned": true,
   "days": [
    7
   ]
  },
  {
   "id": "k:1.2:六家对比",
   "type": "knowledge",
   "name": "六家对比",
   "desc": "Claude（安全/代码）/ GPT（生态/多模态）/ Gemini（搜索）/ Llama（开源）/ DeepSeek（性价比/中文）/ Qwen（中文）",
   "module": "1.2",
   "stage": "1",
   "pitfalls": [],
   "learned": true,
   "days": [
    4
   ]
  },
  {
   "id": "k:1.2:选模型口诀",
   "type": "knowledge",
   "name": "选模型口诀",
   "desc": "日常 DeepSeek、写代码 Claude、多模态 GPT/Gemini、私有化 Llama/Qwen",
   "module": "1.2",
   "stage": "1",
   "pitfalls": [
    {
     "num": 27,
     "err": "模型不存在",
     "fix": "模型 ID 用连字符：`claude-haiku-4-5`"
    }
   ],
   "learned": true,
   "days": [
    4
   ]
  },
  {
   "id": "k:1.2:中转平台",
   "type": "knowledge",
   "name": "中转平台",
   "desc": "大陆调 Claude 的替代方案（jiekou.vip 等，OpenAI 兼容格式）",
   "module": "1.2",
   "stage": "1",
   "pitfalls": [
    {
     "num": 27,
     "err": "模型不存在",
     "fix": "模型 ID 用连字符：`claude-haiku-4-5`"
    }
   ],
   "learned": true,
   "days": [
    4
   ]
  },
  {
   "id": "k:1.3:HTTP 基础",
   "type": "knowledge",
   "name": "HTTP 基础",
   "desc": "GET/POST/Header/Body/JSON",
   "module": "1.3",
   "stage": "1",
   "pitfalls": [],
   "learned": true,
   "days": [
    4,
    5
   ]
  },
  {
   "id": "k:1.3:API Key 安全",
   "type": "knowledge",
   "name": "API Key 安全",
   "desc": "放 .env，用 python-dotenv 加载，绝不写进代码",
   "module": "1.3",
   "stage": "1",
   "pitfalls": [
    {
     "num": 14,
     "err": "返回了 API Key 而不是回复",
     "fix": "命名语义化，返回前核对"
    }
   ],
   "learned": true,
   "days": [
    4,
    5,
    3
   ]
  },
  {
   "id": "k:1.3:Messages 结构",
   "type": "knowledge",
   "name": "Messages 结构",
   "desc": "统一 messages 数组，换 base_url 即可换模型",
   "module": "1.3",
   "stage": "1",
   "pitfalls": [],
   "learned": true,
   "days": [
    4,
    5
   ]
  },
  {
   "id": "k:1.3:四角色",
   "type": "knowledge",
   "name": "四角色",
   "desc": "system（宪法，第一条）/ user（用户话）/ assistant（AI 回填）/ tool（工具结果）",
   "module": "1.3",
   "stage": "1",
   "pitfalls": [
    {
     "num": 30,
     "err": "KeyError: 'choices'",
     "fix": "顺序必须 assistant(tool_calls) → tool 结果 → assistant(final)"
    }
   ],
   "learned": true,
   "days": [
    4,
    5,
    7
   ]
  },
  {
   "id": "k:1.3:参数",
   "type": "knowledge",
   "name": "参数",
   "desc": "max_tokens、temperature",
   "module": "1.3",
   "stage": "1",
   "pitfalls": [],
   "learned": true,
   "days": []
  },
  {
   "id": "k:1.3:返回结构",
   "type": "knowledge",
   "name": "返回结构",
   "desc": "`response.json()[\"choices\"][0][\"message\"][\"content\"]`",
   "module": "1.3",
   "stage": "1",
   "pitfalls": [],
   "learned": true,
   "days": [
    4,
    5
   ]
  },
  {
   "id": "k:1.3:usage",
   "type": "knowledge",
   "name": "usage",
   "desc": "看 token 消耗（~84 token 固定开销）",
   "module": "1.3",
   "stage": "1",
   "pitfalls": [],
   "learned": true,
   "days": [
    4,
    7
   ]
  },
  {
   "id": "k:1.3:跨轮记忆",
   "type": "knowledge",
   "name": "跨轮记忆",
   "desc": "LLM 无状态，把整个 history 塞回 messages = 记忆",
   "module": "1.3",
   "stage": "1",
   "pitfalls": [],
   "learned": true,
   "days": [
    4,
    7,
    5
   ]
  },
  {
   "id": "k:1.4:SSE 协议",
   "type": "knowledge",
   "name": "SSE 协议",
   "desc": "每行 `data: {JSON}`，`data: [DONE]` 结束",
   "module": "1.4",
   "stage": "1",
   "pitfalls": [],
   "learned": true,
   "days": [
    4,
    5
   ]
  },
  {
   "id": "k:1.4:两处 stream",
   "type": "knowledge",
   "name": "两处 stream",
   "desc": "body `\"stream\": True` + 请求 `stream=True`",
   "module": "1.4",
   "stage": "1",
   "pitfalls": [
    {
     "num": 53,
     "err": "detect 对干净输入也返回 True",
     "fix": "遍历名单要遍历【列表】(PATTERNS)"
    }
   ],
   "learned": true,
   "days": [
    4
   ]
  },
  {
   "id": "k:1.4:yield 生成器",
   "type": "knowledge",
   "name": "yield 生成器",
   "desc": "产出后暂停，流式的灵魂",
   "module": "1.4",
   "stage": "1",
   "pitfalls": [],
   "learned": true,
   "days": [
    4
   ]
  },
  {
   "id": "k:1.4:iter_lines()",
   "type": "knowledge",
   "name": "iter_lines()",
   "desc": "逐行读取 SSE 数据块",
   "module": "1.4",
   "stage": "1",
   "pitfalls": [],
   "learned": true,
   "days": [
    4
   ]
  },
  {
   "id": "k:1.4:delta vs message",
   "type": "knowledge",
   "name": "delta vs message",
   "desc": "流式取 delta（增量），非流式取 message（完整）",
   "module": "1.4",
   "stage": "1",
   "pitfalls": [
    {
     "num": 28,
     "err": "流式没有 content",
     "fix": "`delta.get(\"content\") or delta.get(\"reasoning_content\")`"
    }
   ],
   "learned": true,
   "days": [
    4
   ]
  },
  {
   "id": "k:1.4:reasoning_content",
   "type": "knowledge",
   "name": "reasoning_content",
   "desc": "DeepSeek 推理模型的思考字段，需兜底取值",
   "module": "1.4",
   "stage": "1",
   "pitfalls": [
    {
     "num": 28,
     "err": "流式没有 content",
     "fix": "`delta.get(\"content\") or delta.get(\"reasoning_content\")`"
    }
   ],
   "learned": true,
   "days": [
    4
   ]
  },
  {
   "id": "k:1.5:System Prompt 四法则",
   "type": "knowledge",
   "name": "System Prompt 四法则",
   "desc": "角色+边界 / 输出格式约束 / 正向指令>负向 / Few-shot 锚定",
   "module": "1.5",
   "stage": "1",
   "pitfalls": [],
   "learned": true,
   "days": [
    4,
    6,
    7
   ]
  },
  {
   "id": "k:1.5:Zero-shot",
   "type": "knowledge",
   "name": "Zero-shot",
   "desc": "不举例直接问",
   "module": "1.5",
   "stage": "1",
   "pitfalls": [],
   "learned": true,
   "days": [
    4
   ]
  },
  {
   "id": "k:1.5:Few-shot",
   "type": "knowledge",
   "name": "Few-shot",
   "desc": "给 2-3 个例子，AI 自动模仿",
   "module": "1.5",
   "stage": "1",
   "pitfalls": [],
   "learned": true,
   "days": [
    4
   ]
  },
  {
   "id": "k:1.5:CoT",
   "type": "knowledge",
   "name": "CoT",
   "desc": "加\"一步步思考\"→ 推理能力飙升",
   "module": "1.5",
   "stage": "1",
   "pitfalls": [],
   "learned": true,
   "days": [
    4
   ]
  },
  {
   "id": "k:1.5:XML 标签",
   "type": "knowledge",
   "name": "XML 标签",
   "desc": "`<system>` `<rules>` `<input>` 划分指令区域，遵守率更高",
   "module": "1.5",
   "stage": "1",
   "pitfalls": [],
   "learned": true,
   "days": [
    4
   ]
  },
  {
   "id": "k:1.5:深度角色",
   "type": "knowledge",
   "name": "深度角色",
   "desc": "描述性格+风格+知识边界+典型反应（4-5 行）",
   "module": "1.5",
   "stage": "1",
   "pitfalls": [],
   "learned": true,
   "days": [
    4
   ]
  },
  {
   "id": "k:1.5:水平差异化",
   "type": "knowledge",
   "name": "水平差异化",
   "desc": "同一 topic 不同 student_level 用不同讲解方式",
   "module": "1.5",
   "stage": "1",
   "pitfalls": [],
   "learned": true,
   "days": [
    4
   ]
  },
  {
   "id": "k:1.5:JSON 剥壳",
   "type": "knowledge",
   "name": "JSON 剥壳",
   "desc": "AI 包 ```json 代码块时用正则 re.sub 兜底",
   "module": "1.5",
   "stage": "1",
   "pitfalls": [
    {
     "num": 29,
     "err": "提示词要求 JSON 仍带代码块",
     "fix": "正则 re.sub 剥壳兜底"
    }
   ],
   "learned": true,
   "days": [
    4,
    5
   ]
  },
  {
   "id": "k:1.6:Pydantic BaseModel",
   "type": "knowledge",
   "name": "Pydantic BaseModel",
   "desc": "类定义数据结构，自动校验类型和必填",
   "module": "1.6",
   "stage": "1",
   "pitfalls": [],
   "learned": true,
   "days": [
    4
   ]
  },
  {
   "id": "k:1.6:Field(description=)",
   "type": "knowledge",
   "name": "Field(description=)",
   "desc": "字段说明文档",
   "module": "1.6",
   "stage": "1",
   "pitfalls": [],
   "learned": true,
   "days": [
    4
   ]
  },
  {
   "id": "k:1.6:`Recipe(**dict)`",
   "type": "knowledge",
   "name": "`Recipe(**dict)`",
   "desc": "字典解包成 Pydantic 对象（Agent 底座：代码可安全消费 LLM 输出）",
   "module": "1.6",
   "stage": "1",
   "pitfalls": [],
   "learned": true,
   "days": [
    4,
    5,
    7
   ]
  },
  {
   "id": "k:2.1:工具的本质",
   "type": "knowledge",
   "name": "工具的本质",
   "desc": "普通 Python 函数 + JSON Schema（给 LLM 的说明书）",
   "module": "2.1",
   "stage": "2",
   "pitfalls": [
    {
     "num": 29,
     "err": "提示词要求 JSON 仍带代码块",
     "fix": "正则 re.sub 剥壳兜底"
    }
   ],
   "learned": true,
   "days": [
    5,
    4,
    9
   ]
  },
  {
   "id": "k:2.1:执行流程",
   "type": "knowledge",
   "name": "执行流程",
   "desc": "tool_use → execute → tool_result",
   "module": "2.1",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": [
    5,
    8
   ]
  },
  {
   "id": "k:2.1:核心循环",
   "type": "knowledge",
   "name": "核心循环",
   "desc": "构造 tools → 调用 → 判断 tool_calls → 执行 → 回填 → 二次调用回答",
   "module": "2.1",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": [
    5
   ]
  },
  {
   "id": "k:2.1:消息顺序",
   "type": "knowledge",
   "name": "消息顺序",
   "desc": "user → assistant(tool_calls) → tool 结果们 → assistant(final)，assistant 必须在 tool 之前",
   "module": "2.1",
   "stage": "2",
   "pitfalls": [
    {
     "num": 30,
     "err": "KeyError: 'choices'",
     "fix": "顺序必须 assistant(tool_calls) → tool 结果 → assistant(final)"
    }
   ],
   "learned": true,
   "days": [
    5,
    4
   ]
  },
  {
   "id": "k:2.1:tool_call_id",
   "type": "knowledge",
   "name": "tool_call_id",
   "desc": "回填 tool 消息时必须带上，一一对应",
   "module": "2.1",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": [
    5
   ]
  },
  {
   "id": "k:2.1:并行调用",
   "type": "knowledge",
   "name": "并行调用",
   "desc": "`for tc in tool_calls` 逐个执行+回填多条 tool 消息",
   "module": "2.1",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": [
    5,
    4
   ]
  },
  {
   "id": "k:2.1:Schema 设计",
   "type": "knowledge",
   "name": "Schema 设计",
   "desc": "type→function→name/parameters/properties 层级",
   "module": "2.1",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": [
    5,
    4
   ]
  },
  {
   "id": "k:2.1:safe_get()",
   "type": "knowledge",
   "name": "safe_get()",
   "desc": "逐层 isinstance + key in dict 检查，缺层返回 default",
   "module": "2.1",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": [
    5,
    4
   ]
  },
  {
   "id": "k:2.1:安检闸门模式",
   "type": "knowledge",
   "name": "安检闸门模式",
   "desc": "逐条件 return False，全过才 True",
   "module": "2.1",
   "stage": "2",
   "pitfalls": [
    {
     "num": 11,
     "err": "找到第一条就 return False",
     "fix": "循环结束后再 return 结果"
    },
    {
     "num": 22,
     "err": "return False 报类型不匹配",
     "fix": "按签名返回 (False, 错误消息)"
    }
   ],
   "learned": true,
   "days": [
    4,
    5,
    2
   ]
  },
  {
   "id": "k:2.1:parse_tool_arguments()",
   "type": "knowledge",
   "name": "parse_tool_arguments()",
   "desc": "dict 直接用；字符串 try json.loads；失败返回 None",
   "module": "2.1",
   "stage": "2",
   "pitfalls": [
    {
     "num": 13,
     "err": "json.loads 崩溃",
     "fix": "`text = text[6:]`"
    },
    {
     "num": 40,
     "err": "摘要为空时返回 None",
     "fix": "无旧消息时返回 `\"\"`"
    }
   ],
   "learned": true,
   "days": [
    5,
    4,
    7
   ]
  },
  {
   "id": "k:2.2:ReAct 原理",
   "type": "knowledge",
   "name": "ReAct 原理",
   "desc": "Reasoning + Acting 交替：思考→行动→观察→再思考→完成",
   "module": "2.2",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": [
    5
   ]
  },
  {
   "id": "k:2.2:tool_loop vs ReAct",
   "type": "knowledge",
   "name": "tool_loop vs ReAct",
   "desc": "固定 1 轮 vs 动态 N 轮（for/while 包住整段）",
   "module": "2.2",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": [
    5
   ]
  },
  {
   "id": "k:2.2:body 重建",
   "type": "knowledge",
   "name": "body 重建",
   "desc": "每轮 messages 变了，body 必须重新构造",
   "module": "2.2",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": [
    5,
    4
   ]
  },
  {
   "id": "k:2.2:终止条件",
   "type": "knowledge",
   "name": "终止条件",
   "desc": "max_iterations 上限 + consecutive_errors ≥ 3 连续错误终止",
   "module": "2.2",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": [
    5
   ]
  },
  {
   "id": "k:2.2:AgentState",
   "type": "knowledge",
   "name": "AgentState",
   "desc": "@dataclass 记录 messages/iteration/tool_calls_made/consecutive_errors",
   "module": "2.2",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": [
    5,
    7,
    4
   ]
  },
  {
   "id": "k:2.2:路径沙箱",
   "type": "knowledge",
   "name": "路径沙箱",
   "desc": "_safe_path() 限制工具只能访问白名单目录",
   "module": "2.2",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": [
    5,
    9
   ]
  },
  {
   "id": "k:2.3:滑动窗口",
   "type": "knowledge",
   "name": "滑动窗口",
   "desc": "只保留 system + 最近 N 轮，旧消息丢弃，省空间",
   "module": "2.3",
   "stage": "2",
   "pitfalls": [
    {
     "num": 45,
     "err": "窗口保留了最旧消息、保留率 1.0",
     "fix": "窗口永远负索引从尾数 `rest[-N:]`"
    }
   ],
   "learned": true,
   "days": [
    6,
    7
   ]
  },
  {
   "id": "k:2.3:system 常驻豁免",
   "type": "knowledge",
   "name": "system 常驻豁免",
   "desc": "system 是“宪法”，永远保留且在最前",
   "module": "2.3",
   "stage": "2",
   "pitfalls": [
    {
     "num": 41,
     "err": "新建 system 消息 role 写成 recent",
     "fix": "固定写 `\"system\"`"
    }
   ],
   "learned": true,
   "days": [
    4,
    6,
    7
   ]
  },
  {
   "id": "k:2.3:轮（turn）",
   "type": "knowledge",
   "name": "轮（turn）",
   "desc": "1 轮 = 1 user + 1 assistant，裁剪按“轮”不按“条”",
   "module": "2.3",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": [
    4,
    5
   ]
  },
  {
   "id": "k:2.3:摘要压缩",
   "type": "knowledge",
   "name": "摘要压缩",
   "desc": "旧消息压成一段摘要，保留要点，不直接丢光",
   "module": "2.3",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": [
    6,
    7
   ]
  },
  {
   "id": "k:2.3:摘要合并进 system",
   "type": "knowledge",
   "name": "摘要合并进 system",
   "desc": "把摘要拼进 system 内容，让 LLM 每轮都能看到旧要点",
   "module": "2.3",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": [
    6,
    7,
    4
   ]
  },
  {
   "id": "k:2.3:混合策略",
   "type": "knowledge",
   "name": "混合策略",
   "desc": "旧对话用摘要，新对话用窗口，兼顾省空间和记忆",
   "module": "2.3",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": [
    6
   ]
  },
  {
   "id": "k:2.3:token 粗估",
   "type": "knowledge",
   "name": "token 粗估",
   "desc": "role + content 字符数相加，粗略判断离上下文上限多远",
   "module": "2.3",
   "stage": "2",
   "pitfalls": [
    {
     "num": 42,
     "err": "`int(msg[\"role\"])` ValueError",
     "fix": "求字符数用 `len()`"
    }
   ],
   "learned": true,
   "days": [
    4,
    7
   ]
  },
  {
   "id": "k:2.3:三种记忆分工",
   "type": "knowledge",
   "name": "三种记忆分工",
   "desc": "短期=对话内 messages；长期=跨对话落盘档案；工作=AgentState 任务状态",
   "module": "2.3",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": [
    7,
    6,
    5
   ]
  },
  {
   "id": "k:2.3:对比实验设计",
   "type": "knowledge",
   "name": "对比实验设计",
   "desc": "控制变量（同数据同窗口）+ 固定指标（token 占用/信息保留率）+ 基线对照",
   "module": "2.3",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": [
    7,
    9,
    4
   ]
  },
  {
   "id": "k:2.3:埋事实测记忆",
   "type": "knowledge",
   "name": "埋事实测记忆",
   "desc": "数据里预埋\"关键事实\"，裁剪后数还剩几条 → 记忆力变成 0~1 数字",
   "module": "2.3",
   "stage": "2",
   "pitfalls": [],
   "learned": false,
   "days": []
  },
  {
   "id": "k:2.3:回调函数注入",
   "type": "knowledge",
   "name": "回调函数注入",
   "desc": "summarize 等作为参数传入，测试传离线 fake、生产传 LLM，接口不变",
   "module": "2.3",
   "stage": "2",
   "pitfalls": [
    {
     "num": 51,
     "err": "脚本化 fake 永远返回第一稿",
     "fix": "剧本放函数体外（闭包），或用工厂每次产新机器"
    }
   ],
   "learned": true,
   "days": [
    7,
    5,
    8
   ]
  },
  {
   "id": "k:2.3:长期记忆闭环",
   "type": "knowledge",
   "name": "长期记忆闭环",
   "desc": "抽取 → 入档 → 落盘 → 新对话读盘 → 注入 system",
   "module": "2.3",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": [
    7,
    6
   ]
  },
  {
   "id": "k:2.3:抽取",
   "type": "knowledge",
   "name": "抽取",
   "desc": "人话（非结构化）→ 表格（结构化），长期记忆的第一环",
   "module": "2.3",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": [
    7
   ]
  },
  {
   "id": "k:2.3:规则抽取 vs LLM 抽取",
   "type": "knowledge",
   "name": "规则抽取 vs LLM 抽取",
   "desc": "写死的 if 免费/死板；LLM 什么话都懂但花钱联网，接口相同时可互换",
   "module": "2.3",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": [
    7,
    4,
    5
   ]
  },
  {
   "id": "k:2.3:system 注入点",
   "type": "knowledge",
   "name": "system 注入点",
   "desc": "记忆拼进 system（常驻第一条），比拼 user 消息更稳",
   "module": "2.3",
   "stage": "2",
   "pitfalls": [
    {
     "num": 41,
     "err": "新建 system 消息 role 写成 recent",
     "fix": "固定写 `\"system\"`"
    }
   ],
   "learned": true,
   "days": [
    4,
    7,
    6
   ]
  },
  {
   "id": "k:2.3:json 落盘",
   "type": "knowledge",
   "name": "json 落盘",
   "desc": "dict ↔ 文件往返：dump/load 吃文件，dumps/loads 吃字符串（d 写 l 读，带 s 换字符串）",
   "module": "2.3",
   "stage": "2",
   "pitfalls": [
    {
     "num": 13,
     "err": "json.loads 崩溃",
     "fix": "`text = text[6:]`"
    }
   ],
   "learned": true,
   "days": [
    7,
    4,
    5
   ]
  },
  {
   "id": "k:2.3:ensure_ascii=False + indent=2",
   "type": "knowledge",
   "name": "ensure_ascii=False + indent=2",
   "desc": "json 中文原样落盘 + 缩进可读",
   "module": "2.3",
   "stage": "2",
   "pitfalls": [
    {
     "num": 11,
     "err": "找到第一条就 return False",
     "fix": "循环结束后再 return 结果"
    },
    {
     "num": 22,
     "err": "return False 报类型不匹配",
     "fix": "按签名返回 (False, 错误消息)"
    }
   ],
   "learned": true,
   "days": [
    4,
    5
   ]
  },
  {
   "id": "k:2.3:容错兜底",
   "type": "knowledge",
   "name": "容错兜底",
   "desc": "FileNotFoundError / JSONDecodeError 都返回空档案，坏一块不崩全部",
   "module": "2.3",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": []
  },
  {
   "id": "k:2.3:不可变更新",
   "type": "knowledge",
   "name": "不可变更新",
   "desc": "dict(old) 复印后改复印件，原件留快照、无副作用",
   "module": "2.3",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": [
    7
   ]
  },
  {
   "id": "k:2.3:表驱动",
   "type": "knowledge",
   "name": "表驱动",
   "desc": "(前缀, 键名) 规则卡 + 循环，加规则只加数据不改逻辑",
   "module": "2.3",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": [
    8
   ]
  },
  {
   "id": "k:2.3:startswith()",
   "type": "knowledge",
   "name": "startswith()",
   "desc": "前缀判断，替代手数长度的切片比较（新规范点名）",
   "module": "2.3",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": []
  },
  {
   "id": "k:2.3:assert 断言收窄",
   "type": "knowledge",
   "name": "assert 断言收窄",
   "desc": "assert x is not None 让类型检查器确认\"此处不为 None\"，修 Pylance 报错",
   "module": "2.3",
   "stage": "2",
   "pitfalls": [
    {
     "num": 19,
     "err": "`self.books = None` 后遍历报错",
     "fix": "初始化为 `[]`"
    },
    {
     "num": 21,
     "err": "Pylance 类型缩窄告警",
     "fix": "调一次存变量 `para = fn.get(...)`"
    },
    {
     "num": 24,
     "err": "Pylance 标红但运行正常",
     "fix": "类型标注 ≠ 运行时行为，`basic` 模式减噪"
    },
    {
     "num": 40,
     "err": "摘要为空时返回 None",
     "fix": "无旧消息时返回 `\"\"`"
    },
    {
     "num": 34,
     "err": "Pylance 自动补全不弹窗",
     "fix": "检查 VS Code 设置"
    }
   ],
   "learned": true,
   "days": [
    3,
    5
   ]
  },
  {
   "id": "k:2.3:过严断言",
   "type": "knowledge",
   "name": "过严断言",
   "desc": "测试只验证意图（startswith+in），不耦合与目标无关的格式细节（如全半角标点）",
   "module": "2.3",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": [
    7
   ]
  },
  {
   "id": "k:2.3:浅拷贝陷阱",
   "type": "knowledge",
   "name": "浅拷贝陷阱",
   "desc": "dict(vault) 只复印外层，内层档案仍是原件——两层结构要两层都复印",
   "module": "2.3",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": [
    7
   ]
  },
  {
   "id": "k:2.3:{**d, k: v} 合并",
   "type": "knowledge",
   "name": "{**d, k: v} 合并",
   "desc": "字典解包合并：老库倒进新库+替换一个键，一行完成外层复印",
   "module": "2.3",
   "stage": "2",
   "pitfalls": [],
   "learned": false,
   "days": []
  },
  {
   "id": "k:2.3:dict 保持插入顺序",
   "type": "knowledge",
   "name": "dict 保持插入顺序",
   "desc": "Python 3.7+ 字典键按插入顺序存放，next(iter(d)) = 最旧的键",
   "module": "2.3",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": [
    7,
    5,
    4
   ]
  },
  {
   "id": "k:2.3:FIFO 淘汰",
   "type": "knowledge",
   "name": "FIFO 淘汰",
   "desc": "容量满时踢掉最先进入的条目（LRU 缓存的雏形），覆盖不算新条目",
   "module": "2.3",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": [
    7
   ]
  },
  {
   "id": "k:2.3:del 语句",
   "type": "knowledge",
   "name": "del 语句",
   "desc": "del d[key] 删除字典的键，d[k]=v 的反面",
   "module": "2.3",
   "stage": "2",
   "pitfalls": [
    {
     "num": 44,
     "err": "`del profile[user]` KeyError",
     "fix": "动手前先想清楚自己在哪一层"
    }
   ],
   "learned": true,
   "days": []
  },
  {
   "id": "k:2.3:卫语句双条件",
   "type": "knowledge",
   "name": "卫语句双条件",
   "desc": "user not in vault or key not in vault[user]——两种\"不用干活\"提前返回",
   "module": "2.3",
   "stage": "2",
   "pitfalls": [
    {
     "num": 43,
     "err": "`vault.items(user)` TypeError",
     "fix": "`vault.get(user, {})`"
    },
    {
     "num": 44,
     "err": "`del profile[user]` KeyError",
     "fix": "动手前先想清楚自己在哪一层"
    }
   ],
   "learned": true,
   "days": [
    7,
    5,
    4
   ]
  },
  {
   "id": "k:2.4:Plan-and-Execute 模式",
   "type": "knowledge",
   "name": "Plan-and-Execute 模式",
   "desc": "先生成完整计划再逐步执行，vs ReAct 走一步看一步（边炒菜边想 vs 先看菜谱）",
   "module": "2.4",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": [
    8,
    9,
    5
   ]
  },
  {
   "id": "k:2.4:计划即数据",
   "type": "knowledge",
   "name": "计划即数据",
   "desc": "plan 是 list[dict]，可校验、可打印、可给人过目",
   "module": "2.4",
   "stage": "2",
   "pitfalls": [
    {
     "num": 39,
     "err": "`merged + recent_messages[1:]` 报错",
     "fix": "用 `[merged] + recent_messages[1:]` 包成列表再拼接"
    }
   ],
   "learned": true,
   "days": [
    7,
    8,
    6
   ]
  },
  {
   "id": "k:2.4:静态清单循环 vs 动态决定",
   "type": "knowledge",
   "name": "静态清单循环 vs 动态决定",
   "desc": "P&E 循环一个静态列表，ReAct 每轮问 LLM——前者省调用、可审计",
   "module": "2.4",
   "stage": "2",
   "pitfalls": [
    {
     "num": 12,
     "err": "列表推导结果全是同一个值",
     "fix": "推导式变量名与循环一致"
    }
   ],
   "learned": true,
   "days": [
    8,
    5,
    9
   ]
  },
  {
   "id": "k:2.4:工具注册表分发",
   "type": "knowledge",
   "name": "工具注册表分发",
   "desc": "{\"动作名\": 函数}，按 action 查表调用，加工具只加表项",
   "module": "2.4",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": []
  },
  {
   "id": "k:2.4:*args 调用侧解包",
   "type": "knowledge",
   "name": "*args 调用侧解包",
   "desc": "fn(*[2,3]) = fn(2,3)；safe_get 的 *keys 是签名侧收拢，一体两面",
   "module": "2.4",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": [
    5,
    8
   ]
  },
  {
   "id": "k:2.4:优雅降级",
   "type": "knowledge",
   "name": "优雅降级",
   "desc": "未知操作返回错误字符串不崩溃，引擎继续跑",
   "module": "2.4",
   "stage": "2",
   "pitfalls": [],
   "learned": false,
   "days": []
  },
  {
   "id": "k:2.4:校验器参数放宽",
   "type": "knowledge",
   "name": "校验器参数放宽",
   "desc": "安检员天生要接\"可能不合法\"的输入，签名用 list 而非 list[dict]",
   "module": "2.4",
   "stage": "2",
   "pitfalls": [
    {
     "num": 2,
     "err": "`self.tags = list[str] = []` 语法错误",
     "fix": "`self.tags: list[str] = []`"
    },
    {
     "num": 3,
     "err": "`self.tags : list[str] = []` 报错",
     "fix": "冒号紧跟变量名"
    },
    {
     "num": 50,
     "err": "`id in list[dict]` 永远 False 不报错",
     "fix": "in 之前核对两边类型一致；查 id 集合用 set"
    }
   ],
   "learned": false,
   "days": [
    4,
    3,
    6
   ]
  },
  {
   "id": "k:2.4:动态重规划",
   "type": "knowledge",
   "name": "动态重规划",
   "desc": "受阻→重算【剩余】路线→继续，已完成的结果不回滚（导航改道不回出发点）",
   "module": "2.4",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": [
    8
   ]
  },
  {
   "id": "k:2.4:重规划预算 max_replans",
   "type": "knowledge",
   "name": "重规划预算 max_replans",
   "desc": "防庸医 replanner 无限变道烧钱，max_iterations 的直系亲戚",
   "module": "2.4",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": [
    8
   ]
  },
  {
   "id": "k:2.4:错误即数据",
   "type": "knowledge",
   "name": "错误即数据",
   "desc": "优雅降级的产出（未知操作字符串）= 上游系统的触发信号",
   "module": "2.4",
   "stage": "2",
   "pitfalls": [],
   "learned": false,
   "days": [
    8
   ]
  },
  {
   "id": "k:2.4:while+手动索引",
   "type": "knowledge",
   "name": "while+手动索引",
   "desc": "循环对象要中途整体替换时，for 锁死迭代对象，while 才能边跑边换",
   "module": "2.4",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": [
    1
   ]
  },
  {
   "id": "k:2.4:import 自己的模块",
   "type": "knowledge",
   "name": "import 自己的模块",
   "desc": "同目录 from plan_and_execute import ...，DRY 复用零件",
   "module": "2.4",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": [
    8
   ]
  },
  {
   "id": "k:2.4:失败痕迹保留",
   "type": "knowledge",
   "name": "失败痕迹保留",
   "desc": "results 记录每次失败——审计时能看到在哪改的道",
   "module": "2.4",
   "stage": "2",
   "pitfalls": [],
   "learned": false,
   "days": []
  },
  {
   "id": "k:2.4:planner vs replanner",
   "type": "knowledge",
   "name": "planner vs replanner",
   "desc": "出发前盲规划(只知任务) vs 受阻时知情改道(知任务+进度+故障)，只管剩余",
   "module": "2.4",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": [
    8
   ]
  },
  {
   "id": "k:2.4:共享黑板 state",
   "type": "knowledge",
   "name": "共享黑板 state",
   "desc": "步骤间数据流走闭包 dict，不走返回值（框架 checkpoint 思想）",
   "module": "2.4",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": []
  },
  {
   "id": "k:2.4:zip 拉链配对",
   "type": "knowledge",
   "name": "zip 拉链配对",
   "desc": "zip(a,b) 按位置咬合成对，配权重/配对计算一步到位",
   "module": "2.4",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": []
  },
  {
   "id": "k:2.4:CWD vs 脚本目录",
   "type": "knowledge",
   "name": "CWD vs 脚本目录",
   "desc": "相对路径跟着\"从哪运行\"走；Path(__file__).parent 锚定\"文件在哪\"",
   "module": "2.4",
   "stage": "2",
   "pitfalls": [
    {
     "num": 60,
     "err": "Pylance: Unable to resolve import（跨目录）",
     "fix": "pyrightconfig extraPaths + mypy_path 白名单"
    },
    {
     "num": 49,
     "err": "报告文件落在仓库根而不是脚本目录",
     "fix": "`Path(__file__).parent / path` 锚定脚本目录"
    },
    {
     "num": 52,
     "err": "落盘 FileNotFoundError",
     "fix": "写文件三件套：open(path, \"w\", encoding=\"utf-8\")"
    }
   ],
   "learned": true,
   "days": [
    9
   ]
  },
  {
   "id": "k:2.4:Workflow vs Agent",
   "type": "knowledge",
   "name": "Workflow vs Agent",
   "desc": "流程固定（下一步听代码）vs 动态流程（下一步听 LLM）——run_plan vs react_loop",
   "module": "2.4",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": [
    8,
    5,
    4
   ]
  },
  {
   "id": "k:2.4:gate 闸门思想",
   "type": "knowledge",
   "name": "gate 闸门思想",
   "desc": "步骤之间加检查点：validate_plan 拦进门计划、is_failed 拦半路结果，脏数据不流向下一步",
   "module": "2.4",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": [
    8
   ]
  },
  {
   "id": "k:2.4:何时该用 Agent",
   "type": "knowledge",
   "name": "何时该用 Agent",
   "desc": "任务步骤无法预知、需现场决策才上 Agent；宁简勿繁，从最简单方案开始",
   "module": "2.4",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": [
    8,
    5,
    7
   ]
  },
  {
   "id": "k:2.4:依赖感知执行（拓扑排序朴素版）",
   "type": "knowledge",
   "name": "依赖感知执行（拓扑排序朴素版）",
   "desc": "每步声明 needs，循环挑\"依赖全就位\"的步骤执行，清单顺序≠执行顺序",
   "module": "2.4",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": [
    8,
    5
   ]
  },
  {
   "id": "k:2.4:死锁检测",
   "type": "knowledge",
   "name": "死锁检测",
   "desc": "还有剩余但挑不出任何就绪步骤 = 依赖成环，报告终止而非挂死",
   "module": "2.4",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": [
    8
   ]
  },
  {
   "id": "k:2.4:done 用 set",
   "type": "knowledge",
   "name": "done 用 set",
   "desc": "已完成 id 集合用 set——`n in done` 是 O(1) 查询，list 是 O(n)",
   "module": "2.4",
   "stage": "2",
   "pitfalls": [
    {
     "num": 6,
     "err": "`text == \"DONE\"` 永远不触发",
     "fix": "`text == \"[DONE]\"` 写完整"
    }
   ],
   "learned": true,
   "days": [
    4
   ]
  },
  {
   "id": "k:2.4:sorted(key=lambda)",
   "type": "knowledge",
   "name": "sorted(key=lambda)",
   "desc": "排 dict 列表给一把\"尺子\"：key=lambda s: s[\"id\"] 量哪个字段",
   "module": "2.4",
   "stage": "2",
   "pitfalls": [
    {
     "num": 14,
     "err": "返回了 API Key 而不是回复",
     "fix": "命名语义化，返回前核对"
    }
   ],
   "learned": true,
   "days": [
    5,
    4,
    8
   ]
  },
  {
   "id": "k:2.4:all() / any()",
   "type": "knowledge",
   "name": "all() / any()",
   "desc": "全都成立吗 / 有一个成立吗——all 管闸门全过才放行，any 管警报有一个就响",
   "module": "2.4",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": []
  },
  {
   "id": "k:2.5:反思循环",
   "type": "knowledge",
   "name": "反思循环",
   "desc": "生成→自评→改进：ReAct 对外行动，反思对内检讨自己上一稿",
   "module": "2.5",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": [
    8
   ]
  },
  {
   "id": "k:2.5:批评家=规则代码",
   "type": "knowledge",
   "name": "批评家=规则代码",
   "desc": "硬约束检查用代码不用 LLM——免费、确定、可测试（离线可验的逻辑不花钱）",
   "module": "2.5",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": [
    8,
    7,
    4
   ]
  },
  {
   "id": "k:2.5:反思便签=工作记忆",
   "type": "knowledge",
   "name": "反思便签=工作记忆",
   "desc": "问题清单翻译成便签喂回下一轮生成器，note 跨轮传递",
   "module": "2.5",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": [
    8
   ]
  },
  {
   "id": "k:2.5:问题收敛曲线",
   "type": "knowledge",
   "name": "问题收敛曲线",
   "desc": "problems_history 里问题数递减（如 [2,1,0]）——反思有效的数字证据",
   "module": "2.5",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": [
    8
   ]
  },
  {
   "id": "k:2.5:critic 返回问题清单",
   "type": "knowledge",
   "name": "critic 返回问题清单",
   "desc": "比 bool 信息量大：清单直接变成下一轮的改进指令（错误即数据第三次登场）",
   "module": "2.5",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": [
    8,
    4
   ]
  },
  {
   "id": "k:2.5:预算即圈数",
   "type": "knowledge",
   "name": "预算即圈数",
   "desc": "for range(max_rounds)：每圈必然消耗预算，放学铃必须存在",
   "module": "2.5",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": []
  },
  {
   "id": "k:2.5:语言强化学习",
   "type": "knowledge",
   "name": "语言强化学习",
   "desc": "不改权重改文字记忆——不做脑手术，改贴便利贴（Reflexion）",
   "module": "2.5",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": [
    8
   ]
  },
  {
   "id": "k:2.5:Actor/Evaluator/Self-reflection",
   "type": "knowledge",
   "name": "Actor/Evaluator/Self-reflection",
   "desc": "= generator/check_slogan/build_reflection，我写过 Reflexion 迷你版",
   "module": "2.5",
   "stage": "2",
   "pitfalls": [
    {
     "num": 19,
     "err": "`self.books = None` 后遍历报错",
     "fix": "初始化为 `[]`"
    }
   ],
   "learned": true,
   "days": [
    8,
    2,
    3
   ]
  },
  {
   "id": "k:2.5:episodic memory",
   "type": "knowledge",
   "name": "episodic memory",
   "desc": "反思跨试次（任务）存活；note 只在单任务内——长期记忆+反思便签的合体",
   "module": "2.5",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": [
    8
   ]
  },
  {
   "id": "k:2.5:反思按需付费",
   "type": "knowledge",
   "name": "反思按需付费",
   "desc": "第 1 轮=裸奔，一稿过零成本，烂稿才补轮——怕翻倍不敢开是错觉",
   "module": "2.5",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": [
    8
   ]
  },
  {
   "id": "k:7.1:三遍寻宝法",
   "type": "knowledge",
   "name": "三遍寻宝法",
   "desc": "侦察(摘要/图表/结论5分钟)→挖宝(Intro末段+方法+Figure1)→按需拆解(复现时才精读)",
   "module": "7.1",
   "stage": "2",
   "pitfalls": [],
   "learned": false,
   "days": []
  },
  {
   "id": "k:7.1:Figure 1 定律",
   "type": "knowledge",
   "name": "Figure 1 定律",
   "desc": "Agent 论文 90% 精华在架构图——先看懂图再看字",
   "module": "7.1",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": []
  },
  {
   "id": "k:7.1:代码锚定法",
   "type": "knowledge",
   "name": "代码锚定法",
   "desc": "把论文组件翻译成自己写过的函数，概念立刻落地",
   "module": "7.1",
   "stage": "2",
   "pitfalls": [],
   "learned": false,
   "days": []
  },
  {
   "id": "k:7.1:费曼检验",
   "type": "knowledge",
   "name": "费曼检验",
   "desc": "写不出 3 行总结=没读懂，回去重读 Figure 1",
   "module": "7.1",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": []
  },
  {
   "id": "k:7.1:episodic memory 实现",
   "type": "knowledge",
   "name": "episodic memory 实现",
   "desc": "长期记忆(落盘教训库)×反思(便签)的组合——lesson 跨任务传递",
   "module": "7.1",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": [
    8
   ]
  },
  {
   "id": "k:7.1:读旧+append+写回",
   "type": "knowledge",
   "name": "读旧+append+写回",
   "desc": "追加式落盘三步：复用 load 读旧库，别只写新条目（会覆盖历史）",
   "module": "7.1",
   "stage": "2",
   "pitfalls": [],
   "learned": false,
   "days": []
  },
  {
   "id": "k:7.1:容错返回同形状",
   "type": "knowledge",
   "name": "容错返回同形状",
   "desc": "异常路径返回值类型必须与正常路径一致（[] 而非 False，否则下游 .append 爆炸）",
   "module": "7.1",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": [
    5,
    4,
    2
   ]
  },
  {
   "id": "k:7.1:剧本放闭包外",
   "type": "knowledge",
   "name": "剧本放闭包外",
   "desc": "脚本化 fake 的剧本必须定义在函数体外——体内=每次调用重发剧本永远第一稿",
   "module": "7.1",
   "stage": "2",
   "pitfalls": [
    {
     "num": 51,
     "err": "脚本化 fake 永远返回第一稿",
     "fix": "剧本放函数体外（闭包），或用工厂每次产新机器"
    }
   ],
   "learned": false,
   "days": []
  },
  {
   "id": "k:2.6:威胁矩阵",
   "type": "knowledge",
   "name": "威胁矩阵",
   "desc": "5 大攻击面: 注入/越权工具/数据泄露/输出投毒/供应链——对应防御: 过滤/分级/校验/校验/沙箱",
   "module": "2.6",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": [
    8
   ]
  },
  {
   "id": "k:2.6:Prompt 注入",
   "type": "knowledge",
   "name": "Prompt 注入",
   "desc": "指令藏在数据里（留言板/网页/文件）——LLM 眼里数据和指令都是文字，天生分不清",
   "module": "2.6",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": [
    4,
    8,
    7
   ]
  },
  {
   "id": "k:2.6:大小写归一化",
   "type": "knowledge",
   "name": "大小写归一化",
   "desc": "文本检测先 text.lower()——否则 DISREGARD 大写攻击直接穿防",
   "module": "2.6",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": []
  },
  {
   "id": "k:2.6:表驱动特征检测",
   "type": "knowledge",
   "name": "表驱动特征检测",
   "desc": "危险短语进 PATTERNS 表 + 循环，加特征零改逻辑",
   "module": "2.6",
   "stage": "2",
   "pitfalls": [],
   "learned": false,
   "days": []
  },
  {
   "id": "k:2.6:过滤 vs 拦截",
   "type": "knowledge",
   "name": "过滤 vs 拦截",
   "desc": "sanitize 消毒放行（柔和）vs guard 命中即拒（强硬）——纵深防御两层都上",
   "module": "2.6",
   "stage": "2",
   "pitfalls": [
    {
     "num": 56,
     "err": "审计记错、guard 交给消毒员",
     "fix": "用词表锚定角色语义，写前默念名字含义"
    }
   ],
   "learned": true,
   "days": [
    8
   ]
  },
  {
   "id": "k:2.6:规则模拟 LLM",
   "type": "knowledge",
   "name": "规则模拟 LLM",
   "desc": "用 if 模拟\"被劫持的 LLM\"——离线靶场不花 API 钱",
   "module": "2.6",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": [
    4,
    5,
    8
   ]
  },
  {
   "id": "k:2.6:遍历字符串陷阱",
   "type": "knowledge",
   "name": "遍历字符串陷阱",
   "desc": "for x in \"字符串\" 拆成逐字符——遍历名单要遍历【列表】",
   "module": "2.6",
   "stage": "2",
   "pitfalls": [
    {
     "num": 53,
     "err": "detect 对干净输入也返回 True",
     "fix": "遍历名单要遍历【列表】(PATTERNS)"
    }
   ],
   "learned": true,
   "days": []
  },
  {
   "id": "k:2.6:绿黄红权限分级",
   "type": "knowledge",
   "name": "绿黄红权限分级",
   "desc": "按副作用: 无副作用(绿自动放行)/可逆(黄需确认)/不可逆(红人工通道)",
   "module": "2.6",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": []
  },
  {
   "id": "k:2.6:默认拒绝 Default Deny",
   "type": "knowledge",
   "name": "默认拒绝 Default Deny",
   "desc": "未登记=红——dict.get(k, 'red') 一行落地，宁可误拒不可误放",
   "module": "2.6",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": [
    5
   ]
  },
  {
   "id": "k:2.6:审计记裁决不记申报",
   "type": "knowledge",
   "name": "审计记裁决不记申报",
   "desc": "日志记闸门的 allowed，不是申请人的 auto_confirm——被拒的试图才是警报",
   "module": "2.6",
   "stage": "2",
   "pitfalls": [
    {
     "num": 56,
     "err": "审计记错、guard 交给消毒员",
     "fix": "用词表锚定角色语义，写前默念名字含义"
    }
   ],
   "learned": true,
   "days": [
    8
   ]
  },
  {
   "id": "k:2.6:闸门与执行分离",
   "type": "knowledge",
   "name": "闸门与执行分离",
   "desc": "authorize 只决策，run_tool 先闸后执行——安检员不搬货",
   "module": "2.6",
   "stage": "2",
   "pitfalls": [],
   "learned": false,
   "days": []
  },
  {
   "id": "k:2.6:输出校验(出口安检)",
   "type": "knowledge",
   "name": "输出校验(出口安检)",
   "desc": "Agent 产物流进下游前的最后一道闸：SQL只读/单语句/无破坏词",
   "module": "2.6",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": [
    9,
    4
   ]
  },
  {
   "id": "k:2.6:检查优先级=契约",
   "type": "knowledge",
   "name": "检查优先级=契约",
   "desc": "多规则同时踩线先报哪个由契约(测试)定——多语句是注入最本质签名优先报",
   "module": "2.6",
   "stage": "2",
   "pitfalls": [],
   "learned": false,
   "days": []
  },
  {
   "id": "k:2.6:resolve后再验身",
   "type": "knowledge",
   "name": "resolve后再验身",
   "desc": "永不信字面路径: ../先展开再 is_relative_to 比对，伪装即失效",
   "module": "2.6",
   "stage": "2",
   "pitfalls": [],
   "learned": false,
   "days": []
  },
  {
   "id": "k:2.6:纵深防御代码形状",
   "type": "knowledge",
   "name": "纵深防御代码形状",
   "desc": "两道闸串联(各自独立可测)，authorize→run_tool 同构第三台",
   "module": "2.6",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": []
  },
  {
   "id": "k:2.6:OWASP LLM Top 10",
   "type": "knowledge",
   "name": "OWASP LLM Top 10",
   "desc": "业界十大病清单——注入/输出处理/过度代理/供应链我防过，泄露/DoS/数据投毒是新面孔",
   "module": "2.6",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": [
    9,
    8,
    4
   ]
  },
  {
   "id": "k:2.6:5攻5防口诀",
   "type": "knowledge",
   "name": "5攻5防口诀",
   "desc": "进口过滤、手分级、出口校验、范围圈死、来源审查",
   "module": "2.6",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": []
  },
  {
   "id": "k:2.6:LLM输出=概率猜测",
   "type": "knowledge",
   "name": "LLM输出=概率猜测",
   "desc": "不是可信结果——过度依赖(LLM09)的病根，进出口设闸的总依据",
   "module": "2.6",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": [
    4,
    8,
    5
   ]
  },
  {
   "id": "k:2.6:文字版ReAct协议",
   "type": "knowledge",
   "name": "文字版ReAct协议",
   "desc": "ACTION/OBSERVATION/ANSWER 文本协议——不依赖API原生tool_calls，与手写react_loop同构",
   "module": "2.6",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": [
    5,
    8
   ]
  },
  {
   "id": "k:2.6:脚本自举模式",
   "type": "knowledge",
   "name": "脚本自举模式",
   "desc": "sys.path.insert挂载.tools/——仓库自带依赖，裸python3直跑，/tmp蒸发免疫",
   "module": "2.6",
   "stage": "2",
   "pitfalls": [
    {
     "num": 60,
     "err": "Pylance: Unable to resolve import（跨目录）",
     "fix": "pyrightconfig extraPaths + mypy_path 白名单"
    },
    {
     "num": 49,
     "err": "报告文件落在仓库根而不是脚本目录",
     "fix": "`Path(__file__).parent / path` 锚定脚本目录"
    }
   ],
   "learned": true,
   "days": [
    9,
    4
   ]
  },
  {
   "id": "k:2.6:Agent可靠性来源",
   "type": "knowledge",
   "name": "Agent可靠性来源",
   "desc": "不是模型聪明，是每个进出口设闸+引擎逼它先查资料再开口",
   "module": "2.6",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": [
    4,
    5,
    8
   ]
  },
  {
   "id": "x:0",
   "type": "planned",
   "name": "2.4 任务规划（Plan-and-Execute）",
   "stage": "2"
  },
  {
   "id": "x:1",
   "type": "planned",
   "name": "2.5 Reflection（生成→自评→改进）",
   "stage": "2"
  },
  {
   "id": "x:2",
   "type": "planned",
   "name": "2.6 安全护栏",
   "stage": "2"
  },
  {
   "id": "x:3",
   "type": "planned",
   "name": "阶段 3：RAG 全流程",
   "stage": null
  },
  {
   "id": "x:4",
   "type": "planned",
   "name": "阶段 4：框架（SDK / LangGraph / MCP / 多 Agent）",
   "stage": null
  },
  {
   "id": "x:5",
   "type": "planned",
   "name": "阶段 5：工程化（评估 / 可观测 / CI/CD / 部署）",
   "stage": null
  }
 ],
 "edges": [
  {
   "source": "s:0",
   "target": "m:0.1",
   "type": "contain"
  },
  {
   "source": "s:0",
   "target": "m:0.2",
   "type": "contain"
  },
  {
   "source": "s:0",
   "target": "m:0.3",
   "type": "contain"
  },
  {
   "source": "s:0",
   "target": "m:0.4",
   "type": "contain"
  },
  {
   "source": "s:1",
   "target": "m:1.1",
   "type": "contain"
  },
  {
   "source": "s:1",
   "target": "m:1.2",
   "type": "contain"
  },
  {
   "source": "s:1",
   "target": "m:1.3",
   "type": "contain"
  },
  {
   "source": "s:1",
   "target": "m:1.4",
   "type": "contain"
  },
  {
   "source": "s:1",
   "target": "m:1.5",
   "type": "contain"
  },
  {
   "source": "s:1",
   "target": "m:1.6",
   "type": "contain"
  },
  {
   "source": "s:2",
   "target": "m:2.1",
   "type": "contain"
  },
  {
   "source": "s:2",
   "target": "m:2.2",
   "type": "contain"
  },
  {
   "source": "s:2",
   "target": "m:2.3",
   "type": "contain"
  },
  {
   "source": "s:2",
   "target": "m:2.4",
   "type": "contain"
  },
  {
   "source": "s:2",
   "target": "m:2.5",
   "type": "contain"
  },
  {
   "source": "s:2",
   "target": "m:7.1",
   "type": "contain"
  },
  {
   "source": "s:2",
   "target": "m:2.6",
   "type": "contain"
  },
  {
   "source": "m:0.1",
   "target": "k:0.1:变量与数据类型",
   "type": "contain"
  },
  {
   "source": "m:0.1",
   "target": "k:0.1:条件判断",
   "type": "contain"
  },
  {
   "source": "m:0.1",
   "target": "k:0.1:循环",
   "type": "contain"
  },
  {
   "source": "m:0.1",
   "target": "k:0.1:四种数据结构",
   "type": "contain"
  },
  {
   "source": "m:0.1",
   "target": "k:0.1:内置函数",
   "type": "contain"
  },
  {
   "source": "m:0.1",
   "target": "k:0.1:字符串操作",
   "type": "contain"
  },
  {
   "source": "m:0.1",
   "target": "k:0.1:卫语句",
   "type": "contain"
  },
  {
   "source": "m:0.1",
   "target": "k:0.1:异常处理",
   "type": "contain"
  },
  {
   "source": "m:0.2",
   "target": "k:0.2:with open()",
   "type": "contain"
  },
  {
   "source": "m:0.2",
   "target": "k:0.2:读取模式",
   "type": "contain"
  },
  {
   "source": "m:0.2",
   "target": "k:0.2:CSV 解析套路",
   "type": "contain"
  },
  {
   "source": "m:0.2",
   "target": "k:0.2:跳过表头",
   "type": "contain"
  },
  {
   "source": "m:0.2",
   "target": "k:0.2:脏数据跳过",
   "type": "contain"
  },
  {
   "source": "m:0.3",
   "target": "k:0.3:class + __init__",
   "type": "contain"
  },
  {
   "source": "m:0.3",
   "target": "k:0.3:实例属性 vs 方法",
   "type": "contain"
  },
  {
   "source": "m:0.3",
   "target": "k:0.3:__repr__",
   "type": "contain"
  },
  {
   "source": "m:0.3",
   "target": "k:0.3:布尔状态管理",
   "type": "contain"
  },
  {
   "source": "m:0.3",
   "target": "k:0.3:继承",
   "type": "contain"
  },
  {
   "source": "m:0.3",
   "target": "k:0.3:super().__init__()",
   "type": "contain"
  },
  {
   "source": "m:0.3",
   "target": "k:0.3:方法覆盖",
   "type": "contain"
  },
  {
   "source": "m:0.3",
   "target": "k:0.3:isinstance()",
   "type": "contain"
  },
  {
   "source": "m:0.3",
   "target": "k:0.3:@dataclass",
   "type": "contain"
  },
  {
   "source": "m:0.3",
   "target": "k:0.3:field(default_factory=list)",
   "type": "contain"
  },
  {
   "source": "m:0.3",
   "target": "k:0.3:Literal[1,2,3]",
   "type": "contain"
  },
  {
   "source": "m:0.3",
   "target": "k:0.3:类型注解 vs 赋值",
   "type": "contain"
  },
  {
   "source": "m:0.4",
   "target": "k:0.4:Git 三区模型",
   "type": "contain"
  },
  {
   "source": "m:0.4",
   "target": "k:0.4:.gitignore",
   "type": "contain"
  },
  {
   "source": "m:0.4",
   "target": "k:0.4:conda + pip",
   "type": "contain"
  },
  {
   "source": "m:0.4",
   "target": "k:0.4:PYTHONUTF8=1",
   "type": "contain"
  },
  {
   "source": "m:1.1",
   "target": "k:1.1:AI→ML→DL→LLM→Agent",
   "type": "contain"
  },
  {
   "source": "m:1.1",
   "target": "k:1.1:Token",
   "type": "contain"
  },
  {
   "source": "m:1.1",
   "target": "k:1.1:参数（7B/70B）",
   "type": "contain"
  },
  {
   "source": "m:1.1",
   "target": "k:1.1:训练 vs 推理",
   "type": "contain"
  },
  {
   "source": "m:1.1",
   "target": "k:1.1:幻觉",
   "type": "contain"
  },
  {
   "source": "m:1.1",
   "target": "k:1.1:上下文窗口",
   "type": "contain"
  },
  {
   "source": "m:1.2",
   "target": "k:1.2:六家对比",
   "type": "contain"
  },
  {
   "source": "m:1.2",
   "target": "k:1.2:选模型口诀",
   "type": "contain"
  },
  {
   "source": "m:1.2",
   "target": "k:1.2:中转平台",
   "type": "contain"
  },
  {
   "source": "m:1.3",
   "target": "k:1.3:HTTP 基础",
   "type": "contain"
  },
  {
   "source": "m:1.3",
   "target": "k:1.3:API Key 安全",
   "type": "contain"
  },
  {
   "source": "m:1.3",
   "target": "k:1.3:Messages 结构",
   "type": "contain"
  },
  {
   "source": "m:1.3",
   "target": "k:1.3:四角色",
   "type": "contain"
  },
  {
   "source": "m:1.3",
   "target": "k:1.3:参数",
   "type": "contain"
  },
  {
   "source": "m:1.3",
   "target": "k:1.3:返回结构",
   "type": "contain"
  },
  {
   "source": "m:1.3",
   "target": "k:1.3:usage",
   "type": "contain"
  },
  {
   "source": "m:1.3",
   "target": "k:1.3:跨轮记忆",
   "type": "contain"
  },
  {
   "source": "m:1.4",
   "target": "k:1.4:SSE 协议",
   "type": "contain"
  },
  {
   "source": "m:1.4",
   "target": "k:1.4:两处 stream",
   "type": "contain"
  },
  {
   "source": "m:1.4",
   "target": "k:1.4:yield 生成器",
   "type": "contain"
  },
  {
   "source": "m:1.4",
   "target": "k:1.4:iter_lines()",
   "type": "contain"
  },
  {
   "source": "m:1.4",
   "target": "k:1.4:delta vs message",
   "type": "contain"
  },
  {
   "source": "m:1.4",
   "target": "k:1.4:reasoning_content",
   "type": "contain"
  },
  {
   "source": "m:1.5",
   "target": "k:1.5:System Prompt 四法则",
   "type": "contain"
  },
  {
   "source": "m:1.5",
   "target": "k:1.5:Zero-shot",
   "type": "contain"
  },
  {
   "source": "m:1.5",
   "target": "k:1.5:Few-shot",
   "type": "contain"
  },
  {
   "source": "m:1.5",
   "target": "k:1.5:CoT",
   "type": "contain"
  },
  {
   "source": "m:1.5",
   "target": "k:1.5:XML 标签",
   "type": "contain"
  },
  {
   "source": "m:1.5",
   "target": "k:1.5:深度角色",
   "type": "contain"
  },
  {
   "source": "m:1.5",
   "target": "k:1.5:水平差异化",
   "type": "contain"
  },
  {
   "source": "m:1.5",
   "target": "k:1.5:JSON 剥壳",
   "type": "contain"
  },
  {
   "source": "m:1.6",
   "target": "k:1.6:Pydantic BaseModel",
   "type": "contain"
  },
  {
   "source": "m:1.6",
   "target": "k:1.6:Field(description=)",
   "type": "contain"
  },
  {
   "source": "m:1.6",
   "target": "k:1.6:`Recipe(**dict)`",
   "type": "contain"
  },
  {
   "source": "m:2.1",
   "target": "k:2.1:工具的本质",
   "type": "contain"
  },
  {
   "source": "m:2.1",
   "target": "k:2.1:执行流程",
   "type": "contain"
  },
  {
   "source": "m:2.1",
   "target": "k:2.1:核心循环",
   "type": "contain"
  },
  {
   "source": "m:2.1",
   "target": "k:2.1:消息顺序",
   "type": "contain"
  },
  {
   "source": "m:2.1",
   "target": "k:2.1:tool_call_id",
   "type": "contain"
  },
  {
   "source": "m:2.1",
   "target": "k:2.1:并行调用",
   "type": "contain"
  },
  {
   "source": "m:2.1",
   "target": "k:2.1:Schema 设计",
   "type": "contain"
  },
  {
   "source": "m:2.1",
   "target": "k:2.1:safe_get()",
   "type": "contain"
  },
  {
   "source": "m:2.1",
   "target": "k:2.1:安检闸门模式",
   "type": "contain"
  },
  {
   "source": "m:2.1",
   "target": "k:2.1:parse_tool_arguments()",
   "type": "contain"
  },
  {
   "source": "m:2.2",
   "target": "k:2.2:ReAct 原理",
   "type": "contain"
  },
  {
   "source": "m:2.2",
   "target": "k:2.2:tool_loop vs ReAct",
   "type": "contain"
  },
  {
   "source": "m:2.2",
   "target": "k:2.2:body 重建",
   "type": "contain"
  },
  {
   "source": "m:2.2",
   "target": "k:2.2:终止条件",
   "type": "contain"
  },
  {
   "source": "m:2.2",
   "target": "k:2.2:AgentState",
   "type": "contain"
  },
  {
   "source": "m:2.2",
   "target": "k:2.2:路径沙箱",
   "type": "contain"
  },
  {
   "source": "m:2.3",
   "target": "k:2.3:滑动窗口",
   "type": "contain"
  },
  {
   "source": "m:2.3",
   "target": "k:2.3:system 常驻豁免",
   "type": "contain"
  },
  {
   "source": "m:2.3",
   "target": "k:2.3:轮（turn）",
   "type": "contain"
  },
  {
   "source": "m:2.3",
   "target": "k:2.3:摘要压缩",
   "type": "contain"
  },
  {
   "source": "m:2.3",
   "target": "k:2.3:摘要合并进 system",
   "type": "contain"
  },
  {
   "source": "m:2.3",
   "target": "k:2.3:混合策略",
   "type": "contain"
  },
  {
   "source": "m:2.3",
   "target": "k:2.3:token 粗估",
   "type": "contain"
  },
  {
   "source": "m:2.3",
   "target": "k:2.3:三种记忆分工",
   "type": "contain"
  },
  {
   "source": "m:2.3",
   "target": "k:2.3:对比实验设计",
   "type": "contain"
  },
  {
   "source": "m:2.3",
   "target": "k:2.3:埋事实测记忆",
   "type": "contain"
  },
  {
   "source": "m:2.3",
   "target": "k:2.3:回调函数注入",
   "type": "contain"
  },
  {
   "source": "m:2.3",
   "target": "k:2.3:长期记忆闭环",
   "type": "contain"
  },
  {
   "source": "m:2.3",
   "target": "k:2.3:抽取",
   "type": "contain"
  },
  {
   "source": "m:2.3",
   "target": "k:2.3:规则抽取 vs LLM 抽取",
   "type": "contain"
  },
  {
   "source": "m:2.3",
   "target": "k:2.3:system 注入点",
   "type": "contain"
  },
  {
   "source": "m:2.3",
   "target": "k:2.3:json 落盘",
   "type": "contain"
  },
  {
   "source": "m:2.3",
   "target": "k:2.3:ensure_ascii=False + indent=2",
   "type": "contain"
  },
  {
   "source": "m:2.3",
   "target": "k:2.3:容错兜底",
   "type": "contain"
  },
  {
   "source": "m:2.3",
   "target": "k:2.3:不可变更新",
   "type": "contain"
  },
  {
   "source": "m:2.3",
   "target": "k:2.3:表驱动",
   "type": "contain"
  },
  {
   "source": "m:2.3",
   "target": "k:2.3:startswith()",
   "type": "contain"
  },
  {
   "source": "m:2.3",
   "target": "k:2.3:assert 断言收窄",
   "type": "contain"
  },
  {
   "source": "m:2.3",
   "target": "k:2.3:过严断言",
   "type": "contain"
  },
  {
   "source": "m:2.3",
   "target": "k:2.3:浅拷贝陷阱",
   "type": "contain"
  },
  {
   "source": "m:2.3",
   "target": "k:2.3:{**d, k: v} 合并",
   "type": "contain"
  },
  {
   "source": "m:2.3",
   "target": "k:2.3:dict 保持插入顺序",
   "type": "contain"
  },
  {
   "source": "m:2.3",
   "target": "k:2.3:FIFO 淘汰",
   "type": "contain"
  },
  {
   "source": "m:2.3",
   "target": "k:2.3:del 语句",
   "type": "contain"
  },
  {
   "source": "m:2.3",
   "target": "k:2.3:卫语句双条件",
   "type": "contain"
  },
  {
   "source": "m:2.4",
   "target": "k:2.4:Plan-and-Execute 模式",
   "type": "contain"
  },
  {
   "source": "m:2.4",
   "target": "k:2.4:计划即数据",
   "type": "contain"
  },
  {
   "source": "m:2.4",
   "target": "k:2.4:静态清单循环 vs 动态决定",
   "type": "contain"
  },
  {
   "source": "m:2.4",
   "target": "k:2.4:工具注册表分发",
   "type": "contain"
  },
  {
   "source": "m:2.4",
   "target": "k:2.4:*args 调用侧解包",
   "type": "contain"
  },
  {
   "source": "m:2.4",
   "target": "k:2.4:优雅降级",
   "type": "contain"
  },
  {
   "source": "m:2.4",
   "target": "k:2.4:校验器参数放宽",
   "type": "contain"
  },
  {
   "source": "m:2.4",
   "target": "k:2.4:动态重规划",
   "type": "contain"
  },
  {
   "source": "m:2.4",
   "target": "k:2.4:重规划预算 max_replans",
   "type": "contain"
  },
  {
   "source": "m:2.4",
   "target": "k:2.4:错误即数据",
   "type": "contain"
  },
  {
   "source": "m:2.4",
   "target": "k:2.4:while+手动索引",
   "type": "contain"
  },
  {
   "source": "m:2.4",
   "target": "k:2.4:import 自己的模块",
   "type": "contain"
  },
  {
   "source": "m:2.4",
   "target": "k:2.4:失败痕迹保留",
   "type": "contain"
  },
  {
   "source": "m:2.4",
   "target": "k:2.4:planner vs replanner",
   "type": "contain"
  },
  {
   "source": "m:2.4",
   "target": "k:2.4:共享黑板 state",
   "type": "contain"
  },
  {
   "source": "m:2.4",
   "target": "k:2.4:zip 拉链配对",
   "type": "contain"
  },
  {
   "source": "m:2.4",
   "target": "k:2.4:CWD vs 脚本目录",
   "type": "contain"
  },
  {
   "source": "m:2.4",
   "target": "k:2.4:Workflow vs Agent",
   "type": "contain"
  },
  {
   "source": "m:2.4",
   "target": "k:2.4:gate 闸门思想",
   "type": "contain"
  },
  {
   "source": "m:2.4",
   "target": "k:2.4:何时该用 Agent",
   "type": "contain"
  },
  {
   "source": "m:2.4",
   "target": "k:2.4:依赖感知执行（拓扑排序朴素版）",
   "type": "contain"
  },
  {
   "source": "m:2.4",
   "target": "k:2.4:死锁检测",
   "type": "contain"
  },
  {
   "source": "m:2.4",
   "target": "k:2.4:done 用 set",
   "type": "contain"
  },
  {
   "source": "m:2.4",
   "target": "k:2.4:sorted(key=lambda)",
   "type": "contain"
  },
  {
   "source": "m:2.4",
   "target": "k:2.4:all() / any()",
   "type": "contain"
  },
  {
   "source": "m:2.5",
   "target": "k:2.5:反思循环",
   "type": "contain"
  },
  {
   "source": "m:2.5",
   "target": "k:2.5:批评家=规则代码",
   "type": "contain"
  },
  {
   "source": "m:2.5",
   "target": "k:2.5:反思便签=工作记忆",
   "type": "contain"
  },
  {
   "source": "m:2.5",
   "target": "k:2.5:问题收敛曲线",
   "type": "contain"
  },
  {
   "source": "m:2.5",
   "target": "k:2.5:critic 返回问题清单",
   "type": "contain"
  },
  {
   "source": "m:2.5",
   "target": "k:2.5:预算即圈数",
   "type": "contain"
  },
  {
   "source": "m:2.5",
   "target": "k:2.5:语言强化学习",
   "type": "contain"
  },
  {
   "source": "m:2.5",
   "target": "k:2.5:Actor/Evaluator/Self-reflection",
   "type": "contain"
  },
  {
   "source": "m:2.5",
   "target": "k:2.5:episodic memory",
   "type": "contain"
  },
  {
   "source": "m:2.5",
   "target": "k:2.5:反思按需付费",
   "type": "contain"
  },
  {
   "source": "m:7.1",
   "target": "k:7.1:三遍寻宝法",
   "type": "contain"
  },
  {
   "source": "m:7.1",
   "target": "k:7.1:Figure 1 定律",
   "type": "contain"
  },
  {
   "source": "m:7.1",
   "target": "k:7.1:代码锚定法",
   "type": "contain"
  },
  {
   "source": "m:7.1",
   "target": "k:7.1:费曼检验",
   "type": "contain"
  },
  {
   "source": "m:7.1",
   "target": "k:7.1:episodic memory 实现",
   "type": "contain"
  },
  {
   "source": "m:7.1",
   "target": "k:7.1:读旧+append+写回",
   "type": "contain"
  },
  {
   "source": "m:7.1",
   "target": "k:7.1:容错返回同形状",
   "type": "contain"
  },
  {
   "source": "m:7.1",
   "target": "k:7.1:剧本放闭包外",
   "type": "contain"
  },
  {
   "source": "m:2.6",
   "target": "k:2.6:威胁矩阵",
   "type": "contain"
  },
  {
   "source": "m:2.6",
   "target": "k:2.6:Prompt 注入",
   "type": "contain"
  },
  {
   "source": "m:2.6",
   "target": "k:2.6:大小写归一化",
   "type": "contain"
  },
  {
   "source": "m:2.6",
   "target": "k:2.6:表驱动特征检测",
   "type": "contain"
  },
  {
   "source": "m:2.6",
   "target": "k:2.6:过滤 vs 拦截",
   "type": "contain"
  },
  {
   "source": "m:2.6",
   "target": "k:2.6:规则模拟 LLM",
   "type": "contain"
  },
  {
   "source": "m:2.6",
   "target": "k:2.6:遍历字符串陷阱",
   "type": "contain"
  },
  {
   "source": "m:2.6",
   "target": "k:2.6:绿黄红权限分级",
   "type": "contain"
  },
  {
   "source": "m:2.6",
   "target": "k:2.6:默认拒绝 Default Deny",
   "type": "contain"
  },
  {
   "source": "m:2.6",
   "target": "k:2.6:审计记裁决不记申报",
   "type": "contain"
  },
  {
   "source": "m:2.6",
   "target": "k:2.6:闸门与执行分离",
   "type": "contain"
  },
  {
   "source": "m:2.6",
   "target": "k:2.6:输出校验(出口安检)",
   "type": "contain"
  },
  {
   "source": "m:2.6",
   "target": "k:2.6:检查优先级=契约",
   "type": "contain"
  },
  {
   "source": "m:2.6",
   "target": "k:2.6:resolve后再验身",
   "type": "contain"
  },
  {
   "source": "m:2.6",
   "target": "k:2.6:纵深防御代码形状",
   "type": "contain"
  },
  {
   "source": "m:2.6",
   "target": "k:2.6:OWASP LLM Top 10",
   "type": "contain"
  },
  {
   "source": "m:2.6",
   "target": "k:2.6:5攻5防口诀",
   "type": "contain"
  },
  {
   "source": "m:2.6",
   "target": "k:2.6:LLM输出=概率猜测",
   "type": "contain"
  },
  {
   "source": "m:2.6",
   "target": "k:2.6:文字版ReAct协议",
   "type": "contain"
  },
  {
   "source": "m:2.6",
   "target": "k:2.6:脚本自举模式",
   "type": "contain"
  },
  {
   "source": "m:2.6",
   "target": "k:2.6:Agent可靠性来源",
   "type": "contain"
  },
  {
   "source": "k:0.1:变量与数据类型",
   "target": "k:0.1:条件判断",
   "type": "path"
  },
  {
   "source": "k:0.1:条件判断",
   "target": "k:0.1:循环",
   "type": "path"
  },
  {
   "source": "k:0.1:循环",
   "target": "k:0.1:四种数据结构",
   "type": "path"
  },
  {
   "source": "k:0.1:四种数据结构",
   "target": "k:0.1:内置函数",
   "type": "path"
  },
  {
   "source": "k:0.1:内置函数",
   "target": "k:0.1:字符串操作",
   "type": "path"
  },
  {
   "source": "k:0.1:字符串操作",
   "target": "k:0.1:卫语句",
   "type": "path"
  },
  {
   "source": "k:0.1:卫语句",
   "target": "k:0.1:异常处理",
   "type": "path"
  },
  {
   "source": "k:0.1:异常处理",
   "target": "k:0.2:with open()",
   "type": "path"
  },
  {
   "source": "k:0.2:with open()",
   "target": "k:0.2:读取模式",
   "type": "path"
  },
  {
   "source": "k:0.2:读取模式",
   "target": "k:0.2:CSV 解析套路",
   "type": "path"
  },
  {
   "source": "k:0.2:CSV 解析套路",
   "target": "k:0.2:跳过表头",
   "type": "path"
  },
  {
   "source": "k:0.2:跳过表头",
   "target": "k:0.2:脏数据跳过",
   "type": "path"
  },
  {
   "source": "k:0.2:脏数据跳过",
   "target": "k:0.3:class + __init__",
   "type": "path"
  },
  {
   "source": "k:0.3:class + __init__",
   "target": "k:0.3:实例属性 vs 方法",
   "type": "path"
  },
  {
   "source": "k:0.3:实例属性 vs 方法",
   "target": "k:0.3:__repr__",
   "type": "path"
  },
  {
   "source": "k:0.3:__repr__",
   "target": "k:0.3:布尔状态管理",
   "type": "path"
  },
  {
   "source": "k:0.3:布尔状态管理",
   "target": "k:0.3:继承",
   "type": "path"
  },
  {
   "source": "k:0.3:继承",
   "target": "k:0.3:super().__init__()",
   "type": "path"
  },
  {
   "source": "k:0.3:super().__init__()",
   "target": "k:0.3:方法覆盖",
   "type": "path"
  },
  {
   "source": "k:0.3:方法覆盖",
   "target": "k:0.3:isinstance()",
   "type": "path"
  },
  {
   "source": "k:0.3:isinstance()",
   "target": "k:0.3:@dataclass",
   "type": "path"
  },
  {
   "source": "k:0.3:@dataclass",
   "target": "k:0.3:field(default_factory=list)",
   "type": "path"
  },
  {
   "source": "k:0.3:field(default_factory=list)",
   "target": "k:0.3:Literal[1,2,3]",
   "type": "path"
  },
  {
   "source": "k:0.3:Literal[1,2,3]",
   "target": "k:0.3:类型注解 vs 赋值",
   "type": "path"
  },
  {
   "source": "k:0.3:类型注解 vs 赋值",
   "target": "k:0.4:Git 三区模型",
   "type": "path"
  },
  {
   "source": "k:0.4:Git 三区模型",
   "target": "k:0.4:.gitignore",
   "type": "path"
  },
  {
   "source": "k:0.4:.gitignore",
   "target": "k:0.4:conda + pip",
   "type": "path"
  },
  {
   "source": "k:0.4:conda + pip",
   "target": "k:0.4:PYTHONUTF8=1",
   "type": "path"
  },
  {
   "source": "k:0.4:PYTHONUTF8=1",
   "target": "k:1.1:AI→ML→DL→LLM→Agent",
   "type": "path"
  },
  {
   "source": "k:1.1:AI→ML→DL→LLM→Agent",
   "target": "k:1.1:Token",
   "type": "path"
  },
  {
   "source": "k:1.1:Token",
   "target": "k:1.1:参数（7B/70B）",
   "type": "path"
  },
  {
   "source": "k:1.1:参数（7B/70B）",
   "target": "k:1.1:训练 vs 推理",
   "type": "path"
  },
  {
   "source": "k:1.1:训练 vs 推理",
   "target": "k:1.1:幻觉",
   "type": "path"
  },
  {
   "source": "k:1.1:幻觉",
   "target": "k:1.1:上下文窗口",
   "type": "path"
  },
  {
   "source": "k:1.1:上下文窗口",
   "target": "k:1.2:六家对比",
   "type": "path"
  },
  {
   "source": "k:1.2:六家对比",
   "target": "k:1.2:选模型口诀",
   "type": "path"
  },
  {
   "source": "k:1.2:选模型口诀",
   "target": "k:1.2:中转平台",
   "type": "path"
  },
  {
   "source": "k:1.2:中转平台",
   "target": "k:1.3:HTTP 基础",
   "type": "path"
  },
  {
   "source": "k:1.3:HTTP 基础",
   "target": "k:1.3:API Key 安全",
   "type": "path"
  },
  {
   "source": "k:1.3:API Key 安全",
   "target": "k:1.3:Messages 结构",
   "type": "path"
  },
  {
   "source": "k:1.3:Messages 结构",
   "target": "k:1.3:四角色",
   "type": "path"
  },
  {
   "source": "k:1.3:四角色",
   "target": "k:1.3:参数",
   "type": "path"
  },
  {
   "source": "k:1.3:参数",
   "target": "k:1.3:返回结构",
   "type": "path"
  },
  {
   "source": "k:1.3:返回结构",
   "target": "k:1.3:usage",
   "type": "path"
  },
  {
   "source": "k:1.3:usage",
   "target": "k:1.3:跨轮记忆",
   "type": "path"
  },
  {
   "source": "k:1.3:跨轮记忆",
   "target": "k:1.4:SSE 协议",
   "type": "path"
  },
  {
   "source": "k:1.4:SSE 协议",
   "target": "k:1.4:两处 stream",
   "type": "path"
  },
  {
   "source": "k:1.4:两处 stream",
   "target": "k:1.4:yield 生成器",
   "type": "path"
  },
  {
   "source": "k:1.4:yield 生成器",
   "target": "k:1.4:iter_lines()",
   "type": "path"
  },
  {
   "source": "k:1.4:iter_lines()",
   "target": "k:1.4:delta vs message",
   "type": "path"
  },
  {
   "source": "k:1.4:delta vs message",
   "target": "k:1.4:reasoning_content",
   "type": "path"
  },
  {
   "source": "k:1.4:reasoning_content",
   "target": "k:1.5:System Prompt 四法则",
   "type": "path"
  },
  {
   "source": "k:1.5:System Prompt 四法则",
   "target": "k:1.5:Zero-shot",
   "type": "path"
  },
  {
   "source": "k:1.5:Zero-shot",
   "target": "k:1.5:Few-shot",
   "type": "path"
  },
  {
   "source": "k:1.5:Few-shot",
   "target": "k:1.5:CoT",
   "type": "path"
  },
  {
   "source": "k:1.5:CoT",
   "target": "k:1.5:XML 标签",
   "type": "path"
  },
  {
   "source": "k:1.5:XML 标签",
   "target": "k:1.5:深度角色",
   "type": "path"
  },
  {
   "source": "k:1.5:深度角色",
   "target": "k:1.5:水平差异化",
   "type": "path"
  },
  {
   "source": "k:1.5:水平差异化",
   "target": "k:1.5:JSON 剥壳",
   "type": "path"
  },
  {
   "source": "k:1.5:JSON 剥壳",
   "target": "k:1.6:Pydantic BaseModel",
   "type": "path"
  },
  {
   "source": "k:1.6:Pydantic BaseModel",
   "target": "k:1.6:Field(description=)",
   "type": "path"
  },
  {
   "source": "k:1.6:Field(description=)",
   "target": "k:1.6:`Recipe(**dict)`",
   "type": "path"
  },
  {
   "source": "k:1.6:`Recipe(**dict)`",
   "target": "k:2.1:工具的本质",
   "type": "path"
  },
  {
   "source": "k:2.1:工具的本质",
   "target": "k:2.1:执行流程",
   "type": "path"
  },
  {
   "source": "k:2.1:执行流程",
   "target": "k:2.1:核心循环",
   "type": "path"
  },
  {
   "source": "k:2.1:核心循环",
   "target": "k:2.1:消息顺序",
   "type": "path"
  },
  {
   "source": "k:2.1:消息顺序",
   "target": "k:2.1:tool_call_id",
   "type": "path"
  },
  {
   "source": "k:2.1:tool_call_id",
   "target": "k:2.1:并行调用",
   "type": "path"
  },
  {
   "source": "k:2.1:并行调用",
   "target": "k:2.1:Schema 设计",
   "type": "path"
  },
  {
   "source": "k:2.1:Schema 设计",
   "target": "k:2.1:safe_get()",
   "type": "path"
  },
  {
   "source": "k:2.1:safe_get()",
   "target": "k:2.1:安检闸门模式",
   "type": "path"
  },
  {
   "source": "k:2.1:安检闸门模式",
   "target": "k:2.1:parse_tool_arguments()",
   "type": "path"
  },
  {
   "source": "k:2.1:parse_tool_arguments()",
   "target": "k:2.2:ReAct 原理",
   "type": "path"
  },
  {
   "source": "k:2.2:ReAct 原理",
   "target": "k:2.2:tool_loop vs ReAct",
   "type": "path"
  },
  {
   "source": "k:2.2:tool_loop vs ReAct",
   "target": "k:2.2:body 重建",
   "type": "path"
  },
  {
   "source": "k:2.2:body 重建",
   "target": "k:2.2:终止条件",
   "type": "path"
  },
  {
   "source": "k:2.2:终止条件",
   "target": "k:2.2:AgentState",
   "type": "path"
  },
  {
   "source": "k:2.2:AgentState",
   "target": "k:2.2:路径沙箱",
   "type": "path"
  },
  {
   "source": "k:2.2:路径沙箱",
   "target": "k:2.3:滑动窗口",
   "type": "path"
  },
  {
   "source": "k:2.3:滑动窗口",
   "target": "k:2.3:system 常驻豁免",
   "type": "path"
  },
  {
   "source": "k:2.3:system 常驻豁免",
   "target": "k:2.3:轮（turn）",
   "type": "path"
  },
  {
   "source": "k:2.3:轮（turn）",
   "target": "k:2.3:摘要压缩",
   "type": "path"
  },
  {
   "source": "k:2.3:摘要压缩",
   "target": "k:2.3:摘要合并进 system",
   "type": "path"
  },
  {
   "source": "k:2.3:摘要合并进 system",
   "target": "k:2.3:混合策略",
   "type": "path"
  },
  {
   "source": "k:2.3:混合策略",
   "target": "k:2.3:token 粗估",
   "type": "path"
  },
  {
   "source": "k:2.3:token 粗估",
   "target": "k:2.3:三种记忆分工",
   "type": "path"
  },
  {
   "source": "k:2.3:三种记忆分工",
   "target": "k:2.3:对比实验设计",
   "type": "path"
  },
  {
   "source": "k:2.3:对比实验设计",
   "target": "k:2.3:埋事实测记忆",
   "type": "path"
  },
  {
   "source": "k:2.3:埋事实测记忆",
   "target": "k:2.3:回调函数注入",
   "type": "path"
  },
  {
   "source": "k:2.3:回调函数注入",
   "target": "k:2.3:长期记忆闭环",
   "type": "path"
  },
  {
   "source": "k:2.3:长期记忆闭环",
   "target": "k:2.3:抽取",
   "type": "path"
  },
  {
   "source": "k:2.3:抽取",
   "target": "k:2.3:规则抽取 vs LLM 抽取",
   "type": "path"
  },
  {
   "source": "k:2.3:规则抽取 vs LLM 抽取",
   "target": "k:2.3:system 注入点",
   "type": "path"
  },
  {
   "source": "k:2.3:system 注入点",
   "target": "k:2.3:json 落盘",
   "type": "path"
  },
  {
   "source": "k:2.3:json 落盘",
   "target": "k:2.3:ensure_ascii=False + indent=2",
   "type": "path"
  },
  {
   "source": "k:2.3:ensure_ascii=False + indent=2",
   "target": "k:2.3:容错兜底",
   "type": "path"
  },
  {
   "source": "k:2.3:容错兜底",
   "target": "k:2.3:不可变更新",
   "type": "path"
  },
  {
   "source": "k:2.3:不可变更新",
   "target": "k:2.3:表驱动",
   "type": "path"
  },
  {
   "source": "k:2.3:表驱动",
   "target": "k:2.3:startswith()",
   "type": "path"
  },
  {
   "source": "k:2.3:startswith()",
   "target": "k:2.3:assert 断言收窄",
   "type": "path"
  },
  {
   "source": "k:2.3:assert 断言收窄",
   "target": "k:2.3:过严断言",
   "type": "path"
  },
  {
   "source": "k:2.3:过严断言",
   "target": "k:2.3:浅拷贝陷阱",
   "type": "path"
  },
  {
   "source": "k:2.3:浅拷贝陷阱",
   "target": "k:2.3:{**d, k: v} 合并",
   "type": "path"
  },
  {
   "source": "k:2.3:{**d, k: v} 合并",
   "target": "k:2.3:dict 保持插入顺序",
   "type": "path"
  },
  {
   "source": "k:2.3:dict 保持插入顺序",
   "target": "k:2.3:FIFO 淘汰",
   "type": "path"
  },
  {
   "source": "k:2.3:FIFO 淘汰",
   "target": "k:2.3:del 语句",
   "type": "path"
  },
  {
   "source": "k:2.3:del 语句",
   "target": "k:2.3:卫语句双条件",
   "type": "path"
  },
  {
   "source": "k:2.3:卫语句双条件",
   "target": "k:2.4:Plan-and-Execute 模式",
   "type": "path"
  },
  {
   "source": "k:2.4:Plan-and-Execute 模式",
   "target": "k:2.4:计划即数据",
   "type": "path"
  },
  {
   "source": "k:2.4:计划即数据",
   "target": "k:2.4:静态清单循环 vs 动态决定",
   "type": "path"
  },
  {
   "source": "k:2.4:静态清单循环 vs 动态决定",
   "target": "k:2.4:工具注册表分发",
   "type": "path"
  },
  {
   "source": "k:2.4:工具注册表分发",
   "target": "k:2.4:*args 调用侧解包",
   "type": "path"
  },
  {
   "source": "k:2.4:*args 调用侧解包",
   "target": "k:2.4:优雅降级",
   "type": "path"
  },
  {
   "source": "k:2.4:优雅降级",
   "target": "k:2.4:校验器参数放宽",
   "type": "path"
  },
  {
   "source": "k:2.4:校验器参数放宽",
   "target": "k:2.4:动态重规划",
   "type": "path"
  },
  {
   "source": "k:2.4:动态重规划",
   "target": "k:2.4:重规划预算 max_replans",
   "type": "path"
  },
  {
   "source": "k:2.4:重规划预算 max_replans",
   "target": "k:2.4:错误即数据",
   "type": "path"
  },
  {
   "source": "k:2.4:错误即数据",
   "target": "k:2.4:while+手动索引",
   "type": "path"
  },
  {
   "source": "k:2.4:while+手动索引",
   "target": "k:2.4:import 自己的模块",
   "type": "path"
  },
  {
   "source": "k:2.4:import 自己的模块",
   "target": "k:2.4:失败痕迹保留",
   "type": "path"
  },
  {
   "source": "k:2.4:失败痕迹保留",
   "target": "k:2.4:planner vs replanner",
   "type": "path"
  },
  {
   "source": "k:2.4:planner vs replanner",
   "target": "k:2.4:共享黑板 state",
   "type": "path"
  },
  {
   "source": "k:2.4:共享黑板 state",
   "target": "k:2.4:zip 拉链配对",
   "type": "path"
  },
  {
   "source": "k:2.4:zip 拉链配对",
   "target": "k:2.4:CWD vs 脚本目录",
   "type": "path"
  },
  {
   "source": "k:2.4:CWD vs 脚本目录",
   "target": "k:2.4:Workflow vs Agent",
   "type": "path"
  },
  {
   "source": "k:2.4:Workflow vs Agent",
   "target": "k:2.4:gate 闸门思想",
   "type": "path"
  },
  {
   "source": "k:2.4:gate 闸门思想",
   "target": "k:2.4:何时该用 Agent",
   "type": "path"
  },
  {
   "source": "k:2.4:何时该用 Agent",
   "target": "k:2.4:依赖感知执行（拓扑排序朴素版）",
   "type": "path"
  },
  {
   "source": "k:2.4:依赖感知执行（拓扑排序朴素版）",
   "target": "k:2.4:死锁检测",
   "type": "path"
  },
  {
   "source": "k:2.4:死锁检测",
   "target": "k:2.4:done 用 set",
   "type": "path"
  },
  {
   "source": "k:2.4:done 用 set",
   "target": "k:2.4:sorted(key=lambda)",
   "type": "path"
  },
  {
   "source": "k:2.4:sorted(key=lambda)",
   "target": "k:2.4:all() / any()",
   "type": "path"
  },
  {
   "source": "k:2.4:all() / any()",
   "target": "k:2.5:反思循环",
   "type": "path"
  },
  {
   "source": "k:2.5:反思循环",
   "target": "k:2.5:批评家=规则代码",
   "type": "path"
  },
  {
   "source": "k:2.5:批评家=规则代码",
   "target": "k:2.5:反思便签=工作记忆",
   "type": "path"
  },
  {
   "source": "k:2.5:反思便签=工作记忆",
   "target": "k:2.5:问题收敛曲线",
   "type": "path"
  },
  {
   "source": "k:2.5:问题收敛曲线",
   "target": "k:2.5:critic 返回问题清单",
   "type": "path"
  },
  {
   "source": "k:2.5:critic 返回问题清单",
   "target": "k:2.5:预算即圈数",
   "type": "path"
  },
  {
   "source": "k:2.5:预算即圈数",
   "target": "k:2.5:语言强化学习",
   "type": "path"
  },
  {
   "source": "k:2.5:语言强化学习",
   "target": "k:2.5:Actor/Evaluator/Self-reflection",
   "type": "path"
  },
  {
   "source": "k:2.5:Actor/Evaluator/Self-reflection",
   "target": "k:2.5:episodic memory",
   "type": "path"
  },
  {
   "source": "k:2.5:episodic memory",
   "target": "k:2.5:反思按需付费",
   "type": "path"
  },
  {
   "source": "k:2.5:反思按需付费",
   "target": "k:7.1:三遍寻宝法",
   "type": "path"
  },
  {
   "source": "k:7.1:三遍寻宝法",
   "target": "k:7.1:Figure 1 定律",
   "type": "path"
  },
  {
   "source": "k:7.1:Figure 1 定律",
   "target": "k:7.1:代码锚定法",
   "type": "path"
  },
  {
   "source": "k:7.1:代码锚定法",
   "target": "k:7.1:费曼检验",
   "type": "path"
  },
  {
   "source": "k:7.1:费曼检验",
   "target": "k:7.1:episodic memory 实现",
   "type": "path"
  },
  {
   "source": "k:7.1:episodic memory 实现",
   "target": "k:7.1:读旧+append+写回",
   "type": "path"
  },
  {
   "source": "k:7.1:读旧+append+写回",
   "target": "k:7.1:容错返回同形状",
   "type": "path"
  },
  {
   "source": "k:7.1:容错返回同形状",
   "target": "k:7.1:剧本放闭包外",
   "type": "path"
  },
  {
   "source": "k:7.1:剧本放闭包外",
   "target": "k:2.6:威胁矩阵",
   "type": "path"
  },
  {
   "source": "k:2.6:威胁矩阵",
   "target": "k:2.6:Prompt 注入",
   "type": "path"
  },
  {
   "source": "k:2.6:Prompt 注入",
   "target": "k:2.6:大小写归一化",
   "type": "path"
  },
  {
   "source": "k:2.6:大小写归一化",
   "target": "k:2.6:表驱动特征检测",
   "type": "path"
  },
  {
   "source": "k:2.6:表驱动特征检测",
   "target": "k:2.6:过滤 vs 拦截",
   "type": "path"
  },
  {
   "source": "k:2.6:过滤 vs 拦截",
   "target": "k:2.6:规则模拟 LLM",
   "type": "path"
  },
  {
   "source": "k:2.6:规则模拟 LLM",
   "target": "k:2.6:遍历字符串陷阱",
   "type": "path"
  },
  {
   "source": "k:2.6:遍历字符串陷阱",
   "target": "k:2.6:绿黄红权限分级",
   "type": "path"
  },
  {
   "source": "k:2.6:绿黄红权限分级",
   "target": "k:2.6:默认拒绝 Default Deny",
   "type": "path"
  },
  {
   "source": "k:2.6:默认拒绝 Default Deny",
   "target": "k:2.6:审计记裁决不记申报",
   "type": "path"
  },
  {
   "source": "k:2.6:审计记裁决不记申报",
   "target": "k:2.6:闸门与执行分离",
   "type": "path"
  },
  {
   "source": "k:2.6:闸门与执行分离",
   "target": "k:2.6:输出校验(出口安检)",
   "type": "path"
  },
  {
   "source": "k:2.6:输出校验(出口安检)",
   "target": "k:2.6:检查优先级=契约",
   "type": "path"
  },
  {
   "source": "k:2.6:检查优先级=契约",
   "target": "k:2.6:resolve后再验身",
   "type": "path"
  },
  {
   "source": "k:2.6:resolve后再验身",
   "target": "k:2.6:纵深防御代码形状",
   "type": "path"
  },
  {
   "source": "k:2.6:纵深防御代码形状",
   "target": "k:2.6:OWASP LLM Top 10",
   "type": "path"
  },
  {
   "source": "k:2.6:OWASP LLM Top 10",
   "target": "k:2.6:5攻5防口诀",
   "type": "path"
  },
  {
   "source": "k:2.6:5攻5防口诀",
   "target": "k:2.6:LLM输出=概率猜测",
   "type": "path"
  },
  {
   "source": "k:2.6:LLM输出=概率猜测",
   "target": "k:2.6:文字版ReAct协议",
   "type": "path"
  },
  {
   "source": "k:2.6:文字版ReAct协议",
   "target": "k:2.6:脚本自举模式",
   "type": "path"
  },
  {
   "source": "k:2.6:脚本自举模式",
   "target": "k:2.6:Agent可靠性来源",
   "type": "path"
  },
  {
   "source": "k:2.6:Agent可靠性来源",
   "target": "x:0",
   "type": "path"
  },
  {
   "source": "x:0",
   "target": "x:1",
   "type": "path"
  },
  {
   "source": "x:1",
   "target": "x:2",
   "type": "path"
  },
  {
   "source": "x:2",
   "target": "x:3",
   "type": "path"
  },
  {
   "source": "x:3",
   "target": "x:4",
   "type": "path"
  },
  {
   "source": "x:4",
   "target": "x:5",
   "type": "path"
  },
  {
   "source": "k:1.2:六家对比",
   "target": "k:1.2:选模型口诀",
   "type": "related",
   "label": "gpt"
  },
  {
   "source": "k:2.5:episodic memory",
   "target": "k:7.1:episodic memory 实现",
   "type": "related",
   "label": "memory"
  },
  {
   "source": "k:2.3:规则抽取 vs LLM 抽取",
   "target": "k:2.6:规则模拟 LLM",
   "type": "related",
   "label": "llm"
  },
  {
   "source": "k:2.1:parse_tool_arguments()",
   "target": "k:2.3:json 落盘",
   "type": "related",
   "label": "loads"
  },
  {
   "source": "k:0.3:class + __init__",
   "target": "k:0.3:super().__init__()",
   "type": "related",
   "label": "__init__"
  },
  {
   "source": "k:1.3:四角色",
   "target": "k:2.1:消息顺序",
   "type": "related",
   "label": "assistant"
  },
  {
   "source": "k:2.3:system 常驻豁免",
   "target": "k:2.3:system 注入点",
   "type": "related",
   "label": "system"
  },
  {
   "source": "k:2.3:摘要合并进 system",
   "target": "k:2.3:system 注入点",
   "type": "related",
   "label": "system"
  },
  {
   "source": "k:1.1:AI→ML→DL→LLM→Agent",
   "target": "k:2.4:Workflow vs Agent",
   "type": "related",
   "label": "agent"
  },
  {
   "source": "k:2.3:system 常驻豁免",
   "target": "k:2.3:摘要合并进 system",
   "type": "related",
   "label": "system"
  },
  {
   "source": "k:0.1:四种数据结构",
   "target": "k:2.4:计划即数据",
   "type": "related",
   "label": "dict"
  },
  {
   "source": "k:1.3:四角色",
   "target": "k:2.3:system 注入点",
   "type": "related",
   "label": "system"
  },
  {
   "source": "k:0.1:异常处理",
   "target": "k:0.2:脏数据跳过",
   "type": "related",
   "label": "try"
  },
  {
   "source": "k:1.5:System Prompt 四法则",
   "target": "k:2.6:Prompt 注入",
   "type": "related",
   "label": "prompt"
  },
  {
   "source": "k:1.6:`Recipe(**dict)`",
   "target": "k:2.3:dict 保持插入顺序",
   "type": "related",
   "label": "dict"
  },
  {
   "source": "k:1.6:`Recipe(**dict)`",
   "target": "k:2.4:Workflow vs Agent",
   "type": "related",
   "label": "llm"
  },
  {
   "source": "k:2.3:规则抽取 vs LLM 抽取",
   "target": "k:2.5:批评家=规则代码",
   "type": "related",
   "label": "llm"
  },
  {
   "source": "k:2.5:批评家=规则代码",
   "target": "k:2.6:规则模拟 LLM",
   "type": "related",
   "label": "llm"
  },
  {
   "source": "k:0.1:四种数据结构",
   "target": "k:2.4:校验器参数放宽",
   "type": "related",
   "label": "dict"
  },
  {
   "source": "k:0.1:字符串操作",
   "target": "k:0.2:CSV 解析套路",
   "type": "related",
   "label": "strip"
  },
  {
   "source": "k:0.3:field(default_factory=list)",
   "target": "k:1.6:Field(description=)",
   "type": "related",
   "label": "field"
  },
  {
   "source": "k:0.3:field(default_factory=list)",
   "target": "k:2.4:校验器参数放宽",
   "type": "related",
   "label": "list"
  },
  {
   "source": "k:1.1:AI→ML→DL→LLM→Agent",
   "target": "k:1.6:`Recipe(**dict)`",
   "type": "related",
   "label": "llm"
  },
  {
   "source": "k:1.1:AI→ML→DL→LLM→Agent",
   "target": "k:2.3:规则抽取 vs LLM 抽取",
   "type": "related",
   "label": "llm"
  },
  {
   "source": "k:1.1:AI→ML→DL→LLM→Agent",
   "target": "k:2.4:何时该用 Agent",
   "type": "related",
   "label": "agent"
  },
  {
   "source": "k:1.1:Token",
   "target": "k:1.3:usage",
   "type": "related",
   "label": "token"
  },
  {
   "source": "k:1.1:Token",
   "target": "k:2.3:token 粗估",
   "type": "related",
   "label": "token"
  },
  {
   "source": "k:1.3:API Key 安全",
   "target": "k:2.4:sorted(key=lambda)",
   "type": "related",
   "label": "key"
  },
  {
   "source": "k:1.3:四角色",
   "target": "k:2.3:轮（turn）",
   "type": "related",
   "label": "assistant"
  },
  {
   "source": "k:1.3:usage",
   "target": "k:2.3:token 粗估",
   "type": "related",
   "label": "token"
  },
  {
   "source": "k:1.5:System Prompt 四法则",
   "target": "k:2.3:system 常驻豁免",
   "type": "related",
   "label": "system"
  },
  {
   "source": "k:1.5:System Prompt 四法则",
   "target": "k:2.3:摘要合并进 system",
   "type": "related",
   "label": "system"
  },
  {
   "source": "k:1.5:System Prompt 四法则",
   "target": "k:2.3:system 注入点",
   "type": "related",
   "label": "system"
  },
  {
   "source": "k:1.5:JSON 剥壳",
   "target": "k:2.3:json 落盘",
   "type": "related",
   "label": "json"
  },
  {
   "source": "k:2.1:消息顺序",
   "target": "k:2.3:轮（turn）",
   "type": "related",
   "label": "assistant"
  },
  {
   "source": "k:2.1:safe_get()",
   "target": "k:2.4:sorted(key=lambda)",
   "type": "related",
   "label": "key"
  },
  {
   "source": "k:2.1:safe_get()",
   "target": "k:2.6:默认拒绝 Default Deny",
   "type": "related",
   "label": "dict"
  },
  {
   "source": "k:2.2:ReAct 原理",
   "target": "k:2.6:文字版ReAct协议",
   "type": "related",
   "label": "react"
  },
  {
   "source": "k:2.2:tool_loop vs ReAct",
   "target": "k:2.6:文字版ReAct协议",
   "type": "related",
   "label": "react"
  },
  {
   "source": "k:2.2:AgentState",
   "target": "k:2.3:三种记忆分工",
   "type": "related",
   "label": "messages"
  },
  {
   "source": "k:2.3:规则抽取 vs LLM 抽取",
   "target": "k:2.6:OWASP LLM Top 10",
   "type": "related",
   "label": "llm"
  },
  {
   "source": "k:2.4:Workflow vs Agent",
   "target": "k:2.6:Agent可靠性来源",
   "type": "related",
   "label": "agent"
  },
  {
   "source": "k:2.4:何时该用 Agent",
   "target": "k:2.6:Agent可靠性来源",
   "type": "related",
   "label": "agent"
  },
  {
   "source": "k:2.3:表驱动",
   "target": "k:2.6:表驱动特征检测",
   "type": "related",
   "label": "表驱"
  },
  {
   "source": "k:0.1:四种数据结构",
   "target": "k:2.3:不可变更新",
   "type": "related",
   "label": "dict"
  },
  {
   "source": "k:1.1:上下文窗口",
   "target": "k:2.3:token 粗估",
   "type": "related",
   "label": "token"
  },
  {
   "source": "k:1.3:跨轮记忆",
   "target": "k:2.3:三种记忆分工",
   "type": "related",
   "label": "messages"
  },
  {
   "source": "k:2.3:回调函数注入",
   "target": "k:2.5:批评家=规则代码",
   "type": "related",
   "label": "llm"
  },
  {
   "source": "k:2.3:回调函数注入",
   "target": "k:2.6:Prompt 注入",
   "type": "related",
   "label": "llm"
  },
  {
   "source": "k:2.4:静态清单循环 vs 动态决定",
   "target": "k:2.5:反思循环",
   "type": "related",
   "label": "react"
  },
  {
   "source": "k:2.4:CWD vs 脚本目录",
   "target": "k:2.6:脚本自举模式",
   "type": "related",
   "label": "path"
  },
  {
   "source": "s:2",
   "target": "x:0",
   "type": "planned"
  },
  {
   "source": "s:2",
   "target": "x:1",
   "type": "planned"
  },
  {
   "source": "s:2",
   "target": "x:2",
   "type": "planned"
  }
 ],
 "stages": [
  {
   "code": "0",
   "name": "0. Python 基础",
   "progress": 100
  },
  {
   "code": "1",
   "name": "1. LLM 基础",
   "progress": 98
  },
  {
   "code": "2",
   "name": "2. Agent 核心",
   "progress": 100
  }
 ],
 "modules": [
  {
   "id": "m:0.1",
   "code": "0.1",
   "name": "语法与数据结构",
   "stage": "0",
   "points": [
    "k:0.1:变量与数据类型",
    "k:0.1:条件判断",
    "k:0.1:循环",
    "k:0.1:四种数据结构",
    "k:0.1:内置函数",
    "k:0.1:字符串操作",
    "k:0.1:卫语句",
    "k:0.1:异常处理"
   ]
  },
  {
   "id": "m:0.2",
   "code": "0.2",
   "name": "文件读写",
   "stage": "0",
   "points": [
    "k:0.2:with open()",
    "k:0.2:读取模式",
    "k:0.2:CSV 解析套路",
    "k:0.2:跳过表头",
    "k:0.2:脏数据跳过"
   ]
  },
  {
   "id": "m:0.3",
   "code": "0.3",
   "name": "面向对象",
   "stage": "0",
   "points": [
    "k:0.3:class + __init__",
    "k:0.3:实例属性 vs 方法",
    "k:0.3:__repr__",
    "k:0.3:布尔状态管理",
    "k:0.3:继承",
    "k:0.3:super().__init__()",
    "k:0.3:方法覆盖",
    "k:0.3:isinstance()",
    "k:0.3:@dataclass",
    "k:0.3:field(default_factory=list)",
    "k:0.3:Literal[1,2,3]",
    "k:0.3:类型注解 vs 赋值"
   ]
  },
  {
   "id": "m:0.4",
   "code": "0.4",
   "name": "Git 与工具",
   "stage": "0",
   "points": [
    "k:0.4:Git 三区模型",
    "k:0.4:.gitignore",
    "k:0.4:conda + pip",
    "k:0.4:PYTHONUTF8=1"
   ]
  },
  {
   "id": "m:1.1",
   "code": "1.1",
   "name": "概念",
   "stage": "1",
   "points": [
    "k:1.1:AI→ML→DL→LLM→Agent",
    "k:1.1:Token",
    "k:1.1:参数（7B/70B）",
    "k:1.1:训练 vs 推理",
    "k:1.1:幻觉",
    "k:1.1:上下文窗口"
   ]
  },
  {
   "id": "m:1.2",
   "code": "1.2",
   "name": "模型全景",
   "stage": "1",
   "points": [
    "k:1.2:六家对比",
    "k:1.2:选模型口诀",
    "k:1.2:中转平台"
   ]
  },
  {
   "id": "m:1.3",
   "code": "1.3",
   "name": "API 调用",
   "stage": "1",
   "points": [
    "k:1.3:HTTP 基础",
    "k:1.3:API Key 安全",
    "k:1.3:Messages 结构",
    "k:1.3:四角色",
    "k:1.3:参数",
    "k:1.3:返回结构",
    "k:1.3:usage",
    "k:1.3:跨轮记忆"
   ]
  },
  {
   "id": "m:1.4",
   "code": "1.4",
   "name": "流式输出",
   "stage": "1",
   "points": [
    "k:1.4:SSE 协议",
    "k:1.4:两处 stream",
    "k:1.4:yield 生成器",
    "k:1.4:iter_lines()",
    "k:1.4:delta vs message",
    "k:1.4:reasoning_content"
   ]
  },
  {
   "id": "m:1.5",
   "code": "1.5",
   "name": "Prompt Engineering",
   "stage": "1",
   "points": [
    "k:1.5:System Prompt 四法则",
    "k:1.5:Zero-shot",
    "k:1.5:Few-shot",
    "k:1.5:CoT",
    "k:1.5:XML 标签",
    "k:1.5:深度角色",
    "k:1.5:水平差异化",
    "k:1.5:JSON 剥壳"
   ]
  },
  {
   "id": "m:1.6",
   "code": "1.6",
   "name": "结构化输出",
   "stage": "1",
   "points": [
    "k:1.6:Pydantic BaseModel",
    "k:1.6:Field(description=)",
    "k:1.6:`Recipe(**dict)`"
   ]
  },
  {
   "id": "m:2.1",
   "code": "2.1",
   "name": "Tool Calling",
   "stage": "2",
   "points": [
    "k:2.1:工具的本质",
    "k:2.1:执行流程",
    "k:2.1:核心循环",
    "k:2.1:消息顺序",
    "k:2.1:tool_call_id",
    "k:2.1:并行调用",
    "k:2.1:Schema 设计",
    "k:2.1:safe_get()",
    "k:2.1:安检闸门模式",
    "k:2.1:parse_tool_arguments()"
   ]
  },
  {
   "id": "m:2.2",
   "code": "2.2",
   "name": "Agent 循环手写（ReAct）",
   "stage": "2",
   "points": [
    "k:2.2:ReAct 原理",
    "k:2.2:tool_loop vs ReAct",
    "k:2.2:body 重建",
    "k:2.2:终止条件",
    "k:2.2:AgentState",
    "k:2.2:路径沙箱"
   ]
  },
  {
   "id": "m:2.3",
   "code": "2.3",
   "name": "记忆系统",
   "stage": "2",
   "points": [
    "k:2.3:滑动窗口",
    "k:2.3:system 常驻豁免",
    "k:2.3:轮（turn）",
    "k:2.3:摘要压缩",
    "k:2.3:摘要合并进 system",
    "k:2.3:混合策略",
    "k:2.3:token 粗估",
    "k:2.3:三种记忆分工",
    "k:2.3:对比实验设计",
    "k:2.3:埋事实测记忆",
    "k:2.3:回调函数注入",
    "k:2.3:长期记忆闭环",
    "k:2.3:抽取",
    "k:2.3:规则抽取 vs LLM 抽取",
    "k:2.3:system 注入点",
    "k:2.3:json 落盘",
    "k:2.3:ensure_ascii=False + indent=2",
    "k:2.3:容错兜底",
    "k:2.3:不可变更新",
    "k:2.3:表驱动",
    "k:2.3:startswith()",
    "k:2.3:assert 断言收窄",
    "k:2.3:过严断言",
    "k:2.3:浅拷贝陷阱",
    "k:2.3:{**d, k: v} 合并",
    "k:2.3:dict 保持插入顺序",
    "k:2.3:FIFO 淘汰",
    "k:2.3:del 语句",
    "k:2.3:卫语句双条件"
   ]
  },
  {
   "id": "m:2.4",
   "code": "2.4",
   "name": "任务规划与分解",
   "stage": "2",
   "points": [
    "k:2.4:Plan-and-Execute 模式",
    "k:2.4:计划即数据",
    "k:2.4:静态清单循环 vs 动态决定",
    "k:2.4:工具注册表分发",
    "k:2.4:*args 调用侧解包",
    "k:2.4:优雅降级",
    "k:2.4:校验器参数放宽",
    "k:2.4:动态重规划",
    "k:2.4:重规划预算 max_replans",
    "k:2.4:错误即数据",
    "k:2.4:while+手动索引",
    "k:2.4:import 自己的模块",
    "k:2.4:失败痕迹保留",
    "k:2.4:planner vs replanner",
    "k:2.4:共享黑板 state",
    "k:2.4:zip 拉链配对",
    "k:2.4:CWD vs 脚本目录",
    "k:2.4:Workflow vs Agent",
    "k:2.4:gate 闸门思想",
    "k:2.4:何时该用 Agent",
    "k:2.4:依赖感知执行（拓扑排序朴素版）",
    "k:2.4:死锁检测",
    "k:2.4:done 用 set",
    "k:2.4:sorted(key=lambda)",
    "k:2.4:all() / any()"
   ]
  },
  {
   "id": "m:2.5",
   "code": "2.5",
   "name": "Reflection 反思机制",
   "stage": "2",
   "points": [
    "k:2.5:反思循环",
    "k:2.5:批评家=规则代码",
    "k:2.5:反思便签=工作记忆",
    "k:2.5:问题收敛曲线",
    "k:2.5:critic 返回问题清单",
    "k:2.5:预算即圈数",
    "k:2.5:语言强化学习",
    "k:2.5:Actor/Evaluator/Self-reflection",
    "k:2.5:episodic memory",
    "k:2.5:反思按需付费"
   ]
  },
  {
   "id": "m:7.1",
   "code": "7.1",
   "name": "论文阅读（元能力）",
   "stage": "2",
   "points": [
    "k:7.1:三遍寻宝法",
    "k:7.1:Figure 1 定律",
    "k:7.1:代码锚定法",
    "k:7.1:费曼检验",
    "k:7.1:episodic memory 实现",
    "k:7.1:读旧+append+写回",
    "k:7.1:容错返回同形状",
    "k:7.1:剧本放闭包外"
   ]
  },
  {
   "id": "m:2.6",
   "code": "2.6",
   "name": "安全与护栏",
   "stage": "2",
   "points": [
    "k:2.6:威胁矩阵",
    "k:2.6:Prompt 注入",
    "k:2.6:大小写归一化",
    "k:2.6:表驱动特征检测",
    "k:2.6:过滤 vs 拦截",
    "k:2.6:规则模拟 LLM",
    "k:2.6:遍历字符串陷阱",
    "k:2.6:绿黄红权限分级",
    "k:2.6:默认拒绝 Default Deny",
    "k:2.6:审计记裁决不记申报",
    "k:2.6:闸门与执行分离",
    "k:2.6:输出校验(出口安检)",
    "k:2.6:检查优先级=契约",
    "k:2.6:resolve后再验身",
    "k:2.6:纵深防御代码形状",
    "k:2.6:OWASP LLM Top 10",
    "k:2.6:5攻5防口诀",
    "k:2.6:LLM输出=概率猜测",
    "k:2.6:文字版ReAct协议",
    "k:2.6:脚本自举模式",
    "k:2.6:Agent可靠性来源"
   ]
  }
 ],
 "points": [
  {
   "id": "k:0.1:变量与数据类型",
   "name": "变量与数据类型",
   "desc": "int/float/str/bool，类型由值决定",
   "module": "0.1",
   "stage": "0",
   "pitfalls": [
    {
     "num": 42,
     "err": "`int(msg[\"role\"])` ValueError",
     "fix": "求字符数用 `len()`"
    }
   ],
   "learned": true,
   "days": [
    3,
    1,
    7
   ]
  },
  {
   "id": "k:0.1:条件判断",
   "name": "条件判断",
   "desc": "if/elif/else 分支，elif 可多个",
   "module": "0.1",
   "stage": "0",
   "pitfalls": [],
   "learned": true,
   "days": [
    1
   ]
  },
  {
   "id": "k:0.1:循环",
   "name": "循环",
   "desc": "while（条件循环）/ for（遍历循环）+ break/continue",
   "module": "0.1",
   "stage": "0",
   "pitfalls": [],
   "learned": true,
   "days": [
    1,
    5
   ]
  },
  {
   "id": "k:0.1:四种数据结构",
   "name": "四种数据结构",
   "desc": "list（有序可变）/ tuple（有序不可变）/ dict（键值对）/ set（去重）",
   "module": "0.1",
   "stage": "0",
   "pitfalls": [
    {
     "num": 39,
     "err": "`merged + recent_messages[1:]` 报错",
     "fix": "用 `[merged] + recent_messages[1:]` 包成列表再拼接"
    },
    {
     "num": 50,
     "err": "`id in list[dict]` 永远 False 不报错",
     "fix": "in 之前核对两边类型一致；查 id 集合用 set"
    }
   ],
   "learned": true,
   "days": [
    4,
    7,
    5
   ]
  },
  {
   "id": "k:0.1:内置函数",
   "name": "内置函数",
   "desc": "sum/max/min/len/round/float 等",
   "module": "0.1",
   "stage": "0",
   "pitfalls": [
    {
     "num": 23,
     "err": "变量名 max/min 行为诡异",
     "fix": "别用内置函数名做变量名"
    }
   ],
   "learned": true,
   "days": [
    1
   ]
  },
  {
   "id": "k:0.1:字符串操作",
   "name": "字符串操作",
   "desc": "split() 切分、strip() 去空格、f-string 格式化",
   "module": "0.1",
   "stage": "0",
   "pitfalls": [
    {
     "num": 5,
     "err": "f-string 内 `{'c': 42}` 格式冲突",
     "fix": "先存变量再放进 f-string"
    },
    {
     "num": 7,
     "err": "f-string 输出 `{student_level}` 字面量",
     "fix": "检查字符串前有 f"
    }
   ],
   "learned": true,
   "days": [
    1,
    3,
    2
   ]
  },
  {
   "id": "k:0.1:卫语句",
   "name": "卫语句",
   "desc": "空值/非法输入提前 return，减少嵌套",
   "module": "0.1",
   "stage": "0",
   "pitfalls": [],
   "learned": true,
   "days": []
  },
  {
   "id": "k:0.1:异常处理",
   "name": "异常处理",
   "desc": "try/except + 具体异常类型（ValueError/FileNotFoundError）",
   "module": "0.1",
   "stage": "0",
   "pitfalls": [],
   "learned": true,
   "days": [
    1,
    2,
    5
   ]
  },
  {
   "id": "k:0.2:with open()",
   "name": "with open()",
   "desc": "自动管理资源，不用手动 close",
   "module": "0.2",
   "stage": "0",
   "pitfalls": [
    {
     "num": 52,
     "err": "落盘 FileNotFoundError",
     "fix": "写文件三件套：open(path, \"w\", encoding=\"utf-8\")"
    }
   ],
   "learned": true,
   "days": [
    2
   ]
  },
  {
   "id": "k:0.2:读取模式",
   "name": "读取模式",
   "desc": "read() 全读 / readlines() 按行列表 / 逐行 for 遍历",
   "module": "0.2",
   "stage": "0",
   "pitfalls": [],
   "learned": true,
   "days": []
  },
  {
   "id": "k:0.2:CSV 解析套路",
   "name": "CSV 解析套路",
   "desc": "读行 → strip → split → 类型转换 → 收集",
   "module": "0.2",
   "stage": "0",
   "pitfalls": [],
   "learned": true,
   "days": [
    2,
    1
   ]
  },
  {
   "id": "k:0.2:跳过表头",
   "name": "跳过表头",
   "desc": "`lines[1:]` 切片",
   "module": "0.2",
   "stage": "0",
   "pitfalls": [
    {
     "num": 9,
     "err": "列名被当数据处理",
     "fix": "`for line in lines[1:]`"
    }
   ],
   "learned": true,
   "days": [
    2
   ]
  },
  {
   "id": "k:0.2:脏数据跳过",
   "name": "脏数据跳过",
   "desc": "try/except 包裹类型转换，失败 continue",
   "module": "0.2",
   "stage": "0",
   "pitfalls": [],
   "learned": true,
   "days": [
    1,
    5,
    2
   ]
  },
  {
   "id": "k:0.3:class + __init__",
   "name": "class + __init__",
   "desc": "类定义与构造方法，self 指实例本身",
   "module": "0.3",
   "stage": "0",
   "pitfalls": [],
   "learned": true,
   "days": [
    2,
    3
   ]
  },
  {
   "id": "k:0.3:实例属性 vs 方法",
   "name": "实例属性 vs 方法",
   "desc": "属性不加括号，方法要加括号调用",
   "module": "0.3",
   "stage": "0",
   "pitfalls": [
    {
     "num": 18,
     "err": "把属性当方法调（b.title()）",
     "fix": "属性不加括号"
    }
   ],
   "learned": true,
   "days": [
    2
   ]
  },
  {
   "id": "k:0.3:__repr__",
   "name": "__repr__",
   "desc": "魔法方法，控制 print(obj) 的输出",
   "module": "0.3",
   "stage": "0",
   "pitfalls": [],
   "learned": true,
   "days": [
    2,
    3
   ]
  },
  {
   "id": "k:0.3:布尔状态管理",
   "name": "布尔状态管理",
   "desc": "用 available 等布尔属性控制状态（借/还）",
   "module": "0.3",
   "stage": "0",
   "pitfalls": [],
   "learned": true,
   "days": [
    2
   ]
  },
  {
   "id": "k:0.3:继承",
   "name": "继承",
   "desc": "`class A(B):`，子类复用父类接口",
   "module": "0.3",
   "stage": "0",
   "pitfalls": [],
   "learned": true,
   "days": [
    3
   ]
  },
  {
   "id": "k:0.3:super().__init__()",
   "name": "super().__init__()",
   "desc": "调父类构造，不传 self",
   "module": "0.3",
   "stage": "0",
   "pitfalls": [],
   "learned": true,
   "days": [
    3,
    2
   ]
  },
  {
   "id": "k:0.3:方法覆盖",
   "name": "方法覆盖",
   "desc": "子类重写父类方法，各自实现",
   "module": "0.3",
   "stage": "0",
   "pitfalls": [],
   "learned": true,
   "days": [
    3
   ]
  },
  {
   "id": "k:0.3:isinstance()",
   "name": "isinstance()",
   "desc": "验证继承关系",
   "module": "0.3",
   "stage": "0",
   "pitfalls": [],
   "learned": true,
   "days": [
    3,
    5
   ]
  },
  {
   "id": "k:0.3:@dataclass",
   "name": "@dataclass",
   "desc": "自动生成 __init__/__repr__/__eq__，省 80% 样板代码",
   "module": "0.3",
   "stage": "0",
   "pitfalls": [],
   "learned": true,
   "days": [
    3,
    2
   ]
  },
  {
   "id": "k:0.3:field(default_factory=list)",
   "name": "field(default_factory=list)",
   "desc": "可变默认值的正确写法",
   "module": "0.3",
   "stage": "0",
   "pitfalls": [
    {
     "num": 2,
     "err": "`self.tags = list[str] = []` 语法错误",
     "fix": "`self.tags: list[str] = []`"
    },
    {
     "num": 3,
     "err": "`self.tags : list[str] = []` 报错",
     "fix": "冒号紧跟变量名"
    },
    {
     "num": 4,
     "err": "f-string 输出带引号 `'a', 'b'`",
     "fix": "`', '.join(list)` 手动拼"
    }
   ],
   "learned": true,
   "days": [
    3
   ]
  },
  {
   "id": "k:0.3:Literal[1,2,3]",
   "name": "Literal[1,2,3]",
   "desc": "限制取值只能是字面量集合",
   "module": "0.3",
   "stage": "0",
   "pitfalls": [],
   "learned": true,
   "days": [
    3
   ]
  },
  {
   "id": "k:0.3:类型注解 vs 赋值",
   "name": "类型注解 vs 赋值",
   "desc": "`变量: 类型 = 值`，冒号管类型、等号管值",
   "module": "0.3",
   "stage": "0",
   "pitfalls": [],
   "learned": true,
   "days": [
    3
   ]
  },
  {
   "id": "k:0.4:Git 三区模型",
   "name": "Git 三区模型",
   "desc": "工作区(add)→暂存区(commit)→本地仓库(push)→远程",
   "module": "0.4",
   "stage": "0",
   "pitfalls": [
    {
     "num": 36,
     "err": "git push 慢/超时",
     "fix": "正常现象，小项目可接受；必要时走代理"
    }
   ],
   "learned": true,
   "days": [
    1
   ]
  },
  {
   "id": "k:0.4:.gitignore",
   "name": ".gitignore",
   "desc": "排除缓存/虚拟环境/IDE 配置",
   "module": "0.4",
   "stage": "0",
   "pitfalls": [],
   "learned": true,
   "days": [
    1
   ]
  },
  {
   "id": "k:0.4:conda + pip",
   "name": "conda + pip",
   "desc": "环境管理；pip 用清华镜像加速",
   "module": "0.4",
   "stage": "0",
   "pitfalls": [
    {
     "num": 35,
     "err": "conda 环境混乱",
     "fix": "只用一个源"
    }
   ],
   "learned": true,
   "days": [
    1
   ]
  },
  {
   "id": "k:0.4:PYTHONUTF8=1",
   "name": "PYTHONUTF8=1",
   "desc": "环境变量根治 Windows GBK 终端编码问题",
   "module": "0.4",
   "stage": "0",
   "pitfalls": [
    {
     "num": 31,
     "err": "终端输出 emoji 崩溃",
     "fix": "`setx PYTHONUTF8 1` 根治"
    }
   ],
   "learned": true,
   "days": [
    4,
    2
   ]
  },
  {
   "id": "k:1.1:AI→ML→DL→LLM→Agent",
   "name": "AI→ML→DL→LLM→Agent",
   "desc": "俄罗斯套娃层级关系",
   "module": "1.1",
   "stage": "1",
   "pitfalls": [],
   "learned": true,
   "days": [
    4,
    5,
    7
   ]
  },
  {
   "id": "k:1.1:Token",
   "name": "Token",
   "desc": "LLM 最小计数单位，1 token ≈ 1 英文词 ≈ 0.6 中文字",
   "module": "1.1",
   "stage": "1",
   "pitfalls": [],
   "learned": true,
   "days": [
    4,
    7
   ]
  },
  {
   "id": "k:1.1:参数（7B/70B）",
   "name": "参数（7B/70B）",
   "desc": "模型\"脑容量\"，越大越强越贵",
   "module": "1.1",
   "stage": "1",
   "pitfalls": [],
   "learned": true,
   "days": [
    4
   ]
  },
  {
   "id": "k:1.1:训练 vs 推理",
   "name": "训练 vs 推理",
   "desc": "训练=大厂烧钱造模型；推理=你用 API 答题",
   "module": "1.1",
   "stage": "1",
   "pitfalls": [],
   "learned": true,
   "days": [
    4
   ]
  },
  {
   "id": "k:1.1:幻觉",
   "name": "幻觉",
   "desc": "LLM 本质是\"预测下一个词\"，不是查数据库",
   "module": "1.1",
   "stage": "1",
   "pitfalls": [],
   "learned": true,
   "days": [
    4,
    8
   ]
  },
  {
   "id": "k:1.1:上下文窗口",
   "name": "上下文窗口",
   "desc": "一次能处理的 token 上限",
   "module": "1.1",
   "stage": "1",
   "pitfalls": [],
   "learned": true,
   "days": [
    7
   ]
  },
  {
   "id": "k:1.2:六家对比",
   "name": "六家对比",
   "desc": "Claude（安全/代码）/ GPT（生态/多模态）/ Gemini（搜索）/ Llama（开源）/ DeepSeek（性价比/中文）/ Qwen（中文）",
   "module": "1.2",
   "stage": "1",
   "pitfalls": [],
   "learned": true,
   "days": [
    4
   ]
  },
  {
   "id": "k:1.2:选模型口诀",
   "name": "选模型口诀",
   "desc": "日常 DeepSeek、写代码 Claude、多模态 GPT/Gemini、私有化 Llama/Qwen",
   "module": "1.2",
   "stage": "1",
   "pitfalls": [
    {
     "num": 27,
     "err": "模型不存在",
     "fix": "模型 ID 用连字符：`claude-haiku-4-5`"
    }
   ],
   "learned": true,
   "days": [
    4
   ]
  },
  {
   "id": "k:1.2:中转平台",
   "name": "中转平台",
   "desc": "大陆调 Claude 的替代方案（jiekou.vip 等，OpenAI 兼容格式）",
   "module": "1.2",
   "stage": "1",
   "pitfalls": [
    {
     "num": 27,
     "err": "模型不存在",
     "fix": "模型 ID 用连字符：`claude-haiku-4-5`"
    }
   ],
   "learned": true,
   "days": [
    4
   ]
  },
  {
   "id": "k:1.3:HTTP 基础",
   "name": "HTTP 基础",
   "desc": "GET/POST/Header/Body/JSON",
   "module": "1.3",
   "stage": "1",
   "pitfalls": [],
   "learned": true,
   "days": [
    4,
    5
   ]
  },
  {
   "id": "k:1.3:API Key 安全",
   "name": "API Key 安全",
   "desc": "放 .env，用 python-dotenv 加载，绝不写进代码",
   "module": "1.3",
   "stage": "1",
   "pitfalls": [
    {
     "num": 14,
     "err": "返回了 API Key 而不是回复",
     "fix": "命名语义化，返回前核对"
    }
   ],
   "learned": true,
   "days": [
    4,
    5,
    3
   ]
  },
  {
   "id": "k:1.3:Messages 结构",
   "name": "Messages 结构",
   "desc": "统一 messages 数组，换 base_url 即可换模型",
   "module": "1.3",
   "stage": "1",
   "pitfalls": [],
   "learned": true,
   "days": [
    4,
    5
   ]
  },
  {
   "id": "k:1.3:四角色",
   "name": "四角色",
   "desc": "system（宪法，第一条）/ user（用户话）/ assistant（AI 回填）/ tool（工具结果）",
   "module": "1.3",
   "stage": "1",
   "pitfalls": [
    {
     "num": 30,
     "err": "KeyError: 'choices'",
     "fix": "顺序必须 assistant(tool_calls) → tool 结果 → assistant(final)"
    }
   ],
   "learned": true,
   "days": [
    4,
    5,
    7
   ]
  },
  {
   "id": "k:1.3:参数",
   "name": "参数",
   "desc": "max_tokens、temperature",
   "module": "1.3",
   "stage": "1",
   "pitfalls": [],
   "learned": true,
   "days": []
  },
  {
   "id": "k:1.3:返回结构",
   "name": "返回结构",
   "desc": "`response.json()[\"choices\"][0][\"message\"][\"content\"]`",
   "module": "1.3",
   "stage": "1",
   "pitfalls": [],
   "learned": true,
   "days": [
    4,
    5
   ]
  },
  {
   "id": "k:1.3:usage",
   "name": "usage",
   "desc": "看 token 消耗（~84 token 固定开销）",
   "module": "1.3",
   "stage": "1",
   "pitfalls": [],
   "learned": true,
   "days": [
    4,
    7
   ]
  },
  {
   "id": "k:1.3:跨轮记忆",
   "name": "跨轮记忆",
   "desc": "LLM 无状态，把整个 history 塞回 messages = 记忆",
   "module": "1.3",
   "stage": "1",
   "pitfalls": [],
   "learned": true,
   "days": [
    4,
    7,
    5
   ]
  },
  {
   "id": "k:1.4:SSE 协议",
   "name": "SSE 协议",
   "desc": "每行 `data: {JSON}`，`data: [DONE]` 结束",
   "module": "1.4",
   "stage": "1",
   "pitfalls": [],
   "learned": true,
   "days": [
    4,
    5
   ]
  },
  {
   "id": "k:1.4:两处 stream",
   "name": "两处 stream",
   "desc": "body `\"stream\": True` + 请求 `stream=True`",
   "module": "1.4",
   "stage": "1",
   "pitfalls": [
    {
     "num": 53,
     "err": "detect 对干净输入也返回 True",
     "fix": "遍历名单要遍历【列表】(PATTERNS)"
    }
   ],
   "learned": true,
   "days": [
    4
   ]
  },
  {
   "id": "k:1.4:yield 生成器",
   "name": "yield 生成器",
   "desc": "产出后暂停，流式的灵魂",
   "module": "1.4",
   "stage": "1",
   "pitfalls": [],
   "learned": true,
   "days": [
    4
   ]
  },
  {
   "id": "k:1.4:iter_lines()",
   "name": "iter_lines()",
   "desc": "逐行读取 SSE 数据块",
   "module": "1.4",
   "stage": "1",
   "pitfalls": [],
   "learned": true,
   "days": [
    4
   ]
  },
  {
   "id": "k:1.4:delta vs message",
   "name": "delta vs message",
   "desc": "流式取 delta（增量），非流式取 message（完整）",
   "module": "1.4",
   "stage": "1",
   "pitfalls": [
    {
     "num": 28,
     "err": "流式没有 content",
     "fix": "`delta.get(\"content\") or delta.get(\"reasoning_content\")`"
    }
   ],
   "learned": true,
   "days": [
    4
   ]
  },
  {
   "id": "k:1.4:reasoning_content",
   "name": "reasoning_content",
   "desc": "DeepSeek 推理模型的思考字段，需兜底取值",
   "module": "1.4",
   "stage": "1",
   "pitfalls": [
    {
     "num": 28,
     "err": "流式没有 content",
     "fix": "`delta.get(\"content\") or delta.get(\"reasoning_content\")`"
    }
   ],
   "learned": true,
   "days": [
    4
   ]
  },
  {
   "id": "k:1.5:System Prompt 四法则",
   "name": "System Prompt 四法则",
   "desc": "角色+边界 / 输出格式约束 / 正向指令>负向 / Few-shot 锚定",
   "module": "1.5",
   "stage": "1",
   "pitfalls": [],
   "learned": true,
   "days": [
    4,
    6,
    7
   ]
  },
  {
   "id": "k:1.5:Zero-shot",
   "name": "Zero-shot",
   "desc": "不举例直接问",
   "module": "1.5",
   "stage": "1",
   "pitfalls": [],
   "learned": true,
   "days": [
    4
   ]
  },
  {
   "id": "k:1.5:Few-shot",
   "name": "Few-shot",
   "desc": "给 2-3 个例子，AI 自动模仿",
   "module": "1.5",
   "stage": "1",
   "pitfalls": [],
   "learned": true,
   "days": [
    4
   ]
  },
  {
   "id": "k:1.5:CoT",
   "name": "CoT",
   "desc": "加\"一步步思考\"→ 推理能力飙升",
   "module": "1.5",
   "stage": "1",
   "pitfalls": [],
   "learned": true,
   "days": [
    4
   ]
  },
  {
   "id": "k:1.5:XML 标签",
   "name": "XML 标签",
   "desc": "`<system>` `<rules>` `<input>` 划分指令区域，遵守率更高",
   "module": "1.5",
   "stage": "1",
   "pitfalls": [],
   "learned": true,
   "days": [
    4
   ]
  },
  {
   "id": "k:1.5:深度角色",
   "name": "深度角色",
   "desc": "描述性格+风格+知识边界+典型反应（4-5 行）",
   "module": "1.5",
   "stage": "1",
   "pitfalls": [],
   "learned": true,
   "days": [
    4
   ]
  },
  {
   "id": "k:1.5:水平差异化",
   "name": "水平差异化",
   "desc": "同一 topic 不同 student_level 用不同讲解方式",
   "module": "1.5",
   "stage": "1",
   "pitfalls": [],
   "learned": true,
   "days": [
    4
   ]
  },
  {
   "id": "k:1.5:JSON 剥壳",
   "name": "JSON 剥壳",
   "desc": "AI 包 ```json 代码块时用正则 re.sub 兜底",
   "module": "1.5",
   "stage": "1",
   "pitfalls": [
    {
     "num": 29,
     "err": "提示词要求 JSON 仍带代码块",
     "fix": "正则 re.sub 剥壳兜底"
    }
   ],
   "learned": true,
   "days": [
    4,
    5
   ]
  },
  {
   "id": "k:1.6:Pydantic BaseModel",
   "name": "Pydantic BaseModel",
   "desc": "类定义数据结构，自动校验类型和必填",
   "module": "1.6",
   "stage": "1",
   "pitfalls": [],
   "learned": true,
   "days": [
    4
   ]
  },
  {
   "id": "k:1.6:Field(description=)",
   "name": "Field(description=)",
   "desc": "字段说明文档",
   "module": "1.6",
   "stage": "1",
   "pitfalls": [],
   "learned": true,
   "days": [
    4
   ]
  },
  {
   "id": "k:1.6:`Recipe(**dict)`",
   "name": "`Recipe(**dict)`",
   "desc": "字典解包成 Pydantic 对象（Agent 底座：代码可安全消费 LLM 输出）",
   "module": "1.6",
   "stage": "1",
   "pitfalls": [],
   "learned": true,
   "days": [
    4,
    5,
    7
   ]
  },
  {
   "id": "k:2.1:工具的本质",
   "name": "工具的本质",
   "desc": "普通 Python 函数 + JSON Schema（给 LLM 的说明书）",
   "module": "2.1",
   "stage": "2",
   "pitfalls": [
    {
     "num": 29,
     "err": "提示词要求 JSON 仍带代码块",
     "fix": "正则 re.sub 剥壳兜底"
    }
   ],
   "learned": true,
   "days": [
    5,
    4,
    9
   ]
  },
  {
   "id": "k:2.1:执行流程",
   "name": "执行流程",
   "desc": "tool_use → execute → tool_result",
   "module": "2.1",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": [
    5,
    8
   ]
  },
  {
   "id": "k:2.1:核心循环",
   "name": "核心循环",
   "desc": "构造 tools → 调用 → 判断 tool_calls → 执行 → 回填 → 二次调用回答",
   "module": "2.1",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": [
    5
   ]
  },
  {
   "id": "k:2.1:消息顺序",
   "name": "消息顺序",
   "desc": "user → assistant(tool_calls) → tool 结果们 → assistant(final)，assistant 必须在 tool 之前",
   "module": "2.1",
   "stage": "2",
   "pitfalls": [
    {
     "num": 30,
     "err": "KeyError: 'choices'",
     "fix": "顺序必须 assistant(tool_calls) → tool 结果 → assistant(final)"
    }
   ],
   "learned": true,
   "days": [
    5,
    4
   ]
  },
  {
   "id": "k:2.1:tool_call_id",
   "name": "tool_call_id",
   "desc": "回填 tool 消息时必须带上，一一对应",
   "module": "2.1",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": [
    5
   ]
  },
  {
   "id": "k:2.1:并行调用",
   "name": "并行调用",
   "desc": "`for tc in tool_calls` 逐个执行+回填多条 tool 消息",
   "module": "2.1",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": [
    5,
    4
   ]
  },
  {
   "id": "k:2.1:Schema 设计",
   "name": "Schema 设计",
   "desc": "type→function→name/parameters/properties 层级",
   "module": "2.1",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": [
    5,
    4
   ]
  },
  {
   "id": "k:2.1:safe_get()",
   "name": "safe_get()",
   "desc": "逐层 isinstance + key in dict 检查，缺层返回 default",
   "module": "2.1",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": [
    5,
    4
   ]
  },
  {
   "id": "k:2.1:安检闸门模式",
   "name": "安检闸门模式",
   "desc": "逐条件 return False，全过才 True",
   "module": "2.1",
   "stage": "2",
   "pitfalls": [
    {
     "num": 11,
     "err": "找到第一条就 return False",
     "fix": "循环结束后再 return 结果"
    },
    {
     "num": 22,
     "err": "return False 报类型不匹配",
     "fix": "按签名返回 (False, 错误消息)"
    }
   ],
   "learned": true,
   "days": [
    4,
    5,
    2
   ]
  },
  {
   "id": "k:2.1:parse_tool_arguments()",
   "name": "parse_tool_arguments()",
   "desc": "dict 直接用；字符串 try json.loads；失败返回 None",
   "module": "2.1",
   "stage": "2",
   "pitfalls": [
    {
     "num": 13,
     "err": "json.loads 崩溃",
     "fix": "`text = text[6:]`"
    },
    {
     "num": 40,
     "err": "摘要为空时返回 None",
     "fix": "无旧消息时返回 `\"\"`"
    }
   ],
   "learned": true,
   "days": [
    5,
    4,
    7
   ]
  },
  {
   "id": "k:2.2:ReAct 原理",
   "name": "ReAct 原理",
   "desc": "Reasoning + Acting 交替：思考→行动→观察→再思考→完成",
   "module": "2.2",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": [
    5
   ]
  },
  {
   "id": "k:2.2:tool_loop vs ReAct",
   "name": "tool_loop vs ReAct",
   "desc": "固定 1 轮 vs 动态 N 轮（for/while 包住整段）",
   "module": "2.2",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": [
    5
   ]
  },
  {
   "id": "k:2.2:body 重建",
   "name": "body 重建",
   "desc": "每轮 messages 变了，body 必须重新构造",
   "module": "2.2",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": [
    5,
    4
   ]
  },
  {
   "id": "k:2.2:终止条件",
   "name": "终止条件",
   "desc": "max_iterations 上限 + consecutive_errors ≥ 3 连续错误终止",
   "module": "2.2",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": [
    5
   ]
  },
  {
   "id": "k:2.2:AgentState",
   "name": "AgentState",
   "desc": "@dataclass 记录 messages/iteration/tool_calls_made/consecutive_errors",
   "module": "2.2",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": [
    5,
    7,
    4
   ]
  },
  {
   "id": "k:2.2:路径沙箱",
   "name": "路径沙箱",
   "desc": "_safe_path() 限制工具只能访问白名单目录",
   "module": "2.2",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": [
    5,
    9
   ]
  },
  {
   "id": "k:2.3:滑动窗口",
   "name": "滑动窗口",
   "desc": "只保留 system + 最近 N 轮，旧消息丢弃，省空间",
   "module": "2.3",
   "stage": "2",
   "pitfalls": [
    {
     "num": 45,
     "err": "窗口保留了最旧消息、保留率 1.0",
     "fix": "窗口永远负索引从尾数 `rest[-N:]`"
    }
   ],
   "learned": true,
   "days": [
    6,
    7
   ]
  },
  {
   "id": "k:2.3:system 常驻豁免",
   "name": "system 常驻豁免",
   "desc": "system 是“宪法”，永远保留且在最前",
   "module": "2.3",
   "stage": "2",
   "pitfalls": [
    {
     "num": 41,
     "err": "新建 system 消息 role 写成 recent",
     "fix": "固定写 `\"system\"`"
    }
   ],
   "learned": true,
   "days": [
    4,
    6,
    7
   ]
  },
  {
   "id": "k:2.3:轮（turn）",
   "name": "轮（turn）",
   "desc": "1 轮 = 1 user + 1 assistant，裁剪按“轮”不按“条”",
   "module": "2.3",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": [
    4,
    5
   ]
  },
  {
   "id": "k:2.3:摘要压缩",
   "name": "摘要压缩",
   "desc": "旧消息压成一段摘要，保留要点，不直接丢光",
   "module": "2.3",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": [
    6,
    7
   ]
  },
  {
   "id": "k:2.3:摘要合并进 system",
   "name": "摘要合并进 system",
   "desc": "把摘要拼进 system 内容，让 LLM 每轮都能看到旧要点",
   "module": "2.3",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": [
    6,
    7,
    4
   ]
  },
  {
   "id": "k:2.3:混合策略",
   "name": "混合策略",
   "desc": "旧对话用摘要，新对话用窗口，兼顾省空间和记忆",
   "module": "2.3",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": [
    6
   ]
  },
  {
   "id": "k:2.3:token 粗估",
   "name": "token 粗估",
   "desc": "role + content 字符数相加，粗略判断离上下文上限多远",
   "module": "2.3",
   "stage": "2",
   "pitfalls": [
    {
     "num": 42,
     "err": "`int(msg[\"role\"])` ValueError",
     "fix": "求字符数用 `len()`"
    }
   ],
   "learned": true,
   "days": [
    4,
    7
   ]
  },
  {
   "id": "k:2.3:三种记忆分工",
   "name": "三种记忆分工",
   "desc": "短期=对话内 messages；长期=跨对话落盘档案；工作=AgentState 任务状态",
   "module": "2.3",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": [
    7,
    6,
    5
   ]
  },
  {
   "id": "k:2.3:对比实验设计",
   "name": "对比实验设计",
   "desc": "控制变量（同数据同窗口）+ 固定指标（token 占用/信息保留率）+ 基线对照",
   "module": "2.3",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": [
    7,
    9,
    4
   ]
  },
  {
   "id": "k:2.3:埋事实测记忆",
   "name": "埋事实测记忆",
   "desc": "数据里预埋\"关键事实\"，裁剪后数还剩几条 → 记忆力变成 0~1 数字",
   "module": "2.3",
   "stage": "2",
   "pitfalls": [],
   "learned": false,
   "days": []
  },
  {
   "id": "k:2.3:回调函数注入",
   "name": "回调函数注入",
   "desc": "summarize 等作为参数传入，测试传离线 fake、生产传 LLM，接口不变",
   "module": "2.3",
   "stage": "2",
   "pitfalls": [
    {
     "num": 51,
     "err": "脚本化 fake 永远返回第一稿",
     "fix": "剧本放函数体外（闭包），或用工厂每次产新机器"
    }
   ],
   "learned": true,
   "days": [
    7,
    5,
    8
   ]
  },
  {
   "id": "k:2.3:长期记忆闭环",
   "name": "长期记忆闭环",
   "desc": "抽取 → 入档 → 落盘 → 新对话读盘 → 注入 system",
   "module": "2.3",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": [
    7,
    6
   ]
  },
  {
   "id": "k:2.3:抽取",
   "name": "抽取",
   "desc": "人话（非结构化）→ 表格（结构化），长期记忆的第一环",
   "module": "2.3",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": [
    7
   ]
  },
  {
   "id": "k:2.3:规则抽取 vs LLM 抽取",
   "name": "规则抽取 vs LLM 抽取",
   "desc": "写死的 if 免费/死板；LLM 什么话都懂但花钱联网，接口相同时可互换",
   "module": "2.3",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": [
    7,
    4,
    5
   ]
  },
  {
   "id": "k:2.3:system 注入点",
   "name": "system 注入点",
   "desc": "记忆拼进 system（常驻第一条），比拼 user 消息更稳",
   "module": "2.3",
   "stage": "2",
   "pitfalls": [
    {
     "num": 41,
     "err": "新建 system 消息 role 写成 recent",
     "fix": "固定写 `\"system\"`"
    }
   ],
   "learned": true,
   "days": [
    4,
    7,
    6
   ]
  },
  {
   "id": "k:2.3:json 落盘",
   "name": "json 落盘",
   "desc": "dict ↔ 文件往返：dump/load 吃文件，dumps/loads 吃字符串（d 写 l 读，带 s 换字符串）",
   "module": "2.3",
   "stage": "2",
   "pitfalls": [
    {
     "num": 13,
     "err": "json.loads 崩溃",
     "fix": "`text = text[6:]`"
    }
   ],
   "learned": true,
   "days": [
    7,
    4,
    5
   ]
  },
  {
   "id": "k:2.3:ensure_ascii=False + indent=2",
   "name": "ensure_ascii=False + indent=2",
   "desc": "json 中文原样落盘 + 缩进可读",
   "module": "2.3",
   "stage": "2",
   "pitfalls": [
    {
     "num": 11,
     "err": "找到第一条就 return False",
     "fix": "循环结束后再 return 结果"
    },
    {
     "num": 22,
     "err": "return False 报类型不匹配",
     "fix": "按签名返回 (False, 错误消息)"
    }
   ],
   "learned": true,
   "days": [
    4,
    5
   ]
  },
  {
   "id": "k:2.3:容错兜底",
   "name": "容错兜底",
   "desc": "FileNotFoundError / JSONDecodeError 都返回空档案，坏一块不崩全部",
   "module": "2.3",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": []
  },
  {
   "id": "k:2.3:不可变更新",
   "name": "不可变更新",
   "desc": "dict(old) 复印后改复印件，原件留快照、无副作用",
   "module": "2.3",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": [
    7
   ]
  },
  {
   "id": "k:2.3:表驱动",
   "name": "表驱动",
   "desc": "(前缀, 键名) 规则卡 + 循环，加规则只加数据不改逻辑",
   "module": "2.3",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": [
    8
   ]
  },
  {
   "id": "k:2.3:startswith()",
   "name": "startswith()",
   "desc": "前缀判断，替代手数长度的切片比较（新规范点名）",
   "module": "2.3",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": []
  },
  {
   "id": "k:2.3:assert 断言收窄",
   "name": "assert 断言收窄",
   "desc": "assert x is not None 让类型检查器确认\"此处不为 None\"，修 Pylance 报错",
   "module": "2.3",
   "stage": "2",
   "pitfalls": [
    {
     "num": 19,
     "err": "`self.books = None` 后遍历报错",
     "fix": "初始化为 `[]`"
    },
    {
     "num": 21,
     "err": "Pylance 类型缩窄告警",
     "fix": "调一次存变量 `para = fn.get(...)`"
    },
    {
     "num": 24,
     "err": "Pylance 标红但运行正常",
     "fix": "类型标注 ≠ 运行时行为，`basic` 模式减噪"
    },
    {
     "num": 40,
     "err": "摘要为空时返回 None",
     "fix": "无旧消息时返回 `\"\"`"
    },
    {
     "num": 34,
     "err": "Pylance 自动补全不弹窗",
     "fix": "检查 VS Code 设置"
    }
   ],
   "learned": true,
   "days": [
    3,
    5
   ]
  },
  {
   "id": "k:2.3:过严断言",
   "name": "过严断言",
   "desc": "测试只验证意图（startswith+in），不耦合与目标无关的格式细节（如全半角标点）",
   "module": "2.3",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": [
    7
   ]
  },
  {
   "id": "k:2.3:浅拷贝陷阱",
   "name": "浅拷贝陷阱",
   "desc": "dict(vault) 只复印外层，内层档案仍是原件——两层结构要两层都复印",
   "module": "2.3",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": [
    7
   ]
  },
  {
   "id": "k:2.3:{**d, k: v} 合并",
   "name": "{**d, k: v} 合并",
   "desc": "字典解包合并：老库倒进新库+替换一个键，一行完成外层复印",
   "module": "2.3",
   "stage": "2",
   "pitfalls": [],
   "learned": false,
   "days": []
  },
  {
   "id": "k:2.3:dict 保持插入顺序",
   "name": "dict 保持插入顺序",
   "desc": "Python 3.7+ 字典键按插入顺序存放，next(iter(d)) = 最旧的键",
   "module": "2.3",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": [
    7,
    5,
    4
   ]
  },
  {
   "id": "k:2.3:FIFO 淘汰",
   "name": "FIFO 淘汰",
   "desc": "容量满时踢掉最先进入的条目（LRU 缓存的雏形），覆盖不算新条目",
   "module": "2.3",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": [
    7
   ]
  },
  {
   "id": "k:2.3:del 语句",
   "name": "del 语句",
   "desc": "del d[key] 删除字典的键，d[k]=v 的反面",
   "module": "2.3",
   "stage": "2",
   "pitfalls": [
    {
     "num": 44,
     "err": "`del profile[user]` KeyError",
     "fix": "动手前先想清楚自己在哪一层"
    }
   ],
   "learned": true,
   "days": []
  },
  {
   "id": "k:2.3:卫语句双条件",
   "name": "卫语句双条件",
   "desc": "user not in vault or key not in vault[user]——两种\"不用干活\"提前返回",
   "module": "2.3",
   "stage": "2",
   "pitfalls": [
    {
     "num": 43,
     "err": "`vault.items(user)` TypeError",
     "fix": "`vault.get(user, {})`"
    },
    {
     "num": 44,
     "err": "`del profile[user]` KeyError",
     "fix": "动手前先想清楚自己在哪一层"
    }
   ],
   "learned": true,
   "days": [
    7,
    5,
    4
   ]
  },
  {
   "id": "k:2.4:Plan-and-Execute 模式",
   "name": "Plan-and-Execute 模式",
   "desc": "先生成完整计划再逐步执行，vs ReAct 走一步看一步（边炒菜边想 vs 先看菜谱）",
   "module": "2.4",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": [
    8,
    9,
    5
   ]
  },
  {
   "id": "k:2.4:计划即数据",
   "name": "计划即数据",
   "desc": "plan 是 list[dict]，可校验、可打印、可给人过目",
   "module": "2.4",
   "stage": "2",
   "pitfalls": [
    {
     "num": 39,
     "err": "`merged + recent_messages[1:]` 报错",
     "fix": "用 `[merged] + recent_messages[1:]` 包成列表再拼接"
    }
   ],
   "learned": true,
   "days": [
    7,
    8,
    6
   ]
  },
  {
   "id": "k:2.4:静态清单循环 vs 动态决定",
   "name": "静态清单循环 vs 动态决定",
   "desc": "P&E 循环一个静态列表，ReAct 每轮问 LLM——前者省调用、可审计",
   "module": "2.4",
   "stage": "2",
   "pitfalls": [
    {
     "num": 12,
     "err": "列表推导结果全是同一个值",
     "fix": "推导式变量名与循环一致"
    }
   ],
   "learned": true,
   "days": [
    8,
    5,
    9
   ]
  },
  {
   "id": "k:2.4:工具注册表分发",
   "name": "工具注册表分发",
   "desc": "{\"动作名\": 函数}，按 action 查表调用，加工具只加表项",
   "module": "2.4",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": []
  },
  {
   "id": "k:2.4:*args 调用侧解包",
   "name": "*args 调用侧解包",
   "desc": "fn(*[2,3]) = fn(2,3)；safe_get 的 *keys 是签名侧收拢，一体两面",
   "module": "2.4",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": [
    5,
    8
   ]
  },
  {
   "id": "k:2.4:优雅降级",
   "name": "优雅降级",
   "desc": "未知操作返回错误字符串不崩溃，引擎继续跑",
   "module": "2.4",
   "stage": "2",
   "pitfalls": [],
   "learned": false,
   "days": []
  },
  {
   "id": "k:2.4:校验器参数放宽",
   "name": "校验器参数放宽",
   "desc": "安检员天生要接\"可能不合法\"的输入，签名用 list 而非 list[dict]",
   "module": "2.4",
   "stage": "2",
   "pitfalls": [
    {
     "num": 2,
     "err": "`self.tags = list[str] = []` 语法错误",
     "fix": "`self.tags: list[str] = []`"
    },
    {
     "num": 3,
     "err": "`self.tags : list[str] = []` 报错",
     "fix": "冒号紧跟变量名"
    },
    {
     "num": 50,
     "err": "`id in list[dict]` 永远 False 不报错",
     "fix": "in 之前核对两边类型一致；查 id 集合用 set"
    }
   ],
   "learned": false,
   "days": [
    4,
    3,
    6
   ]
  },
  {
   "id": "k:2.4:动态重规划",
   "name": "动态重规划",
   "desc": "受阻→重算【剩余】路线→继续，已完成的结果不回滚（导航改道不回出发点）",
   "module": "2.4",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": [
    8
   ]
  },
  {
   "id": "k:2.4:重规划预算 max_replans",
   "name": "重规划预算 max_replans",
   "desc": "防庸医 replanner 无限变道烧钱，max_iterations 的直系亲戚",
   "module": "2.4",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": [
    8
   ]
  },
  {
   "id": "k:2.4:错误即数据",
   "name": "错误即数据",
   "desc": "优雅降级的产出（未知操作字符串）= 上游系统的触发信号",
   "module": "2.4",
   "stage": "2",
   "pitfalls": [],
   "learned": false,
   "days": [
    8
   ]
  },
  {
   "id": "k:2.4:while+手动索引",
   "name": "while+手动索引",
   "desc": "循环对象要中途整体替换时，for 锁死迭代对象，while 才能边跑边换",
   "module": "2.4",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": [
    1
   ]
  },
  {
   "id": "k:2.4:import 自己的模块",
   "name": "import 自己的模块",
   "desc": "同目录 from plan_and_execute import ...，DRY 复用零件",
   "module": "2.4",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": [
    8
   ]
  },
  {
   "id": "k:2.4:失败痕迹保留",
   "name": "失败痕迹保留",
   "desc": "results 记录每次失败——审计时能看到在哪改的道",
   "module": "2.4",
   "stage": "2",
   "pitfalls": [],
   "learned": false,
   "days": []
  },
  {
   "id": "k:2.4:planner vs replanner",
   "name": "planner vs replanner",
   "desc": "出发前盲规划(只知任务) vs 受阻时知情改道(知任务+进度+故障)，只管剩余",
   "module": "2.4",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": [
    8
   ]
  },
  {
   "id": "k:2.4:共享黑板 state",
   "name": "共享黑板 state",
   "desc": "步骤间数据流走闭包 dict，不走返回值（框架 checkpoint 思想）",
   "module": "2.4",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": []
  },
  {
   "id": "k:2.4:zip 拉链配对",
   "name": "zip 拉链配对",
   "desc": "zip(a,b) 按位置咬合成对，配权重/配对计算一步到位",
   "module": "2.4",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": []
  },
  {
   "id": "k:2.4:CWD vs 脚本目录",
   "name": "CWD vs 脚本目录",
   "desc": "相对路径跟着\"从哪运行\"走；Path(__file__).parent 锚定\"文件在哪\"",
   "module": "2.4",
   "stage": "2",
   "pitfalls": [
    {
     "num": 60,
     "err": "Pylance: Unable to resolve import（跨目录）",
     "fix": "pyrightconfig extraPaths + mypy_path 白名单"
    },
    {
     "num": 49,
     "err": "报告文件落在仓库根而不是脚本目录",
     "fix": "`Path(__file__).parent / path` 锚定脚本目录"
    },
    {
     "num": 52,
     "err": "落盘 FileNotFoundError",
     "fix": "写文件三件套：open(path, \"w\", encoding=\"utf-8\")"
    }
   ],
   "learned": true,
   "days": [
    9
   ]
  },
  {
   "id": "k:2.4:Workflow vs Agent",
   "name": "Workflow vs Agent",
   "desc": "流程固定（下一步听代码）vs 动态流程（下一步听 LLM）——run_plan vs react_loop",
   "module": "2.4",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": [
    8,
    5,
    4
   ]
  },
  {
   "id": "k:2.4:gate 闸门思想",
   "name": "gate 闸门思想",
   "desc": "步骤之间加检查点：validate_plan 拦进门计划、is_failed 拦半路结果，脏数据不流向下一步",
   "module": "2.4",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": [
    8
   ]
  },
  {
   "id": "k:2.4:何时该用 Agent",
   "name": "何时该用 Agent",
   "desc": "任务步骤无法预知、需现场决策才上 Agent；宁简勿繁，从最简单方案开始",
   "module": "2.4",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": [
    8,
    5,
    7
   ]
  },
  {
   "id": "k:2.4:依赖感知执行（拓扑排序朴素版）",
   "name": "依赖感知执行（拓扑排序朴素版）",
   "desc": "每步声明 needs，循环挑\"依赖全就位\"的步骤执行，清单顺序≠执行顺序",
   "module": "2.4",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": [
    8,
    5
   ]
  },
  {
   "id": "k:2.4:死锁检测",
   "name": "死锁检测",
   "desc": "还有剩余但挑不出任何就绪步骤 = 依赖成环，报告终止而非挂死",
   "module": "2.4",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": [
    8
   ]
  },
  {
   "id": "k:2.4:done 用 set",
   "name": "done 用 set",
   "desc": "已完成 id 集合用 set——`n in done` 是 O(1) 查询，list 是 O(n)",
   "module": "2.4",
   "stage": "2",
   "pitfalls": [
    {
     "num": 6,
     "err": "`text == \"DONE\"` 永远不触发",
     "fix": "`text == \"[DONE]\"` 写完整"
    }
   ],
   "learned": true,
   "days": [
    4
   ]
  },
  {
   "id": "k:2.4:sorted(key=lambda)",
   "name": "sorted(key=lambda)",
   "desc": "排 dict 列表给一把\"尺子\"：key=lambda s: s[\"id\"] 量哪个字段",
   "module": "2.4",
   "stage": "2",
   "pitfalls": [
    {
     "num": 14,
     "err": "返回了 API Key 而不是回复",
     "fix": "命名语义化，返回前核对"
    }
   ],
   "learned": true,
   "days": [
    5,
    4,
    8
   ]
  },
  {
   "id": "k:2.4:all() / any()",
   "name": "all() / any()",
   "desc": "全都成立吗 / 有一个成立吗——all 管闸门全过才放行，any 管警报有一个就响",
   "module": "2.4",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": []
  },
  {
   "id": "k:2.5:反思循环",
   "name": "反思循环",
   "desc": "生成→自评→改进：ReAct 对外行动，反思对内检讨自己上一稿",
   "module": "2.5",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": [
    8
   ]
  },
  {
   "id": "k:2.5:批评家=规则代码",
   "name": "批评家=规则代码",
   "desc": "硬约束检查用代码不用 LLM——免费、确定、可测试（离线可验的逻辑不花钱）",
   "module": "2.5",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": [
    8,
    7,
    4
   ]
  },
  {
   "id": "k:2.5:反思便签=工作记忆",
   "name": "反思便签=工作记忆",
   "desc": "问题清单翻译成便签喂回下一轮生成器，note 跨轮传递",
   "module": "2.5",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": [
    8
   ]
  },
  {
   "id": "k:2.5:问题收敛曲线",
   "name": "问题收敛曲线",
   "desc": "problems_history 里问题数递减（如 [2,1,0]）——反思有效的数字证据",
   "module": "2.5",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": [
    8
   ]
  },
  {
   "id": "k:2.5:critic 返回问题清单",
   "name": "critic 返回问题清单",
   "desc": "比 bool 信息量大：清单直接变成下一轮的改进指令（错误即数据第三次登场）",
   "module": "2.5",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": [
    8,
    4
   ]
  },
  {
   "id": "k:2.5:预算即圈数",
   "name": "预算即圈数",
   "desc": "for range(max_rounds)：每圈必然消耗预算，放学铃必须存在",
   "module": "2.5",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": []
  },
  {
   "id": "k:2.5:语言强化学习",
   "name": "语言强化学习",
   "desc": "不改权重改文字记忆——不做脑手术，改贴便利贴（Reflexion）",
   "module": "2.5",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": [
    8
   ]
  },
  {
   "id": "k:2.5:Actor/Evaluator/Self-reflection",
   "name": "Actor/Evaluator/Self-reflection",
   "desc": "= generator/check_slogan/build_reflection，我写过 Reflexion 迷你版",
   "module": "2.5",
   "stage": "2",
   "pitfalls": [
    {
     "num": 19,
     "err": "`self.books = None` 后遍历报错",
     "fix": "初始化为 `[]`"
    }
   ],
   "learned": true,
   "days": [
    8,
    2,
    3
   ]
  },
  {
   "id": "k:2.5:episodic memory",
   "name": "episodic memory",
   "desc": "反思跨试次（任务）存活；note 只在单任务内——长期记忆+反思便签的合体",
   "module": "2.5",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": [
    8
   ]
  },
  {
   "id": "k:2.5:反思按需付费",
   "name": "反思按需付费",
   "desc": "第 1 轮=裸奔，一稿过零成本，烂稿才补轮——怕翻倍不敢开是错觉",
   "module": "2.5",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": [
    8
   ]
  },
  {
   "id": "k:7.1:三遍寻宝法",
   "name": "三遍寻宝法",
   "desc": "侦察(摘要/图表/结论5分钟)→挖宝(Intro末段+方法+Figure1)→按需拆解(复现时才精读)",
   "module": "7.1",
   "stage": "2",
   "pitfalls": [],
   "learned": false,
   "days": []
  },
  {
   "id": "k:7.1:Figure 1 定律",
   "name": "Figure 1 定律",
   "desc": "Agent 论文 90% 精华在架构图——先看懂图再看字",
   "module": "7.1",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": []
  },
  {
   "id": "k:7.1:代码锚定法",
   "name": "代码锚定法",
   "desc": "把论文组件翻译成自己写过的函数，概念立刻落地",
   "module": "7.1",
   "stage": "2",
   "pitfalls": [],
   "learned": false,
   "days": []
  },
  {
   "id": "k:7.1:费曼检验",
   "name": "费曼检验",
   "desc": "写不出 3 行总结=没读懂，回去重读 Figure 1",
   "module": "7.1",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": []
  },
  {
   "id": "k:7.1:episodic memory 实现",
   "name": "episodic memory 实现",
   "desc": "长期记忆(落盘教训库)×反思(便签)的组合——lesson 跨任务传递",
   "module": "7.1",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": [
    8
   ]
  },
  {
   "id": "k:7.1:读旧+append+写回",
   "name": "读旧+append+写回",
   "desc": "追加式落盘三步：复用 load 读旧库，别只写新条目（会覆盖历史）",
   "module": "7.1",
   "stage": "2",
   "pitfalls": [],
   "learned": false,
   "days": []
  },
  {
   "id": "k:7.1:容错返回同形状",
   "name": "容错返回同形状",
   "desc": "异常路径返回值类型必须与正常路径一致（[] 而非 False，否则下游 .append 爆炸）",
   "module": "7.1",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": [
    5,
    4,
    2
   ]
  },
  {
   "id": "k:7.1:剧本放闭包外",
   "name": "剧本放闭包外",
   "desc": "脚本化 fake 的剧本必须定义在函数体外——体内=每次调用重发剧本永远第一稿",
   "module": "7.1",
   "stage": "2",
   "pitfalls": [
    {
     "num": 51,
     "err": "脚本化 fake 永远返回第一稿",
     "fix": "剧本放函数体外（闭包），或用工厂每次产新机器"
    }
   ],
   "learned": false,
   "days": []
  },
  {
   "id": "k:2.6:威胁矩阵",
   "name": "威胁矩阵",
   "desc": "5 大攻击面: 注入/越权工具/数据泄露/输出投毒/供应链——对应防御: 过滤/分级/校验/校验/沙箱",
   "module": "2.6",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": [
    8
   ]
  },
  {
   "id": "k:2.6:Prompt 注入",
   "name": "Prompt 注入",
   "desc": "指令藏在数据里（留言板/网页/文件）——LLM 眼里数据和指令都是文字，天生分不清",
   "module": "2.6",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": [
    4,
    8,
    7
   ]
  },
  {
   "id": "k:2.6:大小写归一化",
   "name": "大小写归一化",
   "desc": "文本检测先 text.lower()——否则 DISREGARD 大写攻击直接穿防",
   "module": "2.6",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": []
  },
  {
   "id": "k:2.6:表驱动特征检测",
   "name": "表驱动特征检测",
   "desc": "危险短语进 PATTERNS 表 + 循环，加特征零改逻辑",
   "module": "2.6",
   "stage": "2",
   "pitfalls": [],
   "learned": false,
   "days": []
  },
  {
   "id": "k:2.6:过滤 vs 拦截",
   "name": "过滤 vs 拦截",
   "desc": "sanitize 消毒放行（柔和）vs guard 命中即拒（强硬）——纵深防御两层都上",
   "module": "2.6",
   "stage": "2",
   "pitfalls": [
    {
     "num": 56,
     "err": "审计记错、guard 交给消毒员",
     "fix": "用词表锚定角色语义，写前默念名字含义"
    }
   ],
   "learned": true,
   "days": [
    8
   ]
  },
  {
   "id": "k:2.6:规则模拟 LLM",
   "name": "规则模拟 LLM",
   "desc": "用 if 模拟\"被劫持的 LLM\"——离线靶场不花 API 钱",
   "module": "2.6",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": [
    4,
    5,
    8
   ]
  },
  {
   "id": "k:2.6:遍历字符串陷阱",
   "name": "遍历字符串陷阱",
   "desc": "for x in \"字符串\" 拆成逐字符——遍历名单要遍历【列表】",
   "module": "2.6",
   "stage": "2",
   "pitfalls": [
    {
     "num": 53,
     "err": "detect 对干净输入也返回 True",
     "fix": "遍历名单要遍历【列表】(PATTERNS)"
    }
   ],
   "learned": true,
   "days": []
  },
  {
   "id": "k:2.6:绿黄红权限分级",
   "name": "绿黄红权限分级",
   "desc": "按副作用: 无副作用(绿自动放行)/可逆(黄需确认)/不可逆(红人工通道)",
   "module": "2.6",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": []
  },
  {
   "id": "k:2.6:默认拒绝 Default Deny",
   "name": "默认拒绝 Default Deny",
   "desc": "未登记=红——dict.get(k, 'red') 一行落地，宁可误拒不可误放",
   "module": "2.6",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": [
    5
   ]
  },
  {
   "id": "k:2.6:审计记裁决不记申报",
   "name": "审计记裁决不记申报",
   "desc": "日志记闸门的 allowed，不是申请人的 auto_confirm——被拒的试图才是警报",
   "module": "2.6",
   "stage": "2",
   "pitfalls": [
    {
     "num": 56,
     "err": "审计记错、guard 交给消毒员",
     "fix": "用词表锚定角色语义，写前默念名字含义"
    }
   ],
   "learned": true,
   "days": [
    8
   ]
  },
  {
   "id": "k:2.6:闸门与执行分离",
   "name": "闸门与执行分离",
   "desc": "authorize 只决策，run_tool 先闸后执行——安检员不搬货",
   "module": "2.6",
   "stage": "2",
   "pitfalls": [],
   "learned": false,
   "days": []
  },
  {
   "id": "k:2.6:输出校验(出口安检)",
   "name": "输出校验(出口安检)",
   "desc": "Agent 产物流进下游前的最后一道闸：SQL只读/单语句/无破坏词",
   "module": "2.6",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": [
    9,
    4
   ]
  },
  {
   "id": "k:2.6:检查优先级=契约",
   "name": "检查优先级=契约",
   "desc": "多规则同时踩线先报哪个由契约(测试)定——多语句是注入最本质签名优先报",
   "module": "2.6",
   "stage": "2",
   "pitfalls": [],
   "learned": false,
   "days": []
  },
  {
   "id": "k:2.6:resolve后再验身",
   "name": "resolve后再验身",
   "desc": "永不信字面路径: ../先展开再 is_relative_to 比对，伪装即失效",
   "module": "2.6",
   "stage": "2",
   "pitfalls": [],
   "learned": false,
   "days": []
  },
  {
   "id": "k:2.6:纵深防御代码形状",
   "name": "纵深防御代码形状",
   "desc": "两道闸串联(各自独立可测)，authorize→run_tool 同构第三台",
   "module": "2.6",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": []
  },
  {
   "id": "k:2.6:OWASP LLM Top 10",
   "name": "OWASP LLM Top 10",
   "desc": "业界十大病清单——注入/输出处理/过度代理/供应链我防过，泄露/DoS/数据投毒是新面孔",
   "module": "2.6",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": [
    9,
    8,
    4
   ]
  },
  {
   "id": "k:2.6:5攻5防口诀",
   "name": "5攻5防口诀",
   "desc": "进口过滤、手分级、出口校验、范围圈死、来源审查",
   "module": "2.6",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": []
  },
  {
   "id": "k:2.6:LLM输出=概率猜测",
   "name": "LLM输出=概率猜测",
   "desc": "不是可信结果——过度依赖(LLM09)的病根，进出口设闸的总依据",
   "module": "2.6",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": [
    4,
    8,
    5
   ]
  },
  {
   "id": "k:2.6:文字版ReAct协议",
   "name": "文字版ReAct协议",
   "desc": "ACTION/OBSERVATION/ANSWER 文本协议——不依赖API原生tool_calls，与手写react_loop同构",
   "module": "2.6",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": [
    5,
    8
   ]
  },
  {
   "id": "k:2.6:脚本自举模式",
   "name": "脚本自举模式",
   "desc": "sys.path.insert挂载.tools/——仓库自带依赖，裸python3直跑，/tmp蒸发免疫",
   "module": "2.6",
   "stage": "2",
   "pitfalls": [
    {
     "num": 60,
     "err": "Pylance: Unable to resolve import（跨目录）",
     "fix": "pyrightconfig extraPaths + mypy_path 白名单"
    },
    {
     "num": 49,
     "err": "报告文件落在仓库根而不是脚本目录",
     "fix": "`Path(__file__).parent / path` 锚定脚本目录"
    }
   ],
   "learned": true,
   "days": [
    9,
    4
   ]
  },
  {
   "id": "k:2.6:Agent可靠性来源",
   "name": "Agent可靠性来源",
   "desc": "不是模型聪明，是每个进出口设闸+引擎逼它先查资料再开口",
   "module": "2.6",
   "stage": "2",
   "pitfalls": [],
   "learned": true,
   "days": [
    4,
    5,
    8
   ]
  }
 ],
 "planned": [
  {
   "id": "x:0",
   "name": "2.4 任务规划（Plan-and-Execute）",
   "stage": "2"
  },
  {
   "id": "x:1",
   "name": "2.5 Reflection（生成→自评→改进）",
   "stage": "2"
  },
  {
   "id": "x:2",
   "name": "2.6 安全护栏",
   "stage": "2"
  },
  {
   "id": "x:3",
   "name": "阶段 3：RAG 全流程",
   "stage": null
  },
  {
   "id": "x:4",
   "name": "阶段 4：框架（SDK / LangGraph / MCP / 多 Agent）",
   "stage": null
  },
  {
   "id": "x:5",
   "name": "阶段 5：工程化（评估 / 可观测 / CI/CD / 部署）",
   "stage": null
  }
 ],
 "path": [
  "k:0.1:变量与数据类型",
  "k:0.1:条件判断",
  "k:0.1:循环",
  "k:0.1:四种数据结构",
  "k:0.1:内置函数",
  "k:0.1:字符串操作",
  "k:0.1:卫语句",
  "k:0.1:异常处理",
  "k:0.2:with open()",
  "k:0.2:读取模式",
  "k:0.2:CSV 解析套路",
  "k:0.2:跳过表头",
  "k:0.2:脏数据跳过",
  "k:0.3:class + __init__",
  "k:0.3:实例属性 vs 方法",
  "k:0.3:__repr__",
  "k:0.3:布尔状态管理",
  "k:0.3:继承",
  "k:0.3:super().__init__()",
  "k:0.3:方法覆盖",
  "k:0.3:isinstance()",
  "k:0.3:@dataclass",
  "k:0.3:field(default_factory=list)",
  "k:0.3:Literal[1,2,3]",
  "k:0.3:类型注解 vs 赋值",
  "k:0.4:Git 三区模型",
  "k:0.4:.gitignore",
  "k:0.4:conda + pip",
  "k:0.4:PYTHONUTF8=1",
  "k:1.1:AI→ML→DL→LLM→Agent",
  "k:1.1:Token",
  "k:1.1:参数（7B/70B）",
  "k:1.1:训练 vs 推理",
  "k:1.1:幻觉",
  "k:1.1:上下文窗口",
  "k:1.2:六家对比",
  "k:1.2:选模型口诀",
  "k:1.2:中转平台",
  "k:1.3:HTTP 基础",
  "k:1.3:API Key 安全",
  "k:1.3:Messages 结构",
  "k:1.3:四角色",
  "k:1.3:参数",
  "k:1.3:返回结构",
  "k:1.3:usage",
  "k:1.3:跨轮记忆",
  "k:1.4:SSE 协议",
  "k:1.4:两处 stream",
  "k:1.4:yield 生成器",
  "k:1.4:iter_lines()",
  "k:1.4:delta vs message",
  "k:1.4:reasoning_content",
  "k:1.5:System Prompt 四法则",
  "k:1.5:Zero-shot",
  "k:1.5:Few-shot",
  "k:1.5:CoT",
  "k:1.5:XML 标签",
  "k:1.5:深度角色",
  "k:1.5:水平差异化",
  "k:1.5:JSON 剥壳",
  "k:1.6:Pydantic BaseModel",
  "k:1.6:Field(description=)",
  "k:1.6:`Recipe(**dict)`",
  "k:2.1:工具的本质",
  "k:2.1:执行流程",
  "k:2.1:核心循环",
  "k:2.1:消息顺序",
  "k:2.1:tool_call_id",
  "k:2.1:并行调用",
  "k:2.1:Schema 设计",
  "k:2.1:safe_get()",
  "k:2.1:安检闸门模式",
  "k:2.1:parse_tool_arguments()",
  "k:2.2:ReAct 原理",
  "k:2.2:tool_loop vs ReAct",
  "k:2.2:body 重建",
  "k:2.2:终止条件",
  "k:2.2:AgentState",
  "k:2.2:路径沙箱",
  "k:2.3:滑动窗口",
  "k:2.3:system 常驻豁免",
  "k:2.3:轮（turn）",
  "k:2.3:摘要压缩",
  "k:2.3:摘要合并进 system",
  "k:2.3:混合策略",
  "k:2.3:token 粗估",
  "k:2.3:三种记忆分工",
  "k:2.3:对比实验设计",
  "k:2.3:埋事实测记忆",
  "k:2.3:回调函数注入",
  "k:2.3:长期记忆闭环",
  "k:2.3:抽取",
  "k:2.3:规则抽取 vs LLM 抽取",
  "k:2.3:system 注入点",
  "k:2.3:json 落盘",
  "k:2.3:ensure_ascii=False + indent=2",
  "k:2.3:容错兜底",
  "k:2.3:不可变更新",
  "k:2.3:表驱动",
  "k:2.3:startswith()",
  "k:2.3:assert 断言收窄",
  "k:2.3:过严断言",
  "k:2.3:浅拷贝陷阱",
  "k:2.3:{**d, k: v} 合并",
  "k:2.3:dict 保持插入顺序",
  "k:2.3:FIFO 淘汰",
  "k:2.3:del 语句",
  "k:2.3:卫语句双条件",
  "k:2.4:Plan-and-Execute 模式",
  "k:2.4:计划即数据",
  "k:2.4:静态清单循环 vs 动态决定",
  "k:2.4:工具注册表分发",
  "k:2.4:*args 调用侧解包",
  "k:2.4:优雅降级",
  "k:2.4:校验器参数放宽",
  "k:2.4:动态重规划",
  "k:2.4:重规划预算 max_replans",
  "k:2.4:错误即数据",
  "k:2.4:while+手动索引",
  "k:2.4:import 自己的模块",
  "k:2.4:失败痕迹保留",
  "k:2.4:planner vs replanner",
  "k:2.4:共享黑板 state",
  "k:2.4:zip 拉链配对",
  "k:2.4:CWD vs 脚本目录",
  "k:2.4:Workflow vs Agent",
  "k:2.4:gate 闸门思想",
  "k:2.4:何时该用 Agent",
  "k:2.4:依赖感知执行（拓扑排序朴素版）",
  "k:2.4:死锁检测",
  "k:2.4:done 用 set",
  "k:2.4:sorted(key=lambda)",
  "k:2.4:all() / any()",
  "k:2.5:反思循环",
  "k:2.5:批评家=规则代码",
  "k:2.5:反思便签=工作记忆",
  "k:2.5:问题收敛曲线",
  "k:2.5:critic 返回问题清单",
  "k:2.5:预算即圈数",
  "k:2.5:语言强化学习",
  "k:2.5:Actor/Evaluator/Self-reflection",
  "k:2.5:episodic memory",
  "k:2.5:反思按需付费",
  "k:7.1:三遍寻宝法",
  "k:7.1:Figure 1 定律",
  "k:7.1:代码锚定法",
  "k:7.1:费曼检验",
  "k:7.1:episodic memory 实现",
  "k:7.1:读旧+append+写回",
  "k:7.1:容错返回同形状",
  "k:7.1:剧本放闭包外",
  "k:2.6:威胁矩阵",
  "k:2.6:Prompt 注入",
  "k:2.6:大小写归一化",
  "k:2.6:表驱动特征检测",
  "k:2.6:过滤 vs 拦截",
  "k:2.6:规则模拟 LLM",
  "k:2.6:遍历字符串陷阱",
  "k:2.6:绿黄红权限分级",
  "k:2.6:默认拒绝 Default Deny",
  "k:2.6:审计记裁决不记申报",
  "k:2.6:闸门与执行分离",
  "k:2.6:输出校验(出口安检)",
  "k:2.6:检查优先级=契约",
  "k:2.6:resolve后再验身",
  "k:2.6:纵深防御代码形状",
  "k:2.6:OWASP LLM Top 10",
  "k:2.6:5攻5防口诀",
  "k:2.6:LLM输出=概率猜测",
  "k:2.6:文字版ReAct协议",
  "k:2.6:脚本自举模式",
  "k:2.6:Agent可靠性来源",
  "x:0",
  "x:1",
  "x:2",
  "x:3",
  "x:4",
  "x:5"
 ],
 "related": [
  {
   "source": "k:1.2:六家对比",
   "target": "k:1.2:选模型口诀",
   "label": "gpt"
  },
  {
   "source": "k:2.5:episodic memory",
   "target": "k:7.1:episodic memory 实现",
   "label": "memory"
  },
  {
   "source": "k:2.3:规则抽取 vs LLM 抽取",
   "target": "k:2.6:规则模拟 LLM",
   "label": "llm"
  },
  {
   "source": "k:2.1:parse_tool_arguments()",
   "target": "k:2.3:json 落盘",
   "label": "loads"
  },
  {
   "source": "k:0.3:class + __init__",
   "target": "k:0.3:super().__init__()",
   "label": "__init__"
  },
  {
   "source": "k:1.3:四角色",
   "target": "k:2.1:消息顺序",
   "label": "assistant"
  },
  {
   "source": "k:2.3:system 常驻豁免",
   "target": "k:2.3:system 注入点",
   "label": "system"
  },
  {
   "source": "k:2.3:摘要合并进 system",
   "target": "k:2.3:system 注入点",
   "label": "system"
  },
  {
   "source": "k:1.1:AI→ML→DL→LLM→Agent",
   "target": "k:2.4:Workflow vs Agent",
   "label": "agent"
  },
  {
   "source": "k:2.3:system 常驻豁免",
   "target": "k:2.3:摘要合并进 system",
   "label": "system"
  },
  {
   "source": "k:0.1:四种数据结构",
   "target": "k:2.4:计划即数据",
   "label": "dict"
  },
  {
   "source": "k:1.3:四角色",
   "target": "k:2.3:system 注入点",
   "label": "system"
  },
  {
   "source": "k:0.1:异常处理",
   "target": "k:0.2:脏数据跳过",
   "label": "try"
  },
  {
   "source": "k:1.5:System Prompt 四法则",
   "target": "k:2.6:Prompt 注入",
   "label": "prompt"
  },
  {
   "source": "k:1.6:`Recipe(**dict)`",
   "target": "k:2.3:dict 保持插入顺序",
   "label": "dict"
  },
  {
   "source": "k:1.6:`Recipe(**dict)`",
   "target": "k:2.4:Workflow vs Agent",
   "label": "llm"
  },
  {
   "source": "k:2.3:规则抽取 vs LLM 抽取",
   "target": "k:2.5:批评家=规则代码",
   "label": "llm"
  },
  {
   "source": "k:2.5:批评家=规则代码",
   "target": "k:2.6:规则模拟 LLM",
   "label": "llm"
  },
  {
   "source": "k:0.1:四种数据结构",
   "target": "k:2.4:校验器参数放宽",
   "label": "dict"
  },
  {
   "source": "k:0.1:字符串操作",
   "target": "k:0.2:CSV 解析套路",
   "label": "strip"
  },
  {
   "source": "k:0.3:field(default_factory=list)",
   "target": "k:1.6:Field(description=)",
   "label": "field"
  },
  {
   "source": "k:0.3:field(default_factory=list)",
   "target": "k:2.4:校验器参数放宽",
   "label": "list"
  },
  {
   "source": "k:1.1:AI→ML→DL→LLM→Agent",
   "target": "k:1.6:`Recipe(**dict)`",
   "label": "llm"
  },
  {
   "source": "k:1.1:AI→ML→DL→LLM→Agent",
   "target": "k:2.3:规则抽取 vs LLM 抽取",
   "label": "llm"
  },
  {
   "source": "k:1.1:AI→ML→DL→LLM→Agent",
   "target": "k:2.4:何时该用 Agent",
   "label": "agent"
  },
  {
   "source": "k:1.1:Token",
   "target": "k:1.3:usage",
   "label": "token"
  },
  {
   "source": "k:1.1:Token",
   "target": "k:2.3:token 粗估",
   "label": "token"
  },
  {
   "source": "k:1.3:API Key 安全",
   "target": "k:2.4:sorted(key=lambda)",
   "label": "key"
  },
  {
   "source": "k:1.3:四角色",
   "target": "k:2.3:轮（turn）",
   "label": "assistant"
  },
  {
   "source": "k:1.3:usage",
   "target": "k:2.3:token 粗估",
   "label": "token"
  },
  {
   "source": "k:1.5:System Prompt 四法则",
   "target": "k:2.3:system 常驻豁免",
   "label": "system"
  },
  {
   "source": "k:1.5:System Prompt 四法则",
   "target": "k:2.3:摘要合并进 system",
   "label": "system"
  },
  {
   "source": "k:1.5:System Prompt 四法则",
   "target": "k:2.3:system 注入点",
   "label": "system"
  },
  {
   "source": "k:1.5:JSON 剥壳",
   "target": "k:2.3:json 落盘",
   "label": "json"
  },
  {
   "source": "k:2.1:消息顺序",
   "target": "k:2.3:轮（turn）",
   "label": "assistant"
  },
  {
   "source": "k:2.1:safe_get()",
   "target": "k:2.4:sorted(key=lambda)",
   "label": "key"
  },
  {
   "source": "k:2.1:safe_get()",
   "target": "k:2.6:默认拒绝 Default Deny",
   "label": "dict"
  },
  {
   "source": "k:2.2:ReAct 原理",
   "target": "k:2.6:文字版ReAct协议",
   "label": "react"
  },
  {
   "source": "k:2.2:tool_loop vs ReAct",
   "target": "k:2.6:文字版ReAct协议",
   "label": "react"
  },
  {
   "source": "k:2.2:AgentState",
   "target": "k:2.3:三种记忆分工",
   "label": "messages"
  },
  {
   "source": "k:2.3:规则抽取 vs LLM 抽取",
   "target": "k:2.6:OWASP LLM Top 10",
   "label": "llm"
  },
  {
   "source": "k:2.4:Workflow vs Agent",
   "target": "k:2.6:Agent可靠性来源",
   "label": "agent"
  },
  {
   "source": "k:2.4:何时该用 Agent",
   "target": "k:2.6:Agent可靠性来源",
   "label": "agent"
  },
  {
   "source": "k:2.3:表驱动",
   "target": "k:2.6:表驱动特征检测",
   "label": "表驱"
  },
  {
   "source": "k:0.1:四种数据结构",
   "target": "k:2.3:不可变更新",
   "label": "dict"
  },
  {
   "source": "k:1.1:上下文窗口",
   "target": "k:2.3:token 粗估",
   "label": "token"
  },
  {
   "source": "k:1.3:跨轮记忆",
   "target": "k:2.3:三种记忆分工",
   "label": "messages"
  },
  {
   "source": "k:2.3:回调函数注入",
   "target": "k:2.5:批评家=规则代码",
   "label": "llm"
  },
  {
   "source": "k:2.3:回调函数注入",
   "target": "k:2.6:Prompt 注入",
   "label": "llm"
  },
  {
   "source": "k:2.4:静态清单循环 vs 动态决定",
   "target": "k:2.5:反思循环",
   "label": "react"
  },
  {
   "source": "k:2.4:CWD vs 脚本目录",
   "target": "k:2.6:脚本自举模式",
   "label": "path"
  }
 ],
 "days": [
  {
   "num": 1,
   "date": "2026-07-18",
   "title": "2026-07-18"
  },
  {
   "num": 2,
   "date": "2026-07-22",
   "title": "2026-07-22"
  },
  {
   "num": 3,
   "date": "2026-07-31",
   "title": "2026-07-31（08:00-09:10"
  },
  {
   "num": 4,
   "date": "2026-08-01",
   "title": "2026-08-01（06:00-11:05"
  },
  {
   "num": 5,
   "date": "2026-08-09",
   "title": "2026-08-09（Tool Calling 深入 + JSON 实战"
  },
  {
   "num": 6,
   "date": "2026-08-16",
   "title": "2026-08-16（复习 + 2.3 记忆系统"
  },
  {
   "num": 7,
   "date": "2026-08-30",
   "title": "2026-08-30（08:00-19:30，含休息"
  },
  {
   "num": 8,
   "date": "2026-09-05",
   "title": "2026-09-05（10:00-22:47，含午休/出门/晚饭"
  },
  {
   "num": 9,
   "date": "2026-09-06",
   "title": "2026-09-06（08:45-14:39"
  }
 ],
 "stats": {
  "stages": 3,
  "modules": 17,
  "knowledge": 172,
  "pitfalls": 60,
  "planned": 6,
  "related": 51
 }
};
