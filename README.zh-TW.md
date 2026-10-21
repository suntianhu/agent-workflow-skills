# Agent Workflow Skills

供程式開發代理組合使用的開發工作流程，明確定義專案前置條件，並以實際證據支持完成結論。

[English](README.md) · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Русский](README.ru.md)

![License: MIT](https://img.shields.io/badge/license-MIT-blue)
![Skills: 29](https://img.shields.io/badge/skills-29-2563eb)
![Workflows: 9](https://img.shields.io/badge/workflows-9-0f766e)

**版本 1.2.8** · Agent Skills 目錄格式 · Python 3.10+ 工具 · 執行工具僅依賴 Python 標準函式庫

**依任務選技能，沿用專案既有規範。** 29 個技能、9 套條件組合涵蓋新舊專案開發、[專案遷移](docs/project-migration.md)、[效能與可觀測性](docs/adoption-integration.md)。承接有效決定，按需分工，以實際證據說明交付成果。

[GitHub 借鑑來源](#sources) · [使用範例](examples/README.md) · [版本紀錄](CHANGELOG.md)

## 為什麼使用這套技能

- **精簡入口：** 移除重複說明，先選一項主要能力，有缺口才補讀相關資料；直接沿用有效決定及未變更的已讀內容。
- **精準觸發：** 九套組合依條件選擇階段。明確的局部修改不自動啟動大範圍調研、模型比較或多代理；估時也有獨立觸發條件。
- **變更有邊界：** 多項小任務逐一對應需求與驗收，只做有依據的必要連動；保留其他功能的既有行為，無關的新問題只記錄、不順手修復。
- **沿用既有專案規範：** 核對完整程式碼基線及後續差異，繼續維護原規範目錄與規則來源。新頁面即使業務全新，也繼承專案字型、主題、元件與互動慣例。
- **依風險驗證：** 範圍、TDD 順序與產物保留分別決定。小改動不自動採用 TDD，也不擅自刪除使用者既有測試。
- **按需使用資源：** 額外技能、模型與代理需要具體效益，以及執行環境的實際能力與相應授權。

本專案提供指令與本機工具。組合 JSON 描述條件與順序，不是執行環境原生的工作流程引擎。

## 快速開始

1. 在下表選擇組合，或查看 [29 個技能的職責邊界](docs/skill-map.md)（簡體中文）。
2. 讓代理讀取所需的 `skills/<name>/SKILL.md` 及其引用資源，只載入本次任務適用的能力。
3. 如需在儲存庫以外的新目錄準備完整組合：

```sh
python scripts/export_bundle.py --bundle existing-frontend --out ../workflow-export
```

加上 `--include-optional` 可一併匯出代理協作技能。匯出不會安裝技能或更改預設設定；既有目標、重新導向路徑、過期生成檔案、儲存庫內部目標及原生安裝位置都會被拒絕。

需要原生技能探索時，僅在確定要安裝的情況下，依執行環境目前的文件複製完整的個別技能目錄。詳見[代理相容性](docs/agent-compatibility.md)（英文）。

### 選用的 Skills CLI

使用 Node.js 22.20+ 時，可透過官方 CLI 列出本儲存庫的技能：

```sh
npx skills@1.7.4 add suntianhu/agent-workflow-skills --list
```

專案範圍安裝、停用遙測及 skills.sh 分組請見[安裝與隱私說明](docs/skills-sh.md)（英文／簡體中文）。CLI 探索與代理執行證據分開說明。

## 九套工作流程

| 工作流程 | 適用任務 | 核心前置條件 |
| --- | --- | --- |
| [existing-frontend](bundles/existing-frontend.json) | 既有專案的前端開發 | 全部程式碼審閱 → 內部規範 → 前端設計與實作 |
| [existing-backend](bundles/existing-backend.json) | 既有專案的後端開發 | 全部程式碼審閱 → 內部規範 → 後端實作 |
| [new-frontend](bundles/new-frontend.json) | 真正從零開始的前端專案 | 語言/平台 → 框架查核 → 使用者選擇 → 範例慣例 → 規範 |
| [new-backend](bundles/new-backend.json) | 真正從零開始的後端專案 | 語言/部署需求 → 使用者選擇技術組合 → 範例慣例 → 規範 |
| [fullstack](bundles/fullstack.json) | 前後端跨端開發 | 選擇新舊專案分支，分別維護端內規範，共同核對 API 契約 |
| [project-migration](bundles/project-migration.json) | 更換框架、前後台或資料庫重構 | 保留台帳 → 目標／共存 → 業務分批 → 驗證後切換與復原 |
| [small-change](bundles/small-change.json) | 範圍有限、影響較低的修改 | 精簡流程，仍須滿足適用的新舊專案前置條件 |
| [debug-and-fix](bundles/debug-and-fix.json) | 可重現缺陷或整合異常 | 執行重現前選定驗證策略，修復前滿足程式碼與規範前置條件 |
| [release](bundles/release.json) | 已提出要求的整合、封裝或發布 | 準備相容性、復原與驗收證據；程式碼修正交回開發流程 |

`skills` 欄位是可匯出的完整能力集合，不代表所有技能都要執行。各階段依條件觸發；選擇 TDD 時由其循環統籌實作，跳過獨立實作階段。詳細的[組合條件與順序](docs/bundles.md)目前以簡體中文提供。

## 能力分布

| 領域 | 技能 |
| --- | --- |
| 任務與資源判斷 | `aw-project-triage`, `aw-skill-selection`, `aw-model-routing`, `aw-effort-estimation` |
| 程式碼理解與架構 | `aw-repository-audit`, `aw-project-standards`, `aw-framework-selection`, `aw-github-reference`, `aw-project-migration` |
| 需求與實作 | `aw-requirements-design`, `aw-design-reference`, `aw-design-standards`, `aw-ui-design`, `aw-frontend-implementation`, `aw-backend-implementation` |
| 效能與可觀測性 | `aw-performance-optimization`, `aw-observability` |
| 契約與安全邊界 | `aw-api-contracts`, `aw-security-boundaries` |
| 驗證與問題診斷 | `aw-test-strategy`, `aw-scoped-tdd`, `aw-evidence-debugging`, `aw-adversarial-review`, `aw-evidence-verification` |
| 交付與維護 | `aw-delivery-cleanup`, `aw-release-readiness`, `aw-agent-coordination`, `aw-skill-authoring`, `aw-open-source-readiness` |

每個技能都有自己的指令、必要參考資料/資源與授權條款。catalog 與來源指南是維護依據，生成的技能副本必須保持同步。

## 代理相容性

| 執行環境 | 封裝方式 | 實際證據 |
| --- | --- | --- |
| Codex | Agent Skills 目錄，可選用 `agents/openai.yaml` 介面中繼資料 | 1.2.7 Windows Codex 原生探索：29/29 本機已安裝技能啟用，無解析錯誤；未執行模型任務 |
| Claude Code | 在文件指定位置放置完整技能目錄 | 1.2.0: 原生 CLI 與官方 SDK 探索 24/24；未成功執行模型任務 |
| Gemini CLI | 在文件指定位置放置完整技能目錄 | 僅依文件對應；尚未進行端到端測試 |
| GitHub Copilot | 在支援的用戶端使用完整技能目錄 | 僅依文件對應；尚未測試各用戶端 |
| 其他代理 | 支援時讀取 `SKILL.md` 及相對引用 | 不概括承諾未經驗證的原生相容性 |

[協作角色說明](docs/role-briefs.md)（簡體中文）定義可選的多代理職責，不會自動註冊代理設定。實際權限、工具、信任設定與模型能力仍以執行環境為準。

## 驗證

```sh
python scripts/build_catalog.py
python scripts/validate.py
```

驗證器會檢查宣告、生成內容是否同步、精確資源集合、本機連結、Python 語法、組合順序及部分分發衛生規則；不證明代理決策正確，也不保證框架沒有漏洞。

Windows/Linux CI 檢查原始碼、離線工具及可重現封裝。1.2.7 的 Windows Codex 原生探索辨識並啟用全部 29 個本機技能，無解析錯誤；154 個安裝檔案與原始碼一致。早期 Codex/Claude 隔離探索與 42 項瀏覽器檢查保留原範圍，不代表本版自動觸發準確率、模型遵循率或正式環境覆蓋。見[驗證紀錄](docs/validation.md)及[原生證據](docs/agent-loading.md)。

## 使用範例與自動發佈

[完整範例](examples/README.md)包含已執行的本儲存庫案例，以及小改、既有後端與新前後端的提示詞。執行 `python scripts/run_examples.py` 可在 TEMP 重現離線工具檢查。

推送符合版本的標籤後自動檢查並發佈 ZIP 與 SHA-256 檔案，見[發佈步驟](docs/github-publishing.md)。[原生探索重跑](docs/agent-loading.md)使用隔離目錄，不改預設技能。選用原生檢查需要實際客戶端；Claude 另需 Node 與官方 Agent SDK，其餘 Python 工具只依賴標準函式庫。

## 語言

專案簡介提供英文、簡體中文、繁體中文、日文、韓文與俄文。GitHub 貢獻文件與範本使用英文，歡迎英文或中文貢獻。本版技能正文、詳細指南與工具訊息仍使用簡體中文，並非整套技能的六語翻譯。可以要求代理以你偏好的語言回覆。

## 貢獻與發布

先用實際任務說明缺口，優先完善負責該能力的技能，避免新增重疊規則。參見[貢獻指南](CONTRIBUTING.md)、[安全政策](SECURITY.md)與[GitHub 發布指南](docs/github-publishing.md)（英文）。

匯出與驗證工具不會發布儲存庫或操作遠端帳號，未預設私密通報地址或使用規模。

<a id="sources"></a>

## GitHub 借鑑與蒸餾來源

本專案研究以下 14 個 GitHub 專案的部分內容，將適用原則重新組織為獨立撰寫的技能與指南。紀錄涵蓋固定提交下實際取得的 73 份檔案，不代表完整審查這些儲存庫。主要借鑑點如下；閱讀範圍、未採納規則與許可見[來源取捨](docs/provenance.md)、[固定提交及檔案指紋](provenance/upstreams.json)、[第三方說明](THIRD_PARTY_NOTICES.md)。

| 專案 | 主要借鑑內容 |
| --- | --- |
| [anthropics/skills](https://github.com/anthropics/skills) | 精簡技能入口、按需展開引用資源 |
| [openai/skills](https://github.com/openai/skills) | 歷史技能封裝、來源與生成副本分離、腳本實證 |
| [obra/superpowers](https://github.com/obra/superpowers) | 證據導向除錯、明確假設、限定範圍的審查 |
| [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | 依框架觸發、依影響排序效能問題 |
| [github/awesome-copilot](https://github.com/github/awesome-copilot) | 區分技能、指令與代理角色，保持職責集中 |
| [trailofbits/skills](https://github.com/trailofbits/skills) | 沿實際呼叫鏈核對安全邊界，以反例檢驗結論 |
| [supabase/agent-skills](https://github.com/supabase/agent-skills) | PostgreSQL 執行計畫、索引、連線預算與交易／鎖定邊界 |
| [microsoft/playwright-cli](https://github.com/microsoft/playwright-cli) | 依即時定位器操作、隔離瀏覽器工作階段、區分動作與斷言證據 |
| [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | 從介面需求推導字型、元件與平台選擇 |
| [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | 繼承既有設計慣例，區分局部設計與共用標準 |
| [wshobson/agents](https://github.com/wshobson/agents) | 設計權杖、可重用元件、平台差異與適量動效 |
| [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | 需求就緒度、任務交接、品質門檻、遷移、效能與可觀測性 |
| [magnus919/agent-skills](https://github.com/magnus919/agent-skills) | 遷移相容性、資料核對與實際恢復限制 |
| [rmyndharis/antigravity-skills](https://github.com/rmyndharis/antigravity-skills) | 整合關係梳理、依業務分批遷移、明確執行責任 |

## 授權

原創內容採用 [MIT](LICENSE)，未重新散布上游技能正文、程式碼、範本、素材或資料庫。各來源授權獨立適用；Trail of Bits 來源為 CC-BY-SA-4.0，未將其正文改編為 MIT 內容。逐項授權範圍見第三方說明。
