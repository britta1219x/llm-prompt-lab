# LLM Prompt Lab

一个持续记录、测试与改进 LLM 提示词的小型实验仓库。

这里不追求“万能提示词”，而是保留可复用的提示词、可验证的案例，以及实验过程中得到的判断。

## 仓库里的三类内容

1. **Prompts**：可直接使用的提示词模板。
2. **Evals**：用于检查提示词是否真的稳定有效的测试案例。
3. **Tools**：不依赖 API Key 的小工具，用来检查提示词文件和整理实验。

## 提示词索引

| 提示词 | 用途 | 评测集 |
| --- | --- | --- |
| [中文写作教练](prompts/chinese-writing-coach.md) | 改进中文表达，保留作者原本的语气和观点 | [写作教练评测](evals/chinese-writing-coach.json) |
| [代码审查助手](prompts/code-review-assistant.md) | 对一段代码做聚焦审查，只报告有依据的问题 | [代码审查评测](evals/code-review-assistant.json) |
| [Git 提交信息助手](prompts/commit-message-writer.md) | 按 Conventional Commits 生成提交信息，改动混杂时先建议拆分 | [提交信息评测](evals/commit-message-writer.json) |

每个提示词都带一份评测集，覆盖正常输入、已经足够好的输入和信息不足的输入三类情况。新增提示词先过检查器：

```bash
python3 tools/prompt_linter.py prompts/
```

## 实验记录模板

每次改一个提示词时，记录：

```text
目标：
改动：
测试输入：
观察结果：
结论 / 下一步：
```

## 原则

- 不提交 API Key、真实私密对话或客户资料。
- 一个提示词只解决一个清晰问题。
- 先有 3–5 个测试案例，再说“这个提示词好用”。
