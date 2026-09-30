# Local Feasibility and 12-Week Roadmap

Last verified: 2026-10-01

## Verdict

이 노트북 한 대로 프로젝트의 핵심 범위는 구현 가능하다.

- ION-DTN 빌드, 1~3개 로컬 노드, BPv7 정상 통신, GDB 디버깅,
  ASan/UBSan 빌드, TShark 분석, 제한된 protocol-aware fuzzing은 가능하다.
- Docker나 여러 전체 VM을 먼저 도입할 필요는 없다. WSL2 Ubuntu에서 직접
  시작하는 편이 단순하고 현재 자원을 가장 효율적으로 사용한다.
- 가장 먼저 예상되는 병목은 CPU나 디스크가 아니라 RAM이다. 특히 sanitizer
  빌드와 다수 fuzz worker, 패킷 캡처, 브라우저를 동시에 실행할 때 주의한다.
- 이 노트북에서 얻은 성능 수치는 로컬 구현 비교에는 사용할 수 있지만 실제
  위성 또는 비행 하드웨어의 성능을 대표하지 않는다.

## Verified Local Capacity

민감한 장치 식별자는 기록하지 않고 연구 재현에 필요한 자원만 기록한다.

| Resource | Verified state | Assessment |
| --- | --- | --- |
| CPU | Intel Core Ultra 5 125H, 14 cores / 18 logical processors | 빌드, 디버깅, 소규모 병렬 fuzzing에 충분 |
| Host memory | 15.7 GiB usable | 핵심 연구에는 충분; 대규모 병렬 작업에는 제약 |
| WSL2 memory | 7.6 GiB available ceiling, 2 GiB swap | 기본 실험에 적절; ASan/fuzz worker 수 제한 필요 |
| Host storage | C: 약 335 GB 여유 | 소스, 빌드, 선별 PCAP/결과에 충분 |
| WSL2 | Ubuntu 24.04.4 LTS, x86_64, 18 logical CPUs | ION의 공식 Linux 지원 경로와 부합 |
| Compiler/debug | GCC/G++ 13.3, GNU Make 4.3, GDB 15.1 | 기본 C 빌드·디버깅 가능 |
| Packet/network | tcpdump, TShark 4.2.2, `tc`/iproute2 | 캡처와 지연/손실 에뮬레이션 준비됨 |
| Missing build tools | automake, autoconf, libtool, m4 | 공식 기본 빌드 전에 설치 필요 |
| Optional missing tools | CMake, Clang, Ninja, Valgrind, Docker | 선택한 빌드/분석 방식이 요구할 때만 설치 |

WSL2가 정상 실행되므로 펌웨어 가상화 상태를 별도로 변경할 이유는 현재 없다.
전역 `.wslconfig`도 없다. 먼저 기본 8 GiB 수준에서 측정하고, 실제 OOM 증거가
있기 전에는 자원 설정을 바꾸지 않는다.

## Workload Feasibility

| Workload | Feasibility | Operating limit |
| --- | --- | --- |
| RFC/문서/소스 분석 | 매우 여유 | 특별한 제약 없음 |
| ION release build and tests | 여유 | Automake prerequisites 설치 필요 |
| 1-node loopback | 매우 여유 | 정상 동작 기준선으로 먼저 수행 |
| 2~3 nodes on one WSL host | 여유 | 공식 `ionrun`이 같은 호스트 구성을 지원 |
| GDB and packet analysis | 여유 | 디버깅 빌드와 캡처 보관 규칙 사용 |
| ASan/UBSan experiments | 가능 | 일반 빌드와 분리하고 메모리 감시 |
| BPSec with cryptography | 가능 | 정확한 crypto dependency/version을 먼저 고정 |
| Protocol-aware fuzzing | 제한적으로 가능 | 2 workers로 시작해 측정 후 4까지 확장 |
| Many full VMs / large fuzz farm | 비권장 | RAM 병목; 필요하면 외부 머신/클라우드 고려 |
| Flight-hardware performance claims | 불가능 | 로컬 PC 결과는 상대 비교로만 사용 |

## Recommended Local Architecture

1. **WSL2 Ubuntu를 연구 실행 환경으로 사용한다.** Windows는 Codex, 문서,
   Git, 브라우저 UI를 담당한다.
2. **공식 stable tag를 고정한다.** 현재 후보는
   `ion-open-source-4.2.0` (`568df88`)이다. 최종 채택은 별도 결정으로 기록한다.
3. **Docker 없이 정상 경로부터 검증한다.** loopback → 같은 호스트 2-node →
   3-node relay 순서로 늘린다. 공식 quick start는 이 구성을 `ionrun`으로 지원한다.
4. **네트워크 장애는 Linux `tc netem`으로 시작한다.** 별도 VM은 커널/권한
   격리가 실제 연구 변수일 때만 추가한다.
5. **빌드 프로필을 분리한다.** `baseline`, `debug`, `asan-ubsan`을 같은 결과로
   취급하지 않고 각 실행의 compiler flags와 commit을 기록한다.
6. **공격 도구는 별도 사용자/작업 디렉터리와 명시적 포트를 사용한다.** 모든
   대상 주소는 loopback 또는 프로젝트 전용 사설망으로 제한한다.

## Resource Rules

- 일반 빌드는 `make -j4`로 시작한다. 더 높은 병렬도는 실제 빌드 시간과 메모리를
  측정한 뒤 올린다. 개발용 Makefile을 선택한다면 공식 문서 지침에 따라 병렬
  `make`를 사용하지 않는다.
- fuzzing은 2 workers로 시작한다. WSL available memory가 1.5 GiB 아래로 계속
  떨어지거나 swap 사용이 증가하면 worker를 줄인다.
- sanitizer와 fuzzing을 동시에 확장하지 않는다. 먼저 단일 입력 재현과 root
  cause 분석을 끝낸다.
- 장시간 측정은 AC 전원에서 수행하고, 같은 전원 모드와 백그라운드 조건을
  기록한다. 3회 이상 반복하여 중앙값과 변동을 함께 보고한다.
- 원시 PCAP, sanitizer 로그, fuzz output에는 크기 제한과 회전 정책을 둔다.
  최소화된 testcase와 요약 결과만 Git에 넣는다.
- 호스트 C: 여유 공간이 100 GB 아래로 내려가면 새로운 장시간 fuzzing/PCAP
  실험을 시작하기 전에 데이터를 정리하거나 외부 저장소를 계획한다.

위 숫자는 연구 안전을 위한 초기 운영 기준이며 성능 사실이 아니다. 실제 측정에
따라 `docs/DECISIONS.md`에서 변경 근거를 기록한다.

## Installation Gap

공식 ION quick start의 기본 Automake 경로에는 `automake`, `autoconf`,
`libtool`, `m4`, `gcc`, `make`, `pkg-config`가 필요하다. 현재 WSL에는 마지막
세 항목만 준비되어 있다.

다음 설치는 관리자 권한이 필요하므로 실제 환경 구축 단계에서 사용자 확인 후
수행한다.

```sh
sudo apt update
sudo apt install automake autoconf libtool m4
```

CMake, Clang, Ninja, Valgrind, Docker, GUI Wireshark는 지금 설치하지 않는다.
선택한 실험이나 빌드 방식이 필요성을 만들 때만 추가한다.

## 12-Week Roadmap

### Weeks 1–2: Foundations and source pinning

- RFC 9171, 9172, 9173, 8949의 프로젝트 관련 부분을 학습한다.
- ION 4.2.0 stable tag를 연구 baseline으로 사용할지 결정하고 commit hash를 고정한다.
- 공식 build dependencies와 라이선스를 확인한다.

**Gate:** BPv7 bundle/block 구조, BPSec 역할, 연구 대상 ION 버전을 설명할 수 있다.

### Weeks 3–4: Reproducible normal operation

- 승인 후 WSL build prerequisites를 설치한다.
- baseline/debug 빌드와 upstream regression smoke test를 기록한다.
- loopback, same-host 2-node, 3-node relay를 순서대로 재현한다.
- 정상 TCP/UDP/LTP 트래픽의 작은 PCAP과 명령을 보존한다.

**Gate:** 깨끗한 환경에서 문서만 보고 build와 정상 bundle 전달을 재현할 수 있다.

### Weeks 5–6: Implementation map and threat model

- 네트워크 입력에서 BP parsing, storage, forwarding, delivery까지 call path를 추적한다.
- 프로세스, shared memory/SDR, queue, admin interface, BPSec 경계를 문서화한다.
- 공격자 능력과 성공 기준을 하나의 우선 연구 질문에 맞춰 확정한다.

**Gate:** 선택한 공격 표면의 정상 처리 경로와 trust boundary를 설명할 수 있다.

### Weeks 7–9: Controlled experiments

- `EXP-001`에 정상 baseline과 측정 방법을 사전 등록한다.
- 지연·손실·접속 중단을 한 변수씩 적용한다.
- 그다음 replay, resource pressure, malformed input 중 하나만 우선 선택한다.
- 실패가 발생하면 재현 → 최소화 → root cause → impact 순서로 분석한다.

**Gate:** 원시 데이터, 재현 명령, 대조군, 반복 측정이 있는 완결된 실험 1개.

### Weeks 10–11: Optional fuzzing or mitigation

- parser 경로와 input model을 이해한 경우에만 작은 protocol-aware harness를 만든다.
- 그렇지 않으면 확인된 failure mode의 방어/관측/회귀 테스트에 시간을 사용한다.
- crash count가 아니라 unique reproducible root cause를 기준으로 평가한다.

**Gate:** 재현 가능한 finding 또는 근거 있는 negative result와 한계가 기록되어 있다.

### Week 12: Evaluation and reporting

- baseline 대비 보안·성능 영향을 동일 조건에서 비교한다.
- 과장 없이 verified fact, inference, hypothesis, limitation을 분리한다.
- 새로운 취약점이 의심되면 공개 전에 responsible disclosure 여부를 검토한다.
- `PROJECT_STATE.md`, 결정, 실험 기록, README를 최종 상태로 맞춘다.

## First Decision Checkpoint

다음 구현 작업 전에 아래 두 항목만 결정한다.

1. 연구 baseline을 stable `ion-open-source-4.2.0`으로 고정할지.
2. 첫 환경을 WSL2 직접 설치로 진행할지.

현재 증거로는 두 항목 모두 **Yes**가 가장 단순하고 재현 가능한 기본 선택이다.

## Sources

- NASA/JPL ION-DTN repository: https://github.com/nasa-jpl/ION-DTN
- Official quick start: https://github.com/nasa-jpl/ION-DTN/blob/integration/site-docs/docs/quick-start-guide.md
- Official releases: https://github.com/nasa-jpl/ION-DTN/releases
