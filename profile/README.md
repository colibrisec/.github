<p align="center">
  <a href="https://github.com/colibrisec">
    <img src="https://avatars.githubusercontent.com/u/121567324?v=4" width="150" alt="ColibriSec logo" />
  </a>
</p>

<h1 align="center">COLIBRISEC</h1>

<p align="center">
  <strong>Open-source security engineering for the systems that matter.</strong>
</p>

<p align="center">
  <a href="https://git.io/typing-svg">
    <img src="https://readme-typing-svg.demolab.com/?lines=SECURE+BY+DESIGN.;SCAN.+TRIAGE.+REMEDIATE.;OPEN-SOURCE+DEFENSE+ENGINEERING.&amp;font=Fira+Code&amp;center=true&amp;vCenter=true&amp;width=760&amp;height=58&amp;duration=3000&amp;pause=700&amp;color=FF3D21&amp;background=0B0B1000" alt="ColibriSec mission" />
  </a>
</p>

<p align="center">
  <a href="https://github.com/colibrisec/ojo"><img src="https://img.shields.io/badge/OJO-Security%20Scanner-FF3D21?style=for-the-badge&amp;logo=go&amp;logoColor=FFD447" alt="OJO security scanner" /></a>
  <a href="https://git.colibrisec.org/ColibriSec/balam"><img src="https://img.shields.io/badge/BALAM-Vulnerability%20Management-FF7A35?style=for-the-badge&amp;logo=shield&amp;logoColor=FFD447" alt="Balam vulnerability management" /></a>
  <a href="https://github.com/colibrisec/ojo-action"><img src="https://img.shields.io/badge/OJO--ACTION-CI%20Security%20Scanning-FFD447?style=for-the-badge&amp;logo=githubactions&amp;logoColor=0B0B10" alt="OJO Action" /></a>
</p>

---

```text
┌─[ colibrisec@github ]─[ ~/security-engineering ]
└──╼ $ build --secure --observable --open-source

[✓] Scan code, dependencies, containers, and infrastructure
[✓] Manage findings with tenant-aware vulnerability workflows
[✓] Automate verified remediation from issue to pull request
[✓] Build hardened environments for authorized research and assessment
```

## Signal, not noise

ColibriSec builds practical security tooling for teams that want clear findings, defensible workflows, and automation that keeps humans in control.

| System | Mission | Stack |
| --- | --- | --- |
| [**OJO**](https://github.com/colibrisec/ojo) | Scan dependencies, secrets, misconfigurations, and code | Go · CLI · SBOM · Containers |
| [**Balam**](https://git.colibrisec.org/ColibriSec/balam) | Manage vulnerabilities from intake through remediation | Go · React · TypeScript · PostgreSQL |
| [**Secretly**](https://github.com/colibrisec/secretly) | Identify and remove secrets from Slack workflows | Security automation · Helm |
| [**ojo-action**](https://github.com/colibrisec/ojo-action) | Run OJO security scanning directly in GitHub Actions | GitHub Actions · OJO · CI/CD |

## Operational principles

<p align="center">
  <code>AUTHORIZED USE</code> · <code>DEFENSE IN DEPTH</code> · <code>HUMAN REVIEW</code> · <code>REPRODUCIBLE BUILDS</code> · <code>OPEN SOURCE</code>
</p>

- **Authorized security work only.** Our tools support defensive security, research, and assessment within documented scope.
- **Secure defaults.** Isolation, least privilege, auditability, and strong identity controls belong in the baseline.
- **Automation with guardrails.** Detection and remediation should improve signal while preserving review and accountability.

## Featured systems

<table>
  <tr>
    <td width="50%">
      <h3><a href="https://github.com/colibrisec/ojo">OJO</a></h3>
      <p>Security scanner for dependencies, secrets, misconfiguration, and code.</p>
      <p><a href="https://github.com/colibrisec/ojo/actions"><img src="https://github.com/colibrisec/ojo/actions/workflows/ci.yml/badge.svg" alt="OJO CI status" /></a> <a href="https://github.com/colibrisec/ojo/releases"><img src="https://img.shields.io/github/v/release/colibrisec/ojo?color=FFD447&amp;label=release" alt="OJO latest release" /></a></p>
    </td>
    <td width="50%">
      <h3><a href="https://git.colibrisec.org/ColibriSec/balam">Balam</a></h3>
      <p>Self-hosted vulnerability management with a modern UI and API.</p>
      <p><a href="https://git.colibrisec.org/ColibriSec/balam/actions/workflows/test.yml"><img src="https://git.colibrisec.org/ColibriSec/balam/actions/workflows/test.yml/badge.svg?branch=main" alt="Balam CI status" /></a> <a href="https://git.colibrisec.org/ColibriSec/balam/tags"><img src="https://img.shields.io/static/v1?label=latest%20tag&amp;message=v0.0.22&amp;color=FFD447" alt="Balam latest tag" /></a></p>
    </td>
  </tr>
  <tr>
    <td width="50%">
      <h3><a href="https://github.com/colibrisec/secretly">Secretly</a></h3>
      <p>Slack automation to identify and remove exposed secrets from workflows.</p>
      <p><a href="https://github.com/colibrisec/secretly/actions"><img src="https://github.com/colibrisec/secretly/actions/workflows/ci.yml/badge.svg" alt="Secretly CI status" /></a> <a href="https://github.com/colibrisec/secretly"><img src="https://img.shields.io/github/languages/top/colibrisec/secretly?color=FF3D21" alt="Secretly primary language" /></a></p>
    </td>
    <td width="50%">
      <h3><a href="https://github.com/colibrisec/ojo-action">ojo-action</a></h3>
      <p>GitHub Action integration for running OJO security scans in CI.</p>
      <p><a href="https://github.com/colibrisec/ojo-action/actions"><img src="https://github.com/colibrisec/ojo-action/actions/workflows/test.yml/badge.svg" alt="ojo-action test status" /></a> <a href="https://github.com/colibrisec/ojo-action"><img src="https://img.shields.io/github/languages/top/colibrisec/ojo-action?color=FFD447" alt="ojo-action primary language" /></a></p>
    </td>
  </tr>
</table>

## Contribution stream

<p align="center">
  <img src="https://raw.githubusercontent.com/colibrisec/.github/output/contribution-stream.svg" alt="Animated ColibriSec organization contribution stream" />
</p>

<p align="center">
  <a href="https://github.com/colibrisec">Explore the organization</a>
  ·
  <a href="https://github.com/colibrisec/ojo/releases">OJO releases</a>
  ·
  <a href="https://www.buymeacoffee.com/colibrisec">Support the project</a>
</p>
