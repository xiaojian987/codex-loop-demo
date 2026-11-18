---
name: clamp-fix
description: 在 codex-loop-demo 的独立 Git worktree 中修复 clamp 下界故障并验证。仅用于本仓库的 clamp 演示工单。
---

# 修复 clamp 演示故障

1. 在用户指定的演示 worktree 根目录执行 `python3 -B -m unittest -v`。预期退出码为 `1`，仅 `test_below_lower` 失败（实际 `-2`，预期 `0`），另外两个测试通过。若不是这个结果，或当前不在指定的 worktree 中，报告情况并停止，不修改文件。
2. 只修改 `clamp.py`，让低于下界的输入返回下界，同时保留区间内和高于上界的行为。不修改测试或其他文件。
3. 在同一目录重跑 `python3 -B -m unittest -v`。只有全部 3 个测试通过且退出码为 `0`，才算修复通过。
4. 报告改动、两次测试结果和 worktree 路径。不提交、不推送、不合并、不修改工单。独立审查和跨轮记录由外层任务安排。
