# Contributing Guidelines

Thank you for your interest in contributing to Radix Off-Ledger Authentication (ROLA)!

# Clarification on GitHub Issue Usage and Feature Requests

We want to clarify that Github Issues are primarily meant for the purpose of reporting problems or concerns, rather than functioning as an open bug tracker. This means that reported issues on Github may be closed and reported in our internal tracking system or added to our roadmap.

If you are thinking of requesting a feature, make sure it’s not already part of our upcoming features outlined in the [Roadmap](https://docs.radixdlt.com/docs/roadmap). If you have a feature suggestion, we kindly ask that you share it through [Discord](http://discord.gg/radixdlt) or [Telegram](https://t.me/RadixDevelopers).

Our primary focus is on the priorities outlined in our [Roadmap](https://docs.radixdlt.com/docs/roadmap). We appreciate your understanding that addressing reported issues may not always align with our immediate goals.

# Table of Contents

- [Contributing Guidelines](#contributing-guidelines)
- [Clarification on GitHub Issue Usage and Feature Requests](#clarification-on-github-issue-usage-and-feature-requests)
- [Table of Contents](#table-of-contents)
- [Code of Conduct](#code-of-conduct)
- [Reporting Issues](#reporting-issues)
- [Contributing Code](#contributing-code)
  - [Setting Up Your Development Environment](#setting-up-your-development-environment)
  - [Making Changes](#making-changes)
    - [Commits](#commits)
    - [Commit types](#commit-types)
  - [Submitting a Pull Request](#submitting-a-pull-request)
  - [Review Process](#review-process)
- [License](#license)

# Code of Conduct

This project adheres to the Contributor Covenant [code of conduct](CODE_OF_CONDUCT.md).
By participating, you are expected to uphold this code.
Please report unacceptable behavior to [hello@radixdlt.com](mailto:hello@radixdlt.com).

# Reporting Issues

Ensure the bug was not already reported by searching on GitHub under [Issues](https://github.com/radixdlt/rola/issues).

If you encounter a bug or have a problem with the project, please open a [Github Issue](https://github.com/radixdlt/rola/issues). Make sure to provide as much detail as possible, including:

- A clear and descriptive title.
- Steps to reproduce the issue.
- Expected behavior and actual behavior.
- Your operating system, browser, or other relevant information.
- If possible, include screenshots or code snippets that illustrate the issue.

# Contributing Code

Submitting a Pull Request does not guarantee the acceptance of your proposed changes. We strongly advise initiating a discussion with the team via Discord, Telegram, or Github Issues (for bugs) prior to commencing work on a PR.

## Setting Up Your Development Environment

1. Fork the repository to your GitHub account.
2. Clone your forked repository to your local machine.
3. Create a new branch for your changes.

## Making Changes

1. Write clear, concise, and well-documented code.
2. Commit your changes with a descriptive commit message.


### Commits

Please follow the Conventional Commits specification. It is a lightweight convention on top of commit message that provides an easy set of rules for creating an explicit commit history; which makes it easier to write automated tools on top of. This convention dovetails with SemVer, by describing the features, fixes, and breaking changes made in commit messages.

The commit message should be structured as follows:

```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

1. The commit contains the following structural elements, to communicate intent to the consumers of your library:

1. fix: a commit of the type fix patches a bug in your codebase (this correlates with PATCH in Semantic Versioning).

1. feat: a commit of the type feat introduces a new feature to the codebase (this correlates with MINOR in Semantic Versioning).

1. BREAKING CHANGE: a commit that has a footer BREAKING CHANGE:, or appends a ! after the type/scope, introduces a breaking API change (correlating with MAJOR in Semantic Versioning). A BREAKING CHANGE can be part of commits of any type.

1. types other than fix: and feat: are allowed, for example @commitlint/config-conventional (based on the Angular convention) recommends build:, chore:, ci:, docs:, style:, refactor:, perf:, test:, and others.
   footers other than BREAKING CHANGE: <description> may be provided and follow a convention similar to git trailer format.

1. Additional types are not mandated by the Conventional Commits specification, and have no implicit effect in Semantic Versioning (unless they include a BREAKING CHANGE). A scope may be provided to a commit’s type, to provide additional contextual information and is contained within parenthesis, e.g., feat(parser): add ability to parse arrays.

### Commit types

| Type       | Title                    | Description                                                                                                 |
| ---------- | ------------------------ | ----------------------------------------------------------------------------------------------------------- |
| `feat`     | Features                 | A new feature                                                                                               |
| `fix`      | Bug Fixes                | A bug Fix                                                                                                   |
| `docs`     | Documentation            | Documentation only changes                                                                                  |
| `style`    | Styles                   | Changes that do not affect the meaning of the code (white-space, formatting, missing semi-colons, etc)      |
| `refactor` | Code Refactoring         | A code change that neither fixes a bug nor adds a feature                                                   |
| `perf`     | Performance Improvements | A code change that improves performance                                                                     |
| `test`     | Tests                    | Adding missing tests or correcting existing tests                                                           |
| `build`    | Builds                   | Changes that affect the build system or external dependencies (example scopes: gulp, broccoli, npm)         |
| `ci`       | Continuous Integrations  | Changes to our CI configuration files and scripts (example scopes: Travis, Circle, BrowserStack, SauceLabs) |
| `chore`    | Chores                   | Other changes that don't modify src or test files                                                           |
| `revert`   | Reverts                  | Reverts a previous commit                                                                                   |

[Read more](https://www.conventionalcommits.org/en/v1.0.0/#summary).


## Submitting a Pull Request

1. Push your changes to your forked repository:
2. Open a pull request against the `develop` branch of the original repository.
3. Provide a clear and informative title and description for your pull request.
4. Be prepared to address any feedback or questions during the review process.

## Review Process

Pull requests will be reviewed by project maintainers. Reviewers may provide feedback, request changes, or approve the pull request. We appreciate your patience during this process, and we aim to be responsive and constructive in our feedback.

# License

By contributing to the Radix Off-Ledger Authentication, you agree that your contributions will be licensed under the following licenses:

* The Radix Off-Ledger Authentication (ROLA) binaries are licensed under the [Radix Software EULA](http://www.radixdlt.com/terms/genericEULA).
* The Radix Off-Ledger Authentication (ROLA) code and examples are released under [Apache 2.0 license](LICENSE).

```
Copyright 2023 Radix Publishing Ltd

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License.

You may obtain a copy of the License at: http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
```

See the License for the specific language governing permissions and limitations under the License.

All code in the [examples](./examples/) folder in this repository is licensed under the modified MIT license described in [LICENSE](/LICENSE).

```
Copyright 2023 Radix Publishing Ltd

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software for non-production informational and educational purposes without
restriction, including without limitation the rights to use, copy, modify,
merge, publish, distribute, sublicense, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

This notice shall be included in all copies or substantial portions of the
Software.

THE SOFTWARE HAS BEEN CREATED AND IS PROVIDED FOR NON-PRODUCTION, INFORMATIONAL
AND EDUCATIONAL PURPOSES ONLY.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE, ERROR-FREE PERFORMANCE AND NONINFRINGEMENT. IN NO
EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES,
COSTS OR OTHER LIABILITY OF ANY NATURE WHATSOEVER, WHETHER IN AN ACTION OF
CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE, MISUSE OR OTHER DEALINGS IN THE SOFTWARE. THE AUTHORS SHALL
OWE NO DUTY OF CARE OR FIDUCIARY DUTIES TO USERS OF THE SOFTWARE.
```
