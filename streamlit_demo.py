import streamlit as st
import requests
from traitlets import Unicode
def search_local_knowledge(query):
    """从 knowledge.txt 中检索包含关键词的行"""
    try:
        with open(r"D:\AI_learning\knowledge.txt", "r", encoding="utf-8") as f:
            lines = f.readlines()
        results = [line.strip() for line in lines if query in line]
        return results if results else ["未找到相关信息，请参考通用知识。"]
    except FileNotFoundError:
        return ["⚠️ 知识库文件未找到，请确保 knowledge.txt 在正确目录下。"]
    except UnicodeDecodeError:
        return ["⚠️ 文件编码异常，请将knowledge.txt 保存位UTF-8格式。"]
    
def call_api(question, context):
    # 模拟网络延迟
    import time
    time.sleep(1.5)
    
    # 从检索到的资料中提取前50个字符作为“回答”
    if context:
        return f"根据知识库检索到的资料：{context[:50]}...（此处为模拟回答，接入真实API后可生成完整答案）"
    else:
        return "未找到相关资料，无法生成回答。"

# ===== 1. 设置页面标题和图标 =====
st.set_page_config(page_title="文档问答助手", page_icon="📚")

# ===== 2. 显示大标题 =====
st.title("📚 文档问答助手")
st.caption("基于本地知识库的智能问答原型")

# ===== 3. 侧边栏信息 =====
with st.sidebar:
    st.header("⚙️ 状态信息")
    st.write("📄 知识库状态：已加载")
    st.write("当前模式：模拟回答（无API）")

# ===== 4. 主界面输入区域 =====
st.subheader("💬 输入您的问题")

# 文本输入框
user_question = st.text_input("请输入您的问题：", placeholder="例如：什么是RAG？")

# 按钮（核心交互）
col1, col2 = st.columns([1, 5])  # 两列布局，让按钮不占满
with col1:
    search_btn = st.button("🔍 检索", use_container_width=True)

# ===== 5. 结果显示区域 =====
st.divider()  # 分割线
st.subheader("📖 回答结果")

if search_btn and not user_question:
    st.warning("请输入问题后再点击检索")
if search_btn and user_question:
    # 这里先放占位符，明天我们再把真正的RAG逻辑接进来
    with st.spinner("正在检索知识库..."):
        # 模拟检索过程（实际明天替换为真实函数）
        matched_lines = search_local_knowledge(user_question)
        
    # 模拟显示结果（明天替换为真实答案）
    st.subheader("检索结果")
    if matched_lines and matched_lines !=["未找到相关信息,请参考通识知识。"]:
        st.success(f"找到 {len(matched_lines)}条相关信息")
        for line in matched_lines:
            st.info(line)
    else:
        st.warning("未找到与您问题直接相关的资料，请尝试换一种说法。")

elif search_btn and not user_question:
    st.warning("⚠️ 请先输入问题！")
else:
    st.info("💡 输入问题后点击「检索」按钮，系统将基于本地知识库给出回答。")