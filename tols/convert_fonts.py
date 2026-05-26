#!/usr/bin/env python3
import os
from fontTools.ttLib import TTFont

here = os.path.dirname(__file__)
name = "方正兰亭圆-逐梦星辰.ttf"
src = os.path.join(here, name)
if not os.path.exists(src):
    print(f"源文件不存在: {src}")
    raise SystemExit(1)

base, _ = os.path.splitext(src)
woff = base + '.woff'
woff2 = base + '.woff2'

try:
    font = TTFont(src)
    font.flavor = 'woff'
    font.save(woff)
    font.close()
    print('生成:', woff)
except Exception as e:
    print('生成 woff 失败:', e)

try:
    font = TTFont(src)
    font.flavor = 'woff2'
    font.save(woff2)
    font.close()
    print('生成:', woff2)
except Exception as e:
    print('生成 woff2 失败:', e)

print('完成。')
