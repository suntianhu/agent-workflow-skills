# Agent Workflow Skills

コーディングエージェント向けの、組み合わせて使える開発ワークフロー。プロジェクトごとの前提条件を明確にし、実際の証拠に基づいて完了を判断します。

[English](README.md) · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Русский](README.ru.md)

![License: MIT](https://img.shields.io/badge/license-MIT-blue)
![Skills: 29](https://img.shields.io/badge/skills-29-2563eb)
![Workflows: 9](https://img.shields.io/badge/workflows-9-0f766e)

**バージョン 1.3.1** · Agent Skills ディレクトリ形式 · Python 3.10+ 用ツール · 実行時の依存関係は Python 標準ライブラリのみ

**タスクに合うスキルを選び、既存の規約を引き継ぎます。** 29スキルと9つの条件付き構成で、既存・新規プロジェクト、[移行](docs/project-migration.md)、[性能と可観測性](docs/adoption-integration.md)を扱います。有効な決定を再利用し、必要に応じて分担し、実際の証拠で成果を示します。

不具合修正では、実データの前提と影響を受ける業務フロー全体を確認します。コンパイルとテストダブルの成功だけでは、修正済みとは判断しません。

[参考資料と謝辞](#sources) · [使用例](examples/README.md) · [変更履歴](CHANGELOG.md)

## このコレクションの特徴

- **簡潔な入口：** 重複した説明を減らし、主要な能力を一つ選び、不足する場合だけ関連資料を読みます。有効な決定と、変更されていない既読資料を再利用します。
- **タスクに応じた起動：** 9つの構成は条件に応じて段階を選びます。明確な局所変更で広範な調査、モデル比較、複数エージェントを自動的に開始せず、見積もりも独立した条件で判断します。
- **変更範囲の維持：** 各変更を依頼項目または根拠のある必須の連動に対応させ、無関係な動作を維持します。新たに見つけた範囲外の問題は記録にとどめ、勝手に修正しません。
- **既存規約の継承：** コード全体のベースラインと以後の差分を確認し、同じ規約ディレクトリとルールの管理元を使います。新しい業務のページでも、フォント、テーマ、コンポーネント、操作パターンを引き継ぎます。
- **リスクに見合う検証：** 検証範囲、TDD の実施順序、成果物の保持方針を個別に決めます。小さな変更で TDD を自動的に要求せず、ユーザーの既存テストを保持します。
- **必要なリソースだけを使用：** 追加のスキル、モデル、エージェントは、具体的な効果と実行環境の機能・権限がある場合に使います。

このプロジェクトは指示とローカルツールのコレクションです。ワークフローの JSON は条件と順序を記述するもので、実行環境に組み込まれたワークフローエンジンではありません。

## クイックスタート

1. 下のワークフローを選ぶか、[29 スキルの責務](docs/skill-map.md)（簡体字中国語）を確認します。
2. 必要な `skills/<name>/SKILL.md` と参照リソースを読むようエージェントに指示します。現在のタスクに必要な能力だけを読み込みます。
3. このリポジトリの外にある新しいディレクトリへ、必要なファイルを含む構成をエクスポートするには：

```sh
python scripts/export_bundle.py --bundle existing-frontend --out ../workflow-export
```

`--include-optional` を追加すると、エージェント連携スキルも含められます。エクスポートはスキルのインストールや既定設定の変更を行いません。既存の出力先、リダイレクトされたパス、古い生成ファイル、リポジトリ内の出力先、ネイティブのインストール先は拒否されます。

ネイティブのスキル検出を利用する場合は、インストールする意思があるときに限り、実行環境の最新ドキュメントに従って個々のスキルディレクトリ全体をコピーしてください。[エージェント互換性](docs/agent-compatibility.md)（英語）を参照してください。

### 任意の Skills CLI

Node.js 22.20+ では、公式 CLI でこのリポジトリのスキルを一覧表示できます。

```sh
npx skills@1.7.4 add suntianhu/agent-workflow-skills --list
```

プロジェクト単位のインストール、テレメトリの無効化、skills.sh の分類は[インストールとプライバシー](docs/skills-sh.md)（英語／簡体字中国語）を参照してください。CLI による検出とエージェント実行の証拠は別です。

## 9 つのワークフロー

| ワークフロー | 対象 | 主な前提条件 |
| --- | --- | --- |
| [existing-frontend](bundles/existing-frontend.json) | 既存プロジェクトのフロントエンド開発 | コード全体の確認 → 内部規約 → フロントエンドの設計・実装 |
| [existing-backend](bundles/existing-backend.json) | 既存プロジェクトのバックエンド開発 | コード全体の確認 → 内部規約 → バックエンドの実装 |
| [new-frontend](bundles/new-frontend.json) | ゼロから始めるフロントエンドプロジェクト | 言語・プラットフォーム → 候補調査 → ユーザーの選択 → 参考規約 → 内部規約 |
| [new-backend](bundles/new-backend.json) | ゼロから始めるバックエンドプロジェクト | 言語・デプロイ要件 → ユーザーによる技術選択 → 参考規約 → 内部規約 |
| [fullstack](bundles/fullstack.json) | 両側にまたがる開発 | 既存・新規の分岐を選択し、各側の規約を分け、API 契約を共有 |
| [project-migration](bundles/project-migration.json) | フレームワーク・前後端・DBの移行 | 維持項目 → 移行先と共存 → 業務単位の実装 → 検証と復旧 |
| [small-change](bundles/small-change.json) | 範囲が限定された低影響の変更 | 手順を簡素化しつつ、該当する既存・新規プロジェクトの前提条件を維持 |
| [debug-and-fix](bundles/debug-and-fix.json) | 再現可能な不具合や連携の異常 | 再現操作前に検証方針を選択し、修正前にコードと規約の前提条件を満たす |
| [release](bundles/release.json) | 依頼された統合、パッケージ化、リリース | 互換性・復旧・検証の証拠を準備し、コード修正は開発フローへ戻す |

`skills` はエクスポートに必要な能力を漏れなく含む一覧であり、すべてを実行する指示ではありません。各ステージは条件に従って選択されます。TDD を選択した場合は、そのループ内で実装し、独立した実装ステージはスキップします。詳しい[構成ルール](docs/bundles.md)は現在、簡体字中国語で提供しています。

## 能力マップ

| 分野 | スキル |
| --- | --- |
| タスクとリソースの判断 | `aw-project-triage`, `aw-skill-selection`, `aw-model-routing`, `aw-effort-estimation` |
| コード理解とアーキテクチャ | `aw-repository-audit`, `aw-project-standards`, `aw-framework-selection`, `aw-github-reference`, `aw-project-migration` |
| 要件と実装 | `aw-requirements-design`, `aw-design-reference`, `aw-design-standards`, `aw-ui-design`, `aw-frontend-implementation`, `aw-backend-implementation` |
| 性能と可観測性 | `aw-performance-optimization`, `aw-observability` |
| 契約とセキュリティ境界 | `aw-api-contracts`, `aw-security-boundaries` |
| 検証と不具合調査 | `aw-test-strategy`, `aw-scoped-tdd`, `aw-evidence-debugging`, `aw-adversarial-review`, `aw-evidence-verification` |
| 成果物の引き渡しと保守 | `aw-delivery-cleanup`, `aw-release-readiness`, `aw-agent-coordination`, `aw-skill-authoring`, `aw-open-source-readiness` |

各スキルには、固有の指示、必要な参照資料・リソース、ライセンスが含まれます。catalog と元のガイドを保守の基準とし、生成されたスキルのコピーを同期させます。

## エージェント互換性

| 実行環境 | パッケージ形式 | 確認済みの範囲 |
| --- | --- | --- |
| Codex | Agent Skills ディレクトリと、任意の `agents/openai.yaml` UI メタデータ | 1.2.7 Windows Codexでインストール済み29/29スキルを検出・有効化、解析エラーなし。モデル処理は未実行 |
| Claude Code | ドキュメントに記載された場所へスキルディレクトリ全体を配置 | 1.2.0: ネイティブ CLI と公式 SDK で 24/24 を検出。モデル実行の成功は未検証 |
| Gemini CLI | ドキュメントに記載された場所へスキルディレクトリ全体を配置 | ドキュメント上の対応のみ。エンドツーエンド利用は未検証 |
| GitHub Copilot | 対応クライアントでスキルディレクトリ全体を使用 | ドキュメント上の対応のみ。各クライアントは未検証 |
| その他 | 対応していれば `SKILL.md` と相対参照を読み込む | 未確認のネイティブ互換性を一律に保証しない |

[役割の説明](docs/role-briefs.md)（簡体字中国語）は、任意のマルチエージェント連携における責務を示すもので、自動登録される設定ではありません。実際の権限、ツール、信頼設定、モデルの能力は実行環境に従います。

## 検証

```sh
python scripts/build_catalog.py
python scripts/validate.py
```

検証ツールは、宣言、生成内容の同期、正確なリソース集合、ローカルリンク、Python 構文、ステージ順序、配布物の一部の健全性ルールを確認します。エージェントの判断が正しいことや、フレームワークに脆弱性がないことを証明するものではありません。

Windows/Linux CI はソース、オフラインツール、再現可能なパッケージを検証します。1.2.7 の Windows Codex はインストール済み29スキルを解析エラーなしで検出・有効化し、154ファイルがソースと一致しました。過去の Codex/Claude 隔離検出と42項目のブラウザー確認は当時の範囲を維持します。自動起動精度、モデル遵守率、本番環境の検証ではありません。[検証記録](docs/validation.md)と[検出証拠](docs/agent-loading.md)を参照してください。

## 使用例と自動リリース

[使用例](examples/README.md)には本リポジトリで実行した事例と、小変更、既存バックエンド、新規フロントエンド・バックエンド向けのプロンプトがあります。`python scripts/run_examples.py` で TEMP 内にオフライン検証を再現できます。

一致するバージョンタグを push すると、検証済み ZIP と SHA-256 ファイルを公開します。[公開手順](docs/github-publishing.md)を参照してください。[ネイティブ検出の再実行](docs/agent-loading.md)は隔離ディレクトリを使い、既定のスキルを変更しません。任意のネイティブ検証には実際のクライアント、Claude には Node と公式 Agent SDK も必要です。それ以外の Python ツールは標準ライブラリのみを使います。

## 言語

プロジェクト概要は英語、簡体字中国語、繁体字中国語、日本語、韓国語、ロシア語で提供しています。GitHub の貢献用ドキュメントとテンプレートは英語です。英語または中国語での貢献を歓迎します。このリリースでは、スキル本文、詳細ガイド、ツールのメッセージは簡体字中国語のままであり、スキル全体の 6 言語版ではありません。エージェントには希望する言語での回答を指示できます。

## 貢献とリリース

不足点を示す具体的なタスクから始めてください。重複するルールを追加するよりも、その責務を持つスキルの改善を優先します。[貢献ガイド](CONTRIBUTING.md)、[セキュリティ方針](SECURITY.md)、[GitHub 公開ガイド](docs/github-publishing.md)（英語）を参照してください。

エクスポートと検証のツールは、リポジトリの公開やリモートアカウントの操作を行いません。非公開の報告先や導入実績は設定・主張していません。

<a id="sources"></a>

## 参考資料と謝辞

以下の14のオープンソースプロジェクトの作者・メンテナーの皆さまに感謝します。各プロジェクトの設計や開発手法の一部を参考に、本コレクションのスキルとガイドを独自に作成しました。固定コミットから取得した73ファイルが対象で、リポジトリ全体の監査ではありません。主な採用点を下表に示します。範囲、採用しなかった規則、ライセンスは[出典の検討](docs/provenance.md)、[固定した出典](provenance/upstreams.json)、[第三者に関する通知](THIRD_PARTY_NOTICES.md)を参照してください。

| プロジェクト | 採用した考え方 |
| --- | --- |
| [anthropics/skills](https://github.com/anthropics/skills) | 短いスキル入口と参照資料の段階的な読み込み |
| [openai/skills](https://github.com/openai/skills) | 過去のスキル構成、原本と生成物の分離、スクリプトの実証 |
| [obra/superpowers](https://github.com/obra/superpowers) | 証拠に基づくデバッグ、明確な仮説、範囲を絞ったレビュー |
| [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | フレームワークに応じた起動と影響度による性能課題の優先順位 |
| [github/awesome-copilot](https://github.com/github/awesome-copilot) | スキル・指示・エージェント役割の区別と単一責務 |
| [trailofbits/skills](https://github.com/trailofbits/skills) | 実際の呼び出し経路を追い、反例でセキュリティの結論を検証 |
| [supabase/agent-skills](https://github.com/supabase/agent-skills) | PostgreSQLの実行計画、索引、接続予算、トランザクションとロックの境界 |
| [microsoft/playwright-cli](https://github.com/microsoft/playwright-cli) | 実画面のロケーター、セッション分離、操作とアサーションの証拠の区別 |
| [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | 画面要件から導く書体、コンポーネント、プラットフォーム選択 |
| [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | 既存デザインの継承と局所的な変更・共有規約の区別 |
| [wshobson/agents](https://github.com/wshobson/agents) | デザイントークン、再利用部品、プラットフォーム別の操作と動き |
| [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | 要件の準備状況、タスク引き継ぎ、品質基準、移行、性能、可観測性 |
| [magnus919/agent-skills](https://github.com/magnus919/agent-skills) | 移行の互換性、データ照合、現実的な復旧の限界 |
| [rmyndharis/antigravity-skills](https://github.com/rmyndharis/antigravity-skills) | 連携関係の整理、業務単位の段階移行、実行責任の明確化 |

## ライセンス

独自の内容は [MIT](LICENSE) で公開します。上流のスキル本文、コード、テンプレート、素材、データベースは再配布していません。上流のライセンスは別に適用されます。Trail of Bitsの参照元はCC-BY-SA-4.0であり、その本文をMITの内容に翻案していません。範囲の詳細は通知を参照してください。
