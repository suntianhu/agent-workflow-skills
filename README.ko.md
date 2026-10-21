# Agent Workflow Skills

코딩 에이전트를 위한 조합 가능한 개발 워크플로입니다. 프로젝트별 선행 조건을 명확히 하고 실제 근거에 따라 완료 여부를 판단합니다.

[English](README.md) · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Русский](README.ru.md)

![License: MIT](https://img.shields.io/badge/license-MIT-blue)
![Skills: 29](https://img.shields.io/badge/skills-29-2563eb)
![Workflows: 9](https://img.shields.io/badge/workflows-9-0f766e)

**버전 1.2.9** · Agent Skills 디렉터리 형식 · Python 3.10+ 도구 · 실행 시 Python 표준 라이브러리만 필요

**작업에 맞는 스킬을 선택하고 기존 규칙을 이어갑니다.** 스킬 29개와 조건부 구성 9개로 기존·신규 프로젝트, [마이그레이션](docs/project-migration.md), [성능과 관측성](docs/adoption-integration.md)을 다룹니다. 유효한 결정을 재사용하고 필요할 때 분담하며 실제 근거로 결과를 설명합니다.

[GitHub 참고 출처](#sources) · [사용 예시](examples/README.md) · [변경 이력](CHANGELOG.md)

## 이 컬렉션의 특징

- **간결한 진입 문서:** 반복 설명을 줄이고 주요 기능 하나를 선택한 뒤 부족한 부분이 있을 때만 관련 자료를 읽습니다. 유효한 결정과 변경되지 않은 기존 자료는 다시 활용합니다.
- **작업별 실행 조건:** 9개 구성은 조건에 맞는 단계만 선택합니다. 명확한 국소 수정에 광범위한 조사, 모델 비교, 다중 에이전트를 자동으로 시작하지 않으며 시간 추정에도 별도 실행 조건을 적용합니다.
- **변경 범위 유지:** 각 변경을 요청 항목이나 근거가 있는 필수 연동에 연결하고, 다른 기능의 기존 동작을 유지합니다. 새로 발견한 범위 밖 문제는 기록하고 임의로 수정하지 않습니다.
- **기존 프로젝트 규칙 계승:** 전체 코드 기준 상태와 이후 변경 사항을 확인하고 기존 규칙 디렉터리와 원본을 계속 사용합니다. 새로운 업무의 페이지도 프로젝트 글꼴, 테마, 컴포넌트와 상호작용 방식을 이어갑니다.
- **위험에 맞는 검증:** 검증 범위, TDD 순서, 산출물 보관 방침을 각각 결정합니다. 작은 수정에 TDD를 자동으로 요구하지 않으며 사용자의 기존 테스트를 보존합니다.
- **필요한 자원만 사용:** 추가 스킬, 모델, 에이전트는 구체적인 이점과 실행 환경의 실제 기능 및 권한이 있을 때 사용합니다.

이 프로젝트는 지침과 로컬 도구의 모음입니다. 워크플로 JSON은 조건과 순서를 설명하며 실행 환경에 내장된 워크플로 엔진이 아닙니다.

## 빠른 시작

1. 아래에서 워크플로를 선택하거나 [29개 스킬의 책임 범위](docs/skill-map.md)(중국어 간체)를 확인합니다.
2. 에이전트에게 필요한 `skills/<name>/SKILL.md`와 참조 자료를 읽도록 요청합니다. 현재 작업에 필요한 기능만 불러옵니다.
3. 이 저장소 바깥의 새 디렉터리에 필요한 파일을 모두 포함한 구성을 내보내려면:

```sh
python scripts/export_bundle.py --bundle existing-frontend --out ../workflow-export
```

`--include-optional`을 추가하면 에이전트 협업 스킬도 포함됩니다. 내보내기는 스킬을 설치하거나 기본 설정을 바꾸지 않습니다. 기존 대상, 리디렉션된 경로, 오래된 생성 파일, 저장소 내부 대상, 네이티브 설치 위치는 거부됩니다.

네이티브 스킬 검색을 사용하려면 설치 의도가 있을 때에만 실행 환경의 최신 문서에 따라 개별 스킬 디렉터리 전체를 복사하세요. [에이전트 호환성](docs/agent-compatibility.md)(영어)을 참고하세요.

### 선택적 Skills CLI

Node.js 22.20+에서 공식 CLI로 이 저장소의 스킬 목록을 확인할 수 있습니다.

```sh
npx skills@1.7.4 add suntianhu/agent-workflow-skills --list
```

프로젝트 단위 설치, 텔레메트리 비활성화 및 skills.sh 분류는 [설치와 개인정보 안내](docs/skills-sh.md)(영어/중국어 간체)를 참고하세요. CLI 검색과 에이전트 실행 증거는 별도로 구분합니다.

## 9가지 워크플로

| 워크플로 | 대상 작업 | 핵심 선행 조건 |
| --- | --- | --- |
| [existing-frontend](bundles/existing-frontend.json) | 기존 프로젝트의 프런트엔드 개발 | 전체 코드 검토 → 내부 규칙 → 프런트엔드 설계 및 구현 |
| [existing-backend](bundles/existing-backend.json) | 기존 프로젝트의 백엔드 개발 | 전체 코드 검토 → 내부 규칙 → 백엔드 구현 |
| [new-frontend](bundles/new-frontend.json) | 처음부터 시작하는 프런트엔드 프로젝트 | 언어/플랫폼 → 후보 조사 → 사용자 선택 → 참고 규칙 → 내부 규칙 |
| [new-backend](bundles/new-backend.json) | 처음부터 시작하는 백엔드 프로젝트 | 언어/배포 요구사항 → 사용자의 스택 선택 → 참고 규칙 → 내부 규칙 |
| [fullstack](bundles/fullstack.json) | 프런트엔드와 백엔드를 아우르는 개발 | 기존/신규 분기 선택, 각 영역의 규칙 분리, API 계약 공유 |
| [project-migration](bundles/project-migration.json) | 프레임워크·프런트엔드·백엔드·DB 교체 | 보존 목록 → 대상과 공존 → 업무별 구현 → 검증과 복구 |
| [small-change](bundles/small-change.json) | 범위가 작고 영향이 낮은 수정 | 절차를 간소화하되 해당 기존/신규 프로젝트의 선행 조건 유지 |
| [debug-and-fix](bundles/debug-and-fix.json) | 재현 가능한 결함이나 연동 이상 | 재현 실행 전에 검증 방침 선택, 수정 전에 코드와 규칙의 선행 조건 충족 |
| [release](bundles/release.json) | 요청된 통합, 패키징 또는 릴리스 | 호환성·복구·검증 근거 준비, 코드 수정은 개발 흐름으로 전달 |

`skills`는 내보내기에 필요한 기능을 빠짐없이 포함한 목록이지, 모든 스킬을 실행하라는 지시가 아닙니다. 각 단계는 조건에 따라 선택됩니다. TDD를 선택하면 해당 루프가 구현을 담당하며 별도의 구현 단계는 건너뜁니다. 자세한 [구성 규칙](docs/bundles.md)은 현재 중국어 간체로 제공됩니다.

## 기능 구성

| 분야 | 스킬 |
| --- | --- |
| 작업과 자원 판단 | `aw-project-triage`, `aw-skill-selection`, `aw-model-routing`, `aw-effort-estimation` |
| 코드 이해와 아키텍처 | `aw-repository-audit`, `aw-project-standards`, `aw-framework-selection`, `aw-github-reference`, `aw-project-migration` |
| 요구사항과 구현 | `aw-requirements-design`, `aw-design-reference`, `aw-design-standards`, `aw-ui-design`, `aw-frontend-implementation`, `aw-backend-implementation` |
| 성능과 관측성 | `aw-performance-optimization`, `aw-observability` |
| 계약과 보안 경계 | `aw-api-contracts`, `aw-security-boundaries` |
| 검증과 문제 진단 | `aw-test-strategy`, `aw-scoped-tdd`, `aw-evidence-debugging`, `aw-adversarial-review`, `aw-evidence-verification` |
| 전달과 유지 관리 | `aw-delivery-cleanup`, `aw-release-readiness`, `aw-agent-coordination`, `aw-skill-authoring`, `aw-open-source-readiness` |

각 스킬에는 고유한 지침, 필요한 참조 자료와 리소스, 라이선스가 포함됩니다. catalog와 원본 가이드를 유지 관리의 기준으로 삼고 생성된 스킬 사본을 동기화해야 합니다.

## 에이전트 호환성

| 실행 환경 | 패키징 | 실제 확인 범위 |
| --- | --- | --- |
| Codex | Agent Skills 디렉터리와 선택적 `agents/openai.yaml` UI 메타데이터 | 1.2.7 Windows Codex에서 설치된 29/29 스킬을 검색·활성화, 구문 오류 없음; 모델 작업 미실행 |
| Claude Code | 문서에 명시된 위치에 전체 스킬 디렉터리 배치 | 1.2.0: 네이티브 CLI와 공식 SDK에서 24/24 검색 확인. 성공한 모델 실행은 미검증 |
| Gemini CLI | 문서에 명시된 위치에 전체 스킬 디렉터리 배치 | 문서 기준으로만 대응. 종단 간 사용은 미검증 |
| GitHub Copilot | 지원 클라이언트에서 전체 스킬 디렉터리 사용 | 문서 기준으로만 대응. 개별 클라이언트는 미검증 |
| 기타 에이전트 | 지원하는 경우 `SKILL.md`와 상대 참조 읽기 | 확인하지 않은 네이티브 호환성을 일괄 보장하지 않음 |

[역할 설명](docs/role-briefs.md)(중국어 간체)은 선택적 다중 에이전트 협업의 책임을 설명하며 자동 등록되는 설정이 아닙니다. 실제 권한, 도구, 신뢰 설정과 모델 기능은 실행 환경을 따릅니다.

## 검증

```sh
python scripts/build_catalog.py
python scripts/validate.py
```

검증 도구는 선언, 생성 내용의 동기화, 정확한 리소스 집합, 로컬 링크, Python 문법, 구성 단계 순서, 일부 배포물 점검 규칙을 확인합니다. 에이전트의 판단이 옳거나 프레임워크에 취약점이 없음을 증명하지는 않습니다.

Windows/Linux CI는 소스, 오프라인 도구와 재현 가능한 패키징을 검사합니다. 1.2.7의 Windows Codex는 설치된 스킬 29개를 구문 오류 없이 검색·활성화했고 설치 파일 154개가 소스와 일치했습니다. 과거 Codex/Claude 격리 검색과 브라우저 검사 42개의 범위는 유지합니다. 자동 실행 정확도, 모델 준수율이나 운영 환경 검증은 아닙니다. [검증 기록](docs/validation.md)과 [네이티브 증거](docs/agent-loading.md)를 참고하세요.

## 사용 예제와 자동 릴리스

[전체 예제](examples/README.md)는 이 저장소에서 실행한 사례와 소규모 변경, 기존 백엔드, 새 프런트엔드·백엔드용 프롬프트를 제공합니다. `python scripts/run_examples.py`로 TEMP에서 오프라인 검사를 재현할 수 있습니다.

일치하는 버전 태그를 push하면 검증된 ZIP과 SHA-256 파일이 게시됩니다. [릴리스 단계](docs/github-publishing.md)를 참조하세요. [네이티브 검색 재실행](docs/agent-loading.md)은 격리 디렉터리를 사용하며 기본 스킬을 변경하지 않습니다. 선택적 네이티브 검사에는 실제 클라이언트가, Claude에는 Node와 공식 Agent SDK도 필요합니다. 나머지 Python 도구는 표준 라이브러리만 사용합니다.

## 언어

프로젝트 개요는 영어, 중국어 간체, 중국어 번체, 일본어, 한국어, 러시아어로 제공합니다. GitHub 기여 문서와 템플릿은 영어로 작성되어 있으며 영어 또는 중국어 기여를 환영합니다. 이번 릴리스의 스킬 본문, 상세 가이드, 도구 메시지는 중국어 간체로 유지되며 스킬 전체를 6개 언어로 번역한 것은 아닙니다. 에이전트에게 원하는 언어로 응답하도록 요청할 수 있습니다.

## 기여와 릴리스

구체적인 작업으로 현재의 부족한 점을 설명해 주세요. 겹치는 규칙을 추가하기보다 해당 책임을 맡은 스킬을 개선하는 것을 우선합니다. [기여 가이드](CONTRIBUTING.md), [보안 정책](SECURITY.md), [GitHub 게시 가이드](docs/github-publishing.md)(영어)를 참고하세요.

내보내기와 검증 도구는 저장소를 게시하거나 원격 계정을 조작하지 않습니다. 비공개 신고 주소나 도입 실적을 미리 설정하거나 주장하지 않습니다.

<a id="sources"></a>

## GitHub 참고 프로젝트와 감사의 말

아래 14개 GitHub 프로젝트의 일부를 연구하고 적용 가능한 원칙을 독립적으로 작성한 스킬과 가이드로 정리했습니다. 고정 커밋에서 가져온 파일 73개가 대상이며 저장소 전체를 감사한 것은 아닙니다. 주요 채택 내용은 아래 표에, 범위·미채택 규칙·라이선스는 [출처 검토](docs/provenance.md), [고정 출처](provenance/upstreams.json), [제3자 고지](THIRD_PARTY_NOTICES.md)에 기록되어 있습니다.

| 프로젝트 | 채택한 아이디어 |
| --- | --- |
| [anthropics/skills](https://github.com/anthropics/skills) | 짧은 스킬 진입 문서와 참조 자료의 점진적 로딩 |
| [openai/skills](https://github.com/openai/skills) | 과거 스킬 패키징, 원본과 생성물 분리, 스크립트 검증 |
| [obra/superpowers](https://github.com/obra/superpowers) | 근거 중심 디버깅, 명시적 가설, 범위를 제한한 리뷰 |
| [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | 프레임워크별 실행 조건과 영향에 따른 성능 우선순위 |
| [github/awesome-copilot](https://github.com/github/awesome-copilot) | 스킬·지침·에이전트 역할 구분과 집중된 책임 |
| [trailofbits/skills](https://github.com/trailofbits/skills) | 실제 호출 경로 추적과 반례를 통한 보안 결론 검증 |
| [supabase/agent-skills](https://github.com/supabase/agent-skills) | PostgreSQL 실행 계획, 인덱스, 연결 예산과 트랜잭션·잠금 경계 |
| [microsoft/playwright-cli](https://github.com/microsoft/playwright-cli) | 실제 로케이터 확인, 브라우저 세션 격리, 동작과 단언 근거 구분 |
| [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | 인터페이스 요구사항에서 글꼴·컴포넌트·플랫폼 선택 도출 |
| [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | 기존 디자인 계승과 국소 변경·공통 규칙 구분 |
| [wshobson/agents](https://github.com/wshobson/agents) | 디자인 토큰, 재사용 컴포넌트, 플랫폼별 상호작용과 모션 |
| [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | 요구사항 준비도, 작업 인계, 품질 기준, 마이그레이션, 성능과 관측성 |
| [magnus919/agent-skills](https://github.com/magnus919/agent-skills) | 마이그레이션 호환성, 데이터 대조와 실제 복구 한계 |
| [rmyndharis/antigravity-skills](https://github.com/rmyndharis/antigravity-skills) | 연동 관계 정리, 업무 단위 단계별 이전과 실행 책임 |

## 라이선스

독자적으로 작성한 내용에는 [MIT](LICENSE)가 적용됩니다. 상위 프로젝트의 스킬 본문, 코드, 템플릿, 자산과 데이터베이스를 재배포하지 않습니다. 각 출처의 라이선스는 별개이며, Trail of Bits 출처는 CC-BY-SA-4.0이고 그 본문을 MIT 내용으로 각색하지 않았습니다. 세부 범위는 제3자 고지를 참고하세요.
