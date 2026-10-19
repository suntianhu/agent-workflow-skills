# Agent Workflow Skills

供程式開發代理組合使用的開發工作流程，明確定義專案前置條件，並以實際證據支持完成結論。

[English](README.md) · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Русский](README.ru.md)

![License: MIT](https://img.shields.io/badge/license-MIT-blue)
![Skills: 26](https://img.shields.io/badge/skills-26-2563eb)
![Workflows: 8](https://img.shields.io/badge/workflows-8-0f766e)

**版本 1.2.1** · Agent Skills 目錄格式 · Python 3.10+ 工具 · 執行工具僅依賴 Python 標準函式庫

1.2.1 保留 26 個技能、8 套條件組合：先選主要能力，只補缺口，沿用專案規則；修改使用者既有 Skill 前須展示具體方案並取得確認。見[最短路徑](docs/bundles.md)、[設計流程](docs/design-workflow.md)、[出處](docs/provenance.md)及[版本／標籤紀錄](docs/versioning.md)。

區分既有專案與新專案，依任務選擇適用技能，分別維護前後端規範，在實作前選定驗證策略，並如實回報實際驗證範圍。

## 為什麼使用這套技能

- **承接既有技能：** 梳理專案已設定的 Skills 與代理/外掛規則，後續啟用技能先對齊同一份專案規範與既有決定。
- **既有專案：** 修改程式碼、設定或工程腳本前，閱讀全部專案自有程式碼，並在專案內建立有證據支持的工程規範。
- **新專案：** 尊重指定語言，查核框架維護狀態與已知相關風險，由使用者選擇技術組合，再從相符的公開專案提煉規範。
- **依風險驗證：** 範圍、TDD 順序與產物保留分別決定。小改動不自動採用 TDD，也不擅自刪除使用者既有測試。
- **依實際耗時估算：** 分開計算實作、檢查、審查與外部等待，使用同類工作的實際紀錄校準，不統一套用固定倍數。
- **根據需求設計：** 先明確定義行為與驗收條件，再依實際介面和情境推導視覺方案。
- **按需使用資源：** 額外技能、模型與代理需要具體效益，以及執行環境的實際能力與相應授權。

本專案提供指令與本機工具。組合 JSON 描述條件與順序，不是執行環境原生的工作流程引擎。

## 快速開始

1. 在下表選擇組合，或查看 [26 個技能的職責邊界](docs/skill-map.md)（簡體中文）。
2. 讓代理讀取所需的 `skills/<name>/SKILL.md` 及其引用資源，只載入本次任務適用的能力。
3. 如需在儲存庫以外的新目錄準備完整組合：

```sh
python scripts/export_bundle.py --bundle existing-frontend --out ../workflow-export
```

加上 `--include-optional` 可一併匯出代理協作技能。匯出不會安裝技能或更改預設設定；既有目標、重新導向路徑、過期生成檔案、儲存庫內部目標及原生安裝位置都會被拒絕。

需要原生技能探索時，僅在確定要安裝的情況下，依執行環境目前的文件複製完整的個別技能目錄。詳見[代理相容性](docs/agent-compatibility.md)（英文）。

## 八套工作流程

| 工作流程 | 適用任務 | 核心前置條件 |
| --- | --- | --- |
| [existing-frontend](bundles/existing-frontend.json) | 既有專案的前端開發 | 全部程式碼審閱 → 內部規範 → 前端設計與實作 |
| [existing-backend](bundles/existing-backend.json) | 既有專案的後端開發 | 全部程式碼審閱 → 內部規範 → 後端實作 |
| [new-frontend](bundles/new-frontend.json) | 真正從零開始的前端專案 | 語言/平台 → 框架查核 → 使用者選擇 → 範例慣例 → 規範 |
| [new-backend](bundles/new-backend.json) | 真正從零開始的後端專案 | 語言/部署需求 → 使用者選擇技術組合 → 範例慣例 → 規範 |
| [fullstack](bundles/fullstack.json) | 前後端跨端開發 | 選擇新舊專案分支，分別維護端內規範，共同核對 API 契約 |
| [small-change](bundles/small-change.json) | 範圍有限、影響較低的修改 | 精簡流程，仍須滿足適用的新舊專案前置條件 |
| [debug-and-fix](bundles/debug-and-fix.json) | 可重現缺陷或整合異常 | 執行重現前選定驗證策略，修復前滿足程式碼與規範前置條件 |
| [release](bundles/release.json) | 已提出要求的整合、封裝或發布 | 準備相容性、復原與驗收證據；程式碼修正交回開發流程 |

`skills` 欄位是可匯出的完整能力集合，不代表所有技能都要執行。各階段依條件觸發；選擇 TDD 時由其循環統籌實作，跳過獨立實作階段。詳細的[組合條件與順序](docs/bundles.md)目前以簡體中文提供。

## 能力分布

| 領域 | 技能 |
| --- | --- |
| 任務與資源判斷 | `aw-project-triage`, `aw-skill-selection`, `aw-model-routing`, `aw-effort-estimation` |
| 程式碼理解與架構 | `aw-repository-audit`, `aw-project-standards`, `aw-framework-selection`, `aw-github-reference` |
| 需求與實作 | `aw-requirements-design`, `aw-design-reference`, `aw-design-standards`, `aw-ui-design`, `aw-frontend-implementation`, `aw-backend-implementation` |
| 契約與安全邊界 | `aw-api-contracts`, `aw-security-boundaries` |
| 驗證與問題診斷 | `aw-test-strategy`, `aw-scoped-tdd`, `aw-evidence-debugging`, `aw-adversarial-review`, `aw-evidence-verification` |
| 交付與維護 | `aw-delivery-cleanup`, `aw-release-readiness`, `aw-agent-coordination`, `aw-skill-authoring`, `aw-open-source-readiness` |

每個技能都有自己的指令、必要參考資料/資源與授權條款。catalog 與來源指南是維護依據，生成的技能副本必須保持同步。

## 代理相容性

| 執行環境 | 封裝方式 | 實際證據 |
| --- | --- | --- |
| Codex | Agent Skills 目錄，可選用 `agents/openai.yaml` 介面中繼資料 | 1.2.0: Windows 隔離原生探索 24/24；未執行模型任務 |
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

Windows/Linux CI 檢查原始碼、執行離線範例並預演封裝。Codex 與 Claude 已在 Windows 隔離專案中原生探索全部 24 個技能。另外已在兩個可執行的虛構 Web 工程完成新舊專案與後續需求，最終 42 項瀏覽器檢查通過；這不代表目前 26 個技能的自動探索／觸發或正式環境覆蓋。版本與範圍見[實際流程](docs/executed-workflows.md)、[驗證紀錄](docs/validation.md)及[原生載入證據](docs/agent-loading.md)。

## 使用範例與自動發佈

[完整範例](examples/README.md)包含已執行的本儲存庫案例，以及小改、既有後端與新前後端的提示詞。執行 `python scripts/run_examples.py` 可在 TEMP 重現離線工具檢查。

推送符合版本的標籤後自動檢查並發佈 ZIP 與 SHA-256 檔案，見[發佈步驟](docs/github-publishing.md)。[原生探索重跑](docs/agent-loading.md)使用隔離目錄，不改預設技能。選用原生檢查需要實際客戶端；Claude 另需 Node 與官方 Agent SDK，其餘 Python 工具只依賴標準函式庫。

## 語言

專案簡介提供英文、簡體中文、繁體中文、日文、韓文與俄文。GitHub 貢獻文件與範本使用英文，歡迎英文或中文貢獻。本版技能正文、詳細指南與工具訊息仍使用簡體中文，並非整套技能的六語翻譯。可以要求代理以你偏好的語言回覆。

## 貢獻與發布

先用實際任務說明缺口，優先完善負責該能力的技能，避免新增重疊規則。參見[貢獻指南](CONTRIBUTING.md)、[安全政策](SECURITY.md)與[GitHub 發布指南](docs/github-publishing.md)（英文）。

匯出與驗證工具不會發布儲存庫或操作遠端帳號，未預設私密通報地址或使用規模。

## 授權與來源

原創內容採用 [MIT](LICENSE) 授權。公開上游僅用於研究並重新撰寫原則，不分發其技能正文、實作、素材或資料庫。參見[第三方聲明](THIRD_PARTY_NOTICES.md)、[固定來源](provenance/upstreams.json)及[來源說明](docs/provenance.md)（簡體中文）。本儲存庫的授權不會重新授權第三方內容。
