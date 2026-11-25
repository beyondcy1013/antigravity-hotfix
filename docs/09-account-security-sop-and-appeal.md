# 09. 新号养号 SOP、安全改密顺序与封号申诉指南

> 账号稳定大于一切。绝大多数新号“刚买就死”或“改完资料秒封”，都是因为**一登录就大改安全信息**或**修改顺序错误**。

---

## 一、登录前准备与前两周养号 SOP

1. **出口 IP 体检**
   登录前检查代理节点质量（如使用 `ping0.cc` 检测）：风控值建议控制在 **30 以下**，共享人数尽量不要过高。
2. **一号一浏览器环境（强隔离）**
   - 前两周务必保持**同一台设备 + 同一个稳定 IP 节点 + 同一个 Chrome 独立配置文件（Profile）**。
   - 有多个 Google 账号时，**利用 Chrome 多用户（Add Profile）分窗口隔离**，绝对不要在同一个浏览器窗口频繁退出/切换账号登录。
3. **模拟真实用户行为**
   刚登录新设备时先正常浏览（看会儿 YouTube、搜几个关键词、收发邮件），**切忌一上来就大刀阔斧修改密码、2FA 和设备**。

---

## 二、安全设置修改：严格 6 步顺序（切勿跳步！）

> [!CAUTION]
> **必须严格按以下顺序操作**。如果某一步提示验证失败或无法操作，**立即停止、不要跳过执行下一步**，说明当前账号尚未稳定，等待数小时或 1~2 天后再继续。

1. **第一步：绑定并验证恢复邮箱（辅助邮箱）与恢复号码**
   - 位置：头像 → 管理你的 Google 账号 → 安全性（Security）。
   - 辅助邮箱务必完成验证。**这是账号触发风控后能否找回的最后救命稻草。**
2. **第二步：开启两步验证（2FA）并保存备用验证码**
   - 绑定自己的手机号。
   - **刷新并拍照/离线保存备用验证码（Backup Codes）**（如果是旧号自带的，务必点刷新后再保存）。
3. **第三步：踢出陌生设备（严格限额！）**
   - 访问：`https://myaccount.google.com/device-activity`（或安全页面管理设备）。
   - **每次最多移除 3 台设备！** 切勿一次全部踢光；如果还有剩余陌生设备，**等待 3 小时后再移除下一批**。保留你自己的设备/手机设备。
4. **第四步：更新联系邮箱**
   - 进入“个人信息（Personal info）” → “联系信息（Contact info）” → 将联系邮箱替换为自己的常用邮箱。
5. **第五步：更换 2FA 身份验证器密钥**
   - 点击更换身份验证器 → 选择“无法扫码” → 复制新的密钥文本到你自己的验证器（或 2FA 工具）生成 6 位动态码并回填验证。
   - **关键核验**：更换完成后，页面上的“更换时间”必须显示为 **“刚刚”**，否则说明未生效；务必妥善保存新密钥，旧密钥作废。
6. **第六步：7 天后再修改密码**
   - 前 5 步稳定满 **7 天**后，再访问 `https://myaccount.google.com/signinoptions/password` 修改密码，并复查上述 1~5 步是否全部到位。

---

## 三、Gemini / Antigravity 账号常见问题速查

| 现象 | 排查与快速解法 |
| :--- | :--- |
| **账号显示 `FREE` / 无法使用 Pro 权益** | 检查是否需要年龄验证：`https://myaccount.google.com/age-verification` |
| **Gemini 页面报错“出现有点问题”** | 尝试访问 `https://gemini.google.com/gems/create?hl=en-US&pli=1`，随便输入内容并点击右上角保存 |
| **查看会员有效期与订阅状态** | `https://myaccount.google.com/payments-and-subscriptions` |
| **关闭 / 清理支付资料** | `https://payments.google.com/gp/w/u/0/home/settings` |
| **快速检查 Gmail 账号存活状态** | 使用 `https://www.gmailcheck.com/` 等检测工具 |

---

## 四、服务停用与封号申诉（Appeal）指南

### 1. Antigravity 专属服务停用申诉
当出现以下提示时：
> *`This service has been disabled in this account for violation of Terms of Service. Please submit an appeal to continue using this product.`*

- **官方申诉表单**：`https://forms.gle/hGzM9MEUv2azZsrb9`
- **4 条申诉铁律**：
  1. **只提交一次**：重复提交不会加速，反而会打乱审核队列。
  2. **耐心等待 48–72 小时**：审核期间**不会**发确认邮件或进度邮件，无需天天刷收件箱。
  3. **无声自动恢复**：申诉通过后通常没有额外邮件通知，下次直接登录即可恢复正常。
  4. **珍惜唯一机会**：每个账号通常只有一次申诉机会，恢复后务必改善 IP 与使用习惯，再犯大概率永久封禁。

### 2. Google 账号被冻结申诉技巧与话术
- **语言要求**：**使用英文提交**（不要用简体中文），并留下可联系的备用邮箱。
- **绝对红线**：**千万不要写账号是买的、租的或他人的**，否则直接永久封禁。
- **叙事要点**：
  1. 表明自己是真实个人用户（如居住在国内的普通开发者/用户）；
  2. 因本地网络环境不稳定不得不使用代理（VPN），导致 IP 频繁波动被误判为异常活动；
  3. 强调账号仅用于日常个人/工作使用（邮件、照片、云盘等），内部存有重要数据，严格遵守 Google 服务条款。
- **防模板查重**：参考以下结构用日常口语化的英文重新润色（避免浓重 AI 腔或直接复制粘贴万人模板），提交后通常 **24–48 小时**会有结果：

```text
Hello, my account is <your-email>@gmail.com.

I am located in China and have to use VPN services to access Google products.
Due to the instability and frequent switching of VPN nodes, my account might have been mistakenly suspended.
This account is very important for my daily work and personal data (emails, backups, etc.), and I always follow Google's Terms of Service.
I sincerely hope you can review my case and help me restore access.

Thank you very much for your time and help.
```
