# Project Context

這份文件保存本組專案脈絡、教師設定的預設值與學生已確認的偏好。除明列的預設值外，未填項目不代表已確認；AI 應詢問當前任務需要的資訊。

## Repository Context

三人共用一個 GitHub repo，每人各自 clone。由一人先建立 repo、放入完整工作包並 commit／push，另外兩人取得權限後再 clone 同一個 repo。AI 可唯讀核對並提供說明；stage、commit、push、pull／sync 由學生親自操作。此空白範本不代表已完成 repo 設定，不代填學生的 URL 或提交狀態。

| Field | Details |
| --- | --- |
| Remote repository | 待學生提供或唯讀核對，不記錄帳密或 token |
| Target branch | 待學生確認或唯讀核對 |
| Setup status | 待確認學生的 repo、remote 與開啟的專案根目錄 |
| Last push verification | 待核對；記錄核對對象、分支、commit、依據及時間 |

## Research Question

- 待本組先用自己的話填寫：關心的現象或初步疑問，以及為什麼想研究。不必已有正式題目；AI 依本組想法協助釐清，教師範例不代表本組構想。

## Team

**三人一組，共用一個 repo。** 請填本組已確認的姓名與實際工作；人數規定不代表名單已確認。AI 沿用已有資訊，只補問當前任務缺少的姓名、工作與目前對話者。分工由學生決定，未確認處保留待確認；實際名單與人數規定不同時先保留事實並釐清，不補造或刪除成員。

AI 只整理學生提供或明確確認的姓名與工作，不自行指派 PM／DE／DA，也不從 Git 作者、電腦帳號、檔名、範本示例或檔案提供者推定作者或責任；保留有依據的既有作者，不自動改成本次提供檔案的學生。等待回答時可先進行不依賴歸屬的檢查或討論。保留下列既有欄位，按已確認名單一人一列；尚無名單時保持空表，不先填入假成員。`Role` 記錄學生提供的角色與實際工作，確認姓名與工作不需額外要求學號或 GitHub 帳號。

目前對話的學生：待確認（依本次對話更新，不自動沿用上一次的對話者）。

| Name | Student ID | GitHub Account | Role |
| 蔡尚恩 | XXXXXX | 123@gmail.com | PM |

## Student Preferences

- Tool / artifact format: 尚未選定；開始資料文件或分析工作時再確認 Python／Jupyter 或 R／R Markdown。只寫 Markdown proposal 不需先選分析工具；明確選用 Stata 時依專用格式。
- Report language: 繁體中文（台灣用語，zh-TW；教師預設，學生明確指定其他語言時優先沿用）
- Other explicit preferences: 尚未提供

## AI Agent Context

依 `AGENTS.md` 的 `Model and Agent Selection`，記錄每位已確認學生目前使用的 AI 工具、模型與選用入口。同組成員可以使用不同模型；不要將前一位學生或教師的設定當作全組預設。姓名確認後按學生一人一列，換工具或模型時更新該列；尚無學生資訊時保持空表。

`Model` 保留學生提供或目前執行環境可靠顯示的名稱；只知道工具或模型家族時註明「完整型號未確認」，不自行猜版本。`Source` 記錄「學生本次提供」或「目前執行環境」等實際依據。先確認選用入口即可，不為填滿模型版本而打斷工作。

| Student | AI tool / client | Model | Agent entrypoint | Source |
| --- | --- | --- | --- | --- |

## Data and Current Focus

| Field | Details |
| --- | --- |
| Data sources / documentation | 待填 |
| Unit of observation | 待填 |
| Current task / target variables | 待填 |
| Assignment constraints | 鼓勵先自行寫作再請 AI 回饋；proposal 保留六節；三人共用一個 repo，學生自行 commit／push 文件與程式；CSV 與其他 raw／processed 資料檔留本機 |

## Data Artifacts

資料建立或核對後，由 AI 依 [資料銜接規則](FINDING-RULES.md#資料銜接與檔案驗證) 填入實際紀錄，一個資料檔一列。尚無資料時保持空表，不把範例當成已完成結果。

| Dataset | Role | Data file | Documentation | Processing notebook | Verification | SHA-256 |
| --- | --- | --- | --- | --- | --- | --- |

路徑與連結相對於本專案根目錄。Role 記錄 raw／analysis／train／test 或已確認用途；Verification 說明實際執行的檢查、日期與限制，未完成時明列 pending／failed。SHA-256 由實際檔案計算。外部整理檔沒有產生程式可記 not available；原始來源可記 not applicable (source)。

資料檔留在本機，不 commit／push；本表仍登記實際本機檔案。資料說明須記錄來源、取得方法、放置路徑與已核對版本，讓各組員自行取得相同輸入。本機資料連結不是 GitHub 下載入口。

## Key Contributions

**課程原則：所有 contribution 都必須由學生在 VS Code 自行 commit 並 push。** 各成員隨成果更新下表，每項貢獻一列，記錄誰、做了什麼，以及實際包含該成果的 commit 連結或 SHA。AI 可整理待提交紀錄，在學生操作後唯讀核對再回填。程式、資料處理、文件、提案及專案紀錄的修改都適用；資料工作以程式、資料說明與驗證紀錄留存，不提交資料檔本身；外部成果須有已 commit 的說明或連結紀錄可追溯。

尚未 commit 的工作標示「待提交」，已有 reference 但尚未核對者標示「待核對」；兩者均不視為完成貢獻紀錄。檔案連結不能取代 commit reference。不要以 commit 次數或程式行數替代成果評估。

已核對的本地 commit 不等於已 push；在 reference 後註明「推送待核對」或經證實的「待 push」，遠端目標分支包含該 commit 的證據核對完成後才記「已推送並核對」。學生自行回報但未核對時註明來源。貢獻表回填後，由學生在下一次 commit／push 納入；reference 指向先前的成果 commit，不要求填該表更新自身的未來 hash。

姓名與貢獻歸屬須由學生提供或確認；資訊缺少時先詢問，未回答前保留待填，不以 commit 作者直接認定實際負責人。commit 用來核對成果紀錄，不取代學生確認的分工。

| Name | Contribution | Commit reference |
| --- | --- | --- |
