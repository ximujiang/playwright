import random
import string

# 一些用于标题的中文形容词列表
chinese_adjectives = [
    "精彩的", "绝妙的", "非凡的", "独特的", "美丽的",
    "卓越的", "创新的", "令人震撼的", "前所未有的", "激动人心的",
    # ... 添加更多形容词 ...
]

# 一些用于标题的中文名词列表
chinese_nouns = [
    "旅行", "冒险", "体验", "发现", "见解",
    "创新", "革命", "趋势", "机遇", "挑战",
    # ... 添加更多名词 ...
]


# 生成随机中文标题
def generate_random_chinese_title():
    num_adjectives = random.randint(1, 3)  # 随机选择1到3个形容词
    adjectives = random.sample(chinese_adjectives, num_adjectives)  # 从列表中随机选择形容词
    noun = random.choice(chinese_nouns)  # 从列表中随机选择一个名词
    random_number = random.randint(100, 999)  # 生成一个100到999的随机数
    title = ''.join(adjectives) + noun + f"（{random_number}）"
    return title


# 生成随机字符串（例如，用于用户名或密码）
def generate_random_string(length=10):
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for i in range(length))


# 生成随机整数（例如，用于ID或数量）
def generate_random_integer(min_value=1, max_value=100):
    return random.randint(min_value, max_value)


# 生成随机浮点数（例如，用于价格或百分比）
def generate_random_float(min_value=0.0, max_value=1.0, decimal_places=2):
    return round(random.uniform(min_value, max_value), decimal_places)


# 生成随机布尔值（True或False）
def generate_random_boolean():
    return random.choice([True, False])

# 示例：生成随机中文标题
random_chinese_title = generate_random_chinese_title()
print(f"随机中文标题: {random_chinese_title}")
